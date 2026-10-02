#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INJECT MESH BACKLINKS SCRIPT (EXPANDED 14+ WEBSITES MESH)
Tự động nhúng ma trận kết nối liên kết chéo vào toàn bộ các web vệ tinh cục bộ:
- 2 Trang Đích: vongquaymayman.web.app & laocaiview.vn
- 6 Web Tiện Ích & Nội Dung: daodaoreview.com, angicungduoc.food, lichampro.com, tinhluonggrossnet.vn, quickpsd.com, taomaqr.online
- 8 Hạ Tầng Đa Đám Mây: GitHub, Cloudflare, Vercel, Netlify, Render, Deno, GitLab, Replit
"""

import os
import sys
import glob
import re

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

SATELLITE_DIRECTORIES = [
    r"G:\Ve-Tinh-SEO-LaoCaiView\satellites\01-github-batdongsan-sapa",
    r"G:\sapa-trekking-cloudflare",
    r"G:\sapa-golden-season-vercel",
    r"G:\sapa-ecolodge-netlify",
    r"G:\sapa-cultural-render",
    r"G:\sapa-photospots-deno",
    r"G:\Ve-Tinh-SEO-LaoCaiView\satellites\06-gitlab-nhadat-laocai",
    r"E:\vong-quay-livestream"
]

WIDGET_HTML = """<!-- SATELLITE MULTI-CLOUD BACKLINK MESH WIDGET (AUTO-INJECTED) -->
<div id="satellite-mesh-hub" class="max-w-7xl mx-auto my-8 p-6 rounded-2xl bg-slate-950/95 border border-slate-800 text-slate-300 font-sans shadow-2xl backdrop-blur-md">
  
  <!-- HEADER: CORE DESTINATIONS -->
  <div class="flex flex-col md:flex-row md:items-center justify-between pb-4 mb-4 border-b border-slate-800 gap-3">
    <div>
      <div class="text-[11px] font-bold tracking-wider text-amber-400 uppercase">Hạ Tầng Dòng Chảy Liên Kết Đa Đám Mây</div>
      <div class="text-base font-extrabold text-white">8 Vệ Tinh Độc Lập ➔ Tập Trung Lực Kéo Về 8 Website Chính</div>
    </div>
    <div class="flex flex-wrap items-center gap-3 text-xs">
      <a href="https://vongquaymayman.web.app" target="_blank" rel="dofollow" class="px-3 py-1.5 rounded-lg bg-amber-500/10 hover:bg-amber-500/20 text-amber-400 font-bold border border-amber-500/30 transition flex items-center gap-1.5">
        <span>🎡 Vòng Quay May Mắn Pro</span>
      </a>
      <a href="https://laocaiview.vn" target="_blank" rel="dofollow" class="px-3 py-1.5 rounded-lg bg-cyan-500/10 hover:bg-cyan-500/20 text-cyan-400 font-bold border border-cyan-500/30 transition flex items-center gap-1.5">
        <span>🏔️ Cổng Du Lịch LaoCaiView.vn</span>
      </a>
    </div>
  </div>

  <!-- SECTION 1: CÔNG CỤ & TIỆN ÍCH SỐ TÊN MIỀN RIÊNG -->
  <div class="mb-4">
    <div class="text-[11px] font-semibold text-slate-400 mb-2 flex items-center gap-1.5">
      <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
      <span>HỆ SINH THÁI TIỆN ÍCH & NỘI DUNG SỐ (CUSTOM DOMAINS)</span>
    </div>
    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2 text-xs">
      <a href="https://daodaoreview.com" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 hover:border-pink-500/50 text-slate-300 hover:text-white transition flex items-center gap-2">
        <span class="text-base">🎬</span>
        <div class="truncate">
          <div class="font-bold text-[11px] text-pink-400 truncate">Đao Đao Review</div>
          <div class="text-[10px] text-slate-500">Hoạt Hình 3D</div>
        </div>
      </a>
      <a href="https://angicungduoc.food" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 hover:border-orange-500/50 text-slate-300 hover:text-white transition flex items-center gap-2">
        <span class="text-base">🍜</span>
        <div class="truncate">
          <div class="font-bold text-[11px] text-orange-400 truncate">Ăn Gì Cũng Được</div>
          <div class="text-[10px] text-slate-500">Cứu Tinh Bữa Trưa</div>
        </div>
      </a>
      <a href="https://lichampro.com" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 hover:border-purple-500/50 text-slate-300 hover:text-white transition flex items-center gap-2">
        <span class="text-base">📅</span>
        <div class="truncate">
          <div class="font-bold text-[11px] text-purple-400 truncate">Lịch Âm Pro</div>
          <div class="text-[10px] text-slate-500">Lịch Vạn Niên</div>
        </div>
      </a>
      <a href="https://tinhluonggrossnet.vn" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 hover:border-emerald-500/50 text-slate-300 hover:text-white transition flex items-center gap-2">
        <span class="text-base">💰</span>
        <div class="truncate">
          <div class="font-bold text-[11px] text-emerald-400 truncate">Tính Lương Gross Net</div>
          <div class="text-[10px] text-slate-500">Thuế Chuẩn 2026</div>
        </div>
      </a>
      <a href="https://quickpsd.com" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 hover:border-blue-500/50 text-slate-300 hover:text-white transition flex items-center gap-2">
        <span class="text-base">🎨</span>
        <div class="truncate">
          <div class="font-bold text-[11px] text-blue-400 truncate">QuickPsd Suite</div>
          <div class="text-[10px] text-slate-500">PSD Editor Online</div>
        </div>
      </a>
      <a href="https://www.taomaqr.online" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 hover:border-cyan-500/50 text-slate-300 hover:text-white transition flex items-center gap-2">
        <span class="text-base">📱</span>
        <div class="truncate">
          <div class="font-bold text-[11px] text-cyan-400 truncate">Tạo Mã QR Online</div>
          <div class="text-[10px] text-slate-500">Bảng VietQR Để Bàn</div>
        </div>
      </a>
    </div>
  </div>

  <!-- SECTION 2: 8 NỀN TẢNG ĐA ĐÁM MÂY (MULTI-CLOUD) -->
  <div>
    <div class="text-[11px] font-semibold text-slate-400 mb-2 flex items-center gap-1.5">
      <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
      <span>HỆ THỐNG VỆ TINH ĐA ĐÁM MÂY (HIGH DA MESH BACKLINK)</span>
    </div>
    <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-2 text-xs">
      <a href="https://nguyenhaithttsapa-rgb.github.io/batdongsan-sapa-review/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex flex-col justify-between">
        <span class="font-bold text-[11px]">🐙 GitHub</span>
        <span class="text-[9px] text-amber-400 font-mono">DA 98</span>
      </a>
      <a href="https://sapa-tour-3n2d.laocaiview-vn.workers.dev/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex flex-col justify-between">
        <span class="font-bold text-[11px]">⚡ Cloudflare</span>
        <span class="text-[9px] text-amber-400 font-mono">DA 96</span>
      </a>
      <a href="https://sapa-travel-experience.vercel.app/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex flex-col justify-between">
        <span class="font-bold text-[11px]">▲ Vercel</span>
        <span class="text-[9px] text-amber-400 font-mono">DA 92</span>
      </a>
      <a href="https://sapa-travel-experience.netlify.app/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex flex-col justify-between">
        <span class="font-bold text-[11px]">💎 Netlify</span>
        <span class="text-[9px] text-amber-400 font-mono">DA 94</span>
      </a>
      <a href="https://anuongsapa-review.onrender.com/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex flex-col justify-between">
        <span class="font-bold text-[11px]">🚀 Render</span>
        <span class="text-[9px] text-amber-400 font-mono">DA 85</span>
      </a>
      <a href="https://sapa-photospots.deno.dev/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex flex-col justify-between">
        <span class="font-bold text-[11px]">🦕 Deno</span>
        <span class="text-[9px] text-amber-400 font-mono">DA 88</span>
      </a>
      <a href="https://nhadatlaocai-review.gitlab.io/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex flex-col justify-between">
        <span class="font-bold text-[11px]">🦊 GitLab</span>
        <span class="text-[9px] text-amber-400 font-mono">DA 93</span>
      </a>
      <a href="https://newsvetinh.replit.app" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex flex-col justify-between">
        <span class="font-bold text-[11px]">⚡ Replit</span>
        <span class="text-[9px] text-amber-400 font-mono">DA 91</span>
      </a>
    </div>
  </div>
