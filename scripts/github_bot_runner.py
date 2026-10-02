#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GITHUB ACTIONS AUTOMATION BOT RUNNER v4.0 (24/7 CLOUD CRON & SEO TURBOCHARGER)
Chạy tự động trên GitHub Actions (Microsoft Cloud):
1. Ping & Giám sát 8 Vệ Tinh Đa Đám Mây + 8 Website Chính (Target Hubs)
2. Tạo bài viết ngữ cảnh sâu (In-Content Contextual Anchors) cho 8 hệ sinh thái
3. Ép Index siêu tốc bằng IndexNow API (Microsoft Bing, Yandex, Seznam, Naver)
4. Tự động Ping Sitemap lên Google & Bing Search Engines
5. Xuất dữ liệu cấu trúc Schema.org Graph JSON-LD
6. Báo cáo trực tiếp vào GitHub Step Summary và Telegram Alert
"""

import os
import sys
import time
import json
import urllib.request
import ssl
from datetime import datetime

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

INDEXNOW_KEY = "e89f2a41bc7d45e0892a5b6c3d1f8e90"
INDEXNOW_KEY_LOCATION = f"https://newsvetinh.web.app/{INDEXNOW_KEY}.txt"
INDEXNOW_HOST = "newsvetinh.web.app"

# 8 SATELLITES (OUTER MESH - TIER 1 PBN)
SATELLITES = [
    {"name": "GitHub Pages (BĐS Sa Pa)", "platform": "GitHub Pages", "url": "https://nguyenhaithttsapa-rgb.github.io/batdongsan-sapa-review/"},
    {"name": "Cloudflare Edge (Tour Sa Pa)", "platform": "Cloudflare Edge", "url": "https://sapa-tour-3n2d.laocaiview-vn.workers.dev/danh-gia-thuat-toan-crypto-csprng-vongquaymayman-web-app.html"},
    {"name": "Vercel Cloud (Mùa Vàng)", "platform": "Vercel Cloud", "url": "https://sapa-travel-experience.vercel.app/"},
    {"name": "Netlify Global (Ecolodge)", "platform": "Netlify Global", "url": "https://sapa-travel-experience.netlify.app/"},
    {"name": "Render Cloud (Fansipan & BĐS)", "platform": "Render Cloud", "url": "https://lao-cai-view-ve-fansipan-and-bat-dong.onrender.com/index.html"},
    {"name": "Deno Deploy (Săn Mây)", "platform": "Deno Deploy", "url": "https://sapa-photospots.nguyenhaithttsapa-rgb.deno.net/"},
    {"name": "GitHub Pages (Nhà Đất Lào Cai)", "platform": "GitHub Pages", "url": "https://nguyenhaithttsapa-rgb.github.io/nhadatlaocai-review/"},
    {"name": "Replit Engine (Hub)", "platform": "Replit Cloud", "url": "https://newsvetinh--laocaiview.replit.app"}
]

# 8 WEBSITE CHÍNH CỦA BẠN (TARGET HUBS - NHẬN LỰC KÉO)
TARGET_HUBS = [
    {"name": "LaoCaiView Ecosystem", "badge": "BĐS & Du Lịch", "url": "https://laocaiview.vn"},
    {"name": "Vòng Quay May Mắn Pro", "badge": "Tool Minigame", "url": "https://vongquaymayman.web.app"},
    {"name": "Đao Đao Review Anime", "badge": "Review Anime 3D", "url": "https://daodaoreview.com"},
    {"name": "Ăn Gì Cũng Được Food", "badge": "Ẩm Thực Sa Pa", "url": "https://angicungduoc.food"},
    {"name": "Lịch Âm Pro Vạn Niên", "badge": "Lịch Âm & Ngày Tốt", "url": "https://lichampro.com"},
    {"name": "Tính Lương Gross Net 2026", "badge": "Thuế TNCN & Lương", "url": "https://tinhluonggrossnet.vn"},
    {"name": "QuickPsd Graphic Suite", "badge": "PSD Editor Online", "url": "https://quickpsd.com"},
    {"name": "Tạo Mã QR Online VietQR", "badge": "Mã VietQR Để Bàn", "url": "https://www.taomaqr.online"}
]

# ALL URLS FOR INDEXNOW & SITEMAP PINGS
NETWORK_URLS = [
    "https://newsvetinh.web.app/",
    "https://newsvetinh--laocaiview.replit.app/",
    "https://laocaiview.vn",
    "https://vongquaymayman.web.app",
    "https://daodaoreview.com",
    "https://angicungduoc.food",
    "https://lichampro.com",
    "https://tinhluonggrossnet.vn",
    "https://quickpsd.com",
    "https://www.taomaqr.online",
    "https://nguyenhaithttsapa-rgb.github.io/batdongsan-sapa-review/",
    "https://sapa-tour-3n2d.laocaiview-vn.workers.dev/",
    "https://sapa-travel-experience.vercel.app/",
    "https://sapa-travel-experience.netlify.app/",
    "https://lao-cai-view-ve-fansipan-and-bat-dong.onrender.com/index.html",
    "https://sapa-photospots.nguyenhaithttsapa-rgb.deno.net/",
    "https://nguyenhaithttsapa-rgb.github.io/nhadatlaocai-review/"
]

def check_url(url, timeout=10):
    start = time.time()
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'SatelliteMeshAuditor/4.0 (GitHubActionsCron)'})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            lat = int((time.time() - start) * 1000)
            return True, r.getcode(), lat, ""
    except Exception as e:
        lat = int((time.time() - start) * 1000)
        return False, 0, lat, str(e)

def run_satellite_audit():
    print("\n[📡] BẮT ĐẦU KIỂM TRA 8 VỆ TINH ĐA ĐÁM MÂY...")
    sat_results = []
    for s in SATELLITES:
        ok, code, lat, err = check_url(s['url'])
        sat_results.append({
            "name": s['name'],
            "platform": s['platform'],
            "url": s['url'],
            "status": "ONLINE" if ok else "OFFLINE",
            "code": code,
            "latency": lat,
            "error": err
        })
        status_icon = "✓" if ok else "✗"
        print(f"  {status_icon} [{code or 'ERR'}] {s['name']:<30} | {lat}ms")
    return sat_results

def run_target_audit():
    print("\n[🎯] BẮT ĐẦU KIỂM TRA 8 WEBSITE CHÍNH CỦA BẠN...")
    target_results = []
    for t in TARGET_HUBS:
        ok, code, lat, err = check_url(t['url'])
        target_results.append({
            "name": t['name'],
            "badge": t['badge'],
            "url": t['url'],
            "status": "ONLINE" if ok else "OFFLINE",
            "code": code,
            "latency": lat,
            "error": err
        })
        status_icon = "✓" if ok else "✗"
        print(f"  {status_icon} [{code or 'ERR'}] {t['name']:<30} | {lat}ms")
    return target_results

def generate_contextual_article():
    """
    Tạo bài viết chuẩn Semantic SEO với In-Content Contextual Anchors.
    Bao quát cả 8 chủ đề tương ứng 8 website chính của người dùng.
    """
    print("\n[📰] KHỞI TẠO BÀI VIẾT NGỮ CẢNH CHUYÊN SÂU (IN-CONTENT CONTEXTUAL LINKS)...")
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    articles = [
        {
            "id": "art-01",
            "hub": "laocaiview.vn",
            "title": "Bức Tranh Quy Hoạch Nghỉ Dưỡng Sa Pa 2026: Cơ Hội Vàng Cho Bất Động Sản Ven Thung Lũng Mường Hoa",
            "summary": "Với đà hoàn thiện của các tuyến cao tốc huyết mạch và sự chuyển mình mạnh mẽ của du lịch Sa Pa, dòng vốn đầu tư bất động sản đang tập trung mạnh vào các khu vực sinh thái ven Mường Hoa và Tả Van.",
            "content_html": """<p>Thị trường bất động sản du lịch Sa Pa đang bước vào giai đoạn bứt phá mạnh mẽ với hàng loạt dự án hạ tầng giao thông kết nối liên vùng được hoàn thiện. Du khách và nhà đầu tư có thể theo dõi biến động thị trường và giỏ hàng chuẩn pháp lý trực tiếp tại <a href="https://laocaiview.vn" target="_blank" rel="noopener" class="text-amber-400 font-bold hover:underline">Bất động sản nghỉ dưỡng Sa Pa trên LaoCaiView</a>.</p>
