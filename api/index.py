import os
import json
import logging
import hashlib
import secrets
from typing import Optional
from datetime import datetime, timezone, timedelta
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import httpx
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Shree Sudhakar Group API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = logging.getLogger("uvicorn.error")

SUPABASE_URL = os.getenv("SUPABASE_URL", "").rstrip("/")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCAL_STORE = os.path.join(BASE_DIR, "local_enquiries.json")
LOCAL_ADMIN_STORE = os.path.join(BASE_DIR, "local_admin_users.json")

# IST Timezone (+5:30)
IST = timezone(timedelta(hours=5, minutes=30))


class EnquiryPayload(BaseModel):
    name: str = Field(..., min_length=2, max_length=120)
    mobile: str = Field(..., min_length=7, max_length=20)
    email: Optional[str] = Field(None, max_length=120)
    vertical: str = Field(..., min_length=2, max_length=150)
    city: Optional[str] = Field(None, max_length=100)
    message: Optional[str] = Field(None, max_length=1500)
    source: Optional[str] = Field("Website", max_length=50)


class StatusUpdatePayload(BaseModel):
    status: str = Field(..., pattern="^(New|Contacted|In Discussion|Closed)$")


class LoginPayload(BaseModel):
    username: str = Field(..., min_length=2)
    password: str = Field(..., min_length=4)


# ==============================================================================
# Helper Functions
# ==============================================================================
def verify_hash(password: str, password_hash: str, salt: str) -> bool:
    expected_hash = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    return secrets.compare_digest(expected_hash, password_hash)


def get_local_admins():
    if os.path.exists(LOCAL_ADMIN_STORE):
        try:
            with open(LOCAL_ADMIN_STORE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    # Default fallback admin
    salt = "ssg_salt_2026"
    pwd_hash = hashlib.sha256((salt + "Password@123").encode("utf-8")).hexdigest()
    default_admin = [{
        "username": "admin",
        "email": "admin@shreesudhakar.com",
        "password_hash": pwd_hash,
        "salt": salt,
        "role": "superadmin",
        "full_name": "Default Administrator"
    }]
    try:
        with open(LOCAL_ADMIN_STORE, "w", encoding="utf-8") as f:
            json.dump(default_admin, f, indent=2)
    except Exception:
        pass
    return default_admin


# ==============================================================================
# Routes
# ==============================================================================
async def _health_handler():
    supabase_configured = bool(SUPABASE_URL and SUPABASE_KEY and "your-project-id" not in SUPABASE_URL)
    now_ist = datetime.now(IST)
    return {
        "status": "healthy",
        "timestamp": now_ist.isoformat(),
        "date": now_ist.strftime("%Y-%m-%d"),
        "time": now_ist.strftime("%H:%M:%S"),
        "supabase_configured": supabase_configured,
        "company": "Shree Sudhakar Group"
    }

app.add_api_route("/health", _health_handler, methods=["GET"])
app.add_api_route("/api/health", _health_handler, methods=["GET"])


async def _enquiry_handler(enquiry: EnquiryPayload, request: Request):
    now_ist = datetime.now(IST)
    enquiry_date = now_ist.strftime("%Y-%m-%d")
    enquiry_time = now_ist.strftime("%H:%M:%S")
    created_at = datetime.now(timezone.utc).isoformat()

    client_ip = request.client.host if request.client else "Unknown"
    user_agent = request.headers.get("user-agent", "Unknown")[:250]

    data = {
        "name": enquiry.name.strip(),
        "mobile": enquiry.mobile.strip(),
        "email": enquiry.email.strip() if enquiry.email else None,
        "vertical": enquiry.vertical.strip(),
        "city": enquiry.city.strip() if enquiry.city else None,
        "message": enquiry.message.strip() if enquiry.message else None,
        "status": "New",
        "enquiry_date": enquiry_date,
        "enquiry_time": enquiry_time,
        "created_at": created_at,
        "source": enquiry.source or "Website",
        "ip_address": client_ip,
        "user_agent": user_agent
    }

    supabase_ready = bool(SUPABASE_URL and SUPABASE_KEY and "your-project-id" not in SUPABASE_URL)

    if supabase_ready:
        endpoint = f"{SUPABASE_URL}/rest/v1/enquiries"
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        }

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                res = await client.post(endpoint, json=data, headers=headers)
                if res.status_code in [200, 201]:
                    return {
                        "success": True,
                        "message": "Thank you! Your enquiry has been received. Our team will contact you shortly.",
                        "storage": "supabase",
                        "data": res.json()
                    }
                else:
                    logger.error(f"Supabase error ({res.status_code}): {res.text}")
                    raise HTTPException(
                        status_code=status.HTTP_502_BAD_GATEWAY,
                        detail=f"Database submission error: {res.text}"
                    )
        except httpx.RequestError as exc:
            logger.error(f"Network error connecting to Supabase: {exc}")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Could not reach database service. Please call us directly at +91 9689820892."
            )
    else:
        # Development / preview local storage fallback
        enquiries_list = []
        if os.path.exists(LOCAL_STORE):
            try:
                with open(LOCAL_STORE, "r", encoding="utf-8") as f:
                    enquiries_list = json.load(f)
            except Exception:
                enquiries_list = []

        data["id"] = f"lead-{len(enquiries_list)+1}"
        enquiries_list.append(data)

        try:
            with open(LOCAL_STORE, "w", encoding="utf-8") as f:
                json.dump(enquiries_list, f, indent=2)
        except Exception as e:
            logger.warning(f"Could not write local enquiry fallback: {e}")

        return {
            "success": True,
            "message": "Thank you! Your enquiry has been received. Our team will contact you shortly.",
            "storage": "local_preview",
            "data": data
        }

