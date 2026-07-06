-- ============================================================
-- Rocket Solutions - Supabase schema
-- Run this in the Supabase SQL editor (Dashboard > SQL Editor).
-- Creates the contact form table with Row Level Security so the
-- public site can insert leads but only signed-in admins can read them.
-- ============================================================

create extension if not exists "pgcrypto";  -- provides gen_random_uuid()

-- ------------------------------------------------------------
-- Table
-- ------------------------------------------------------------
create table if not exists public.contact_submissions (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  name        text not null check (char_length(name) between 1 and 200),
  company     text          check (company is null or char_length(company) <= 200),
  email       text not null check (char_length(email) between 3 and 320),
  phone       text          check (phone is null or char_length(phone) <= 40),
  interest    text          check (interest is null or char_length(interest) <= 80),
  message     text not null check (char_length(message) between 1 and 5000),
  status      text not null default 'new',   -- new | read | contacted | archived
  source      text default 'gorocketsolutions.com',
  page_url    text,
  user_agent  text
);

comment on table public.contact_submissions is 'Leads submitted through the Rocket Solutions website contact form.';

-- ------------------------------------------------------------
-- Row Level Security
-- ------------------------------------------------------------
alter table public.contact_submissions enable row level security;

-- Anonymous website visitors may INSERT only (no read, update, or delete).
drop policy if exists "public_insert_contact" on public.contact_submissions;
create policy "public_insert_contact"
  on public.contact_submissions
  for insert
  to anon
  with check (true);

-- Signed-in admins (your dashboard) may READ submissions.
drop policy if exists "authenticated_read_contact" on public.contact_submissions;
create policy "authenticated_read_contact"
  on public.contact_submissions
  for select
  to authenticated
  using (true);

-- Signed-in admins may UPDATE status (mark read / contacted / archived).
drop policy if exists "authenticated_update_contact" on public.contact_submissions;
create policy "authenticated_update_contact"
  on public.contact_submissions
  for update
  to authenticated
  using (true)
  with check (true);

-- ------------------------------------------------------------
-- Privileges (RLS gates the rows; these grant table access to the roles)
-- ------------------------------------------------------------
grant insert on public.contact_submissions to anon;
grant select, update on public.contact_submissions to authenticated;

-- ------------------------------------------------------------
-- Index for the admin list view
-- ------------------------------------------------------------
create index if not exists contact_submissions_created_at_idx
  on public.contact_submissions (created_at desc);

-- ============================================================
-- OPTIONAL: get notified when a lead comes in.
-- The cleanest way on Supabase is Dashboard > Database > Webhooks:
--   Table: contact_submissions, Event: INSERT
--   Send to an Edge Function or your existing notify endpoint (email / SMS).
-- You can reuse whatever notification flow you already run on your other
-- projects; the new row payload includes name, email, phone, and message.
-- ============================================================
