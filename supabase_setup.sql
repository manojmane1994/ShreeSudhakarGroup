-- ==============================================================================
-- Shree Sudhakar Group - Complete Supabase Database Schema
-- Run this script in your Supabase SQL Editor:
-- https://supabase.com/dashboard/project/_/sql/new
-- ==============================================================================

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ==============================================================================
-- 1. ADMIN & USER CREDENTIALS TABLE
-- ==============================================================================
CREATE TABLE IF NOT EXISTS public.admin_users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    salt TEXT NOT NULL,
    role TEXT DEFAULT 'admin' CHECK (role IN ('superadmin', 'admin', 'manager', 'viewer', 'sales', 'finance')),
    full_name TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    last_login TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT TIMEZONE('utc'::text, NOW()) NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT TIMEZONE('utc'::text, NOW()) NOT NULL
);

-- Index on username and email for fast lookups
CREATE INDEX IF NOT EXISTS idx_admin_users_username ON public.admin_users (username);
CREATE INDEX IF NOT EXISTS idx_admin_users_email ON public.admin_users (email);

-- Enable RLS for admin_users
ALTER TABLE public.admin_users ENABLE ROW LEVEL SECURITY;

-- Only service_role can directly access admin_users table (protects hashes)
CREATE POLICY "Admin users accessible via service_role only"
ON public.admin_users
FOR ALL
TO service_role
USING (true);


-- ==============================================================================
-- 2. USER ENQUIRIES TABLE (With Automatic Date, Time & Metadata)
-- ==============================================================================
CREATE TABLE IF NOT EXISTS public.enquiries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Automatic Date & Time Tracking
    enquiry_date DATE DEFAULT (CURRENT_DATE AT TIME ZONE 'Asia/Kolkata') NOT NULL,
    enquiry_time TIME DEFAULT (CURRENT_TIME AT TIME ZONE 'Asia/Kolkata') NOT NULL,
    created_at TIMESTAMPTZ DEFAULT TIMEZONE('utc'::text, NOW()) NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT TIMEZONE('utc'::text, NOW()) NOT NULL,

    -- Client Details
    name TEXT NOT NULL,
    mobile TEXT NOT NULL,
    email TEXT,
    vertical TEXT NOT NULL,
    city TEXT,
    message TEXT,

    -- Processing & Lead Status
    status TEXT DEFAULT 'New' CHECK (status IN ('New', 'Contacted', 'In Discussion', 'Closed')),
    source TEXT DEFAULT 'Website' CHECK (source IN ('Website', 'Modal Enquiry', 'Phone Direct', 'WhatsApp', 'Manual')),
    ip_address TEXT,
    user_agent TEXT,
    notes TEXT
);

-- Indexes for efficient sorting and filtering
CREATE INDEX IF NOT EXISTS idx_enquiries_date ON public.enquiries (enquiry_date DESC);
CREATE INDEX IF NOT EXISTS idx_enquiries_created_at ON public.enquiries (created_at DESC);
CREATE INDEX IF NOT EXISTS idx_enquiries_status ON public.enquiries (status);
CREATE INDEX IF NOT EXISTS idx_enquiries_vertical ON public.enquiries (vertical);
CREATE INDEX IF NOT EXISTS idx_enquiries_mobile ON public.enquiries (mobile);

-- Trigger to automatically update updated_at timestamp on edit
CREATE OR REPLACE FUNCTION public.set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = TIMEZONE('utc'::text, NOW());
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trigger_set_enquiries_updated_at ON public.enquiries;
CREATE TRIGGER trigger_set_enquiries_updated_at
BEFORE UPDATE ON public.enquiries
FOR EACH ROW
EXECUTE FUNCTION public.set_updated_at();

-- Enable Row Level Security (RLS) on enquiries
ALTER TABLE public.enquiries ENABLE ROW LEVEL SECURITY;

-- Policy: Allow public (anon) to submit an enquiry
CREATE POLICY "Allow public insert to enquiries"
ON public.enquiries
FOR INSERT
TO anon, authenticated
WITH CHECK (true);

-- Policy: Allow service_role and authenticated users to read/update enquiries
CREATE POLICY "Allow read for service_role and authenticated"
ON public.enquiries
FOR SELECT
TO authenticated, service_role
USING (true);

CREATE POLICY "Allow update for service_role and authenticated"
ON public.enquiries
FOR UPDATE
TO authenticated, service_role
USING (true);


-- ==============================================================================
-- 3. SEED DEFAULT ADMIN USER (Username: admin | Password: Password@123)
-- SHA-256 Hash with salt 'ssg_salt_2026'
-- ==============================================================================
INSERT INTO public.admin_users (username, email, password_hash, salt, role, full_name)
VALUES (
    'admin',
    'admin@shreesudhakar.com',
    '4a6ce1780447fa471207e324040e2d83eef590e882a84dbe8a65c275fbdf7a8f',
    'ssg_salt_2026',
    'superadmin',
    'Administrator'
)
ON CONFLICT (username) DO NOTHING;

-- Verification Queries:
-- SELECT * FROM public.admin_users;
-- SELECT * FROM public.enquiries ORDER BY enquiry_date DESC;
