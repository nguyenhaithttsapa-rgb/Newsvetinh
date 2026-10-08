# QUY TẮC QUẢN TRỊ & VẬN HÀNH HỆ SINH THÁI 8 VỆ TINH ĐA ĐÁM MÂY (GEMINI.MD)

> **Dự án:** Satellite Mesh Network & Content Syndication Hub  
> **Cơ sở hạ tầng:** 16 Node Đa Đám Mây (8 Vệ Tinh Tier 1 + 8 Website Chính Tier 0)  
> **Mục tiêu:** Tự động hóa SEO, phân phối link juice an toàn, ép Index tức thì và kéo Social Traffic 24/7.

---

## 🏛️ 1. KIẾN TRÚC MẠNG LƯỚI & BẢN ĐỒ 16 NODE

### A. 8 Website Chính (Target Hubs - Nhận Lực Kéo):
1. `https://laocaiview.vn` - LaoCaiView Ecosystem (BĐS & Du Lịch Sa Pa)
2. `https://vongquaymayman.web.app` - Vòng Quay May Mắn Pro (Tool Minigame CSPRNG)
3. `https://daodaoreview.com` - Đao Đao Review Anime (Review Anime 3D & Tiên Hiệp)
4. `https://angicungduoc.food` - Ăn Gì Cũng Được Food (Ẩm Thực Sa Pa & Tây Bắc)
5. `https://lichampro.com` - Lịch Âm Pro Vạn Niên (Tra Cứu Lịch & Ngày Hoàng Đạo)
6. `https://tinhluonggrossnet.vn` - Tính Lương Gross Net 2026 (Luật Thuế & Lương HR)
7. `https://quickpsd.com` - QuickPsd Graphic Suite (Chỉnh Sửa PSD Online)
8. `https://www.taomaqr.online` - Tạo Mã QR Online VietQR (Mã VietQR Để Bàn Chuẩn)

### B. 8 Vệ Tinh Đa Đám Mây (Outer Mesh - Tier 1 PBN):
1. `GitHub Pages (BĐS Sa Pa)`: `https://nguyenhaithttsapa-rgb.github.io/batdongsan-sapa-review/`
2. `Cloudflare Edge (Tour Sa Pa)`: `https://sapa-tour-3n2d.laocaiview-vn.workers.dev/`
3. `Vercel Cloud (Mùa Vàng)`: `https://sapa-travel-experience.vercel.app/`
4. `Netlify Global (Ecolodge)`: `https://sapa-travel-experience.netlify.app/`
5. `Render Cloud (Fansipan & BĐS)`: `https://lao-cai-view-ve-fansipan-and-bat-dong.onrender.com/index.html`
6. `Deno Deploy (Săn Mây)`: `https://sapa-photospots.nguyenhaithttsapa-rgb.deno.net/`
7. `GitHub Pages (Nhà Đất Lào Cai)`: `https://nguyenhaithttsapa-rgb.github.io/nhadatlaocai-review/`
8. `Replit Cloud (Hub Mirror)`: `https://newsvetinh--laocaiview.replit.app`
- **Master Hub & RSS Host:** `https://newsvetinh.web.app` (Firebase Hosting)

---

## ⚡ 2. NGUYÊN TẮC VIẾT BÀI & BƠM LINK (LINK JUICE INTEGRITY)

1. **Topical Clustering (Đúng chủ đề ngách):**
   - Bài viết cho website nào phải chuẩn nội dung chuyên ngành của website đó (Anime review cho `daodaoreview.com`, BĐS cho `laocaiview.vn`, thuế cho `tinhluonggrossnet.vn`...).
   - Tuyệt đối không viết lan man hoặc nhầm lẫn giữa các chủ đề.

2. **In-Content Contextual Anchors (DoFollow Tự Nhiên):**
   - Mỗi bài viết chứa 1 **Anchor chính (DoFollow)** trỏ trực tiếp ngữ cảnh về Website Chính tương ứng.
   - Mỗi bài viết chứa 1 **Semantic Bridge Link** trỏ chéo sang 1 Vệ Tinh Đám Mây để liên kết mạng lưới thực thể.
   - Không spam từ khóa exact match; sử dụng từ khóa dài tự nhiên (LSI & Semantic Keywords).

3. **Cấu Trúc Bài Viết Chuẩn SEO (RankMath / Yoast):**
   - Tiêu đề H1 hấp dẫn, thẻ tóm tắt (Lead Summary).
   - Tối thiểu 2 đề mục H2, 2 đề mục H3, danh sách bullet points và phần kết luận kêu gọi hành động (CTA).
   - Thẻ dữ liệu cấu trúc Schema.org `Article` / `NewsArticle` JSON-LD.
   - Ảnh đại diện chất lượng cao (Unsplash / Cloudinary CDN).

4. **Buffer Shield (Tầng 2 Telegra.ph DA 91):**
   - Mọi bài viết Tầng 2 trên Telegra.ph chỉ được trỏ về **8 Vệ Tinh Tầng 1** hoặc Cổng Master Hub, **KHÔNG trỏ thẳng** về 8 Website Chính để đảm bảo an toàn tuyệt đối trước thuật toán chống PBN của Google.

---

## 🚀 3. QUY TẮC TỰ ĐỘNG HÓA & PHÂN PHỐI ĐA KÊNH

1. **Lịch trình Cloud Cron:**
   - Lịch chạy tự động mỗi ngày vào **đúng 06:00 Sáng (Giờ Việt Nam GMT+7 = 23:00 UTC)** trên GitHub Actions.
   - Tự động luân phiên chọn cụm chủ đề ngách để phân bổ lực đều cho 8 website.

2. **Ép Index Siêu Tốc (IndexNow Protocol):**
   - Tự động gửi payload JSON 17 URLs tới Bing IndexNow & IndexNow Global Engine mỗi khi có bài mới.
   - Key xác thực bắt buộc luôn duy trì tại: `https://newsvetinh.web.app/e89f2a41bc7d45e0892a5b6c3d1f8e90.txt`.

3. **Social Syndication (Make.com & Pinterest):**
   - **Telegram:** Gửi webhook tới Make.com để bắn thông báo và link bài viết về `@Vetinhbot` (Chat ID `8803740470`).
   - **Pinterest Business:** Nguồn cấp dữ liệu `https://newsvetinh.web.app/feed.xml` tự động tạo Ghim ảnh lên bảng *"Sa Pa Du Lịch & Bất Động Sản"*. Toàn bộ link trong `<item><link>` của `feed.xml` bắt buộc phải thuộc domain `https://newsvetinh.web.app/`.

---

## 🔒 4. QUY TẮC GIT & TRIỂN KHAI (DEPLOYMENT)

1. **Bảo toàn dữ liệu (.env & Secrets):**
   - Tuyệt đối không commit token bí mật hoặc `.env` lên GitHub công khai (đã cấu hình `.gitignore`).
   - Mọi API token được nạp qua GitHub Repository Secrets (`CUSTOM_WEBHOOK_URL`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`).

2. **Đồng bộ Remote & Deploy Firebase:**
   - Khi chỉnh sửa file giao diện hoặc RSS: Deploy ngay bằng `cmd.exe /c "firebase deploy --only hosting:newsvetinh"`.
   - Trước khi push git, luôn chạy `git pull --rebase origin main` để tránh xung đột với các commit tự động của bot.
   - Khi có merge conflict ở `data/*.json`, ưu tiên giữ dữ liệu mới nhất (`git checkout --ours data/*`).
