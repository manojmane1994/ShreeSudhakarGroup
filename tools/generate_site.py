import os

HTML_PART1 = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shree Sudhakar Group | Building Infrastructure. Powering Progress.</title>
  <meta name="description" content="Shree Sudhakar Group is a diversified infrastructure and engineering group in Pune & Maharashtra. Government projects, gas pipelines, electrical works, road construction, CNG stations, residential & commercial buildings, and PEB fabrication.">
  
  <!-- Tailwind CSS via CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            sunrise: {
              50: '#fffbeb',
              100: '#fef3c7',
              200: '#fde68a',
              300: '#fcd34d',
              400: '#fbbf24',
              500: '#f59e0b',
              600: '#d97706',
              700: '#b45309',
              800: '#92400e',
              900: '#78350f',
            },
            dawn: {
              900: '#0b1325',
              850: '#111c35',
              800: '#152238',
              700: '#1e293b'
            }
          }
        }
      }
    }
  </script>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">

  <!-- Custom Sunrise Styles -->
  <link rel="stylesheet" href="/static/css/sunrise.css">
  <style>
    h1, h2, h3, h4, .brand-font { font-family: 'Outfit', sans-serif; }
  </style>
</head>
<body class="bg-white text-slate-800 antialiased selection:bg-amber-500 selection:text-white">

  <!-- Top Announcement Bar -->
  <div class="bg-gradient-to-r from-dawn-900 via-dawn-850 to-dawn-900 text-slate-300 text-xs sm:text-sm py-2 px-4 border-b border-amber-500/20">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row justify-between items-center gap-2">
      <div class="flex items-center gap-4">
        <span class="inline-flex items-center gap-1.5 text-amber-400 font-medium">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
          Moshi - Alandi Road, Pimpri-Chinchwad, Maharashtra
        </span>
      </div>
      <div class="flex items-center gap-5">
        <a href="tel:+919689820892" class="hover:text-amber-400 transition-colors flex items-center gap-1 font-semibold text-white">
          <svg class="w-3.5 h-3.5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
          Enquiry: +91 9689820892
        </a>
        <button class="open-enquiry-modal text-amber-400 hover:underline text-xs font-semibold uppercase tracking-wider">
          Quick Request &rarr;
        </button>
      </div>
    </div>
  </div>

  <!-- Main Navigation -->
  <header class="sticky top-0 z-50 nav-glass">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        
        <!-- Logo & Brand Name -->
        <a href="#" class="flex items-center gap-3 group">
          <div class="w-11 h-11 rounded-xl sunrise-gradient-bg flex items-center justify-center text-dawn-900 font-extrabold text-2xl shadow-lg shadow-amber-500/30 group-hover:rotate-3 transition-transform">
            S
          </div>
          <div>
            <span class="text-xl sm:text-2xl font-bold tracking-tight text-white block">
              Shree <span class="sunrise-gradient-text">Sudhakar Group</span>
            </span>
            <span class="text-[10px] sm:text-xs text-amber-400/90 tracking-wider uppercase font-semibold block">
              Infrastructure & Engineering
            </span>
          </div>
        </a>

        <!-- Desktop Menu -->
        <nav class="hidden md:flex items-center gap-7 text-sm font-medium text-slate-200">
          <a href="#about" class="hover:text-amber-400 transition-colors">About Us</a>
          <a href="#verticals" class="hover:text-amber-400 transition-colors">Business Verticals</a>
          <a href="#capabilities" class="hover:text-amber-400 transition-colors">Capabilities</a>
          <a href="#projects" class="hover:text-amber-400 transition-colors">Projects</a>
          <a href="#why-us" class="hover:text-amber-400 transition-colors">Why Choose Us</a>
          <a href="#contact" class="hover:text-amber-400 transition-colors">Contact</a>
          <a href="/admin" class="hover:text-amber-400 transition-colors">Admin Portal</a>
        </nav>

        <!-- CTA Action -->
        <div class="hidden lg:flex items-center gap-3">
          <a href="tel:+919689820892" class="px-4 py-2 text-sm font-semibold text-white border border-amber-500/40 rounded-lg hover:border-amber-400 transition-all flex items-center gap-2">
            <svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
            Call Us
          </a>
          <button class="open-enquiry-modal px-5 py-2.5 text-sm font-bold text-slate-950 sunrise-gradient-bg rounded-lg shadow-md hover:shadow-amber-500/40 hover:brightness-105 transition-all">
            Enquire Now
          </button>
        </div>

        <!-- Mobile Hamburger Button -->
        <button id="mobile-menu-btn" class="md:hidden p-2 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800/60 focus:outline-none" aria-label="Toggle Navigation">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
        </button>

      </div>
    </div>

    <!-- Mobile Dropdown Menu -->
    <div id="mobile-menu" class="hidden md:hidden bg-dawn-900 border-b border-amber-500/20 px-4 pt-3 pb-6 space-y-3 text-slate-200">
      <a href="#about" class="block py-2 text-base font-medium hover:text-amber-400 border-b border-slate-800">About Us</a>
      <a href="#verticals" class="block py-2 text-base font-medium hover:text-amber-400 border-b border-slate-800">Business Verticals</a>
      <a href="#capabilities" class="block py-2 text-base font-medium hover:text-amber-400 border-b border-slate-800">Capabilities</a>
      <a href="#projects" class="block py-2 text-base font-medium hover:text-amber-400 border-b border-slate-800">Projects</a>
      <a href="#why-us" class="block py-2 text-base font-medium hover:text-amber-400 border-b border-slate-800">Why Choose Us</a>
      <a href="#contact" class="block py-2 text-base font-medium hover:text-amber-400 border-b border-slate-800">Contact</a>
      <div class="pt-2 flex flex-col gap-2">
        <a href="tel:+919689820892" class="w-full text-center py-2.5 text-sm font-semibold border border-amber-500/40 rounded-lg text-white">Call +91 9689820892</a>
        <button class="open-enquiry-modal w-full py-2.5 text-sm font-bold text-slate-950 sunrise-gradient-bg rounded-lg">Submit Enquiry</button>
      </div>
    </div>
  </header>