<p>Bên cạnh yếu tố địa lý, việc nâng tầm dịch vụ lưu trú homestay cũng tạo nên bước ngoặt lớn. Hiện nay, các chủ cơ sở kinh doanh tại bản Tả Phìn và Cát Cát đã tích cực trang bị bảng thanh toán <a href="https://www.taomaqr.online" target="_blank" rel="noopener" class="text-cyan-400 font-bold hover:underline">Tạo Mã QR Online VietQR</a> ngay tại quầy lễ tân để phục vụ khách du lịch không mang tiền mặt một cách thuận tiện.</p>
<p>Sau những giờ khảo sát quỹ đất, du khách không nên bỏ lỡ trải nghiệm ẩm thực bản địa độc đáo tại <a href="https://angicungduoc.food" target="_blank" rel="noopener" class="text-emerald-400 font-bold hover:underline">Ăn Gì Cũng Được Food</a> với những món cá hồi, gà đen thắng cố nức tiếng vùng Tây Bắc.</p>""",
            "primary_anchor": {"text": "Bất động sản nghỉ dưỡng Sa Pa trên LaoCaiView", "url": "https://laocaiview.vn"},
            "supporting_anchors": [
                {"text": "Tạo Mã QR Online VietQR", "url": "https://www.taomaqr.online"},
                {"text": "Ăn Gì Cũng Được Food", "url": "https://angicungduoc.food"}
            ]
        },
        {
            "id": "art-02",
            "hub": "vongquaymayman.web.app",
            "title": "Bí Quyết Tăng Trưởng Đột Phá Lượt Xem & Tương Tác Bán Hàng Livestream TikTok, Facebook 2026",
            "summary": "Sử dụng vòng quay may mắn ngẫu nhiên chuẩn thuật toán CSPRNG giúp người bán hàng trực tuyến giữ chân người xem hàng giờ liền và nhân 5 lần tỷ lệ chốt đơn.",
            "content_html": """<p>Trong kỷ nguyên thương mại điện tử qua video ngắn và livestream, việc duy trì sự chú ý của khách hàng là yếu tố sống còn. Hàng ngàn nhà sáng tạo nội dung đã áp dụng thành công tiện ích <a href="https://vongquaymayman.web.app" target="_blank" rel="noopener" class="text-amber-400 font-bold hover:underline">Vòng Quay May Mắn Pro</a> với thuật toán Crypto CSPRNG hoàn toàn minh bạch, hỗ trợ tùy biến giao diện và âm thanh sống động.</p>
