---
name: topical-content-writer
description: >-
  Generate in-depth SEO articles by topical clusters (real estate, travel, anime review,
  food, lunar calendar, payroll tax, PSD design, VietQR) with natural in-content DoFollow
  backlinks to target money sites and social syndication.
---

# Topical Content Writer & Backlink Injector Runbook

Kỹ năng tự động sản xuất bài viết vệ tinh ngữ cảnh chuyên sâu theo đúng chuyên ngành của 8 website chính và phân phối mạng xã hội.

## 🎯 8 Cụm Chủ Đề Ngách (Topical Clusters)

1. **`cluster-laocaiview`** -> `https://laocaiview.vn`: BĐS & Du Lịch Sa Pa 2026.
2. **`cluster-vongquay`** -> `https://vongquaymayman.web.app`: Tool Minigame Vòng Quay & Thuật toán CSPRNG.
3. **`cluster-daodao`** -> `https://daodaoreview.com`: Review Anime 3D & Phim Hoạt Hình Tiên Hiệp.
4. **`cluster-angicungduoc`** -> `https://angicungduoc.food`: Cẩm Nang Ẩm Thực Sa Pa & Món Ngon Tây Bắc.
5. **`cluster-licham`** -> `https://lichampro.com`: Tra Cứu Lịch Vạn Niên & Ngày Hoàng Đạo Xuất Hành.
6. **`cluster-tinhluong`** -> `https://tinhluonggrossnet.vn`: Quy Đổi Lương Gross Sang Net 2026 & Thuế TNCN.
7. **`cluster-quickpsd`** -> `https://quickpsd.com`: Chỉnh Sửa File Photoshop PSD Online Miễn Phí.
8. **`cluster-taomaqr`** -> `https://www.taomaqr.online`: Tạo Mã VietQR Chuẩn NAPAS247 Để Bàn.

## 🛠️ Quy Trình Sản Xuất & Bơm Lực

### 1. Sinh bài viết theo cụm chỉ định
Sử dụng script `scripts/ai_content_generator.py`:
```python
import sys
sys.path.append('scripts')
from ai_content_generator import generate_article_by_cluster

# Sinh bài cho daodaoreview.com (index 2):
article = generate_article_by_cluster(2)
print(article['title'])
print(article['primary_anchor'])
```

### 2. Tiêu chuẩn bài viết SEO
Mỗi bài viết phải thỏa mãn:
- Độ dài tối thiểu 800 từ (HTML đầy đủ các thẻ H1, H2, H3, thẻ đoạn văn, danh sách).
- **1 DoFollow Contextual Link** gắn Anchor Text tự nhiên trỏ về Web Chính mục tiêu.
- **1 Semantic Bridge Link** trỏ chéo sang 1 Vệ Tinh Đám Mây (GitHub Pages, Cloudflare Workers, Vercel, Netlify...).
- Ảnh đại diện chất lượng cao kích thước chuẩn OpenGraph (1200x630px).
- Thẻ dữ liệu cấu trúc Schema.org `Article` / `NewsArticle` JSON-LD.

### 3. Kích hoạt phân phối mạng xã hội (Telegram & Pinterest)
- Gửi gói tin Webhook tới Make.com để bắn về Telegram `@Vetinhbot`.
- Tự động nạp vào `feed.xml` để Pinterest Business tự động kéo ảnh & tạo Ghim.
