import urllib.request
import ssl
import time
import json
import sys

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

satellites = [
    {
        'id': 's1',
        'platform': 'GitHub Pages',
        'name': 'Bất Động Sản & Review Sa Pa',
        'url': 'https://nguyenhaithttsapa-rgb.github.io/batdongsan-sapa-review/'
    },
    {
        'id': 's2',
        'platform': 'Cloudflare Edge / Workers',
        'name': 'Cẩm Nang Tour & Trải Nghiệm',
        'url': 'https://sapa-tour-3n2d.laocaiview-vn.workers.dev/danh-gia-thuat-toan-crypto-csprng-vongquaymayman-web-app.html'
    },
    {
        'id': 's3',
        'platform': 'Vercel Edge Cloud',
        'name': 'Du Lịch Mùa Vàng Sa Pa',
        'url': 'https://sapa-travel-experience.vercel.app/'
    },
    {
        'id': 's4',
        'platform': 'Netlify Global CDN',
        'name': 'Ecolodge & Nghỉ Dưỡng Xanh',
        'url': 'https://sapa-travel-experience.netlify.app/'
    },
    {
        'id': 's5',
        'platform': 'Render Cloud',
        'name': 'Văn Hóa Bản Làng Sa Pa',
        'url': 'https://anuongsapa-review.onrender.com/'
    },
    {
        'id': 's6',
        'platform': 'Deno Deploy',
        'name': 'Săn Mây & Điểm Check-in',
        'url': 'https://sapa-photospots.deno.dev/'
    },
    {
        'id': 's7',
        'platform': 'GitLab Pages',
        'name': 'Thị Trường Nhà Đất & Dự Án',
        'url': 'https://nhadatlaocai-review.gitlab.io/'
    },
    {
        'id': 's8',
        'platform': 'Firebase Google Cloud',
        'name': 'Cổng Vòng Quay May Mắn (Core)',
        'url': 'https://vongquaymayman.web.app/'
    }
]

print("=" * 80)
print("KIỂM TRA TÌNH TRẠNG HOẠT ĐỘNG THỰC TẾ 8 WEB VỆ TINH")
print("=" * 80)

results = []
for s in satellites:
    start = time.time()
    try:
        req = urllib.request.Request(s['url'], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=12, context=ctx) as resp:
            latency = int((time.time() - start) * 1000)
            code = resp.getcode()
            content = resp.read()
            results.append({
                'name': s['name'],
                'platform': s['platform'],
                'url': s['url'],
                'status': 'ONLINE',
                'code': code,
                'latency': latency,
                'size': len(content)
            })
            print(f"[{code} ONLINE] {s['platform']:<25} | {latency:>4}ms | {len(content):>6} bytes | {s['url']}")
    except Exception as e:
        latency = int((time.time() - start) * 1000)
        results.append({
            'name': s['name'],
            'platform': s['platform'],
            'url': s['url'],
            'status': 'ERROR',
            'code': str(e),
            'latency': latency,
            'size': 0
        })
        print(f"[ERR]        {s['platform']:<25} | {latency:>4}ms | Lỗi: {e} | {s['url']}")

print("\n" + "=" * 80)
print("KIỂM TRA CÁC ĐƯỜNG LINK NEWSEVITINH & MONEY SITES")
print("=" * 80)

hubs = [
    ('Firebase Newsvetinh', 'https://newsvetinh.web.app'),
    ('Vercel Newsvetinh', 'https://newsvetinh.vercel.app'),
    ('Cloudflare Worker Newsvetinh', 'https://newsvetinh.laocaiview-vn.workers.dev'),
    ('Render Newsvetinh', 'https://newsvetinh.onrender.com'),
    ('GitHub Pages Newsvetinh', 'https://nguyenhaithttsapa-rgb.github.io/Newsvetinh/'),
    ('Replit App Newsvetinh', 'https://newsvetinh--laocaiview.replit.app'),
    ('Target Site LaoCaiView', 'https://laocaiview.vn')
]

for label, url in hubs:
    start = time.time()
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            lat = int((time.time() - start) * 1000)
            print(f"[{r.getcode()} ONLINE] {label:<30} | {lat:>4}ms | {url}")
    except Exception as e:
        lat = int((time.time() - start) * 1000)
        print(f"[ERR]        {label:<30} | {lat:>4}ms | Lỗi: {e} | {url}")