app.add_api_route("/enquiry", _enquiry_handler, methods=["POST"], status_code=status.HTTP_201_CREATED)
app.add_api_route("/api/enquiry", _enquiry_handler, methods=["POST"], status_code=status.HTTP_201_CREATED)


# ==============================================================================
# Admin Authentication & Management Routes
# ==============================================================================
async def _admin_login_handler(payload: LoginPayload):
    username = payload.username.strip()
    password = payload.password

    # Check Supabase admin_users if configured
    supabase_ready = bool(SUPABASE_URL and SUPABASE_KEY and "your-project-id" not in SUPABASE_URL)
    if supabase_ready:
        endpoint = f"{SUPABASE_URL}/rest/v1/admin_users?username=eq.{username}&is_active=eq.true"
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
        }
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                res = await client.get(endpoint, headers=headers)
                if res.status_code == 200:
                    records = res.json()
                    if records:
                        user = records[0]
                        if verify_hash(password, user["password_hash"], user["salt"]):
                            # Update last_login
                            await client.patch(
                                f"{SUPABASE_URL}/rest/v1/admin_users?id=eq.{user['id']}",
                                json={"last_login": datetime.now(timezone.utc).isoformat()},
                                headers=headers
                            )
                            return {
                                "success": True,
                                "token": secrets.token_hex(24),
                                "username": user["username"],
                                "role": user.get("role", "admin"),
                                "full_name": user.get("full_name", "Admin")
                            }
        except Exception as e:
            logger.error(f"Error checking Supabase auth: {e}")

    # Fallback to local admin store
    admins = get_local_admins()
    for user in admins:
        if user.get("username").lower() == username.lower():
            if verify_hash(password, user["password_hash"], user["salt"]):
                return {
                    "success": True,
                    "token": secrets.token_hex(24),
                    "username": user["username"],
                    "role": user.get("role", "admin"),
                    "full_name": user.get("full_name", "Admin")
                }

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password.")

app.add_api_route("/admin/login", _admin_login_handler, methods=["POST"])
app.add_api_route("/api/admin/login", _admin_login_handler, methods=["POST"])


async def _get_admin_enquiries():
    supabase_ready = bool(SUPABASE_URL and SUPABASE_KEY and "your-project-id" not in SUPABASE_URL)

    if supabase_ready:
        endpoint = f"{SUPABASE_URL}/rest/v1/enquiries?order=created_at.desc"
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
        }
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                res = await client.get(endpoint, headers=headers)
                if res.status_code == 200:
                    return {"source": "supabase", "enquiries": res.json()}
        except Exception as e:
            logger.error(f"Error fetching from Supabase: {e}")

    # Fallback to local store
    if os.path.exists(LOCAL_STORE):
        try:
            with open(LOCAL_STORE, "r", encoding="utf-8") as f:
                enquiries = json.load(f)
                enquiries.reverse()
                return {"source": "local_file", "enquiries": enquiries}
        except Exception:
            return {"source": "local_file", "enquiries": []}
    return {"source": "none", "enquiries": []}

app.add_api_route("/admin/enquiries", _get_admin_enquiries, methods=["GET"])
app.add_api_route("/api/admin/enquiries", _get_admin_enquiries, methods=["GET"])


async def _update_enquiry_status(id: str, payload: StatusUpdatePayload):
    supabase_ready = bool(SUPABASE_URL and SUPABASE_KEY and "your-project-id" not in SUPABASE_URL)

    if supabase_ready:
        endpoint = f"{SUPABASE_URL}/rest/v1/enquiries?id=eq.{id}"
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        }
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                res = await client.patch(endpoint, json={"status": payload.status}, headers=headers)
                if res.status_code in [200, 204]:
                    return {"success": True, "status": payload.status}
        except Exception as e:
            logger.error(f"Error updating Supabase: {e}")

    # Local fallback update
    if os.path.exists(LOCAL_STORE):
        try:
            with open(LOCAL_STORE, "r", encoding="utf-8") as f:
                enquiries = json.load(f)
            for item in enquiries:
                if str(item.get("id")) == str(id):
                    item["status"] = payload.status
                    break
            with open(LOCAL_STORE, "w", encoding="utf-8") as f:
                json.dump(enquiries, f, indent=2)
            return {"success": True, "status": payload.status}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    raise HTTPException(status_code=404, detail="Enquiry not found")

app.add_api_route("/admin/enquiries/{id}/status", _update_enquiry_status, methods=["PATCH"])
app.add_api_route("/api/admin/enquiries/{id}/status", _update_enquiry_status, methods=["PATCH"])