"""
HTML_PART2 = """
  <!-- Hero Section with Sunrise Background -->
  <section class="hero-sunrise-bg min-h-[92vh] flex items-center relative overflow-hidden py-20">
    <div class="sunrise-ray"></div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Left Hero Content -->
        <div class="lg:col-span-7 space-y-6 text-left">
          
          <!-- Dawn Badge -->
          <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs sm:text-sm font-semibold backdrop-blur-md">
            <span class="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
            Engineering Excellence • Infrastructure Development
          </div>

          <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white leading-tight tracking-tight">
            Building Infrastructure. <br>
            <span class="sunrise-gradient-text">Powering Progress.</span>
          </h1>

          <p class="text-base sm:text-lg text-slate-300 max-w-2xl leading-relaxed font-normal">
            <strong>Shree Sudhakar Group</strong> is a diversified infrastructure and engineering group engaged in government projects, gas pipeline infrastructure, electrical works, road and civil construction, CNG and petrol pump development, residential and commercial buildings, and PEB structural fabrication.
          </p>

          <!-- Core stats / metrics -->
          <div class="grid grid-cols-3 gap-4 pt-2 max-w-lg border-y border-amber-500/20 py-4">
            <div>
              <div class="text-2xl sm:text-3xl font-extrabold text-amber-400 counter-num">7+</div>
              <div class="text-xs text-slate-300">Core Verticals</div>
            </div>
            <div>
              <div class="text-2xl sm:text-3xl font-extrabold text-amber-400 counter-num">100%</div>
              <div class="text-xs text-slate-300">Timely Delivery</div>
            </div>
            <div>
              <div class="text-2xl sm:text-3xl font-extrabold text-amber-400 counter-num">End-to-End</div>
              <div class="text-xs text-slate-300">Project Execution</div>
            </div>
          </div>

          <!-- Buttons -->
          <div class="flex flex-wrap gap-4 pt-2">
            <button class="open-enquiry-modal px-7 py-3.5 rounded-xl sunrise-gradient-bg text-slate-950 font-bold text-base sunrise-glow-shadow hover:brightness-110 transition-all transform hover:-translate-y-0.5">
              Submit Enquiry Now
            </button>
            <a href="#verticals" class="px-6 py-3.5 rounded-xl border border-white/30 text-white font-semibold text-base hover:bg-white/10 backdrop-blur-sm transition-all">
              Our Verticals &rarr;
            </a>
          </div>

          <!-- Sector ticker -->
          <div class="pt-3">
            <span class="text-xs uppercase tracking-widest text-slate-400 font-semibold block mb-2">Key Project Domains:</span>
            <div class="flex flex-wrap gap-2 text-xs text-slate-300">
              <span class="px-2.5 py-1 bg-slate-900/60 rounded border border-slate-700">Govt Infrastructure</span>
              <span class="px-2.5 py-1 bg-slate-900/60 rounded border border-slate-700">Gas Pipelines</span>
              <span class="px-2.5 py-1 bg-slate-900/60 rounded border border-slate-700">Electrical Solutions</span>
              <span class="px-2.5 py-1 bg-slate-900/60 rounded border border-slate-700">CNG & Fuel Pumps</span>
              <span class="px-2.5 py-1 bg-slate-900/60 rounded border border-slate-700">PEB & Fabrication</span>
            </div>
          </div>

        </div>

        <!-- Right Quick Enquiry Card (Embedded in Hero for high conversion) -->
        <div class="lg:col-span-5">
          <div class="bg-dawn-850/95 backdrop-blur-xl border border-amber-500/30 rounded-2xl p-6 sm:p-8 shadow-2xl relative">
            <div class="absolute -top-3.5 right-6 px-3 py-1 sunrise-gradient-bg text-slate-950 text-xs font-extrabold rounded-full uppercase tracking-wider shadow">
              Instant Connect
            </div>

            <h3 class="text-2xl font-bold text-white mb-2">Request a Consultation</h3>
            <p class="text-sm text-slate-300 mb-6">Connect with our engineering specialists for commercial, civil, or infrastructure requirements.</p>

            <form id="page-enquiry-form" class="space-y-4">
              <div id="page-form-feedback" class="hidden p-3 rounded-lg text-sm mb-4"></div>

              <div>
                <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Your Name *</label>
                <input type="text" name="name" required placeholder="e.g. Rajesh Patil" class="w-full px-4 py-2.5 rounded-lg bg-slate-900/80 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:border-amber-500 focus:ring-1 focus:ring-amber-500 text-sm">
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <div>
                  <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Mobile Number *</label>
                  <input type="tel" name="mobile" required placeholder="+91 9876543210" class="w-full px-4 py-2.5 rounded-lg bg-slate-900/80 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:border-amber-500 focus:ring-1 focus:ring-amber-500 text-sm">
                </div>
                <div>
                  <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">City / Location</label>
                  <input type="text" name="city" placeholder="Pune / Maharashtra" class="w-full px-4 py-2.5 rounded-lg bg-slate-900/80 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:border-amber-500 focus:ring-1 focus:ring-amber-500 text-sm">
                </div>
              </div>

              <div>
                <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Project Vertical *</label>
                <select name="vertical" class="w-full px-4 py-2.5 rounded-lg bg-slate-900/80 border border-slate-700 text-white focus:outline-none focus:border-amber-500 focus:ring-1 focus:ring-amber-500 text-sm">
                  <option value="Government Infrastructure">Government Infrastructure & Projects</option>
                  <option value="Gas Pipeline Infrastructure">Gas Pipeline Infrastructure</option>
                  <option value="Electrical Infrastructure">Electrical Works & Infrastructure</option>
                  <option value="Road & Civil Construction">Road & Civil Construction</option>
                  <option value="CNG & Petrol Pump Projects">CNG & Petrol Pump Projects</option>
                  <option value="Residential & Commercial">Residential & Commercial Construction</option>
                  <option value="Fabrication & PEB Structures">Fabrication & PEB Structures</option>
                </select>
              </div>

              <div>
                <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Project Details / Message</label>
                <textarea name="message" rows="2" placeholder="Describe project scope, timeline, or site details..." class="w-full px-4 py-2.5 rounded-lg bg-slate-900/80 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:border-amber-500 focus:ring-1 focus:ring-amber-500 text-sm"></textarea>
              </div>

              <button id="page-submit-btn" type="submit" class="w-full py-3.5 rounded-xl sunrise-gradient-bg text-slate-950 font-extrabold text-sm uppercase tracking-wider hover:brightness-110 shadow-lg shadow-amber-500/30 transition-all">
                Submit Enquiry
              </button>

              <div class="text-center pt-1">
                <span class="text-xs text-slate-400">Direct Contact: <a href="tel:+919689820892" class="text-amber-400 font-semibold hover:underline">+91 9689820892</a></span>
              </div>
            </form>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- About Us Section -->
  <section id="about" class="py-24 bg-white relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="gold-badge text-xs font-bold uppercase tracking-widest px-3.5 py-1.5 rounded-full inline-block mb-3">
          About Shri Sudhakar Group
        </span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
          Who We Are & What We Stand For
        </h2>
        <p class="mt-4 text-slate-600 leading-relaxed text-base sm:text-lg">
          Shri Sudhakar Group is an engineering and infrastructure-focused business group undertaking projects across multiple sectors including government infrastructure, energy, construction, civil engineering, electrical works, and fabrication.
        </p>
      </div>

      <!-- 5 Core Pillars -->
      <div class="mb-16 bg-gradient-to-br from-amber-500/10 via-amber-500/5 to-slate-50 p-8 rounded-2xl border border-amber-200/60">
        <div class="text-center mb-6">
          <span class="text-xs uppercase font-bold tracking-wider text-amber-800">Our Foundational Approach</span>
          <h3 class="text-xl font-bold text-slate-900 mt-1">Engineered for Uncompromising Standards</h3>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-5 gap-4 text-center">
          <div class="p-4 bg-white rounded-xl shadow-sm border border-amber-100">
            <div class="w-10 h-10 mx-auto mb-2 rounded-full bg-amber-100 flex items-center justify-center text-amber-700 font-bold">1</div>
            <div class="font-bold text-slate-900 text-sm">Quality</div>
            <div class="text-xs text-slate-500 mt-0.5">Top-grade engineering</div>
          </div>
          <div class="p-4 bg-white rounded-xl shadow-sm border border-amber-100">
            <div class="w-10 h-10 mx-auto mb-2 rounded-full bg-amber-100 flex items-center justify-center text-amber-700 font-bold">2</div>
            <div class="font-bold text-slate-900 text-sm">Safety</div>
            <div class="text-xs text-slate-500 mt-0.5">Zero-incident focus</div>
          </div>
          <div class="p-4 bg-white rounded-xl shadow-sm border border-amber-100">
            <div class="w-10 h-10 mx-auto mb-2 rounded-full bg-amber-100 flex items-center justify-center text-amber-700 font-bold">3</div>
            <div class="font-bold text-slate-900 text-sm">Timely Execution</div>
            <div class="text-xs text-slate-500 mt-0.5">Strict project timelines</div>
          </div>
          <div class="p-4 bg-white rounded-xl shadow-sm border border-amber-100">
            <div class="w-10 h-10 mx-auto mb-2 rounded-full bg-amber-100 flex items-center justify-center text-amber-700 font-bold">4</div>
            <div class="font-bold text-slate-900 text-sm">Engineering Excellence</div>
            <div class="text-xs text-slate-500 mt-0.5">Technical rigor</div>
          </div>
          <div class="p-4 bg-white rounded-xl shadow-sm border border-amber-100 col-span-2 md:col-span-1">
            <div class="w-10 h-10 mx-auto mb-2 rounded-full bg-amber-100 flex items-center justify-center text-amber-700 font-bold">5</div>
            <div class="font-bold text-slate-900 text-sm">Customer Satisfaction</div>
            <div class="text-xs text-slate-500 mt-0.5">Long-term trust</div>
          </div>
        </div>
      </div>

      <!-- Strengths Grid -->
      <div>
        <div class="text-center mb-8">
          <h3 class="text-2xl font-bold text-slate-900">Our Key Strengths</h3>
          <p class="text-sm text-slate-500">Comprehensive end-to-end execution capabilities across diverse disciplines</p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="p-5 rounded-xl border border-slate-200 bg-white hover:border-amber-400 sunrise-card-glow transition-smooth">
            <div class="w-10 h-10 rounded-lg bg-amber-500/10 text-amber-600 flex items-center justify-center mb-3">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
            </div>
            <h4 class="font-bold text-slate-900 mb-1">Multidisciplinary Execution</h4>
            <p class="text-xs text-slate-600 leading-relaxed">Single-source delivery combining civil, structural, electrical, and mechanical disciplines.</p>
          </div>

          <div class="p-5 rounded-xl border border-slate-200 bg-white hover:border-amber-400 sunrise-card-glow transition-smooth">
            <div class="w-10 h-10 rounded-lg bg-amber-500/10 text-amber-600 flex items-center justify-center mb-3">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
            </div>
            <h4 class="font-bold text-slate-900 mb-1">Civil & Infrastructure</h4>
            <p class="text-xs text-slate-600 leading-relaxed">Deep domain expertise in earthworks, roads, bridges, RCC structures, and public infrastructure.</p>
          </div>

          <div class="p-5 rounded-xl border border-slate-200 bg-white hover:border-amber-400 sunrise-card-glow transition-smooth">
            <div class="w-10 h-10 rounded-lg bg-amber-500/10 text-amber-600 flex items-center justify-center mb-3">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
            </div>
            <h4 class="font-bold text-slate-900 mb-1">Mechanical & Electrical</h4>
            <p class="text-xs text-slate-600 leading-relaxed">High-capacity cable laying, utility electrification, equipment installations, and piping works.</p>
          </div>

          <div class="p-5 rounded-xl border border-slate-200 bg-white hover:border-amber-400 sunrise-card-glow transition-smooth">
            <div class="w-10 h-10 rounded-lg bg-amber-500/10 text-amber-600 flex items-center justify-center mb-3">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
            </div>
            <h4 class="font-bold text-slate-900 mb-1">Pipeline Construction</h4>
            <p class="text-xs text-slate-600 leading-relaxed">Extensive experience in gas pipelines, trenching, city gas distribution, MDPE/steel routes.</p>
          </div>

          <div class="p-5 rounded-xl border border-slate-200 bg-white hover:border-amber-400 sunrise-card-glow transition-smooth">
            <div class="w-10 h-10 rounded-lg bg-amber-500/10 text-amber-600 flex items-center justify-center mb-3">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path></svg>
            </div>
            <h4 class="font-bold text-slate-900 mb-1">Structural Fabrication & PEB</h4>
            <p class="text-xs text-slate-600 leading-relaxed">Precision fabrication of heavy steel columns, trusses, Pre-Engineered Buildings, and industrial sheds.</p>
          </div>

          <div class="p-5 rounded-xl border border-slate-200 bg-white hover:border-amber-400 sunrise-card-glow transition-smooth">
            <div class="w-10 h-10 rounded-lg bg-amber-500/10 text-amber-600 flex items-center justify-center mb-3">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 14v3m4-3v3m4-3v3M3 21h18M3 10h18M3 7l9-4 9 4M4 10h16v11H4V10z"></path></svg>
            </div>
            <h4 class="font-bold text-slate-900 mb-1">Government Projects</h4>
            <p class="text-xs text-slate-600 leading-relaxed">Trusted compliance, tender execution, safety records, and adherence to public sector standards.</p>
          </div>

          <div class="p-5 rounded-xl border border-slate-200 bg-white hover:border-amber-400 sunrise-card-glow transition-smooth">
            <div class="w-10 h-10 rounded-lg bg-amber-500/10 text-amber-600 flex items-center justify-center mb-3">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg>
            </div>
            <h4 class="font-bold text-slate-900 mb-1">Residential & Commercial</h4>
            <p class="text-xs text-slate-600 leading-relaxed">Turnkey construction for apartments, commercial complexes, retail spaces, and offices.</p>
          </div>

          <div class="p-5 rounded-xl border border-slate-200 bg-white hover:border-amber-400 sunrise-card-glow transition-smooth">
            <div class="w-10 h-10 rounded-lg bg-amber-500/10 text-amber-600 flex items-center justify-center mb-3">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path></svg>
            </div>
            <h4 class="font-bold text-slate-900 mb-1">Site & Project Management</h4>
            <p class="text-xs text-slate-600 leading-relaxed">Dedicated supervision, rigorous quality checks, modern machinery, and milestone-driven completion.</p>
          </div>
        </div>
      </div>

    </div>
  </section>
