import os
import sys
import json
import urllib.request
import urllib.error
import hashlib
import uuid
import ssl

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

try:
    sys.path.append(r"G:\laocaiview")
    from cloudflare_engine import CF_TOKEN, ACCOUNT_ID
except Exception:
    CF_TOKEN = os.getenv("CF_TOKEN", "")
    ACCOUNT_ID = os.getenv("CF_ACCOUNT_ID", "48777b1a8744f7681cd7e137985d181e")

SCRIPT_NAME = "newsvetinh"
HTML_PATH = r"E:\web vệ tinh\index.html"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 1. READ HTML
with open(HTML_PATH, "r", encoding="utf-8") as f:
    html_content = f.read()

safe_html = html_content.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")

worker_js = f"""
addEventListener('fetch', event => {{
  event.respondWith(handleRequest(event.request));
}});

async function handleRequest(request) {{
  const html = `{safe_html}`;
  return new Response(html, {{
    headers: {{
      'content-type': 'text/html;charset=UTF-8',
      'cache-control': 'public, max-age=3600',
      'x-powered-by': 'Satellite-Mesh-Edge-Cloudflare'
    }}
  }});
}}
"""

print(f"🚀 Deploying Cloudflare Worker script: {SCRIPT_NAME}...")

upload_url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/workers/scripts/{SCRIPT_NAME}"
req = urllib.request.Request(
    upload_url,
    data=worker_js.encode("utf-8"),
    headers={
        "Authorization": f"Bearer {CF_TOKEN}",
        "Content-Type": "application/javascript"
    },
    method="PUT"
)

try:
    with urllib.request.urlopen(req, context=ctx) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("✓ Cloudflare Worker script uploaded successfully!")
except urllib.error.HTTPError as e:
    print("Upload error:", e.code, e.read().decode("utf-8"))

# Enable Subdomain
subdomain_url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/workers/scripts/{SCRIPT_NAME}/subdomain"
sub_req = urllib.request.Request(
    subdomain_url,
    data=json.dumps({"enabled": True}).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {CF_TOKEN}",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(sub_req, context=ctx) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        print("✓ Subdomain enabled successfully!")
except urllib.error.HTTPError as e:
    print("Subdomain note:", e.code, e.read().decode("utf-8"))

# Get Worker URL
acc_sub_url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/workers/subdomain"
acc_req = urllib.request.Request(acc_sub_url, headers={"Authorization": f"Bearer {CF_TOKEN}"})
try:
    with urllib.request.urlopen(acc_req, context=ctx) as resp:
        sub_data = json.loads(resp.read().decode("utf-8"))
        subdomain = sub_data.get("result", {}).get("subdomain")
        worker_live_url = f"https://{SCRIPT_NAME}.{subdomain}.workers.dev"
        print(f"\n🎉 LIVE CLOUDFLARE WORKER URL: {worker_live_url}")
except Exception as e:
    print("Check subdomain error:", e)

# 2. ALSO DEPLOY TO CLOUDFLARE PAGES (newsvetinh.pages.dev)
print("\n🚀 Deploying to Cloudflare Pages (newsvetinh.pages.dev)...")
sys.path.append(r"G:\laocaiview")
try:
    from cloudflare_engine import deploy_folder_to_cloudflare_pages
    pages_url = deploy_folder_to_cloudflare_pages(r"E:\web vệ tinh", "newsvetinh")
    print(f"🎉 LIVE CLOUDFLARE PAGES URL: {pages_url}")
except Exception as e:
    print("Cloudflare pages error:", e)
