#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import ssl
import re
import time
import sys
import json

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sites = [
    ('LaoCaiView Ecosystem', 'https://laocaiview.vn'),
    ('Vòng Quay May Mắn Pro', 'https://vongquaymayman.web.app'),
    ('Đao Đao Review Anime', 'https://daodaoreview.com'),
    ('Ăn Gì Cũng Được Food', 'https://angicungduoc.food'),
    ('Lịch Âm Pro Vạn Niên', 'https://lichampro.com'),
    ('Tính Lương Gross Net 2026', 'https://tinhluonggrossnet.vn'),
    ('QuickPsd Graphic Suite', 'https://quickpsd.com'),
    ('Tạo Mã QR Online VietQR', 'https://www.taomaqr.online')
]

print("=== BÁO CÁO TOÀN DIỆN 8 WEBSITE CHÍNH CỦA BẠN ===")
for name, url in sites:
    start = time.time()
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=12, context=ctx) as r:
            lat = int((time.time() - start) * 1000)
            code = r.getcode()
            headers = dict(r.getheaders())
            raw_html = r.read()
            html = raw_html.decode('utf-8', errors='ignore')
            
            title_m = re.search(r'<title[^>]*>(.*?)</title>', html, re.I | re.S)
            title = title_m.group(1).strip() if title_m else 'Chưa có thẻ Title'
            title = re.sub(r'\s+', ' ', title)
            
            desc_m = re.search(r'<meta[^>]*name=[\"\']description[\"\'][^>]*content=[\"\'](.*?)[\"\']', html, re.I)
            desc = desc_m.group(1).strip() if desc_m else 'Chưa có Meta Description'
            
            has_mobile = 'viewport' in html.lower()
            has_og = 'og:title' in html.lower() or 'og:image' in html.lower()
            has_gtag = 'gtag' in html.lower() or 'googletagmanager' in html.lower() or 'analytics' in html.lower()
            
            print(f"\n[{code} ONLINE] {name} ({url})")
            print(f"  - Tốc độ: {lat}ms | Dung lượng: {round(len(raw_html)/1024, 1)} KB")
            print(f"  - Tiêu đề SEO (Title): {title}")
            print(f"  - Mô tả SEO (Desc): {desc[:100]}...")
            print(f"  - Mobile Viewport: {'✓ Có' if has_mobile else '✗ Thiếu'} | Open Graph (Mạng xã hội): {'✓ Có' if has_og else '✗ Thiếu'} | Google Analytics: {'✓ Có' if has_gtag else '✗ Chưa gắn'}")
    except Exception as e:
        print(f"\n[✗ LỖI] {name} ({url}): {e}")
