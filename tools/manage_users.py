"""
Shree Sudhakar Group - Admin & User Credentials Management CLI
Usage:
  python tools/manage_users.py list
  python tools/manage_users.py create <username> <email> <password> [full_name] [role]
  python tools/manage_users.py reset <username> <new_password>

Roles: superadmin | admin | manager | viewer | sales | finance
"""
import os
import sys
import json
import hashlib
import secrets
from datetime import datetime
import httpx
from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "").rstrip("/")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCAL_ADMIN_STORE = os.path.join(BASE_DIR, "local_admin_users.json")


def hash_password(password: str, salt: str = None) -> tuple[str, str]:
    if not salt:
        salt = secrets.token_hex(16)
    pwd_hash = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    return pwd_hash, salt


def verify_password(password: str, password_hash: str, salt: str) -> bool:
    expected_hash = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    return secrets.compare_digest(expected_hash, password_hash)


def get_local_users():
    if os.path.exists(LOCAL_ADMIN_STORE):
        try:
            with open(LOCAL_ADMIN_STORE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    # Default seed user in local file
    pwd_hash, salt = hash_password("Password@123", "ssg_salt_2026")
    default_users = [{
        "id": "usr-1",
        "username": "admin",
        "email": "admin@shreesudhakar.com",
        "full_name": "Default Administrator",
        "password_hash": pwd_hash,
        "salt": salt,
        "role": "superadmin",
        "is_active": True,
        "created_at": datetime.utcnow().isoformat()
    }]
    with open(LOCAL_ADMIN_STORE, "w", encoding="utf-8") as f:
        json.dump(default_users, f, indent=2)
    return default_users


def save_local_users(users):
    with open(LOCAL_ADMIN_STORE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)


def list_users():
    print("=" * 80)
    print("  SHREE SUDHAKAR GROUP - REGISTERED ADMIN USERS")
    print("=" * 80)
    users = get_local_users()
    if not users:
        print("  No admin users found.")
        return

    print(f"{'Username':<15} | {'Role':<12} | {'Full Name':<22} | {'Email':<25}")
    print("-" * 80)
    for u in users:
        print(f"{u.get('username'):<15} | {u.get('role'):<12} | {u.get('full_name', 'N/A'):<22} | {u.get('email'):<25}")
    print("=" * 80)


def create_user(username, email, password, full_name="Admin", role="admin"):
    users = get_local_users()
    if any(u.get("username").lower() == username.lower() for u in users):
        print(f"[!] User '{username}' already exists.")
        return

    # Validate role against the allowed enum (mirrors Supabase CHECK)
    allowed_roles = ("superadmin", "admin", "manager", "viewer", "sales", "finance")
    if role.lower() not in allowed_roles:
        print(f"[!] Invalid role '{role}'. Allowed roles: {', '.join(allowed_roles)}")
        return

    pwd_hash, salt = hash_password(password)
    new_user = {
        "id": f"usr-{len(users)+1}",
        "username": username.strip(),
        "email": email.strip(),
        "full_name": full_name.strip(),
        "password_hash": pwd_hash,
        "salt": salt,
        "role": role.lower(),
        "is_active": True,
        "created_at": datetime.utcnow().isoformat()
    }
    users.append(new_user)
    save_local_users(users)
    print(f"[OK] Admin user '{username}' created successfully! Role: {role}")


def reset_password(username, new_password):
    users = get_local_users()
    found = False
    for u in users:
        if u.get("username").lower() == username.lower():
            pwd_hash, salt = hash_password(new_password)
            u["password_hash"] = pwd_hash
            u["salt"] = salt
            found = True
            break
    if found:
        save_local_users(users)
        print(f"[OK] Password for '{username}' has been reset successfully!")
    else:
        print(f"[!] User '{username}' not found.")


def main():
    if len(sys.argv) < 2:
        list_users()
        return

    cmd = sys.argv[1].lower()
    if cmd == "list":
        list_users()
    elif cmd == "create" and len(sys.argv) >= 5:
        username = sys.argv[2]
        email = sys.argv[3]
        password = sys.argv[4]
        full_name = sys.argv[5] if len(sys.argv) > 5 else "Admin"
        role = sys.argv[6] if len(sys.argv) > 6 else "admin"
        create_user(username, email, password, full_name, role)
    elif cmd == "reset" and len(sys.argv) >= 4:
        username = sys.argv[2]
        new_password = sys.argv[3]
        reset_password(username, new_password)
    else:
        print("Usage:")
        print("  python tools/manage_users.py list")
        print("  python tools/manage_users.py create <username> <email> <password> [full_name]")
        print("  python tools/manage_users.py reset <username> <new_password>")


if __name__ == "__main__":
    main()
