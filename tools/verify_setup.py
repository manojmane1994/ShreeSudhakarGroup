"""
Shree Sudhakar Group - Supabase readiness verification
Run: python tools/verify_setup.py
"""
import json
import os
import sys
from pathlib import Path

import httpx
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

load_dotenv()


def print_section(title: str) -> None:
    print("=" * 72)
    print(f"  {title}")
    print("=" * 72)


def main() -> int:
    print_section("Shree Sudhakar Group - Supabase Readiness Check")

    supabase_url = os.getenv("SUPABASE_URL", "").rstrip("/")
    supabase_key = os.getenv("SUPABASE_KEY", "")
    base_url = os.getenv("BASE_URL", "http://localhost:8080").rstrip("/")

    print("\n1. Environment configuration")
    if not supabase_url or not supabase_key:
        print("   [!] SUPABASE_URL or SUPABASE_KEY is missing.")
        print("       Please copy .env.example to .env and fill in your Supabase values.")
        return 1

    if "your-project-id" in supabase_url or "your-anon-or-service" in supabase_key:
        print("   [!] Supabase credentials are still placeholders.")
        print("       Replace them with your actual Supabase project values.")
        return 1

    print(f"   [OK] SUPABASE_URL={supabase_url}")
    print("   [OK] SUPABASE_KEY is present (value hidden).")

    print_section("2. Supabase connection and schema checks")
    enquiries_endpoint = f"{supabase_url}/rest/v1/enquiries?limit=1"
    admin_users_endpoint = f"{supabase_url}/rest/v1/admin_users?limit=1"

    headers = {
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}",
        "Content-Type": "application/json",
    }

    try:
        with httpx.Client(timeout=10.0) as client:
            res = client.get(enquiries_endpoint, headers=headers)
            if res.status_code == 200:
                print("   [OK] enquiries table exists and is accessible.")
            elif res.status_code == 404 or 'relation "public.enquiries" does not exist' in res.text:
                print("   [!] enquiries table does not exist.")
                print("       Run supabase_setup.sql in your Supabase SQL Editor.")
                return 1
            else:
                print(f"   [!] enquiries endpoint returned HTTP {res.status_code}: {res.text}")
                return 1

            res = client.get(admin_users_endpoint, headers=headers)
            if res.status_code == 200:
                print("   [OK] admin_users table exists and is accessible.")
            elif res.status_code == 404 or 'relation "public.admin_users" does not exist' in res.text:
                print("   [!] admin_users table does not exist.")
                print("       Run supabase_setup.sql in your Supabase SQL Editor.")
                return 1
            else:
                print(f"   [!] admin_users endpoint returned HTTP {res.status_code}: {res.text}")
                return 1

            login_res = client.post(
                f"{base_url}/api/admin/login",
                json={"username": "admin", "password": "Password@123"},
            )
            if login_res.status_code == 200:
                login_data = login_res.json()
                print("   [OK] admin login succeeded.")
                print(f"       Login role: {login_data.get('role', 'unknown')}")
            else:
                print(f"   [!] admin login failed with HTTP {login_res.status_code}: {login_res.text}")
                print("       If Supabase is configured, this may indicate the seeded admin user is missing.")
                return 1

            enquiries_res = client.get(f"{base_url}/api/admin/enquiries")
            if enquiries_res.status_code == 200:
                data = enquiries_res.json()
                print("   [OK] admin enquiries endpoint succeeded.")
                print(f"       Source: {data.get('source', 'unknown')}")
                print(f"       Enquiries returned: {len(data.get('enquiries', []))}")
            else:
                print(f"   [!] admin enquiries endpoint failed with HTTP {enquiries_res.status_code}: {enquiries_res.text}")
                return 1

    except httpx.HTTPError as exc:
        print(f"   [!] HTTP error: {exc}")
        return 1
    except Exception as exc:
        print(f"   [!] Unexpected error: {exc}")
        return 1

    print("\n" + "=" * 72)
    print("  SUCCESS: Supabase setup is ready for admin login and enquiry management.")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
