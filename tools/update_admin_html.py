import os

ADMIN_PAGE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Admin Dashboard | Shree Sudhakar Group Enquiries</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Inter', sans-serif; }
    h1, h2, h3, .brand-font { font-family: 'Outfit', sans-serif; }
  </style>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen antialiased selection:bg-amber-500 selection:text-slate-950">

  <!-- Admin Login Overlay Modal -->
  <div id="login-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/90 backdrop-blur-md p-4">
    <div class="bg-slate-900 border border-amber-500/40 rounded-2xl max-w-md w-full p-8 shadow-2xl relative">
      <div class="text-center mb-6">
        <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-amber-600 to-amber-400 flex items-center justify-center text-slate-950 font-black text-2xl mx-auto mb-3 shadow-lg shadow-amber-500/20">
          S
        </div>
        <h2 class="text-2xl font-bold text-white tracking-tight">Admin Authentication</h2>
        <p class="text-xs text-slate-400 mt-1">Shree Sudhakar Group Lead Portal</p>
      </div>

      <div id="login-error" class="hidden p-3 mb-4 rounded-lg bg-red-500/20 border border-red-500/40 text-red-300 text-xs font-semibold"></div>

      <form id="login-form" class="space-y-4">
        <div>
          <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-1">Username</label>
          <input id="login-username" type="text" required value="admin" class="w-full px-4 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-white focus:outline-none focus:border-amber-500 text-sm">
        </div>

        <div>
          <label class="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-1">Password</label>
          <input id="login-password" type="password" required value="Password@123" class="w-full px-4 py-2.5 rounded-lg bg-slate-950 border border-slate-700 text-white focus:outline-none focus:border-amber-500 text-sm">
        </div>

        <button id="login-btn" type="submit" class="w-full py-3 rounded-lg bg-gradient-to-r from-amber-500 to-amber-600 text-slate-950 font-bold text-sm uppercase tracking-wider hover:brightness-110 shadow-lg shadow-amber-500/20 transition-all">
          Sign In to Portal
        </button>

        <div class="text-center pt-2">
          <span class="text-[11px] text-slate-400">Default: <code class="text-amber-300 font-mono">admin</code> / <code class="text-amber-300 font-mono">Password@123</code></span>
        </div>
      </form>
    </div>
  </div>

  <!-- Header -->
  <header class="bg-slate-950 border-b border-amber-500/20 sticky top-0 z-30">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-amber-600 to-amber-400 flex items-center justify-center text-slate-950 font-black text-xl shadow-md">
          S
        </div>
        <div>
          <h1 class="text-xl font-bold text-white tracking-tight">
            Shree <span class="text-amber-400">Sudhakar Group</span>
          </h1>
          <p class="text-xs text-slate-400 font-medium">Enquiry Management & Lead Portal</p>
        </div>
      </div>

      <div class="flex items-center gap-3">
        <span id="logged-user-tag" class="text-xs text-amber-300 font-medium bg-amber-500/10 px-3 py-1.5 rounded-lg border border-amber-500/30 hidden sm:inline-block">
          Logged in: Admin
        </span>
        <a href="/" target="_blank" class="text-xs font-semibold px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition-colors flex items-center gap-1.5">
          <svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
          Website
        </a>
        <button id="refresh-btn" class="text-xs font-bold px-3 py-2 rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 transition-all flex items-center gap-1.5">
          <svg id="refresh-spinner" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
          Refresh
        </button>
        <button id="logout-btn" class="text-xs font-semibold px-3 py-2 rounded-lg bg-red-600/30 hover:bg-red-600/50 text-red-300 border border-red-500/30 transition-colors">
          Logout
        </button>
      </div>
    </div>
  </header>

  <!-- Main Content -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6">

    <!-- Metrics Cards -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
      <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-4">
        <div class="text-xs font-semibold uppercase tracking-wider text-slate-400">Total Enquiries</div>
        <div id="stat-total" class="text-3xl font-extrabold text-white mt-1">0</div>
      </div>
      <div class="bg-slate-800/80 border border-amber-500/30 rounded-xl p-4">
        <div class="text-xs font-semibold uppercase tracking-wider text-amber-400">New Leads</div>
        <div id="stat-new" class="text-3xl font-extrabold text-amber-400 mt-1">0</div>
      </div>
      <div class="bg-slate-800/80 border border-blue-500/30 rounded-xl p-4">
        <div class="text-xs font-semibold uppercase tracking-wider text-blue-400">Contacted / Discussion</div>
        <div id="stat-in-progress" class="text-3xl font-extrabold text-blue-400 mt-1">0</div>
      </div>
      <div class="bg-slate-800/80 border border-emerald-500/30 rounded-xl p-4">
        <div class="text-xs font-semibold uppercase tracking-wider text-emerald-400">Closed / Converted</div>
        <div id="stat-closed" class="text-3xl font-extrabold text-emerald-400 mt-1">0</div>
      </div>
    </div>

    <!-- Controls Bar -->
    <div class="bg-slate-800/90 border border-slate-700 rounded-xl p-4 flex flex-col md:flex-row items-center justify-between gap-4">
      
      <div class="flex flex-wrap items-center gap-3 w-full md:w-auto">
        <!-- Search Input -->
        <div class="relative flex-1 sm:w-64">
          <input id="search-input" type="text" placeholder="Search by name, phone, city..." class="w-full bg-slate-900 border border-slate-700 rounded-lg pl-9 pr-3 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-amber-500">
          <svg class="w-4 h-4 text-slate-500 absolute left-2.5 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        </div>

        <!-- Filter Status -->
        <select id="filter-status" class="bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-xs text-slate-300 focus:outline-none focus:border-amber-500">
          <option value="">All Statuses</option>
          <option value="New">New Only</option>
          <option value="Contacted">Contacted</option>
          <option value="In Discussion">In Discussion</option>
          <option value="Closed">Closed</option>
        </select>

        <!-- Filter Vertical -->
        <select id="filter-vertical" class="bg-slate-900 border border-slate-700 rounded-lg px-3 py-2 text-xs text-slate-300 focus:outline-none focus:border-amber-500">
          <option value="">All Verticals</option>
          <option value="Government">Government Projects</option>
          <option value="Gas Pipeline">Gas Pipeline</option>
          <option value="Electrical">Electrical Infrastructure</option>
          <option value="Road">Road & Civil</option>
          <option value="CNG">CNG & Petrol Pump</option>
          <option value="Residential">Residential & Commercial</option>
          <option value="Fabrication">Fabrication & PEB</option>
        </select>
      </div>

      <!-- Export Button -->
      <button id="export-btn" class="w-full md:w-auto text-xs font-semibold px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white transition-colors flex items-center justify-center gap-1.5 shrink-0">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
        Download CSV / Excel
      </button>

    </div>

    <!-- Enquiries Table Card -->
    <div class="bg-slate-800/90 border border-slate-700 rounded-xl overflow-hidden shadow-xl">
      <div class="p-4 border-b border-slate-700 flex justify-between items-center bg-slate-850">
        <h2 class="font-bold text-white text-sm flex items-center gap-2">
          Received Client Enquiries
          <span id="data-source-badge" class="text-[10px] px-2 py-0.5 rounded bg-slate-700 text-slate-300 font-mono">Loading...</span>
        </h2>
        <span id="table-count" class="text-xs text-slate-400">Showing 0 entries</span>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs text-slate-300">
          <thead class="bg-slate-900/80 text-slate-400 uppercase font-semibold text-[11px] tracking-wider border-b border-slate-700">
            <tr>
              <th class="py-3 px-4">Enquiry Date & Time</th>
              <th class="py-3 px-4">Client Name & City</th>
              <th class="py-3 px-4">Contact Info</th>
              <th class="py-3 px-4">Project Vertical</th>
              <th class="py-3 px-4">Scope / Message</th>
              <th class="py-3 px-4">Status</th>
            </tr>
          </thead>
          <tbody id="enquiries-tbody" class="divide-y divide-slate-700/60">
            <tr>
              <td colspan="6" class="text-center py-8 text-slate-400">Loading enquiries...</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </main>

  <script>
    let rawEnquiries = [];
    let currentSource = "";

    // Auth state check
    function checkAuth() {
      const logged = sessionStorage.getItem("admin_logged_in");
      const user = sessionStorage.getItem("admin_user");
      const modal = document.getElementById("login-modal");
      const userTag = document.getElementById("logged-user-tag");

      if (logged === "true") {
        modal.classList.add("hidden");
        if (userTag) {
          userTag.innerText = `Logged in: ${user || 'Admin'}`;
          userTag.classList.remove("hidden");
        }
        loadEnquiries();
      } else {
        modal.classList.remove("hidden");
      }
    }

    // Login submit
    document.getElementById("login-form").addEventListener("submit", async (e) => {
      e.preventDefault();
      const errBox = document.getElementById("login-error");
      errBox.classList.add("hidden");

      const username = document.getElementById("login-username").value.trim();
      const password = document.getElementById("login-password").value;

      try {
        const res = await fetch("/api/admin/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ username, password })
        });
        const data = await res.json();

        if (res.ok && data.success) {
          sessionStorage.setItem("admin_logged_in", "true");
          sessionStorage.setItem("admin_user", data.username);
          checkAuth();
        } else {
          errBox.innerText = data.detail || "Invalid credentials.";
          errBox.classList.remove("hidden");
        }
      } catch (err) {
        errBox.innerText = "Connection error. Ensure local server is running.";
        errBox.classList.remove("hidden");
      }
    });

    // Logout
    document.getElementById("logout-btn").addEventListener("click", () => {
      sessionStorage.removeItem("admin_logged_in");
      sessionStorage.removeItem("admin_user");
      checkAuth();
    });

    async function loadEnquiries() {
      const spinner = document.getElementById("refresh-spinner");
      spinner.classList.add("animate-spin");

      try {
        const res = await fetch("/api/admin/enquiries");
        const data = await res.json();
        rawEnquiries = data.enquiries || [];
        currentSource = data.source || "local";

        document.getElementById("data-source-badge").innerText = 
          currentSource === "supabase" ? "Supabase Cloud Database" : "Local Storage (local_enquiries.json)";

        updateStats();
        renderTable();
      } catch (err) {
        console.error("Error loading enquiries:", err);
        document.getElementById("enquiries-tbody").innerHTML = `
          <tr><td colspan="6" class="text-center py-8 text-red-400">Failed to connect to server. Please ensure server is running.</td></tr>
        `;
      } finally {
        setTimeout(() => spinner.classList.remove("animate-spin"), 400);
      }
    }

    function updateStats() {
      const total = rawEnquiries.length;
      const newCount = rawEnquiries.filter(e => (e.status || "New") === "New").length;
      const inProgress = rawEnquiries.filter(e => ["Contacted", "In Discussion"].includes(e.status)).length;
      const closed = rawEnquiries.filter(e => e.status === "Closed").length;

      document.getElementById("stat-total").innerText = total;
      document.getElementById("stat-new").innerText = newCount;
      document.getElementById("stat-in-progress").innerText = inProgress;
      document.getElementById("stat-closed").innerText = closed;
    }

    function renderTable() {
      const tbody = document.getElementById("enquiries-tbody");
      const search = document.getElementById("search-input").value.toLowerCase();
      const statusFilter = document.getElementById("filter-status").value;
      const verticalFilter = document.getElementById("filter-vertical").value.toLowerCase();

      const filtered = rawEnquiries.filter(item => {
        const matchesSearch = !search || 
          (item.name || "").toLowerCase().includes(search) || 
          (item.mobile || "").toLowerCase().includes(search) || 
          (item.city || "").toLowerCase().includes(search) ||
          (item.message || "").toLowerCase().includes(search);

        const matchesStatus = !statusFilter || (item.status || "New") === statusFilter;
        const matchesVertical = !verticalFilter || (item.vertical || "").toLowerCase().includes(verticalFilter);

        return matchesSearch && matchesStatus && matchesVertical;
      });

      document.getElementById("table-count").innerText = `Showing ${filtered.length} of ${rawEnquiries.length} entries`;

      if (filtered.length === 0) {
        tbody.innerHTML = `
          <tr><td colspan="6" class="text-center py-10 text-slate-400">No enquiries match your filter criteria.</td></tr>
        `;
        return;
      }

      tbody.innerHTML = filtered.map(item => {
        // Automated date & time display
        const dateStr = item.enquiry_date || (item.created_at ? item.created_at.slice(0,10) : "N/A");
        const timeStr = item.enquiry_time || (item.created_at ? item.created_at.slice(11,19) : "");
        
        const cleanMobile = (item.mobile || "").replace(/[^0-9]/g, "");
        const waLink = `https://wa.me/${cleanMobile}?text=${encodeURIComponent('Hello ' + (item.name || '') + ', this is regarding your enquiry with Shree Sudhakar Group.')}`;

        return `
          <tr class="hover:bg-slate-750/50 transition-colors">
            <td class="py-3 px-4 whitespace-nowrap">
              <div class="font-semibold text-white">${escapeHtml(dateStr)}</div>
              <div class="text-[11px] text-amber-400/80 font-mono">${escapeHtml(timeStr)} IST</div>
              <div class="text-[10px] text-slate-500 mt-0.5">${escapeHtml(item.source || 'Website')}</div>
            </td>
            <td class="py-3 px-4">
              <div class="text-sm font-bold text-white">${escapeHtml(item.name || "N/A")}</div>
              <div class="text-slate-400 text-[11px] flex items-center gap-1">
                <svg class="w-3 h-3 text-slate-500 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                ${escapeHtml(item.city || "Location not provided")}
              </div>
            </td>
            <td class="py-3 px-4">
              <div class="font-mono text-amber-400 font-semibold">${escapeHtml(item.mobile || "")}</div>
              ${item.email ? `<div class="text-[11px] text-slate-400">${escapeHtml(item.email)}</div>` : ""}
              <div class="flex items-center gap-2 mt-1">
                <a href="tel:${escapeHtml(item.mobile || '')}" class="text-[10px] px-2 py-0.5 rounded bg-slate-700 hover:bg-slate-600 text-slate-200">Call</a>
                <a href="${waLink}" target="_blank" rel="noopener" class="text-[10px] px-2 py-0.5 rounded bg-emerald-600 hover:bg-emerald-500 text-white font-semibold">WhatsApp</a>
              </div>
            </td>
            <td class="py-3 px-4">
              <span class="inline-block px-2.5 py-1 rounded-md text-[11px] font-semibold bg-slate-800 text-amber-300 border border-slate-700">
                ${escapeHtml(item.vertical || "General")}
              </span>
            </td>
            <td class="py-3 px-4 max-w-xs text-slate-300 break-words">
              ${escapeHtml(item.message || "No message provided")}
            </td>
            <td class="py-3 px-4 whitespace-nowrap">
              <select onchange="updateStatus('${item.id}', this.value)" class="bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-xs text-white focus:outline-none focus:border-amber-500 font-medium">
                <option value="New" ${item.status === "New" ? "selected" : ""}>New Lead</option>
                <option value="Contacted" ${item.status === "Contacted" ? "selected" : ""}>Contacted</option>
                <option value="In Discussion" ${item.status === "In Discussion" ? "selected" : ""}>In Discussion</option>
                <option value="Closed" ${item.status === "Closed" ? "selected" : ""}>Closed / Won</option>
              </select>
            </td>
          </tr>
        `;
      }).join("");
    }

    async function updateStatus(id, newStatus) {
      try {
        const res = await fetch(`/api/admin/enquiries/${id}/status`, {
          method: "PATCH",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ status: newStatus })
        });
        if (res.ok) {
          const item = rawEnquiries.find(e => String(e.id) === String(id));
          if (item) item.status = newStatus;
          updateStats();
        } else {
          alert("Could not update status.");
        }
      } catch (err) {
        console.error("Status update error:", err);
      }
    }

    function exportToCSV() {
      if (rawEnquiries.length === 0) {
        alert("No enquiries to export.");
        return;
      }
      const headers = ["Enquiry Date", "Enquiry Time", "Name", "Mobile", "Email", "Vertical", "City", "Message", "Status", "Source"];
      const rows = rawEnquiries.map(e => [
        `"${e.enquiry_date || (e.created_at ? e.created_at.slice(0,10) : '')}"`,
        `"${e.enquiry_time || (e.created_at ? e.created_at.slice(11,19) : '')}"`,
        `"${(e.name || "").replace(/"/g, '""')}"`,
        `"${(e.mobile || "").replace(/"/g, '""')}"`,
        `"${(e.email || "").replace(/"/g, '""')}"`,
        `"${(e.vertical || "").replace(/"/g, '""')}"`,
        `"${(e.city || "").replace(/"/g, '""')}"`,
        `"${(e.message || "").replace(/"/g, '""')}"`,
        `"${(e.status || "New").replace(/"/g, '""')}"`,
        `"${(e.source || "Website").replace(/"/g, '""')}"`
      ]);

      const csvContent = "data:text/csv;charset=utf-8," + [headers.join(","), ...rows.map(r => r.join(","))].join("\\n");
      const encodedUri = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", `shree_sudhakar_enquiries_${new Date().toISOString().slice(0,10)}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function escapeHtml(text) {
      const div = document.createElement("div");
      div.innerText = text;
      return div.innerHTML;
    }

    document.getElementById("refresh-btn").addEventListener("click", loadEnquiries);
    document.getElementById("search-input").addEventListener("input", renderTable);
    document.getElementById("filter-status").addEventListener("change", renderTable);
    document.getElementById("filter-vertical").addEventListener("change", renderTable);
    document.getElementById("export-btn").addEventListener("click", exportToCSV);

    checkAuth();
  </script>

</body>
</html>
"""

dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "admin.html")
with open(dest, "w", encoding="utf-8") as f:
    f.write(ADMIN_PAGE_HTML)
print(f"[OK] admin.html successfully updated at {dest} ({len(ADMIN_PAGE_HTML)} bytes)")
