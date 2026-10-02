#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SATELLITE AUTOMATION MASTER ENGINE (REPLIT COMPATIBLE)
Mô-đun máy chủ tự động hóa ngầm:
1. Giám sát & Ping 8 web vệ tinh theo giờ (Hourly Satellite Health Checker)
2. Tự động cào & tổng hợp tin tức BĐS Sa Pa (Real Estate News Aggregator)
3. Đăng bài tự động lên Mạng xã hội / Telegram Bot / Webhook
4. Máy chủ HTTP giữ Replit thức 24/7 (Keep-Alive Endpoint)
"""

import os
import sys
import time
import json
import threading
import urllib.request
import urllib.error
import ssl
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 8 SATELLITE TARGETS
SATELLITES = [
    {"name": "GitHub Pages (BĐS Sa Pa)", "url": "https://nguyenhaithttsapa-rgb.github.io/batdongsan-sapa-review/"},
    {"name": "Cloudflare Workers (Tour Sa Pa)", "url": "https://sapa-tour-3n2d.laocaiview-vn.workers.dev/danh-gia-thuat-toan-crypto-csprng-vongquaymayman-web-app.html"},
    {"name": "Vercel Cloud (Mùa Vàng Sa Pa)", "url": "https://sapa-travel-experience.vercel.app/"},
    {"name": "Netlify Global (Ecolodge Sa Pa)", "url": "https://sapa-travel-experience.netlify.app/"},
    {"name": "Render Cloud (Văn Hóa Sa Pa)", "url": "https://sapa-batdongsan-live.onrender.com/"},
    {"name": "Firebase Hub (Vòng Quay May Mắn)", "url": "https://vongquaymayman.web.app/"},
    {"name": "Newsvetinh Hub (Firebase)", "url": "https://newsvetinh.web.app"},
    {"name": "LaoCaiView Ecosystem (Target)", "url": "https://laocaiview.vn"}
]

# CONFIGURATION
PING_INTERVAL_SECONDS = 3600  # Mỗi 1 giờ kiểm tra 1 lần
CRAWL_INTERVAL_SECONDS = 14400 # Mỗi 4 giờ quét tin BĐS 1 lần

# ==============================================================================
# NHIỆM VỤ 1: BOT KIỂM TRA PING 8 VỆ TINH THEO GIỜ
# ==============================================================================
def job_ping_satellites():
    while True:
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[📡 {now_str}] BẮT ĐẦU CHU KỲ KIỂM TRA PING 8 VỆ TINH...")
        
        status_report = []
        for s in SATELLITES:
            start_t = time.time()
            try:
                req = urllib.request.Request(s["url"], headers={"User-Agent": "SatelliteMeshAuditor/2.0"})
                with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
                    lat = int((time.time() - start_t) * 1000)
                    code = resp.getcode()
                    status_report.append(f"  ✓ [{code}] {s['name']}: {lat}ms")
            except Exception as e:
                lat = int((time.time() - start_t) * 1000)
                status_report.append(f"  ✗ [ERR] {s['name']}: {e}")
        
        print("\n".join(status_report))
        print(f"[✓] Đã hoàn thành chu kỳ kiểm tra. Nghỉ {PING_INTERVAL_SECONDS // 60} phút...\n")
        time.sleep(PING_INTERVAL_SECONDS)

# ==============================================================================
# NHIỆM VỤ 2: BOT CÀO & TỔNG HỢP TIN BĐS SA PA TỰ ĐỘNG
# ==============================================================================
def job_crawl_sapa_news():
    while True:
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[📰 {now_str}] BOT CÀO TIN BĐS SA PA ĐANG QUÉT NGUỒN DỮ LIỆU...")
        
        # Mô phỏng quét dữ liệu từ các cổng tin hoặc file local
        sample_topics = [
            "Thị trường đất nền Thung lũng Mường Hoa Sa Pa đón sóng quy hoạch mới",
            "Cơ hội sở hữu homestay view săn mây Ô Quy Hồ lợi nhuận dòng tiền ổn định",
            "Cập nhật bảng giá đất mặt phố Cầu Mây và Fansipan quý mới",
            "Phân tích tiềm năng khai thác du lịch nghỉ dưỡng bản Cát Cát và Tả Van"
        ]
        
        # Tự động tạo bài viết mẫu và lưu vào database / file
        article = {
            "title": sample_topics[int(time.time()) % len(sample_topics)],
            "timestamp": now_str,
            "target_link": "https://laocaiview.vn",
            "status": "ready_to_publish"
        }
        
        # Ghi nhật ký vào file
        with open("latest_crawled_news.json", "w", encoding="utf-8") as f:
            json.dump(article, f, ensure_ascii=False, indent=2)
            
        print(f"  ✓ Đã cập nhật tin mới: {article['title']}")
        print(f"[✓] Hoàn thành cào tin. Nghỉ {CRAWL_INTERVAL_SECONDS // 3600} giờ...\n")
        time.sleep(CRAWL_INTERVAL_SECONDS)

# ==============================================================================
# NHIỆM VỤ 3: BOT ĐĂNG BÀI MẠNG XÃ HỘI (FACEBOOK / TELEGRAM WEBHOOK)
# ==============================================================================
def post_to_social_channels(message, link="https://vongquaymayman.web.app"):
    """
    Hàm gửi bài lên Facebook Page hoặc Kênh Telegram thông báo tự động.
    """
    print(f"[📢 MẠNG XÃ HỘI] Đang phân phối bài viết: {message[:50]}... -> {link}")
    # Nếu có Telegram Bot Token và Chat ID, gửi trực tiếp qua Telegram Webhook:
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if telegram_token and telegram_chat_id:
        tg_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        payload = json.dumps({
            "chat_id": telegram_chat_id,
            "text": f"🚀 TIN MỚI SA PA:\n{message}\n👉 Xem ngay: {link}",
            "parse_mode": "HTML"
        }).encode("utf-8")
        req = urllib.request.Request(tg_url, data=payload, headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=8, context=ctx) as res:
                print("  ✓ Đã gửi thông báo Telegram thành công!")
        except Exception as e:
            print("  ✗ Lỗi gửi Telegram:", e)

# ==============================================================================
# NHIỆM VỤ 4: KEEP-ALIVE WEB SERVER (CHỐNG REPLIT NGỦ ĐÔNG 24/7)
# ==============================================================================
class KeepAliveHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        
        response_data = {
            "service": "Satellite Automation Master Engine",
            "status": "HEALTHY_200_OK",
            "uptime_check": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "monitored_nodes": len(SATELLITES),
            "message": "Máy chủ ngầm Replit đang hoạt động liên tục 24/7!"
        }
        self.wfile.write(json.dumps(response_data, ensure_ascii=False).encode("utf-8"))

    def log_message(self, format, *args):
        pass  # Giảm bớt log rác

def start_keep_alive_server(port=8080):
    server = HTTPServer(("0.0.0.0", port), KeepAliveHandler)
    print(f"[⚡ KEEP-ALIVE] Máy chủ ngầm lắng nghe tại cổng {port}...")
    server.serve_forever()

# ==============================================================================
# ĐIỀU PHỐI ĐA LUỒNG (MULTI-THREADING ORCHESTRATOR)
# ==============================================================================
if __name__ == "__main__":
    print("=" * 75)
    print("🚀 KHỞI ĐỘNG HỆ THỐNG MÁY CHỦ TỰ ĐỘNG HÓA NGẦM TRÊN REPLIT")
    print("=" * 75)
    
    # 1. Luồng Ping 8 vệ tinh
    t_ping = threading.Thread(target=job_ping_satellites, daemon=True)
    t_ping.start()
    
    # 2. Luồng Cào tin BĐS
    t_crawl = threading.Thread(target=job_crawl_sapa_news, daemon=True)
    t_crawl.start()
    
    # 3. Luồng Keep-Alive Server chính (Chạy ở luồng Foreground để giữ container)
    port = int(os.environ.get("PORT", 8080))
    start_keep_alive_server(port)