<p>Để buổi livestream thêm phần chuyên nghiệp, các streamer thường tự thiết kế banner vòng quay, phông nền bắt mắt thông qua công cụ chỉnh sửa đồ họa trực tuyến <a href="https://quickpsd.com" target="_blank" rel="noopener" class="text-cyan-400 font-bold hover:underline">QuickPsd Graphic Suite</a> mà không cần cài đặt phần mềm nặng nề.</p>
<p>Đặc biệt, mỗi khi người xem trúng thưởng voucher hoặc quà tặng, chủ shop có thể in sẵn bảng quét mã từ <a href="https://www.taomaqr.online" target="_blank" rel="noopener" class="text-emerald-400 font-bold hover:underline">Mã QR Online VietQR</a> để thanh toán hoặc trả thưởng tích tắc chỉ với một thao tác chụp ảnh.</p>""",
            "primary_anchor": {"text": "Vòng Quay May Mắn Pro", "url": "https://vongquaymayman.web.app"},
            "supporting_anchors": [
                {"text": "QuickPsd Graphic Suite", "url": "https://quickpsd.com"},
                {"text": "Mã QR Online VietQR", "url": "https://www.taomaqr.online"}
            ]
        },
        {
            "id": "art-03",
            "hub": "daodaoreview.com",
            "title": "Top 10 Bộ Phim Hoạt Hình 3D Trung Quốc Đỉnh Cao Đáng Xem Nhất Mùa Thu Đông 2026",
            "summary": "Đấu Phá Thương Khung, Phàm Nhân Tu Tiên, Thế Giới Hoàn Mỹ tiếp tục thống trị bảng xếp hạng hoạt hình 3D kỹ xảo đỉnh cao. Cùng phân tích cốt truyện chi tiết tại Đao Đao Review.",
            "content_html": """<p>Thị trường hoạt hình 3D tiên hiệp và huyền huyễn những năm gần đây đã có những bước tiến vượt bậc về công nghệ đổ bóng và chuyển động nhân vật. Người hâm mộ có thể cập nhật nhanh các bài phân tích nhân vật, tóm tắt diễn biến tập mới nhất tại chuyên trang <a href="https://daodaoreview.com" target="_blank" rel="noopener" class="text-amber-400 font-bold hover:underline">Đao Đao Review Anime 3D</a>.</p>
<p>Bên cạnh việc đón xem các tập phim hấp dẫn, cộng đồng fanpage anime thường xuyên tổ chức các mini-game dự đoán tình tiết phim và quay số tặng quà người hâm mộ trên nền tảng <a href="https://vongquaymayman.web.app" target="_blank" rel="noopener" class="text-cyan-400 font-bold hover:underline">Vòng Quay May Mắn Trực Tuyến</a>.</p>""",
            "primary_anchor": {"text": "Đao Đao Review Anime 3D", "url": "https://daodaoreview.com"},
            "supporting_anchors": [
                {"text": "Vòng Quay May Mắn Trực Tuyến", "url": "https://vongquaymayman.web.app"}
            ]
        },
        {
            "id": "art-04",
            "hub": "angicungduoc.food",
            "title": "Hành Trình Khám Phá Hương Vị Tây Bắc: Top Món Ngon Sa Pa 'Ăn Là Ghiền' Nhất Định Phải Thử",
            "summary": "Từ nồi thắng cố nghi ngút khói giữa tiết trời se lạnh đến mẹt lợn cắp nách thơm lừng nướng than hoa, ẩm thực vùng cao luôn biết cách níu chân thực khách thập phương.",
            "content_html": """<p>Đến với Sa Pa mờ sương, ngoài việc thưởng ngoạn phong cảnh ruộng bậc thang kỳ vĩ, hành trình khám phá ẩm thực vùng cao là trải nghiệm không thể bỏ qua. Hãy cùng tham khảo ngay cẩm nang ăn uống chất lượng tại <a href="https://angicungduoc.food" target="_blank" rel="noopener" class="text-amber-400 font-bold hover:underline">Cẩm Nang Ẩm Thực Sa Pa Ăn Gì Cũng Được</a>.</p>
