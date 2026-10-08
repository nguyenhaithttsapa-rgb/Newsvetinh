import urllib.request
import ssl
import re
import time
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8'
}

hubs = [
    ('LaoCaiView Ecosystem', 'https://laocaiview.vn'),
    ('Vòng Quay May Mắn Pro', 'https://vongquaymayman.web.app'),
    ('Đao Đao Review Anime', 'https://daodaoreview.com'),
    ('Ăn Gì Cũng Được Food', 'https://angicungduoc.food'),
    ('Lịch Âm Pro Vạn Niên', 'https://lichampro.com'),
    ('Tính Lương Gross Net 2026', 'https://tinhluonggrossnet.vn'),
    ('QuickPsd Graphic Suite', 'https://quickpsd.com'),
    ('Tạo Mã QR Online VietQR', 'https://www.taomaqr.online')
]

results = []

for name, url in hubs:
    start = time.time()
    site_info = {
        "name": name,
        "url": url,
        "status": "OFFLINE",
        "code": 0,
        "latency_ms": 0,
        "title": "",
        "title_len": 0,
        "description": "",
        "desc_len": 0,
        "canonical": "",
        "robots": "",
        "analytics_tags": [],
        "gsc_verification": "",
        "h1_tags": [],
        "h2_count": 0,
        "has_schema": False,
        "has_og": False,
        "error": ""
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15, context=ctx) as r:
            lat = int((time.time() - start) * 1000)
            code = r.getcode()
            html = r.read().decode('utf-8', errors='ignore')
            
            site_info["status"] = "ONLINE"
            site_info["code"] = code
            site_info["latency_ms"] = lat
            
            # Title
            m_title = re.search(r'<title[^>]*>(.*?)</title>', html, re.I | re.S)
            if m_title:
                t = re.sub(r'\s+', ' ', m_title.group(1)).strip()
                site_info["title"] = t
                site_info["title_len"] = len(t)
                
            # Description
            m_desc = re.search(r'<meta[^>]*name=[\'"]description[\'"][^>]*content=[\'"](.*?)[\'"]', html, re.I | re.S)
            if not m_desc:
                m_desc = re.search(r'<meta[^>]*content=[\'"](.*?)[\'"][^>]*name=[\'"]description[\'"]', html, re.I | re.S)
            if m_desc:
                d = re.sub(r'\s+', ' ', m_desc.group(1)).strip()
                site_info["description"] = d
                site_info["desc_len"] = len(d)
                
            # Robots
            m_rob = re.search(r'<meta[^>]*name=[\'"]robots[\'"][^>]*content=[\'"](.*?)[\'"]', html, re.I | re.S)
            if m_rob:
                site_info["robots"] = m_rob.group(1).strip()
                
            # Canonical
            m_can = re.search(r'<link[^>]*rel=[\'"]canonical[\'"][^>]*href=[\'"](.*?)[\'"]', html, re.I | re.S)
            if m_can:
                site_info["canonical"] = m_can.group(1).strip()
                
            # Analytics
            ga = re.findall(r'G-[A-Z0-9]+|UA-[0-9]+-[0-9]+|GTM-[A-Z0-9]+', html)
            site_info["analytics_tags"] = sorted(list(set(ga)))
            
            # GSC
            m_gsc = re.search(r'<meta[^>]*name=[\'"]google-site-verification[\'"][^>]*content=[\'"](.*?)[\'"]', html, re.I | re.S)
            if m_gsc:
                site_info["gsc_verification"] = m_gsc.group(1).strip()
                
            # H1
            h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.I | re.S)
            site_info["h1_tags"] = [re.sub(r'<[^>]+>', '', h).strip() for h in h1s]
            
            # H2 count
            h2s = re.findall(r'<h2[^>]*>', html, re.I)
            site_info["h2_count"] = len(h2s)
            
            # Schema
            site_info["has_schema"] = ('application/ld+json' in html) or ('itemtype="http://schema.org' in html) or ('itemtype="https://schema.org' in html)
            
            # OpenGraph
            site_info["has_og"] = ('og:title' in html or 'og:description' in html)
            
    except Exception as e:
        lat = int((time.time() - start) * 1000)
        site_info["latency_ms"] = lat
        site_info["error"] = str(e)
        
    results.append(site_info)

output_path = "data/target_sites_audit.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Audit completed. Results saved to {output_path}")
for s in results:
    print(f"\n[{s['name']}] - {s['url']}")
    print(f"Status: {s['status']} ({s['code']}) | Latency: {s['latency_ms']}ms")
    print(f"Title: {s['title'][:70]} (Len: {s['title_len']})")
    print(f"Desc: {s['description'][:80]} (Len: {s['desc_len']})")
    print(f"Analytics: {s['analytics_tags']} | GSC: {'Yes' if s['gsc_verification'] else 'No'}")
    print(f"H1 Count: {len(s['h1_tags'])} | H2 Count: {s['h2_count']} | Schema: {s['has_schema']} | OG: {s['has_og']}")
    if s['error']:
        print(f"Error: {s['error']}")
