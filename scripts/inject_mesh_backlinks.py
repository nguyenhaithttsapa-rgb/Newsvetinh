#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INJECT MESH BACKLINKS SCRIPT
Tự động nhúng widget ma trận kết nối 8 web vệ tinh vào các trang web vệ tinh cục bộ.
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

WIDGET_HTML = """
<!-- SATELLITE MULTI-CLOUD BACKLINK MESH WIDGET (AUTO-INJECTED) -->
<div id="satellite-mesh-hub" class="max-w-7xl mx-auto my-8 p-6 rounded-2xl bg-slate-950/90 border border-slate-800 text-slate-300 font-sans shadow-xl backdrop-blur-md">
  <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 mb-4 border-b border-slate-800 gap-2">
    <div>
      <div class="text-[11px] font-bold tracking-wider text-amber-400 uppercase">Mạng Lưới Vệ Tinh Đa Đám Mây</div>
      <div class="text-base font-extrabold text-white">Hệ Sinh Thái 8 Nền Tảng Trực Thuộc</div>
    </div>
    <div class="flex items-center gap-3 text-xs">
      <a href="https://vongquaymayman.web.app" target="_blank" rel="dofollow" class="text-amber-400 font-bold hover:underline flex items-center gap-1">
        <span>🎡 Vòng Quay May Mắn Livestream</span>
      </a>
      <a href="https://laocaiview.vn" target="_blank" rel="dofollow" class="text-cyan-400 font-bold hover:underline flex items-center gap-1">
        <span>🏔️ Cổng Du Lịch LaoCaiView.vn</span>
      </a>
    </div>
  </div>
  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-xs">
    <a href="https://nguyenhaithttsapa-rgb.github.io/batdongsan-sapa-review/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex items-center justify-between">
      <span>🐙 GitHub Pages</span>
      <span class="text-[10px] text-amber-400 font-mono">DA 98</span>
    </a>
    <a href="https://sapa-tour-3n2d.laocaiview-vn.workers.dev/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex items-center justify-between">
      <span>⚡ Cloudflare Edge</span>
      <span class="text-[10px] text-amber-400 font-mono">DA 96</span>
    </a>
    <a href="https://sapa-travel-experience.vercel.app/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex items-center justify-between">
      <span>▲ Vercel Cloud</span>
      <span class="text-[10px] text-amber-400 font-mono">DA 92</span>
    </a>
    <a href="https://sapa-travel-experience.netlify.app/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex items-center justify-between">
      <span>💎 Netlify Global</span>
      <span class="text-[10px] text-amber-400 font-mono">DA 94</span>
    </a>
    <a href="https://anuongsapa-review.onrender.com/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex items-center justify-between">
      <span>🚀 Render Cloud</span>
      <span class="text-[10px] text-amber-400 font-mono">DA 85</span>
    </a>
    <a href="https://sapa-photospots.deno.dev/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex items-center justify-between">
      <span>🦕 Deno Deploy</span>
      <span class="text-[10px] text-amber-400 font-mono">DA 88</span>
    </a>
    <a href="https://nhadatlaocai-review.gitlab.io/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex items-center justify-between">
      <span>🦊 GitLab Pages</span>
      <span class="text-[10px] text-amber-400 font-mono">DA 93</span>
    </a>
    <a href="https://vongquaymayman.web.app/" target="_blank" rel="dofollow" class="p-2 rounded-lg bg-slate-900/80 hover:bg-slate-800 border border-slate-800 text-slate-300 hover:text-white transition flex items-center justify-between">
      <span>🔥 Firebase Cloud</span>
      <span class="text-[10px] text-amber-400 font-mono">DA 96</span>
    </a>
  </div>
</div>
<!-- END SATELLITE WIDGET -->
"""

def inject_mesh():
    print("=" * 70)
    print("BẮT ĐẦU ĐỒNG BỘ & NHÚNG MA TRẬN LIÊN KẾT 8 WEB VỆ TINH")
    print("=" * 70)

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

                if "satellite-mesh-hub" in content:
                    continue  # Already injected

                # Inject before </body> or </footer>
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
    print(f"KẾT QUẢ ĐỒNG BỘ: Đã nhúng liên kết thành công vào {total_injected} tệp HTML!")
    print("Mạng lưới 8 web vệ tinh đã được kết nối hoàn tất.")
    print("=" * 70)

if __name__ == "__main__":
    inject_mesh()