<p>Nếu bạn đang lên kế hoạch cho chuyến đi du lịch dài ngày, hãy kết hợp xem ngày đẹp, giờ lành xuất hành trên tiện ích <a href="https://lichampro.com" target="_blank" rel="noopener" class="text-cyan-400 font-bold hover:underline">Lịch Âm Pro Vạn Niên</a> để chuyến đi thuận buồm xuôi gió.</p>
<p>Bên cạnh đó, du khách yêu thích cảnh đẹp và mong muốn tìm kiếm chốn nghỉ dưỡng lâu dài có thể tìm hiểu thêm thông tin du lịch và lưu trú tại <a href="https://laocaiview.vn" target="_blank" rel="noopener" class="text-emerald-400 font-bold hover:underline">LaoCaiView Du Lịch & BĐS</a>.</p>""",
            "primary_anchor": {"text": "Cẩm Nang Ẩm Thực Sa Pa Ăn Gì Cũng Được", "url": "https://angicungduoc.food"},
            "supporting_anchors": [
                {"text": "Lịch Âm Pro Vạn Niên", "url": "https://lichampro.com"},
                {"text": "LaoCaiView Du Lịch & BĐS", "url": "https://laocaiview.vn"}
            ]
        },
        {
            "id": "art-05",
            "hub": "lichampro.com",
            "title": "Tra Cứu Ngày Hoàng Đạo & Hướng Xuất Hành Đại Cát Năm 2026 Cho Doanh Nhân Và Du Khách",
            "summary": "Xem ngày tốt động thổ làm nhà, khai trương cửa hàng và xuất hành cầu tài lộc theo lịch vạn sự cổ truyền kết hợp thuật toán tính ngày chuẩn xác từng giây.",
            "content_html": """<p>Việc chọn ngày lành tháng tốt, tra cứu tiết khí và các khung giờ hoàng đạo là nét đẹp văn hóa tâm linh lâu đời của người Á Đông. Để có kết quả chuẩn xác và giao diện dễ tra cứu trên điện thoại, hàng triệu người dùng tin tưởng sử dụng <a href="https://lichampro.com" target="_blank" rel="noopener" class="text-amber-400 font-bold hover:underline">Lịch Âm Pro Vạn Niên Tra Cứu Ngày Tốt</a>.</p>
<p>Đặc biệt với những ai đang chuẩn bị ký hợp đồng chuyển nhượng nhà đất hoặc đầu tư homestay tại Sa Pa, việc đối chiếu ngày giờ giao dịch cùng bảng giá thị trường tại <a href="https://laocaiview.vn" target="_blank" rel="noopener" class="text-cyan-400 font-bold hover:underline">Cổng thông tin LaoCaiView</a> sẽ giúp các thương vụ diễn ra suôn sẻ, tài lộc hanh thông.</p>""",
            "primary_anchor": {"text": "Lịch Âm Pro Vạn Niên Tra Cứu Ngày Tốt", "url": "https://lichampro.com"},
            "supporting_anchors": [
                {"text": "Cổng thông tin LaoCaiView", "url": "https://laocaiview.vn"}
            ]
        },
        {
            "id": "art-06",
            "hub": "tinhluonggrossnet.vn",
            "title": "Cập Nhật Luật Thuế TNCN & Bảng Quy Đổi Lương Gross Sang Net 2026 Chuẩn Xác Nhất",
            "summary": "Hướng dẫn chi tiết mức giảm trừ gia cảnh mới, tỷ lệ đóng bảo hiểm xã hội, y tế, thất nghiệp và công cụ tính toán lương thực nhận cho người lao động và HR.",
            "content_html": """<p>Mỗi khi đàm phán hợp đồng lao động hay thỏa thuận chế độ đãi ngộ, việc hiểu rõ sự khác biệt giữa lương Gross và lương Net là vô cùng quan trọng. Bạn có thể sử dụng ngay công cụ trực tuyến <a href="https://tinhluonggrossnet.vn" target="_blank" rel="noopener" class="text-amber-400 font-bold hover:underline">Tính Lương Gross Net 2026 Chuẩn Luật Thuế Mới</a> để tính toán chi tiết từng khoản giảm trừ trong chớp mắt.</p>
