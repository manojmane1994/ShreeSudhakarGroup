# Shree Sudhakar Group - Corporate Website & Backend

> **Building Infrastructure. Powering Progress.**

A corporate website for **Shree Sudhakar Group** featuring a sunrise aesthetic, interactive project enquiry system, Python (FastAPI/Serverless) backend, interactive **Admin Lead Portal**, and free **Supabase** cloud database integration, fully optimized for deployment on **Vercel**.

---

## Key Highlights

- **Sunrise Aesthetic**: Dawn horizon visuals, warm amber gradients, and realistic infrastructure backdrop.
- **7 Business Verticals**:
  1. Government Infrastructure & Development
  2. Gas Pipeline Infrastructure (MDPE, PE, Steel, CGD)
  3. Electrical Works & Infrastructure
  4. Road & Civil Construction
  5. CNG & Petrol Pump Projects (Civil & Mechanical)
  6. Residential & Commercial Construction
  7. Conventional & PEB Structural Fabrication
- **Interactive Enquiry System**:
  - Embedded instant consultation form on the homepage.
  - Interactive popup modal triggered from any vertical or CTA button.
  - Real-time client validation and submission feedback.
- **Admin Lead Management Portal (`/admin`)**:
  - Live browser dashboard to review all incoming enquiries.
  - Search by client name, mobile, or city.
  - Filter by vertical or lead status (New, Contacted, In Discussion, Closed).
  - 1-Click WhatsApp direct chat and phone dialing.
  - Live status updater and 1-Click "Download CSV / Excel" button.
- **Backend & Database**:
  - Python FastAPI local development server (`app.py`).
  - Vercel Serverless Function entry point (`api/index.py`).
  - Supabase PostgreSQL schema with Row-Level Security (`supabase_setup.sql`).
  - Fallback local JSON storage (`local_enquiries.json`) so enquiries work immediately even before cloud database setup.
- **Admin CLI Tools**:
  - Python CLI tool to inspect leads and export to CSV (`tools/admin_tool.py`).
  - Connectivity tester (`tools/test_supabase.py`).

---

## 1. How to See Enquiries for Admin

### Method 1: Web Admin Portal (Visual in Browser)
Open your browser and navigate to:
👉 **[http://localhost:8080/admin](http://localhost:8080/admin)**

Features:
- View all received leads with date, client name, mobile, vertical, city, and scope.
- Click **"WhatsApp"** or **"Call"** next to any enquiry to contact the client directly.
- Change status (e.g. from *New* to *Contacted* or *Closed*).
- Click **"Download CSV / Excel"** to export leads to spreadsheet.

### Method 2: Python Command Line
From your project directory:
```powershell
# View all received enquiries
python tools/admin_tool.py list

# View only new/unread enquiries
python tools/admin_tool.py new

# Export enquiries to an Excel-compatible CSV file
python tools/admin_tool.py export
```

### Method 3: Supabase Cloud Dashboard (In Production)
Once deployed with Supabase:
1. Log in to [https://supabase.com/dashboard](https://supabase.com/dashboard).
2. Select your project -> Click **Table Editor** -> **enquiries**.
3. View, search, sort, and manage all enquiries in real-time with full cloud backup.

---

## 2. Local Preview & Development

```powershell
# Start local server:
python app.py
```

- **Website**: [http://localhost:8080](http://localhost:8080)
- **Admin Portal**: [http://localhost:8080/admin](http://localhost:8080/admin)
- **API Health**: [http://localhost:8080/api/health](http://localhost:8080/api/health)
- **Submit Enquiry API**: `POST http://localhost:8080/api/enquiry`

---

## 3. Supabase Free Database Setup (3 Minutes)

1. Create a free account at [Supabase](https://supabase.com).
2. Create a new project (e.g., `shree-sudhakar-group`).
3. In your Supabase Dashboard, click on **SQL Editor** -> **New Query**.
4. Copy the contents of [`supabase_setup.sql`](./supabase_setup.sql) and click **Run**.
5. Go to **Project Settings** -> **API**:
   - Copy **Project URL**
   - Copy **anon** public key (or `service_role` key)
6. Copy `.env.example` to `.env`:
   ```powershell
   Copy-Item .env.example .env
   ```
7. Open `.env` and fill in your values:
   ```env
   SUPABASE_URL=https://your-project-id.supabase.co
   SUPABASE_KEY=your-actual-key
   PORT=8080
   ```
8. Verify your database connection:
   ```powershell
   python tools/test_supabase.py
   ```

---

## 4. Deploying to Vercel

1. Push this folder to a GitHub repository.
2. Go to [Vercel Dashboard](https://vercel.com/dashboard) and click **Add New Project**.
3. Import your GitHub repository.
4. Under **Environment Variables**, add:
   - `SUPABASE_URL`: `https://your-project-id.supabase.co`
   - `SUPABASE_KEY`: `your-supabase-key`
5. Click **Deploy**.

---

## Company Details

- **Company**: Shree Sudhakar Group
- **Enquiry Phone**: +91 9689820892
- **Office Address**: Mangalam Life Park, Moshi - Alandi Road, Pimpri-Chinchwad, Maharashtra 412105