"""
HTML_PART3 = """
  <!-- Business Verticals Section -->
  <section id="verticals" class="py-24 bg-slate-50 border-t border-slate-200 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="gold-badge text-xs font-bold uppercase tracking-widest px-3.5 py-1.5 rounded-full inline-block mb-3">
          Our Business Verticals
        </span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
          Comprehensive Capabilities Across Key Sectors
        </h2>
        <p class="mt-4 text-slate-600 text-base sm:text-lg">
          Shree Sudhakar Group delivers end-to-end solutions across civil, mechanical, electrical, pipeline, fabrication, and infrastructure projects.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <!-- Vertical 1: Government Projects -->
        <div class="bg-white rounded-2xl p-7 border border-slate-200 shadow-sm hover:border-amber-400 sunrise-card-glow transition-smooth flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-600 flex items-center justify-center font-bold text-xl mb-5">
              01
            </div>
            <h3 class="text-xl font-bold text-slate-900 mb-2">Government Infrastructure & Development</h3>
            <p class="text-sm text-slate-600 mb-4 leading-relaxed">
              Execution of infrastructure and construction projects for government and public-sector requirements, with uncompromising focus on quality, compliance, safety, and timely completion.
            </p>
            <div class="space-y-1.5 text-xs text-slate-700 font-medium mb-6">
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Civil infrastructure & site development</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Road construction & earthwork</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Government & institutional buildings</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Utility & pipeline infrastructure</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Public sector electrical works</div>
            </div>
          </div>
          <button class="open-enquiry-modal w-full py-2.5 px-4 rounded-lg border border-amber-500/40 text-amber-700 font-semibold text-xs uppercase tracking-wider hover:bg-amber-500 hover:text-slate-950 transition-all" data-vertical="Government Infrastructure">
            Enquire for Govt Projects &rarr;
          </button>
        </div>

        <!-- Vertical 2: Gas Pipeline -->
        <div class="bg-white rounded-2xl p-7 border border-slate-200 shadow-sm hover:border-amber-400 sunrise-card-glow transition-smooth flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-600 flex items-center justify-center font-bold text-xl mb-5">
              02
            </div>
            <h3 class="text-xl font-bold text-slate-900 mb-2">Gas Pipeline Infrastructure</h3>
            <p class="text-sm text-slate-600 mb-4 leading-relaxed">
              End-to-end civil and associated infrastructure works for natural gas and energy pipelines, supporting the development of reliable energy networks.
            </p>
            <div class="space-y-1.5 text-xs text-slate-700 font-medium mb-6">
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Gas pipeline civil & trenching works</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Route development & excavation</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> MDPE, PE, & Steel pipeline civil support</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Road restoration & civil structures</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> City Gas Distribution (CGD) projects</div>
            </div>
          </div>
          <button class="open-enquiry-modal w-full py-2.5 px-4 rounded-lg border border-amber-500/40 text-amber-700 font-semibold text-xs uppercase tracking-wider hover:bg-amber-500 hover:text-slate-950 transition-all" data-vertical="Gas Pipeline Infrastructure">
            Enquire for Pipeline Works &rarr;
          </button>
        </div>

        <!-- Vertical 3: Electrical Infrastructure -->
        <div class="bg-white rounded-2xl p-7 border border-slate-200 shadow-sm hover:border-amber-400 sunrise-card-glow transition-smooth flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-600 flex items-center justify-center font-bold text-xl mb-5">
              03
            </div>
            <h3 class="text-xl font-bold text-slate-900 mb-2">Electrical Works & Infrastructure</h3>
            <p class="text-sm text-slate-600 mb-4 leading-relaxed">
              High-voltage and utility electrical solutions for industrial, commercial, infrastructure, and urban construction projects.
            </p>
            <div class="space-y-1.5 text-xs text-slate-700 font-medium mb-6">
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Electrical infrastructure & cable laying</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Commercial & industrial installation</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Utility distribution infrastructure</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Site electrical systems & panels</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Support for heavy construction sites</div>
            </div>
          </div>
          <button class="open-enquiry-modal w-full py-2.5 px-4 rounded-lg border border-amber-500/40 text-amber-700 font-semibold text-xs uppercase tracking-wider hover:bg-amber-500 hover:text-slate-950 transition-all" data-vertical="Electrical Infrastructure">
            Enquire for Electrical &rarr;
          </button>
        </div>

        <!-- Vertical 4: Road & Civil Construction -->
        <div class="bg-white rounded-2xl p-7 border border-slate-200 shadow-sm hover:border-amber-400 sunrise-card-glow transition-smooth flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-600 flex items-center justify-center font-bold text-xl mb-5">
              04
            </div>
            <h3 class="text-xl font-bold text-slate-900 mb-2">Road & Civil Construction</h3>
            <p class="text-sm text-slate-600 mb-4 leading-relaxed">
              Comprehensive civil construction capabilities for arterial roads, urban corridors, highways, foundations, and heavy concrete structures.
            </p>
            <div class="space-y-1.5 text-xs text-slate-700 font-medium mb-6">
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Road construction & macadam paving</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Excavation, earthwork & grading</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Stormwater drainage & culverts</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> RCC structures & heavy foundations</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Utility corridors & site restoration</div>
            </div>
          </div>
          <button class="open-enquiry-modal w-full py-2.5 px-4 rounded-lg border border-amber-500/40 text-amber-700 font-semibold text-xs uppercase tracking-wider hover:bg-amber-500 hover:text-slate-950 transition-all" data-vertical="Road & Civil Construction">
            Enquire for Civil & Roads &rarr;
          </button>
        </div>

        <!-- Vertical 5: CNG & Petrol Pump Projects -->
        <div class="bg-white rounded-2xl p-7 border border-amber-300 shadow-md hover:border-amber-500 sunrise-card-glow transition-smooth flex flex-col justify-between relative bg-gradient-to-b from-white to-amber-50/30">
          <div class="absolute top-4 right-4 text-[11px] font-bold uppercase tracking-wider px-2 py-0.5 bg-amber-500 text-slate-950 rounded">
            Key Vertical
          </div>
          <div>
            <div class="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-700 flex items-center justify-center font-bold text-xl mb-5">
              05
            </div>
            <h3 class="text-xl font-bold text-slate-900 mb-2">CNG & Petrol Pump Development</h3>
            <p class="text-sm text-slate-600 mb-4 leading-relaxed">
              Full turnkey civil and mechanical execution for CNG fueling stations and retail petroleum retail outlets across urban and highway corridors.
            </p>
            <div class="space-y-1.5 text-xs text-slate-700 font-medium mb-6">
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Site development & paving</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Canopy & RCC equipment foundations</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Office & retail kiosk construction</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> CNG station piping & compressor beds</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Mechanical installation support</div>
            </div>
          </div>
          <button class="open-enquiry-modal w-full py-2.5 px-4 rounded-lg sunrise-gradient-bg text-slate-950 font-bold text-xs uppercase tracking-wider hover:brightness-110 transition-all" data-vertical="CNG & Petrol Pump Projects">
            Enquire for Fuel Station Works &rarr;
          </button>
        </div>

        <!-- Vertical 6: Residential & Commercial Construction -->
        <div class="bg-white rounded-2xl p-7 border border-slate-200 shadow-sm hover:border-amber-400 sunrise-card-glow transition-smooth flex flex-col justify-between">
          <div>
            <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-600 flex items-center justify-center font-bold text-xl mb-5">
              06
            </div>
            <h3 class="text-xl font-bold text-slate-900 mb-2">Residential & Commercial Construction</h3>
            <p class="text-sm text-slate-600 mb-4 leading-relaxed">
              High-standard construction for residential apartments, villas, commercial office buildings, and retail complexes with complete MEP coordination.
            </p>
            <div class="space-y-1.5 text-xs text-slate-700 font-medium mb-6">
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Residential apartments & villas</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Commercial complexes & corporate offices</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> RCC structure design & execution</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Masonry, plastering & finishing works</div>
              <div class="flex items-center gap-2"><span class="text-amber-500">&bull;</span> Integrated MEP site coordination</div>
            </div>
          </div>
          <button class="open-enquiry-modal w-full py-2.5 px-4 rounded-lg border border-amber-500/40 text-amber-700 font-semibold text-xs uppercase tracking-wider hover:bg-amber-500 hover:text-slate-950 transition-all" data-vertical="Residential & Commercial">
            Enquire for Construction &rarr;
          </button>
        </div>

        <!-- Vertical 7: Fabrication & PEB Structures (Wide) -->
        <div class="bg-white rounded-2xl p-7 border border-slate-200 shadow-sm hover:border-amber-400 sunrise-card-glow transition-smooth flex flex-col justify-between md:col-span-2 lg:col-span-3">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
            <div class="lg:col-span-4">
              <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-600 flex items-center justify-center font-bold text-xl mb-4">
                07
              </div>
              <h3 class="text-2xl font-bold text-slate-900 mb-2">Conventional & PEB Structural Fabrication</h3>
              <p class="text-sm text-slate-600 leading-relaxed">
                Shree Sudhakar Group provides structural fabrication solutions covering conventional heavy steel structures as well as modern Pre-Engineered Buildings (PEB).
              </p>
            </div>
            <div class="lg:col-span-5 grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
              <div class="p-3 bg-slate-50 rounded-lg border border-slate-200">
                <div class="font-bold text-slate-900 mb-1">Conventional Steel</div>
                <ul class="text-slate-600 space-y-1">
                  <li>&bull; Heavy columns & beams</li>
                  <li>&bull; Industrial trusses</li>
                  <li>&bull; Platforms & staircases</li>
                  <li>&bull; Custom structural steel</li>
                </ul>
              </div>
              <div class="p-3 bg-slate-50 rounded-lg border border-slate-200">
                <div class="font-bold text-slate-900 mb-1">PEB Solutions</div>
                <ul class="text-slate-600 space-y-1">
                  <li>&bull; Industrial sheds & warehouses</li>
                  <li>&bull; Commercial steel structures</li>
                  <li>&bull; Workshops & logistics parks</li>
                  <li>&bull; Rapid PEB erection & roofing</li>
                </ul>
              </div>
            </div>
            <div class="lg:col-span-3 flex justify-center lg:justify-end">
              <button class="open-enquiry-modal px-6 py-3.5 rounded-xl sunrise-gradient-bg text-slate-950 font-bold text-sm uppercase tracking-wider hover:brightness-110 transition-all" data-vertical="Fabrication & PEB Structures">
                Enquire for PEB & Steel &rarr;
              </button>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>