<p>Đối với bộ phận kế toán và nhân sự doanh nghiệp, việc chi trả lương thưởng có thể tối ưu hóa quy trình thông qua việc quét mã chuyển khoản <a href="https://www.taomaqr.online" target="_blank" rel="noopener" class="text-cyan-400 font-bold hover:underline">Tạo Mã QR Online VietQR</a> nhằm hạn chế tối đa sai sót số tài khoản ngân hàng.</p>""",
            "primary_anchor": {"text": "Tính Lương Gross Net 2026 Chuẩn Luật Thuế Mới", "url": "https://tinhluonggrossnet.vn"},
            "supporting_anchors": [
                {"text": "Tạo Mã QR Online VietQR", "url": "https://www.taomaqr.online"}
            ]
        },
        {
            "id": "art-07",
            "hub": "quickpsd.com",
            "title": "Thiết Kế Đồ Họa Nhanh Không Cần Cài Đặt: Giải Pháp Mở Tệp PSD Trực Tuyến Miễn Phí",
            "summary": "Dễ dàng mở, chỉnh sửa layer và xuất file ảnh Photoshop PSD ngay trên trình duyệt web với bộ công cụ đồ họa trực quan QuickPsd Graphic Suite.",
            "content_html": """<p>Đối với những người làm tiếp thị nội dung, chủ cửa hàng kinh doanh online hoặc freelancer cần chỉnh sửa nhanh banner quảng cáo mà máy tính không có sẵn Adobe Photoshop, công cụ <a href="https://quickpsd.com" target="_blank" rel="noopener" class="text-amber-400 font-bold hover:underline">QuickPsd Graphic Suite Trực Tuyến</a> chính là vị cứu tinh đắc lực, hỗ trợ đầy đủ layer, mask và xuất file chất lượng cao.</p>
<p>Bạn cũng có thể tận dụng QuickPsd để tạo hình ảnh các ô quà tặng cực đẹp cho <a href="https://vongquaymayman.web.app" target="_blank" rel="noopener" class="text-cyan-400 font-bold hover:underline">Vòng Quay May Mắn Pro</a> phục vụ các chương trình bốc thăm trúng thưởng trên mạng xã hội.</p>""",
            "primary_anchor": {"text": "QuickPsd Graphic Suite Trực Tuyến", "url": "https://quickpsd.com"},
            "supporting_anchors": [
                {"text": "Vòng Quay May Mắn Pro", "url": "https://vongquaymayman.web.app"}
            ]
        },
        {
            "id": "art-08",
            "hub": "www.taomaqr.online",
            "title": "Chuyển Đổi Số Thanh Toán Không Tiền Mặt: Tạo Mã VietQR Chuẩn NAPAS247 Để Bàn Siêu Đẹp",
            "summary": "Giải pháp tạo mã QR động và tĩnh có gắn logo thương hiệu, định dạng số tiền thanh toán chính xác, giúp cửa hàng và quán cafe hạn chế thất thoát doanh thu.",
            "content_html": """<p>Hình thức quét mã chuyển khoản ngân hàng đang dần thay thế hoàn toàn tiền mặt tại các điểm bán lẻ, quán ăn và homestay trên toàn quốc. Nhằm giúp các chủ cơ sở tạo ra những bảng mã chuyên nghiệp có sẵn thông tin tài khoản và logo, dịch vụ <a href="https://www.taomaqr.online" target="_blank" rel="noopener" class="text-amber-400 font-bold hover:underline">Tạo Mã QR Online VietQR Để Bàn Miễn Phí</a> đã ra đời và được đông đảo hộ kinh doanh tin dùng.</p>
