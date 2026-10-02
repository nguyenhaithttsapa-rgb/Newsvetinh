import urllib.request
import ssl
import time
import sys

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    ('Deno Deploy', 'https://newsvetinh.deno.dev'),
    ('Firebase Google Cloud', 'https://newsvetinh.web.app'),
    ('Cloudflare Workers Edge', 'https://newsvetinh.laocaiview-vn.workers.dev'),
    ('Vercel Cloud Edge', 'https://newsvetinh.vercel.app'),
    ('Render Cloud', 'https://newsvetinh.onrender.com'),
    ('GitHub Pages', 'https://nguyenhaithttsapa-rgb.github.io/Newsvetinh/'),
    ('Netlify Global CDN', 'https://newsvetinh.netlify.app'),
    ('GitLab Pages (Nhadat)', 'https://nhadatlaocai-review.gitlab.io/')
]

print("=" * 80)
print("BÁO CÁO KIỂM TRA TRẠNG THÁI KẾT NỐI HỆ THỐNG NEWSEVITINH")
print("=" * 80)

for platform, u in urls:
    start = time.time()
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            lat = int((time.time() - start) * 1000)
            code = resp.getcode()
            body = resp.read()
            print(f"[✓ ONLINE {code}] {platform:<25} | {lat:>4}ms | {len(body):>6} bytes | {u}")
    except Exception as e:
        lat = int((time.time() - start) * 1000)
        print(f"[X CHƯA LIVE]  {platform:<25} | {lat:>4}ms | Lỗi: {e} | {u}")

print("=" * 80)
