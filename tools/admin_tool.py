"""
Shree Sudhakar Group - Enquiries Management CLI
Usage:
  python tools/admin_tool.py list          # List all enquiries
  python tools/admin_tool.py new           # List only new enquiries
  python tools/admin_tool.py export        # Export enquiries to enquiries_export.csv
"""
import os
import sys
import csv
import json
from datetime import datetime
import httpx
from dotenv import load_dotenv

# Safe Windows stdout encoding
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "").rstrip("/")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCAL_STORE = os.path.join(BASE_DIR, "local_enquiries.json")


def fetch_enquiries():
    supabase_ready = bool(SUPABASE_URL and SUPABASE_KEY and "your-project-id" not in SUPABASE_URL)
    if supabase_ready:
        endpoint = f"{SUPABASE_URL}/rest/v1/enquiries?order=created_at.desc"
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
        }
        try:
            with httpx.Client(timeout=10.0) as client:
                res = client.get(endpoint, headers=headers)
                if res.status_code == 200:
                    return res.json(), "Supabase Cloud DB"
                else:
                    print(f"Error fetching from Supabase ({res.status_code}): {res.text}")
        except Exception as e:
            print(f"Connection error to Supabase: {e}")

    # Fallback to local store
    if os.path.exists(LOCAL_STORE):
        try:
            with open(LOCAL_STORE, "r", encoding="utf-8") as f:
                return json.load(f), "Local JSON Store"
        except Exception:
            return [], "Local JSON Store (empty)"
    return [], "None"


def print_table(enquiries, source):
    print("=" * 95)
    print(f"  SHREE SUDHAKAR GROUP - ENQUIRIES [{source}] (Total: {len(enquiries)})")
    print("=" * 95)
    if not enquiries:
        print("  No enquiries found.")
        print("=" * 95)
        return

    header = f"{'Date':<16} | {'Name':<18} | {'Mobile':<14} | {'Vertical':<25} | {'City':<12}"
    print(header)
    print("-" * 95)

    for item in enquiries:
        dt = item.get("created_at", "")[:16].replace("T", " ")
        name = (item.get("name") or "")[:17]
        mobile = (item.get("mobile") or "")[:13]
        vertical = (item.get("vertical") or "")[:24]
        city = (item.get("city") or "N/A")[:11]
        print(f"{dt:<16} | {name:<18} | {mobile:<14} | {vertical:<25} | {city:<12}")
        if item.get("message"):
            msg = item.get("message", "").replace("\n", " ")
            print(f"  +-- Message: {msg[:80]}...")
    print("=" * 95)


def export_csv(enquiries):
    if not enquiries:
        print("No enquiries to export.")
        return

    csv_path = os.path.join(BASE_DIR, f"enquiries_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
    fields = ["created_at", "name", "mobile", "email", "vertical", "city", "message", "status"]

    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in enquiries:
            writer.writerow(row)

    print(f"\n[OK] Successfully exported {len(enquiries)} records to:\n     {csv_path}")


def main():
    cmd = sys.argv[1].lower() if len(sys.argv) > 1 else "list"
    enquiries, source = fetch_enquiries()

    if cmd == "new":
        enquiries = [e for e in enquiries if e.get("status", "").lower() == "new"]
        print_table(enquiries, f"{source} - New Only")
    elif cmd == "export":
        export_csv(enquiries)
    else:
        print_table(enquiries, source)


if __name__ == "__main__":
    main()
