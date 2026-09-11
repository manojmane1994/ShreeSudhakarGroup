# Walkthrough: Shree Sudhakar Group Website & Admin Lead Portal

The corporate website, Python backend, and **Admin Lead Portal** for **Shree Sudhakar Group** have been created, verified, and launched.

---

## 1. How Admins Can View Enquiries

### Option A: Web Admin Dashboard (Browser)
Open: 👉 **[http://localhost:8080/admin](http://localhost:8080/admin)**

Features:
- **Real-time Overview**: Total leads, new leads, in-progress, and closed counts.
- **Search & Filtering**: Search by name, phone number, city, or filter by business vertical and status.
- **Instant Client Contact**: Click **"WhatsApp"** or **"Call"** next to any enquiry to open a pre-filled chat or dial directly.
- **Status Updates**: Select *New*, *Contacted*, *In Discussion*, or *Closed* directly from the dropdown.
- **Spreadsheet Export**: Click **"Download CSV / Excel"** to save leads to a spreadsheet.

### Option B: Terminal CLI (Python)
From `D:\AntigravityProject\ShreeSudhakarGroup`:
```powershell
# View all enquiries in a formatted table
python tools/admin_tool.py list

# View only new/unread enquiries
python tools/admin_tool.py new

# Export enquiries to an Excel-friendly CSV file
python tools/admin_tool.py export
```

### Option C: Supabase Cloud Dashboard (In Production)
1. Go to [https://supabase.com/dashboard](https://supabase.com/dashboard)
2. Select your project -> Click **Table Editor** -> **enquiries**
3. Full cloud database view with real-time sync, column filtering, and export.

---

## 2. Core Components Built

- [`index.html`](file:///D:/AntigravityProject/ShreeSudhakarGroup/index.html): Corporate website with sunrise backdrop and 7 business verticals.
- [`admin.html`](file:///D:/AntigravityProject/ShreeSudhakarGroup/admin.html): Dedicated web admin dashboard.
- [`app.py`](file:///D:/AntigravityProject/ShreeSudhakarGroup/app.py): Local FastAPI server serving `/` and `/admin`.
- [`api/index.py`](file:///D:/AntigravityProject/ShreeSudhakarGroup/api/index.py): Vercel Serverless Function handling `/api/enquiry` and `/api/admin/enquiries`.
- [`supabase_setup.sql`](file:///D:/AntigravityProject/ShreeSudhakarGroup/supabase_setup.sql): Database table schema and security policies.
- [`tools/admin_tool.py`](file:///D:/AntigravityProject/ShreeSudhakarGroup/tools/admin_tool.py): Command-line lead viewer and exporter.
- [`tools/test_supabase.py`](file:///D:/AntigravityProject/ShreeSudhakarGroup/tools/test_supabase.py): Supabase connection tester.
- [`local_enquiries.json`](file:///D:/AntigravityProject/ShreeSudhakarGroup/local_enquiries.json): Local preview store preserving leads submitted during testing.