</div>
<!-- END SATELLITE WIDGET -->"""

def inject_mesh():
    print("=" * 70)
    print("BẮT ĐẦU ĐỒNG BỘ & NHÚNG MA TRẬN LIÊN KẾT 14+ WEBSITE MỞ RỘNG")
    print("=" * 70)

    total_updated = 0
    total_injected = 0
    for target_dir in SATELLITE_DIRECTORIES:
        if not os.path.exists(target_dir):
            print(f"[-] Bỏ qua thư mục (không tồn tại): {target_dir}")
            continue

        html_files = glob.glob(os.path.join(target_dir, "*.html"))
        print(f"[*] Quét thư mục: {os.path.basename(target_dir)} ({len(html_files)} files HTML)")

        for fpath in html_files:
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                if '<div id="satellite-mesh-hub"' in content:
                    # Update existing widget cleanly
                    pattern = r'<!-- SATELLITE MULTI-CLOUD BACKLINK MESH WIDGET.*?<!-- END SATELLITE WIDGET -->'
                    if re.search(pattern, content, flags=re.DOTALL):
                        updated = re.sub(pattern, WIDGET_HTML, content, flags=re.DOTALL)
                    else:
                        # Fallback div pattern
                        pattern_div = r'<div id="satellite-mesh-hub".*?</div>\s*<!-- END SATELLITE WIDGET -->'
                        updated = re.sub(pattern_div, WIDGET_HTML, content, flags=re.DOTALL)
                    
                    if updated != content:
                        with open(fpath, "w", encoding="utf-8") as f:
                            f.write(updated)
                        total_updated += 1
                else:
                    # Inject new
                    if "</footer>" in content:
                        updated = content.replace("</footer>", "</footer>\n" + WIDGET_HTML)
                    elif "</body>" in content:
                        updated = content.replace("</body>", WIDGET_HTML + "\n</body>")
                    else:
                        updated = content + "\n" + WIDGET_HTML

                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(updated)
                    total_injected += 1

            except Exception as e:
                print(f"  [!] Lỗi khi xử lý {os.path.basename(fpath)}: {e}")

    print("=" * 70)
    print(f"KẾT QUẢ ĐỒNG BỘ:")
    print(f"- Đã cập nhật ma trận mới vào: {total_updated} tệp HTML hiện có")
    print(f"- Đã nhúng mới vào: {total_injected} tệp HTML")
    print("Mạng lưới 14+ website đã được liên kết chéo khép kín 100%!")
    print("=" * 70)

if __name__ == "__main__":
    inject_mesh()