"""
HTML_PART4 = """
  <!-- Project Showcase Section -->
  <section id="projects" class="py-24 bg-white relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-16">
        <div>
          <span class="gold-badge text-xs font-bold uppercase tracking-widest px-3.5 py-1.5 rounded-full inline-block mb-3">
            Track Record
          </span>
          <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
            Featured Projects & Execution Highlights
          </h2>
          <p class="mt-2 text-slate-600 max-w-xl">
            Real projects delivered with engineering discipline, adherence to strict safety standards, and timely execution.
          </p>
        </div>
        <div class="mt-4 md:mt-0">
          <button class="open-enquiry-modal inline-flex items-center gap-2 text-sm font-bold text-amber-600 hover:text-amber-700">
            Discuss Your Project Scope &rarr;
          </button>
        </div>
      </div>

      <!-- Project Cards Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <!-- Project 1 -->
        <div class="border border-slate-200 rounded-2xl p-6 bg-white hover:border-amber-400 sunrise-card-glow transition-smooth">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-blue-50 text-blue-700 border border-blue-200">Energy / Gas</span>
            <span class="text-xs font-bold text-green-700 bg-green-50 px-2 py-0.5 rounded">Completed</span>
          </div>
          <h3 class="text-lg font-bold text-slate-900 mb-2">Gas Pipeline Infrastructure Project</h3>
          <div class="text-xs text-slate-500 space-y-1.5 border-t border-slate-100 pt-3">
            <div><strong class="text-slate-700">Sector:</strong> Energy / Gas Infrastructure</div>
            <div><strong class="text-slate-700">Location:</strong> Maharashtra</div>
            <div><strong class="text-slate-700">Scope:</strong> Trenching, Civil & Pipeline Laying</div>
          </div>
        </div>

        <!-- Project 2 -->
        <div class="border border-slate-200 rounded-2xl p-6 bg-white hover:border-amber-400 sunrise-card-glow transition-smooth">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-amber-50 text-amber-800 border border-amber-200">CNG / Energy</span>
            <span class="text-xs font-bold text-green-700 bg-green-50 px-2 py-0.5 rounded">Completed</span>
          </div>
          <h3 class="text-lg font-bold text-slate-900 mb-2">CNG Station Development</h3>
          <div class="text-xs text-slate-500 space-y-1.5 border-t border-slate-100 pt-3">
            <div><strong class="text-slate-700">Sector:</strong> CNG / Retail Energy</div>
            <div><strong class="text-slate-700">Location:</strong> Maharashtra Corridor</div>
            <div><strong class="text-slate-700">Scope:</strong> Civil Foundations, Mechanical Piping</div>
          </div>
        </div>

        <!-- Project 3 -->
        <div class="border border-slate-200 rounded-2xl p-6 bg-white hover:border-amber-400 sunrise-card-glow transition-smooth">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-purple-50 text-purple-700 border border-purple-200">Govt / Civil</span>
            <span class="text-xs font-bold text-green-700 bg-green-50 px-2 py-0.5 rounded">Completed</span>
          </div>
          <h3 class="text-lg font-bold text-slate-900 mb-2">Government Road & Civil Works</h3>
          <div class="text-xs text-slate-500 space-y-1.5 border-t border-slate-100 pt-3">
            <div><strong class="text-slate-700">Sector:</strong> Public Infrastructure</div>
            <div><strong class="text-slate-700">Location:</strong> Pimpri-Chinchwad / Pune Region</div>
            <div><strong class="text-slate-700">Scope:</strong> Road Works, Earthmoving & Drainage</div>
          </div>
        </div>

        <!-- Project 4 -->
        <div class="border border-slate-200 rounded-2xl p-6 bg-white hover:border-amber-400 sunrise-card-glow transition-smooth">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-orange-50 text-orange-700 border border-orange-200">Industrial / PEB</span>
            <span class="text-xs font-bold text-green-700 bg-green-50 px-2 py-0.5 rounded">Completed</span>
          </div>
          <h3 class="text-lg font-bold text-slate-900 mb-2">PEB Industrial Warehousing Shed</h3>
          <div class="text-xs text-slate-500 space-y-1.5 border-t border-slate-100 pt-3">
            <div><strong class="text-slate-700">Sector:</strong> Industrial & Logistics</div>
            <div><strong class="text-slate-700">Location:</strong> Maharashtra</div>
            <div><strong class="text-slate-700">Scope:</strong> Structural Steel Fabrication & PEB Erection</div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- Capabilities Matrix & Industries Served -->
  <section id="capabilities" class="py-24 bg-dawn-900 text-white relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="px-3.5 py-1.5 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs font-semibold inline-block mb-3">
          Technical Matrix
        </span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
          Capabilities & Industries Served
        </h2>
        <p class="mt-4 text-slate-300 text-base">
          Proven capabilities backed by heavy machinery, experienced civil and electrical engineers, and skilled workforce.
        </p>
      </div>

      <!-- Capability Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-16">
        <div class="bg-dawn-850 p-5 rounded-xl border border-slate-800">
          <div class="text-amber-400 font-bold text-base mb-1">Civil Engineering</div>
          <div class="text-xs text-slate-300">Roads, buildings, foundations, drainage, earthworks & structural infrastructure</div>
        </div>
        <div class="bg-dawn-850 p-5 rounded-xl border border-slate-800">
          <div class="text-amber-400 font-bold text-base mb-1">Pipeline Works</div>
          <div class="text-xs text-slate-300">Gas pipeline trenching, excavation, civil support, route development & testing</div>
        </div>
        <div class="bg-dawn-850 p-5 rounded-xl border border-slate-800">
          <div class="text-amber-400 font-bold text-base mb-1">Mechanical Works</div>
          <div class="text-xs text-slate-300">CNG/Petrol pump mechanical installation, piping, compressor foundations</div>
        </div>
        <div class="bg-dawn-850 p-5 rounded-xl border border-slate-800">
          <div class="text-amber-400 font-bold text-base mb-1">Electrical Infrastructure</div>
          <div class="text-xs text-slate-300">Cable laying, high-load utility lines, site electricals & distribution panels</div>
        </div>
        <div class="bg-dawn-850 p-5 rounded-xl border border-slate-800">
          <div class="text-amber-400 font-bold text-base mb-1">Building Construction</div>
          <div class="text-xs text-slate-300">Residential apartments, villas, commercial office buildings & retail malls</div>
        </div>
        <div class="bg-dawn-850 p-5 rounded-xl border border-slate-800">
          <div class="text-amber-400 font-bold text-base mb-1">Heavy Fabrication</div>
          <div class="text-xs text-slate-300">Structural steel fabrication, columns, heavy beams, industrial trusses & stairs</div>
        </div>
        <div class="bg-dawn-850 p-5 rounded-xl border border-slate-800">
          <div class="text-amber-400 font-bold text-base mb-1">PEB Solutions</div>
          <div class="text-xs text-slate-300">Pre-Engineered industrial sheds, logistics warehouses & rapid steel structures</div>
        </div>
        <div class="bg-dawn-850 p-5 rounded-xl border border-slate-800">
          <div class="text-amber-400 font-bold text-base mb-1">Government Projects</div>
          <div class="text-xs text-slate-300">Public civil projects, urban utility corridors, institutional developments</div>
        </div>
      </div>

      <!-- Industries We Serve Ticker -->
      <div class="bg-slate-800/40 rounded-2xl p-8 border border-slate-700/60">
        <div class="text-center mb-6">
          <h3 class="text-xl font-bold text-white">Industries We Serve</h3>
          <p class="text-xs text-slate-400 mt-1">Cross-sector infrastructure execution for private & public enterprises</p>
        </div>
        <div class="flex flex-wrap justify-center gap-3 text-sm font-medium">
          <span class="px-4 py-2 rounded-full bg-slate-900 border border-slate-700 text-amber-300">Government & Public Infrastructure</span>
          <span class="px-4 py-2 rounded-full bg-slate-900 border border-slate-700 text-amber-300">Oil & Gas Energy</span>
          <span class="px-4 py-2 rounded-full bg-slate-900 border border-slate-700 text-amber-300">CNG & Fuel Retailing</span>
          <span class="px-4 py-2 rounded-full bg-slate-900 border border-slate-700 text-amber-300">Construction & Real Estate</span>
          <span class="px-4 py-2 rounded-full bg-slate-900 border border-slate-700 text-amber-300">Roads & Highways</span>
          <span class="px-4 py-2 rounded-full bg-slate-900 border border-slate-700 text-amber-300">Industrial & Manufacturing</span>
          <span class="px-4 py-2 rounded-full bg-slate-900 border border-slate-700 text-amber-300">Commercial Developments</span>
          <span class="px-4 py-2 rounded-full bg-slate-900 border border-slate-700 text-amber-300">Public Utilities</span>
        </div>
      </div>

    </div>
  </section>