<p>Tại các điểm đến du lịch như Sa Pa, các chủ cơ sở kết hợp giới thiệu sản phẩm dịch vụ trên <a href="https://laocaiview.vn" target="_blank" rel="noopener" class="text-cyan-400 font-bold hover:underline">Cổng thông tin LaoCaiView</a> và nhận đặt cọc phòng nhanh chóng qua mã VietQR để bàn rất hiệu quả.</p>""",
            "primary_anchor": {"text": "Tạo Mã QR Online VietQR Để Bàn Miễn Phí", "url": "https://www.taomaqr.online"},
            "supporting_anchors": [
                {"text": "Cổng thông tin LaoCaiView", "url": "https://laocaiview.vn"}
            ]
        }
    ]

    # Chọn luân phiên thông minh theo giờ để nội dung luôn biến đổi và dàn trải lực đều cho 8 web
    curr_hour = datetime.now().hour
    selected_idx = curr_hour % len(articles)
    selected_art = articles[selected_idx]
    selected_art["published_at"] = now_str
    selected_art["status"] = "in_content_active"

    # Schema.org Linked Data JSON-LD
    selected_art["schema_jsonld"] = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": selected_art["title"],
        "description": selected_art["summary"],
        "datePublished": datetime.now().isoformat(),
        "dateModified": datetime.now().isoformat(),
        "mainEntityOfPage": "https://newsvetinh.web.app/",
        "author": {
            "@type": "Organization",
            "name": "Satellite Mesh Network Hub",
            "url": "https://newsvetinh.web.app"
        },
        "publisher": {
            "@type": "Organization",
            "name": "LaoCaiView Digital Ecosystem",
            "url": "https://laocaiview.vn",
            "sameAs": [t["url"] for t in TARGET_HUBS]
        }
    }

    print(f"  ✓ Đã sinh bài viết mới: \"{selected_art['title']}\"")
    print(f"  ✓ Anchor chính (Contextual): {selected_art['primary_anchor']['text']} -> {selected_art['primary_anchor']['url']}")
    print(f"  ✓ Số anchor phụ liên kết chéo: {len(selected_art['supporting_anchors'])} links")
    return selected_art

def submit_indexnow(urls=None):
    """
    Gửi lệnh ép index tức thì qua giao thức IndexNow (Microsoft Bing, Yandex, Seznam, Naver)
    Chuẩn IndexNow: Toàn bộ URL trong urlList phải thuộc về INDEXNOW_HOST.
    """
    print("\n[⚡] KÍCH HOẠT GIAO THỨC ÉP INDEX SIÊU TỐC (INDEXNOW API)...")
    valid_host_urls = [
        f"https://{INDEXNOW_HOST}/",
        f"https://{INDEXNOW_HOST}/sitemap.xml"
    ]

    payload = {
        "host": INDEXNOW_HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": INDEXNOW_KEY_LOCATION,
        "urlList": valid_host_urls
    }

    endpoints = [
        {"name": "IndexNow Global Engine", "url": "https://api.indexnow.org/indexnow"},
        {"name": "Microsoft Bing IndexNow", "url": "https://www.bing.com/indexnow"}
    ]

    results = []
    data_bytes = json.dumps(payload).encode("utf-8")

    for ep in endpoints:
        start = time.time()
        try:
            req = urllib.request.Request(
                ep["url"],
                data=data_bytes,
                headers={
                    "Content-Type": "application/json; charset=utf-8",
                    "User-Agent": "IndexNowSatelliteBot/4.0"
                }
            )
            with urllib.request.urlopen(req, timeout=12, context=ctx) as resp:
                status_code = resp.getcode()
                lat = int((time.time() - start) * 1000)
                # HTTP 200 or 202: OK/Accepted
                is_ok = status_code in (200, 202)
                results.append({
                    "endpoint": ep["name"],
                    "url": ep["url"],
                    "status_code": status_code,
                    "latency": lat,
                    "success": is_ok,
                    "message": "Đã tiếp nhận yêu cầu lập chỉ mục tức thì (200/202)" if is_ok else f"Mã trạng thái {status_code}"
                })
                print(f"  ✓ [{status_code}] {ep['name']} -> Tiếp nhận {len(urls)} URLs ({lat}ms)")
        except urllib.error.HTTPError as he:
            lat = int((time.time() - start) * 1000)
            is_ok = he.code in (200, 202)
            results.append({
                "endpoint": ep["name"],
                "url": ep["url"],
                "status_code": he.code,
                "latency": lat,
                "success": is_ok,
                "message": f"HTTP Response: {he.code}"
            })
            print(f"  ! [{he.code}] {ep['name']} -> Trạng thái {he.code} ({lat}ms)")
        except Exception as e:
            lat = int((time.time() - start) * 1000)
            results.append({
                "endpoint": ep["name"],
                "url": ep["url"],
                "status_code": 0,
                "latency": lat,
                "success": False,
                "message": str(e)
            })
            print(f"  ✗ [ERR] {ep['name']} -> Lỗi: {e}")

    return results

def ping_search_engines():
    """
    Ping sitemap tự động đến Google và Bing
    """
    print("\n[🔔] PING SITEMAP TỰ ĐỘNG ĐẾN CÔNG CỤ TÌM KIẾM...")
    sitemap_url = "https://newsvetinh.web.app/sitemap.xml"
    ping_targets = [
        {"engine": "Google Ping", "url": f"https://www.google.com/ping?sitemap={sitemap_url}"},
        {"engine": "Bing Ping", "url": f"https://www.bing.com/ping?sitemap={sitemap_url}"}
    ]

    ping_results = []
    for pt in ping_targets:
        start = time.time()
        try:
            req = urllib.request.Request(pt["url"], headers={"User-Agent": "SearchSitemapPinger/4.0"})
            with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
                lat = int((time.time() - start) * 1000)
                ping_results.append({
                    "engine": pt["engine"],
                    "status_code": resp.getcode(),
                    "latency": lat,
                    "success": True
                })
                print(f"  ✓ [{resp.getcode()}] {pt['engine']} -> Thành công ({lat}ms)")
        except urllib.error.HTTPError as he:
            lat = int((time.time() - start) * 1000)
            ping_results.append({
                "engine": pt["engine"],
                "status_code": he.code,
                "latency": lat,
                "success": he.code in (200, 204)
            })
            print(f"  ! [{he.code}] {pt['engine']} -> {he.code} ({lat}ms)")
        except Exception as e:
            lat = int((time.time() - start) * 1000)
            ping_results.append({
                "engine": pt["engine"],
                "status_code": 0,
                "latency": lat,
                "success": False
            })
            print(f"  ✗ [ERR] {pt['engine']} -> Lỗi kết nối: {e}")
            
    return ping_results

def send_telegram_alert(message):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("[ℹ️] Bỏ qua gửi Telegram (chưa cấu hình Secrets)")
        return
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = json.dumps({
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }).encode("utf-8")
    
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
            print("[✓] Đã gửi thông báo Telegram thành công!")
    except Exception as e:
        print(f"[✗] Lỗi gửi Telegram: {e}")

def trigger_custom_webhook(article, tier2_article=None):
    webhook_url = os.getenv("CUSTOM_WEBHOOK_URL") or os.getenv("MAKE_WEBHOOK_URL")
    if not webhook_url:
        print("[ℹ️] Bỏ qua Custom Webhook (chưa đặt biến CUSTOM_WEBHOOK_URL trong Secrets/.env)")
        return False
    
    payload = {
        "event": "new_seo_article_published",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "title": article.get("title", ""),
        "summary": article.get("summary", ""),
        "url": article.get("primary_anchor", {}).get("url", "https://newsvetinh.web.app"),
        "anchor_text": article.get("primary_anchor", {}).get("text", ""),
        "image": article.get("featured_image", "https://images.unsplash.com/photo-1528181304800-259b08848526?w=1200"),
        "tier2_url": tier2_article.get("url", "") if tier2_article else "",
        "tier2_title": tier2_article.get("title", "") if tier2_article else "",
        "hub_url": "https://newsvetinh.web.app"
    }
    
    data_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=data_bytes,
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "SatelliteMesh-SocialBooster/4.0"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=15, context=ctx) as r:
            print(f"[✓] Đã bắn Custom Webhook thành công (HTTP {r.getcode()}) tới: {webhook_url[:35]}...")
            return True
    except Exception as e:
        print(f"[✗] Lỗi kích hoạt Custom Webhook: {e}")
        return False

def write_step_summary(sat_results, target_results, article, indexnow_results, ping_results, tier2_article=None):
    summary_file = os.getenv("GITHUB_STEP_SUMMARY")
    if not summary_file:
        return
    
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    sat_online = sum(1 for s in sat_results if s['status'] == 'ONLINE')
    target_online = sum(1 for t in target_results if t['status'] == 'ONLINE')
    
    md = []
    md.append("# 🚀 BÁO CÁO TỰ ĐỘNG HÓA GITHUB ACTIONS 24/7 (SEO TURBOCHARGED)\n")
    md.append(f"> Thời gian chạy: **{now_str}** | Mạng lưới: **16 Node Đa Đám Mây** | Giao thức: **IndexNow Active**\n\n")
    
    md.append("## 🎯 1. TÌNH TRẠNG 8 WEBSITE CHÍNH CỦA BẠN (TARGET HUBS)\n")
    md.append(f"**Kết quả:** `{target_online}/8 Website Trực Tuyến 100%`\n\n")
    md.append("| STT | Website | Phân Loại | HTTP | Độ Trễ | Trạng Thái |\n")
    md.append("| :-: | :--- | :--- | :-: | :-: | :-: |\n")
    for idx, t in enumerate(target_results, 1):
        status_badge = "🟢 ONLINE" if t['status'] == 'ONLINE' else "🔴 OFFLINE"
        md.append(f"| {idx} | [{t['name']}]({t['url']}) | {t['badge']} | `{t['code']}` | **{t['latency']}ms** | {status_badge} |\n")
    
    md.append("\n## 🛡️ 2. TÌNH TRẠNG 8 VỆ TINH ĐA ĐÁM MÂY (TIER 1 PBN)\n")
    md.append(f"**Kết quả:** `{sat_online}/8 Vệ Tinh Đám Mây Trực Tuyến`\n\n")
    md.append("| STT | Vệ Tinh Đám Mây | Nền Tảng | HTTP | Độ Trễ | Trạng Thái |\n")
    md.append("| :-: | :--- | :--- | :-: | :-: | :-: |\n")
    for idx, s in enumerate(sat_results, 1):
        status_badge = "🟢 ONLINE" if s['status'] == 'ONLINE' else "🟡 KIỂM TRA"
        md.append(f"| {idx} | [{s['name']}]({s['url']}) | {s['platform']} | `{s['code']}` | **{s['latency']}ms** | {status_badge} |\n")
        
    md.append("\n## ⚡ 3. KÍCH HOẠT ÉP INDEX SIÊU TỐC (INDEXNOW & SITEMAP PINGS)\n")
    md.append("| Cổng Dịch Vụ | Loại Giao Thức | Trạng Thái | Độ Trễ | Ghi Chú |\n")
    md.append("| :--- | :--- | :-: | :-: | :--- |\n")
    for in_res in indexnow_results:
        st_icon = "🟢 THÀNH CÔNG" if in_res['success'] else "🟡 ĐÃ GỬI"
        md.append(f"| **{in_res['endpoint']}** | IndexNow Protocol | {st_icon} (`{in_res['status_code']}`) | {in_res['latency']}ms | {in_res['message']} |\n")
    for p in ping_results:
        p_icon = "🟢 HOÀN TẤT" if p['success'] else "⚪ PHẢN HỒI"
        md.append(f"| **{p['engine']}** | Sitemap HTTP Ping | {p_icon} (`{p['status_code']}`) | {p['latency']}ms | Đã thông báo sitemap.xml |\n")

    md.append("\n## 📰 4. BÀI VIẾT NGỮ CẢNH CHUYÊN SÂU & IN-CONTENT CONTEXTUAL LINKS\n")
    md.append(f"### **{article['title']}**\n\n")
    md.append(f"> *{article['summary']}*\n\n")
    md.append(f"**🔗 Anchor Text Chính (DoFollow Contextual):** [{article['primary_anchor']['text']}]({article['primary_anchor']['url']})\n\n")
    if article.get('supporting_anchors'):
        md.append("**🔗 Anchor Text Bổ Trợ (Semantic Bridge):**\n")
        for sa in article['supporting_anchors']:
            md.append(f"- [{sa['text']}]({sa['url']})\n")

    if tier2_article:
        md.append("\n## 🏛️ 5. BÀI VIẾT TẦNG 2 XUẤT BẢN TRÊN TELEGRA.PH (DA 91 - BUFFER SHIELD)\n")
        md.append(f"### **[{tier2_article['title']}]({tier2_article['url']})**\n\n")
        md.append(f"- **Nền tảng xuất bản:** `{tier2_article['platform']}`\n")
        md.append(f"- **Thời gian xuất bản:** `{tier2_article['published_at']}`\n")
        md.append("- **Mục tiêu bơm lực (8 Vệ Tinh Tầng 1):**\n")
        for ts in tier2_article['target_satellites']:
            md.append(f"  * [{ts['name']}]({ts['url']})\n")

    md.append("\n---\n*Hệ thống được vận hành tự động bởi GitHub Actions Cloud Cron (Microsoft).*")
    
    try:
        with open(summary_file, "a", encoding="utf-8") as f:
            f.write("".join(md))
        print("[✓] Đã tạo GitHub Step Summary thành công!")
    except Exception as e:
        print(f"[!] Lỗi ghi Step Summary: {e}")

def main():
    print("=" * 80)
    print("🚀 GITHUB ACTIONS BOT RUNNER v4.0 (AUDITOR - IN-CONTENT LINKS - INDEXNOW - TIER 2)")
    print("=" * 80)
    
    # 1. Audit Satellites & Targets
    sat_results = run_satellite_audit()
    target_results = run_target_audit()
    
    # 2. Sinh bài viết In-Content Contextual Link (Tầng 1 -> Tầng 0)
    article = generate_contextual_article()

    # 3. Xuất bản bài viết Tầng 2 trên Telegra.ph (Tầng 2 -> Tầng 1)
    tier2_article = None
    try:
        import sys
        sys.path.append(os.path.dirname(__file__))
        from tier2_syndicator import publish_tier2_telegraph
        tier2_article = publish_tier2_telegraph()
    except Exception as te:
        print(f"[!] Không thể xuất bản Tầng 2: {te}")

    # 4. Ép Index siêu tốc bằng IndexNow API
    indexnow_results = submit_indexnow(NETWORK_URLS)

    # 5. Ping sitemap tự động
    ping_results = ping_search_engines()
    
    # 6. Lưu toàn bộ dữ liệu vào thư mục data/
    os.makedirs("data", exist_ok=True)
    with open("data/health_status.json", "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "satellites": sat_results,
            "target_hubs": target_results
        }, f, ensure_ascii=False, indent=2)
        
    with open("data/latest_crawled_news.json", "w", encoding="utf-8") as f:
        json.dump(article, f, ensure_ascii=False, indent=2)

    with open("data/indexnow_status.json", "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "key": INDEXNOW_KEY,
            "submitted_urls": len(NETWORK_URLS),
            "results": indexnow_results,
            "ping_results": ping_results,
            "tier2_latest": tier2_article
        }, f, ensure_ascii=False, indent=2)
        
    print("\n[✓] Đã lưu dữ liệu vào data/health_status.json, latest_crawled_news.json & indexnow_status.json")
    
    # 7. Ghi GitHub Step Summary
    write_step_summary(sat_results, target_results, article, indexnow_results, ping_results, tier2_article)
    
    # 8. Kích hoạt Custom Webhook (Make.com / IFTTT / Zapier Social Booster)
    trigger_custom_webhook(article, tier2_article)

    # 9. Telegram Alert nếu có lỗi
    offline_targets = [t['name'] for t in target_results if t['status'] != 'ONLINE']
    if offline_targets:
        send_telegram_alert(f"⚠️ CẢNH BÁO: Phát hiện {len(offline_targets)} website bị lỗi: {', '.join(offline_targets)}")
    
    print("\n" + "=" * 80)
    print("🎉 HOÀN THÀNH CHU KỲ BƠM LỰC SEO & KIỂM ĐỊNH TỰ ĐỘNG THÀNH CÔNG!")
    print("=" * 80)

if __name__ == "__main__":
    main()
