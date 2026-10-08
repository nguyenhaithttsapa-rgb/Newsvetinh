---
name: satellite-mesh-operations
description: >-
  Manage, audit, and operate the 16-node multi-cloud satellite network
  (GitHub, Cloudflare, Vercel, Netlify, Render, Deno, Replit, Firebase),
  submit IndexNow to Bing/Yandex, and syndicate Tier 2 articles to Telegra.ph.
---

# Satellite Mesh Operations & SEO Turbopack Runbook

Hướng dẫn quy trình vận hành, giám sát 16 node mạng lưới và kích hoạt các giao thức ép Index, Buffer Shield.

## 🛠️ Quy Trình Vận Hành

### 1. Kiểm tra tình trạng 16 Node (8 Satellites + 8 Targets)
Chạy script kiểm tra trực tiếp độ trễ và mã HTTP:
```bash
python scripts/github_bot_runner.py
```
- Đảm bảo 100% các node trả về mã `200 OK`.
- Báo cáo được lưu tự động tại `data/health_status.json`.

### 2. Kích hoạt ép Index tức thì (IndexNow API)
Mỗi khi xuất bản bài viết hoặc cập nhật vệ tinh:
- Key xác thực: `https://newsvetinh.web.app/e89f2a41bc7d45e0892a5b6c3d1f8e90.txt`
- Endpoint 1: `https://api.indexnow.org/indexnow`
- Endpoint 2: `https://www.bing.com/indexnow`
- Danh sách 17 URLs được nộp tự động. Kiểm tra kết quả tại `data/indexnow_status.json`.

### 3. Xuất bản bài viết Tầng 2 lên Telegra.ph (DA 91)
Chạy bộ xuất bản Telegra.ph độc lập:
```bash
python -c "import sys; sys.path.append('scripts'); from tier2_syndicator import publish_tier2_telegraph; print(publish_tier2_telegraph())"
```
- Tự động lấy token tác giả trong `data/telegraph_auth.json`.
- Gắn liên kết trỏ ngược về các vệ tinh đám mây (GitHub, Vercel, Deno, Render).
- Lưu lịch sử vào `data/tier2_articles.json`.

### 4. Triển khai Firebase Hosting
Sau khi cập nhật giao diện `index.html` hoặc `feed.xml`:
```cmd
cmd.exe /c "firebase deploy --only hosting:newsvetinh"
```
Kiểm tra trực tiếp tại: `https://newsvetinh.web.app`.