"""
HTML_PART5 = """
  <!-- Why Choose Us Section -->
  <section id="why-us" class="py-24 bg-white relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="gold-badge text-xs font-bold uppercase tracking-widest px-3.5 py-1.5 rounded-full inline-block mb-3">
          Our Advantage
        </span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
          Why Choose Shree Sudhakar Group?
        </h2>
        <p class="mt-4 text-slate-600 text-base sm:text-lg">
          Engineering infrastructure. Building the future. Here is why clients rely on us for critical infrastructure works.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        
        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200">
          <div class="text-2xl font-extrabold text-amber-500 mb-2">01</div>
          <h3 class="text-lg font-bold text-slate-900 mb-2">Multi-disciplinary Expertise</h3>
          <p class="text-sm text-slate-600 leading-relaxed">
            Civil, mechanical, electrical, pipeline, and structural fabrication capabilities seamlessly coordinated under one group.
          </p>
        </div>

        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200">
          <div class="text-2xl font-extrabold text-amber-500 mb-2">02</div>
          <h3 class="text-lg font-bold text-slate-900 mb-2">End-to-End Execution</h3>
          <p class="text-sm text-slate-600 leading-relaxed">
            From initial site survey, excavation, foundations, and erection to final MEP coordination and commissioning.
          </p>
        </div>

        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200">
          <div class="text-2xl font-extrabold text-amber-500 mb-2">03</div>
          <h3 class="text-lg font-bold text-slate-900 mb-2">Quality Focus</h3>
          <p class="text-sm text-slate-600 leading-relaxed">
            Rigorous adherence to engineering codes, material specifications, and continuous quality audits at every stage.
          </p>
        </div>

        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200">
          <div class="text-2xl font-extrabold text-amber-500 mb-2">04</div>
          <h3 class="text-lg font-bold text-slate-900 mb-2">Safety First Approach</h3>
          <p class="text-sm text-slate-600 leading-relaxed">
            Zero-compromise safety protocols, PPE adherence, and site-level risk assessments safeguarding every workforce member.
          </p>
        </div>

        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200">
          <div class="text-2xl font-extrabold text-amber-500 mb-2">05</div>
          <h3 class="text-lg font-bold text-slate-900 mb-2">Timely Delivery</h3>
          <p class="text-sm text-slate-600 leading-relaxed">
            Disciplined milestone scheduling, proactive material logistics, and real-time site monitoring ensuring on-time handover.
          </p>
        </div>

        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200">
          <div class="text-2xl font-extrabold text-amber-500 mb-2">06</div>
          <h3 class="text-lg font-bold text-slate-900 mb-2">Diverse Project Experience</h3>
          <p class="text-sm text-slate-600 leading-relaxed">
            Proven execution across government departments, gas utilities, commercial developers, and industrial operators.
          </p>
        </div>

      </div>

    </div>
  </section>

  <!-- Vision & Mission Banner -->
  <section class="py-16 bg-gradient-to-r from-dawn-900 via-dawn-850 to-dawn-900 text-white border-y border-amber-500/20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
        
        <div class="p-6 rounded-xl bg-slate-900/50 border border-slate-800">
          <div class="flex items-center gap-3 mb-3">
            <div class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold">V</div>
            <h3 class="text-xl font-bold text-white">Our Vision</h3>
          </div>
          <p class="text-sm text-slate-300 leading-relaxed">
            To become a trusted and recognized infrastructure and engineering group delivering quality projects that contribute to sustainable development and India's growing infrastructure needs.
          </p>
        </div>

        <div class="p-6 rounded-xl bg-slate-900/50 border border-slate-800">
          <div class="flex items-center gap-3 mb-3">
            <div class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold">M</div>
            <h3 class="text-xl font-bold text-white">Our Mission</h3>
          </div>
          <p class="text-sm text-slate-300 leading-relaxed">
            To deliver reliable, safe, and high-quality engineering and construction solutions through skilled people, efficient project execution, and strong commitment to our clients.
          </p>
        </div>

      </div>
    </div>
  </section>

  <!-- Contact & Location Section -->
  <section id="contact" class="py-24 bg-white relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
        
        <!-- Left: Contact Details -->
        <div class="lg:col-span-5 space-y-8">
          <div>
            <span class="gold-badge text-xs font-bold uppercase tracking-widest px-3.5 py-1.5 rounded-full inline-block mb-3">
              Let's Build Together
            </span>
            <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
              Connect with Shree Sudhakar Group
            </h2>
            <p class="mt-3 text-slate-600 text-sm sm:text-base leading-relaxed">
              Have a project requirement in government infrastructure, pipeline works, electrical systems, CNG stations, or PEB structures? Our engineering team is ready to assist.
            </p>
          </div>

          <!-- Contact info list -->
          <div class="space-y-5">
            
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-600 flex items-center justify-center shrink-0">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
              </div>
              <div>
                <div class="text-xs uppercase font-bold text-slate-500 tracking-wider">Office Address</div>
                <div class="text-sm font-semibold text-slate-900 mt-1 leading-snug">
                  Mangalam Life Park, Moshi - Alandi Road,<br>
                  Pimpri-Chinchwad, Maharashtra 412105
                </div>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-600 flex items-center justify-center shrink-0">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
              </div>
              <div>
                <div class="text-xs uppercase font-bold text-slate-500 tracking-wider">Enquiry Phone</div>
                <a href="tel:+919689820892" class="text-lg font-bold text-slate-900 hover:text-amber-600 transition-colors block mt-1">
                  +91 9689820892
                </a>
                <span class="text-xs text-slate-500">Available Mon - Sat for business enquiries</span>
              </div>
            </div>

            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-600 flex items-center justify-center shrink-0">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path></svg>
              </div>
              <div>
                <div class="text-xs uppercase font-bold text-slate-500 tracking-wider">WhatsApp Fast Connect</div>
                <a href="https://wa.me/919689820892?text=Hello%20Shree%20Sudhakar%20Group,%20I%20would%20like%20to%20discuss%20a%20project." target="_blank" rel="noopener" class="text-sm font-semibold text-green-700 hover:underline block mt-1">
                  Chat directly with project lead &rarr;
                </a>
              </div>
            </div>

          </div>

          <!-- Direct Call CTA Banner -->
          <div class="p-6 rounded-2xl bg-amber-50 border border-amber-200">
            <h4 class="font-bold text-amber-950 text-base">Have an Urgent Tender or Site Requirement?</h4>
            <p class="text-xs text-amber-900 mt-1 mb-3">Call our operations desk directly for immediate technical coordination.</p>
            <a href="tel:+919689820892" class="inline-flex items-center gap-2 px-4 py-2.5 rounded-lg bg-amber-600 text-white text-xs font-bold uppercase tracking-wider hover:bg-amber-700 transition-colors">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
              Direct Dial: +91 9689820892
            </a>
          </div>

        </div>

        <!-- Right: Map Card & Directions -->
        <div class="lg:col-span-7">
          <div class="rounded-2xl border border-slate-200 overflow-hidden shadow-lg bg-white">
            
            <div class="bg-dawn-900 text-white p-4 flex items-center justify-between">
              <div class="text-sm font-bold flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-green-400"></span>
                Head Office Location
              </div>
              <a href="https://maps.google.com/?q=Mangalam+Life+Park+Moshi+Alandi+Road+Pimpri+Chinchwad+412105" target="_blank" rel="noopener" class="text-xs text-amber-400 hover:underline flex items-center gap-1">
                Open in Google Maps &rarr;
              </a>
            </div>

            <div class="relative w-full h-[380px] bg-slate-100">
              <iframe 
                title="Office Location Map"
                src="https://maps.google.com/maps?q=Mangalam%20Life%20Park,%20Moshi%20-%20Alandi%20Road,%20Pimpri-Chinchwad,%20Maharashtra%20412105&t=&z=14&ie=UTF8&iwloc=&output=embed"
                class="w-full h-full border-0" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade">
              </iframe>
            </div>

            <div class="p-4 bg-slate-50 border-t border-slate-200 flex flex-col sm:flex-row justify-between items-center text-xs text-slate-600 gap-2">
              <span><strong>Address:</strong> Mangalam Life Park, Moshi - Alandi Road, Pimpri-Chinchwad 412105</span>
              <button class="open-enquiry-modal text-amber-600 font-bold hover:underline shrink-0">
                Book Office Visit &rarr;
              </button>
            </div>

          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- Global Footer -->
  <footer class="bg-dawn-900 text-slate-400 pt-16 pb-12 border-t border-amber-500/20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 pb-12 border-b border-slate-800">
        
        <!-- Brand Summary -->
        <div class="lg:col-span-2 space-y-4">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl sunrise-gradient-bg flex items-center justify-center text-dawn-900 font-extrabold text-xl shadow-md">
              S
            </div>
            <span class="text-xl font-bold text-white tracking-tight">
              Shree <span class="sunrise-gradient-text">Sudhakar Group</span>
            </span>
          </div>
          <p class="text-xs text-slate-400 max-w-sm leading-relaxed">
            Diversified infrastructure and engineering group executing government projects, gas pipelines, electrical works, roads, CNG stations, buildings, and PEB structures across Maharashtra and India.
          </p>
          <div class="text-xs text-amber-400 font-semibold">
            "Building Infrastructure. Powering Progress."
          </div>
        </div>

        <!-- Quick Links -->
        <div>
          <div class="text-xs font-bold uppercase tracking-wider text-white mb-3">Quick Navigation</div>
          <ul class="space-y-2 text-xs">
            <li><a href="#" class="hover:text-amber-400 transition-colors">Home</a></li>
            <li><a href="#about" class="hover:text-amber-400 transition-colors">About Us</a></li>
            <li><a href="#verticals" class="hover:text-amber-400 transition-colors">Business Verticals</a></li>
            <li><a href="#projects" class="hover:text-amber-400 transition-colors">Projects</a></li>
            <li><a href="#capabilities" class="hover:text-amber-400 transition-colors">Capabilities</a></li>
            <li><a href="#contact" class="hover:text-amber-400 transition-colors">Contact</a></li>
          </ul>
        </div>

        <!-- Verticals -->
        <div>
          <div class="text-xs font-bold uppercase tracking-wider text-white mb-3">Core Verticals</div>
          <ul class="space-y-2 text-xs">
            <li><a href="#verticals" class="hover:text-amber-400 transition-colors">Government Projects</a></li>
            <li><a href="#verticals" class="hover:text-amber-400 transition-colors">Gas Pipelines</a></li>
            <li><a href="#verticals" class="hover:text-amber-400 transition-colors">Electrical Works</a></li>
            <li><a href="#verticals" class="hover:text-amber-400 transition-colors">Road & Civil Works</a></li>
            <li><a href="#verticals" class="hover:text-amber-400 transition-colors">CNG & Fuel Pumps</a></li>
            <li><a href="#verticals" class="hover:text-amber-400 transition-colors">PEB & Fabrication</a></li>
          </ul>
        </div>

        <!-- Office & Help -->
        <div>
          <div class="text-xs font-bold uppercase tracking-wider text-white mb-3">Reach Us</div>
          <p class="text-xs text-slate-400 leading-relaxed mb-3">
            Mangalam Life Park, Moshi - Alandi Road, Pimpri-Chinchwad, Maharashtra 412105
          </p>
          <div class="text-xs text-slate-300 font-semibold mb-1">
            Mobile: <a href="tel:+919689820892" class="text-amber-400 hover:underline">+91 9689820892</a>
          </div>
          <button class="open-enquiry-modal mt-3 text-xs px-3 py-1.5 rounded sunrise-gradient-bg text-slate-950 font-bold uppercase tracking-wider">
            Online Enquiry &rarr;
          </button>
        </div>

      </div>

      <!-- Copyright & Deployment Ready Badge -->
      <div class="pt-8 flex flex-col sm:flex-row justify-between items-center text-xs text-slate-400 gap-4">
        <div>
          &copy; 2026 Shree Sudhakar Group. All rights reserved.
        </div>
        <div class="flex items-center gap-4 text-[11px] text-slate-400">
          <span class="inline-flex items-center gap-1.5 text-slate-300">
            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
            Supabase Free Cloud Database Compatible
          </span>
          <span class="text-slate-600">|</span>
          <span class="inline-flex items-center gap-1.5 text-slate-300">
            <svg class="w-3 h-3 text-white inline-block" viewBox="0 0 1155 1000" fill="currentColor"><path d="m577.3 0 577.4 1000H0z"/></svg>
            Vercel Serverless Ready
          </span>
        </div>
      </div>

    </div>
  </footer>

  <!-- Floating Contact Buttons -->
  <div class="floating-actions">
    <!-- WhatsApp Floating Button -->
    <a href="https://wa.me/919689820892?text=Hello%20Shree%20Sudhakar%20Group,%20I%20would%20like%20to%20enquire%20about%20your%20services." target="_blank" rel="noopener" class="floating-btn bg-emerald-500 text-white hover:bg-emerald-600" title="Chat on WhatsApp" aria-label="WhatsApp">
      <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
    </a>

    <!-- Phone Floating Button -->
    <a href="tel:+919689820892" class="floating-btn bg-amber-500 text-slate-950 hover:bg-amber-400" title="Call Enquiry Desk" aria-label="Phone">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
    </a>
  </div>

  <!-- Interactive Enquiry Modal -->
  <div id="enquiry-modal" class="fixed inset-0 z-50 hidden items-center justify-center p-4 modal-backdrop">
    <div class="bg-dawn-850 border border-amber-500/40 rounded-2xl max-w-lg w-full p-6 sm:p-8 shadow-2xl relative text-white">
      
      <!-- Close Button -->
      <button class="close-enquiry-modal absolute top-5 right-5 text-slate-400 hover:text-white p-1" aria-label="Close Modal">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      </button>

      <div class="mb-5">
        <span class="gold-badge text-[11px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full inline-block mb-2">
          Project Enquiry
        </span>
        <h3 class="text-2xl font-bold text-white">Connect with Our Team</h3>
        <p class="text-xs text-slate-300 mt-1">Please fill in your project details. We will respond promptly.</p>
      </div>

      <form id="modal-enquiry-form" class="space-y-4">
        <div id="modal-form-feedback" class="hidden p-3 rounded-lg text-sm mb-4"></div>

        <div>
          <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Full Name *</label>
          <input type="text" name="name" required placeholder="Your full name" class="w-full px-4 py-2.5 rounded-lg bg-slate-900 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:border-amber-500 text-sm">
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Mobile Number *</label>
            <input type="tel" name="mobile" required placeholder="+91 9876543210" class="w-full px-4 py-2.5 rounded-lg bg-slate-900 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:border-amber-500 text-sm">
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Email (Optional)</label>
            <input type="email" name="email" placeholder="name@company.com" class="w-full px-4 py-2.5 rounded-lg bg-slate-900 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:border-amber-500 text-sm">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Project Vertical *</label>
            <select id="modal-vertical" name="vertical" class="w-full px-4 py-2.5 rounded-lg bg-slate-900 border border-slate-700 text-white focus:outline-none focus:border-amber-500 text-sm">
              <option value="Government Infrastructure">Government Infrastructure</option>
              <option value="Gas Pipeline Infrastructure">Gas Pipeline Infrastructure</option>
              <option value="Electrical Infrastructure">Electrical Infrastructure</option>
              <option value="Road & Civil Construction">Road & Civil Construction</option>
              <option value="CNG & Petrol Pump Projects">CNG & Petrol Pump Projects</option>
              <option value="Residential & Commercial">Residential & Commercial</option>
              <option value="Fabrication & PEB Structures">Fabrication & PEB Structures</option>
            </select>
          </div>
          <div>
            <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">City / Region</label>
            <input type="text" name="city" placeholder="e.g. Pune, PCMC" class="w-full px-4 py-2.5 rounded-lg bg-slate-900 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:border-amber-500 text-sm">
          </div>
        </div>

        <div>
          <label class="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-1">Project Requirement / Message</label>
          <textarea name="message" rows="3" placeholder="Provide details regarding project location, estimated timeline, or requirements..." class="w-full px-4 py-2.5 rounded-lg bg-slate-900 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:border-amber-500 text-sm"></textarea>
        </div>

        <button id="modal-submit-btn" type="submit" class="w-full py-3.5 rounded-xl sunrise-gradient-bg text-slate-950 font-bold text-sm uppercase tracking-wider hover:brightness-110 transition-all">
          Submit Enquiry
        </button>

        <div class="text-center pt-2">
          <span class="text-xs text-slate-400">Prefer calling directly? <a href="tel:+919689820892" class="text-amber-400 font-semibold hover:underline">+91 9689820892</a></span>
        </div>
      </form>

    </div>
  </div>

  <!-- Custom Scripts -->
  <script src="/static/js/app.js"></script>
</body>
</html>
"""

def generate():
    full_html = HTML_PART1 + HTML_PART2 + HTML_PART3 + HTML_PART4 + HTML_PART5
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "index.html")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[OK] index.html successfully created at {dest} ({len(full_html)} bytes)")

if __name__ == "__main__":
    generate()
