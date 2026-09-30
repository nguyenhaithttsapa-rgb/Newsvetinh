#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SATELLITE CONNECTOR & HEALTH CHECKER ENGINE
Kiểm tra trực tiếp trạng thái HTTP, độ trễ phản hồi CDN và tính toàn vẹn liên kết của 8 vệ tinh.
"""

import sys
import time
import json
import urllib.request
import urllib.error
import ssl

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

SATELLITES = [
    {
        "id": "s1",
        "name": "Bất Động Sản & Review Sa Pa",
        "platform": "GitHub Pages",
        "icon": "🐙",
        "domain": "github.io",
        "da": 98,
        "url": "https://nguyenhaithttsapa-rgb.github.io/batdongsan-sapa-review/top-cong-cu-vong-quay-may-man-cho-streamer-tiktok-facebook-obs.html",
        "homeUrl": "https://nguyenhaithttsapa-rgb.github.io/batdongsan-sapa-review/",
        "localPath": r"G:\Ve-Tinh-SEO-LaoCaiView\satellites\01-github-batdongsan-sapa",
        "color": "#38bdf8"
    },
    {
        "id": "s2",
        "name": "Cẩm Nang Tour & Trải Nghiệm",
        "platform": "Cloudflare Workers/Pages",
        "icon": "⚡",
        "domain": "workers.dev",
        "da": 96,
        "url": "https://sapa-tour-3n2d.laocaiview-vn.workers.dev/danh-gia-thuat-toan-crypto-csprng-vongquaymayman-web-app.html",
        "homeUrl": "https://sapa-tour-3n2d.laocaiview-vn.workers.dev/",
        "localPath": r"G:\sapa-trekking-cloudflare",
        "color": "#f97316"
    },
    {
        "id": "s3",
        "name": "Du Lịch Mùa Vàng Sa Pa",
        "platform": "Vercel Edge Cloud",
        "icon": "▲",
        "domain": "vercel.app",
        "da": 92,
        "url": "https://sapa-travel-experience.vercel.app/giai-phap-vong-quay-goi-ten-hoc-sinh-khuay-dong-lop-hoc-thoi-40.html",
        "homeUrl": "https://sapa-travel-experience.vercel.app/",
        "localPath": r"G:\sapa-golden-season-vercel",
        "color": "#ffffff"
    },
    {
        "id": "s4",
        "name": "Ecolodge & Nghỉ Dưỡng Xanh",
        "platform": "Netlify Global CDN",
        "icon": "💎",
        "domain": "netlify.app",
        "da": 94,
        "url": "https://sapa-travel-experience.netlify.app/top-cong-cu-vong-quay-may-man-cho-streamer-tiktok-facebook-obs.html",
        "homeUrl": "https://sapa-travel-experience.netlify.app/",
        "localPath": r"G:\sapa-ecolodge-netlify",
        "color": "#06b6d4"
    },
    {
        "id": "s5",
        "name": "Văn Hóa Bản Làng Sa Pa",
        "platform": "Render Cloud",
        "icon": "🚀",
        "domain": "onrender.com",
        "da": 85,
        "url": "https://sapa-batdongsan-live.onrender.com/top-cong-cu-vong-quay-may-man-cho-streamer-tiktok-facebook-obs.html",
        "homeUrl": "https://sapa-batdongsan-live.onrender.com/",
        "localPath": r"G:\sapa-cultural-render",
        "color": "#46e3b7"
    },
    {
        "id": "s6",
        "name": "Săn Mây & Điểm Check-in",
        "platform": "Deno Deploy",
        "icon": "🦕",
        "domain": "deno.dev",
        "da": 88,
        "url": "https://sapa-photospots.deno.dev/",
        "homeUrl": "https://sapa-photospots.deno.dev/",
        "localPath": r"G:\sapa-photospots-deno",
        "color": "#10b981"
    },
    {
        "id": "s7",
        "name": "Thị Trường Nhà Đất & Dự Án",
        "platform": "GitLab Pages",
        "icon": "🦊",
        "domain": "gitlab.io",
        "da": 93,
        "url": "https://nhadatlaocai-review.gitlab.io/",
        "homeUrl": "https://nhadatlaocai-review.gitlab.io/",
        "localPath": r"G:\Ve-Tinh-SEO-LaoCaiView\satellites\06-gitlab-nhadat-laocai",
        "color": "#fc6d26"
    },
    {
        "id": "s8",
        "name": "Cổng Vòng Quay May Mắn (Core Hub)",
        "platform": "Firebase Google Cloud",
        "icon": "🔥",
        "domain": "web.app",
        "da": 96,
        "url": "https://vongquaymayman.web.app/",
        "homeUrl": "https://vongquaymayman.web.app/",
        "localPath": r"E:\vong-quay-livestream",
        "color": "#fbbf24"
    }
]

TARGETS = [
    {
        "name": "Vòng Quay May Mắn Livestream",
        "url": "https://vongquaymayman.web.app",
        "type": "Cổng Mini-Game Livestream Chuyên Nghiệp"
    },
    {
        "name": "Cổng Thông Tin Du Lịch & BĐS LaoCaiView",
        "url": "https://laocaiview.vn",
        "type": "Cổng Sinh Thái BĐS & Du Lịch Sa Pa"
    }
]

def check_single_satellite(sat):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    url = sat["url"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 SatelliteMeshAuditor/1.0'
    }
    
    req = urllib.request.Request(url, headers=headers, method='HEAD')
    start_time = time.time()
    try:
        with urllib.request.urlopen(req, timeout=8, context=ctx) as response:
            latency = int((time.time() - start_time) * 1000)
            status_code = response.getcode()
            return {
                **sat,
                "status": "online" if status_code == 200 else "degraded",
                "statusCode": status_code,
                "latencyMs": latency,
                "error": None
            }
    except urllib.error.HTTPError as e:
        latency = int((time.time() - start_time) * 1000)
        return {
            **sat,
            "status": "online" if e.code in [200, 301, 302, 403] else "degraded",
            "statusCode": e.code,
            "latencyMs": latency,
            "error": f"HTTP {e.code}"
        }
    except Exception as e:
        # Retry with GET in case HEAD is blocked
        try:
            start_time = time.time()
            req_get = urllib.request.Request(url, headers=headers, method='GET')
            with urllib.request.urlopen(req_get, timeout=8, context=ctx) as resp_get:
                latency = int((time.time() - start_time) * 1000)
                return {
                    **sat,
                    "status": "online",
                    "statusCode": resp_get.getcode(),
                    "latencyMs": latency,
                    "error": None
                }
        except Exception as e_get:
            return {
                **sat,
                "status": "offline",
                "statusCode": 0,
                "latencyMs": 999,
                "error": str(e_get)
            }

def run_health_check():
    print("=" * 70)
    print("BẮT ĐẦU KIỂM TRA TRẠNG THÁI KẾT NỐI MẠNG LƯỚI 8 WEB VỆ TINH")
    print("=" * 70)
    results = []
    for s in SATELLITES:
        print(f"[*] Đang kiểm tra [{s['platform']}] {s['name']} ...", end=" ", flush=True)
        res = check_single_satellite(s)
        results.append(res)
        tag = "[ONLINE 200 OK]" if res["status"] == "online" else f"[STATUS {res['statusCode']}]"
        print(f"{tag} - Độ trễ: {res['latencyMs']}ms")
    
    online_count = sum(1 for r in results if r["status"] == "online")
    avg_latency = int(sum(r["latencyMs"] for r in results if r["status"] == "online") / max(1, online_count))
    
    summary = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total": len(results),
        "online": online_count,
        "avgLatencyMs": avg_latency,
        "satellites": results,
        "targets": TARGETS
    }
    
    output_path = "satellites_status.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print("-" * 70)
    print(f"Kết quả: {online_count}/{len(results)} vệ tinh trực tuyến (Online) | Độ trễ trung bình: {avg_latency}ms")
    print(f"Dữ liệu đã được xuất ra file: {output_path}")
    print("=" * 70)
    return summary

if __name__ == "__main__":
    run_health_check()
