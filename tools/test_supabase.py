"""
Supabase Connection & Table Verification Tool
Run: python tools/test_supabase.py
"""
import os
import sys
import httpx
from dotenv import load_dotenv

# Ensure parent directory is in path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "").rstrip("/")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

def main():
    print("=" * 60)
    print("  Shree Sudhakar Group - Supabase Verification")
    print("=" * 60)

    if not SUPABASE_URL or not SUPABASE_KEY or "your-project-id" in SUPABASE_URL:
        print("[!] ERROR: Supabase credentials not found or using default placeholder.")
        print("    Please set SUPABASE_URL and SUPABASE_KEY in your .env file.")
        print("    1. Create a free project at https://supabase.com")
        print("    2. Go to Project Settings -> API")
        print("    3. Copy Project URL and 'anon' public key (or service_role key)")
        print("    4. Paste them into .env")
        return 1

    print(f"[*] Target URL: {SUPABASE_URL}")
    print("[*] Testing API connectivity...")

    endpoint = f"{SUPABASE_URL}/rest/v1/enquiries"
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }

    try:
        # Step 1: Check table existence
        with httpx.Client(timeout=10.0) as client:
            res = client.get(f"{endpoint}?limit=1", headers=headers)
            
            if res.status_code == 200:
                print("[OK] Successfully connected to Supabase!")
                print("[OK] 'enquiries' table exists and is accessible.")
            elif res.status_code == 404 or "relation \"public.enquiries\" does not exist" in res.text:
                print("[!] Table 'enquiries' does NOT exist yet in Supabase.")
                print("    Please run the 'supabase_setup.sql' script in your Supabase SQL Editor:")
                print("    https://supabase.com/dashboard/project/_/sql/new")
                return 1
            else:
                print(f"[!] Supabase responded with status {res.status_code}: {res.text}")
                return 1

        # Step 2: Insert test record
        test_payload = {
            "name": "Test System Verification",
            "mobile": "+91 9689820892",
            "email": "test@shreesudhakar.com",
            "vertical": "Government Projects",
            "city": "Pune",
            "message": "Automated verification test from tools/test_supabase.py",
            "status": "New"
        }

        print("[*] Submitting test enquiry to Supabase...")
        with httpx.Client(timeout=10.0) as client:
            insert_res = client.post(endpoint, json=test_payload, headers=headers)
            if insert_res.status_code in [200, 201]:
                data = insert_res.json()
                print("[OK] Test enquiry created successfully!")
                print(f"     Record ID: {data[0]['id'] if isinstance(data, list) and len(data) > 0 else data}")
            else:
                print(f"[!] Failed to insert test record: {insert_res.status_code} - {insert_res.text}")
                return 1

        print("\n[SUCCESS] Supabase database is fully configured and ready for production!")
        return 0

    except Exception as exc:
        print(f"[!] Connection exception: {exc}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
