#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TIER 2 CONTENT SYNDICATOR (TELEGRA.PH AUTOMATION & BACKLINK MULTIPLIER)
Tự động xuất bản bài viết chất lượng cao lên nền tảng Telegra.ph (Telegram API - DA 91):
- Bơm sức mạnh liên kết (Backlinks) và Social Traffic trực tiếp vào 8 Vệ Tinh Đa Đám Mây (Tầng 1).
- KHÔNG trỏ thẳng về 8 Web Chính (Đóng vai trò là Khiên Bảo Vệ Buff Lực An Toàn Tuyệt Đối).
- Tự động lưu trữ lịch sử bài viết vào data/tier2_articles.json.
"""

import os
import sys
import json
import time
import ssl
import urllib.request
import urllib.parse
from datetime import datetime

try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

TELEGRAPH_AUTH_FILE = "data/telegraph_auth.json"
TIER2_ARTICLES_FILE = "data/tier2_articles.json"

def get_or_create_account():
    """Lấy token tài khoản Telegra.ph có sẵn hoặc tạo mới tự động"""
    if os.path.exists(TELEGRAPH_AUTH_FILE):
        try:
            with open(TELEGRAPH_AUTH_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data.get("access_token"):
                    return data["access_token"]
        except Exception:
            pass

    print("[🔑] Khởi tạo tài khoản tác giả Telegra.ph tự động...")
    url = "https://api.telegra.ph/createAccount"
    payload = urllib.parse.urlencode({
        "short_name": "LaoCaiViewHub",
        "author_name": "Lao Cai View & Satellite Mesh Network",
        "author_url": "https://newsvetinh.web.app"
    }).encode("utf-8")

    req = urllib.request.Request(url, data=payload, headers={"User-Agent": "TelegraphTier2Bot/1.0"})
    with urllib.request.urlopen(req, timeout=10, context=ctx) as r:
        res = json.loads(r.read())
        if res.get("ok"):
            token = res["result"]["access_token"]
            os.makedirs("data", exist_ok=True)
            with open(TELEGRAPH_AUTH_FILE, "w", encoding="utf-8") as f:
                json.dump({
                    "access_token": token,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "author_name": "Lao Cai View & Satellite Mesh Network"
                }, f, ensure_ascii=False, indent=2)
            print("  ✓ Đã cấp token Telegra.ph mới thành công!")
            return token
        else:
            raise RuntimeError(f"Lỗi tạo tài khoản Telegra.ph: {res}")

def get_tier2_templates():
    """Kho bài viết Tầng 2 chuyên sâu, chèn DoFollow link trỏ trực tiếp về 8 Vệ Tinh (Tầng 1)"""
    return [
        {
            "id": "t2-art-01",
            "title": "Cẩm Nang Toàn Tập Chinh Phục Đỉnh Fansipan & Kinh Nghiệm Mua Vé Cáp Treo 2026",
            "target_satellites": [
                {"name": "Render Cloud (Fansipan & BĐS)", "url": "https://lao-cai-view-ve-fansipan-and-bat-dong.onrender.com/index.html"},
                {"name": "Cloudflare Edge (Tour Sa Pa)", "url": "https://sapa-tour-3n2d.laocaiview-vn.workers.dev/"}
            ],
            "content_nodes": [
                {"tag": "p", "children": ["Đỉnh Fansipan - nóc nhà Đông Dương ở độ cao 3.143m luôn là điểm đến mơ ước của hàng triệu du khách. Để có một chuyến đi trọn vẹn, việc nắm rõ giờ vận hành cáp treo Sun World và các kinh nghiệm săn mây là vô cùng quan trọng."]},
                {"tag": "h3", "children": ["1. Giờ đón biển mây đẹp nhất"]},
                {"tag": "p", "children": ["Biển mây trên đỉnh Fansipan thường xuất hiện kỳ ảo nhất vào các khung giờ sáng sớm (7h00 - 9h00) hoặc lúc hoàng hôn chiều muộn (16h00 - 17h30). Du khách có thể theo dõi chi tiết bảng giá vé cáp treo và cẩm nang di chuyển tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://lao-cai-view-ve-fansipan-and-bat-dong.onrender.com/index.html"}, "children": ["👉 Cẩm Nang Chinh Phục Fansipan & Giá Vé Cáp Treo Chi Tiết"]},
                    "."
                ]},
                {"tag": "h3", "children": ["2. Lộ trình kết hợp tour bản làng 3 ngày 2 đêm"]},
                {"tag": "p", "children": ["Sau khi chinh phục đỉnh thiêng, hãy dành thời gian khám phá nét đẹp văn hóa của các bản Tả Van, Cát Cát và thưởng thức ẩm thực thắng cố cá hồi Tây Bắc theo gợi ý lịch trình tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://sapa-tour-3n2d.laocaiview-vn.workers.dev/"}, "children": ["👉 Lịch Trình Tour Trekking Sa Pa 3N2D Trọn Gói Tối Ưu Chi Phí"]},
                    "."
                ]}
            ]
        },
        {
            "id": "t2-art-02",
            "title": "Bức Tranh Bất Động Sản Sa Pa 2026: Đòn Bẩy Hạ Tầng & Dòng Tiền Du Lịch Bứt Phá",
            "target_satellites": [
                {"name": "GitHub Pages (BĐS Sa Pa)", "url": "https://nguyenhaithttsapa-rgb.github.io/batdongsan-sapa-review/"},
                {"name": "GitHub Pages 2 (Nhà Đất Lào Cai)", "url": "https://nguyenhaithttsapa-rgb.github.io/nhadatlaocai-review/"}
            ],
            "content_nodes": [
                {"tag": "p", "children": ["Thị trường bất động sản nghỉ dưỡng tại thị xã Sa Pa và tỉnh Lào Cai đang bước vào chu kỳ tăng trưởng mới nhờ sự hoàn thiện đồng bộ của hệ thống giao thông cao tốc và các dự án quy hoạch đô thị sinh thái."]},
                {"tag": "h3", "children": ["1. Quỹ đất ven thung lũng Mường Hoa & Tả Phìn"]},
                {"tag": "p", "children": ["Làn sóng đầu tư homestay boutique và khu nghỉ dưỡng sinh thái cao cấp đang hướng mạnh về khu vực thung lũng Mường Hoa. Nhà đầu tư quan tâm có thể cập nhật giỏ hàng và pháp lý chuyển nhượng tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://nguyenhaithttsapa-rgb.github.io/batdongsan-sapa-review/"}, "children": ["👉 Đánh Giá Thị Trường Bất Động Sản Nghỉ Dưỡng Sa Pa 2026"]},
                    "."
                ]},
                {"tag": "h3", "children": ["2. Tiềm năng nhà đất trung tâm Lào Cai"]},
                {"tag": "p", "children": ["Khu vực cửa khẩu quốc tế và các trục đại lộ shophouse tại TP Lào Cai ghi nhận thanh khoản ổn định với lợi suất khai thác cho thuê hấp dẫn. Đọc thêm phân tích tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://nguyenhaithttsapa-rgb.github.io/nhadatlaocai-review/"}, "children": ["👉 Báo Cáo Quy Hoạch & Bản Đồ Địa Chính Nhà Đất Lào Cai"]},
                    "."
                ]}
            ]
        },
        {
            "id": "t2-art-03",
            "title": "Top Tọa Độ Săn Mây Đẹp Như Tranh Vẽ & Góc Check-in Sống Ảo Triệu View Sa Pa",
            "target_satellites": [
                {"name": "Deno Deploy (Săn Mây)", "url": "https://sapa-photospots.nguyenhaithttsapa-rgb.deno.net/"},
                {"name": "Vercel Cloud (Mùa Vàng)", "url": "https://sapa-travel-experience.vercel.app/"}
            ],
            "content_nodes": [
                {"tag": "p", "children": ["Sa Pa không chỉ có khí hậu trong lành mát mẻ quanh năm mà còn sở hữu những biển mây cuồn cuộn đổ qua thung lũng, tạo nên khung cảnh bồng lai tiên cảnh thu hút đông đảo bạn trẻ mê nhiếp ảnh."]},
                {"tag": "h3", "children": ["1. Các điểm săn mây không thể bỏ qua"]},
                {"tag": "p", "children": ["Đèo Ô Quy Hồ, đỉnh Hàm Rồng, đồi Mường Hoa và cây cô đơn Tả Phìn là những địa danh có góc máy tuyệt mỹ. Khám phá trọn bộ tọa độ chi tiết tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://sapa-photospots.nguyenhaithttsapa-rgb.deno.net/"}, "children": ["👉 Cẩm Nang Săn Mây & Điểm Check-in Sa Pa Sống Ảo Triệu View"]},
                    "."
                ]},
                {"tag": "h3", "children": ["2. Mùa lúa chín vàng óng trên ruộng bậc thang"]},
                {"tag": "p", "children": ["Thời điểm thu hoạch lúa vào tháng 9 - tháng 10 hàng năm mang đến sắc vàng rực rỡ khắp bản làng. Tham khảo lịch trình ngắm lúa chín tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://sapa-travel-experience.vercel.app/"}, "children": ["👉 Kinh Nghiệm Du Lịch Mùa Vàng Ruộng Bậc Thang Sa Pa"]},
                    "."
                ]}
            ]
        },
        {
            "id": "t2-art-04",
            "title": "Giải Pháp Ứng Dụng Thuật Toán CSPRNG & Vòng Quay May Mắn Giữ Chân Người Xem Livestream",
            "target_satellites": [
                {"name": "Netlify Global (Ecolodge)", "url": "https://sapa-travel-experience.netlify.app/"},
                {"name": "Replit Engine (Hub)", "url": "https://newsvetinh--laocaiview.replit.app"}
            ],
            "content_nodes": [
                {"tag": "p", "children": ["Trong thời đại livestream bán hàng bùng nổ trên TikTok Shop và Facebook, việc tổ chức mini-game công bằng, minh bạch với thuật toán sinh số ngẫu nhiên mật mã (CSPRNG) là chìa khóa giữ chân khách hàng hàng giờ liền."]},
                {"tag": "h3", "children": ["1. Tăng tỷ lệ tương tác và đơn hàng"]},
                {"tag": "p", "children": ["Các streamer chuyên nghiệp áp dụng công cụ quay số bốc thăm voucher nghỉ dưỡng và mã giảm giá để nhân 5 lần tỷ lệ chốt deal. Đọc đánh giá chi tiết thuật toán tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://sapa-travel-experience.netlify.app/"}, "children": ["👉 Phân Tích Công Cụ Vòng Quay Minigame Cho Livestream & Teambuilding"]},
                    "."
                ]},
                {"tag": "h3", "children": ["2. Kiến trúc mạng lưới điều phối đám mây"]},
                {"tag": "p", "children": ["Mô hình kết nối đa nền tảng điều phối liên kết tự động hỗ trợ tăng tốc chỉ số SEO mạng lưới một cách bền vững. Xem thêm tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://newsvetinh--laocaiview.replit.app"}, "children": ["👉 Hệ Thống Điều Phối Trung Tâm Master Hub Đa Đám Mây"]},
                    "."
                ]}
            ]
        },
        {
            "id": "t2-art-05",
            "title": "Sức Hút Hoạt Hình 3D Tiên Hiệp: Đột Phá Đồ Họa Unreal Engine & Cốt Truyện Kinh Điển",
            "target_satellites": [
                {"name": "Replit Engine (Hub)", "url": "https://newsvetinh--laocaiview.replit.app"},
                {"name": "Deno Deploy (Săn Mây)", "url": "https://sapa-photospots.nguyenhaithttsapa-rgb.deno.net/"}
            ],
            "content_nodes": [
                {"tag": "p", "children": ["Thị trường phim hoạt hình 3D Trung Quốc đang bùng nổ mạnh mẽ với các tác phẩm đình đám như Đấu Phá Thương Khung, Phàm Nhân Tu Tiên, Thế Giới Hoàn Mỹ. Kỹ xảo võ thuật mãn nhãn và cốt truyện tu chân sâu sắc thu hút hàng chục triệu lượt xem mỗi tập."]},
                {"tag": "h3", "children": ["1. Phân tích cốt truyện và bảng xếp hạng cảnh giới"]},
                {"tag": "p", "children": ["Người hâm mộ có thể cập nhật các bài phân tích nhân vật, tóm tắt tình tiết tập mới nhất và giải mã cảnh giới tu luyện tại mạng lưới nội dung số "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://newsvetinh--laocaiview.replit.app"}, "children": ["👉 Cổng Thông Tin Đánh Giá Phim Hoạt Hình & Truyền Thông Số Replit"]},
                    "."
                ]},
                {"tag": "h3", "children": ["2. Kết nối cộng đồng và mạng lưới đa nền tảng"]},
                {"tag": "p", "children": ["Hệ thống mạng lưới truyền thông số và phân phối nội dung đa đám mây giúp bạn đọc tiếp cận nhanh chóng những góc nhìn điện ảnh đặc sắc. Khám phá thêm tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://sapa-photospots.nguyenhaithttsapa-rgb.deno.net/"}, "children": ["👉 Không Gian Giải Trí & Góc Trải Nghiệm Đa Chiều Deno"]},
                    "."
                ]}
            ]
        },
        {
            "id": "t2-art-06",
            "title": "Tối Ưu Chi Phí Nhân Sự & Biểu Thuế Thu Nhập Cá Nhân 2026 Cho Doanh Nghiệp Trẻ",
            "target_satellites": [
                {"name": "Vercel Cloud (Mùa Vàng)", "url": "https://sapa-travel-experience.vercel.app/"},
                {"name": "Netlify Global (Ecolodge)", "url": "https://sapa-travel-experience.netlify.app/"}
            ],
            "content_nodes": [
                {"tag": "p", "children": ["Năm 2026 đánh dấu nhiều thay đổi trong chính sách thuế TNCN và các mức đóng bảo hiểm bắt buộc. Hiểu rõ phương pháp tính toán và quản trị quỹ lương giúp doanh nghiệp tối ưu chi phí và tăng sự gắn kết của nhân sự."]},
                {"tag": "h3", "children": ["1. Phân bổ ngân sách lương Gross và Net minh bạch"]},
                {"tag": "p", "children": ["Việc số hóa quy trình tính lương và tra cứu thuế theo thời gian thực giúp giảm thiểu sai sót, nâng cao năng suất phòng kế toán. Xem thêm giải pháp tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://sapa-travel-experience.vercel.app/"}, "children": ["👉 Báo Cáo Chuyên Sâu Về Quản Trị Nhân Sự & Số Hóa Vercel Cloud"]},
                    "."
                ]},
                {"tag": "h3", "children": ["2. Tích hợp thanh toán số tự động"]},
                {"tag": "p", "children": ["Doanh nghiệp hiện đại đang đẩy mạnh thanh toán không tiền mặt và đối soát tự động hàng tháng. Tìm hiểu thêm mô hình vận hành tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://sapa-travel-experience.netlify.app/"}, "children": ["👉 Nền Tảng Tự Động Hóa Vận Hành Doanh Nghiệp Netlify Global"]},
                    "."
                ]}
            ]
        },
        {
            "id": "t2-art-07",
            "title": "Xu Hướng Thiết Kế Đồ Họa Đám Mây: Chỉnh Sửa Trực Tiếp Trên Trình Duyệt Không Cần Cài Đặt",
            "target_satellites": [
                {"name": "Cloudflare Edge (Tour Sa Pa)", "url": "https://sapa-tour-3n2d.laocaiview-vn.workers.dev/danh-gia-thuat-toan-crypto-csprng-vongquaymayman-web-app.html"},
                {"name": "Render Cloud (Fansipan & BĐS)", "url": "https://lao-cai-view-ve-fansipan-and-bat-dong.onrender.com/index.html"}
            ],
            "content_nodes": [
                {"tag": "p", "children": ["Sự phát triển của WebAssembly và Canvas API giúp các công cụ đồ họa trực tuyến đạt tốc độ xử lý layer và render vector ngang ngửa phần mềm desktop chuyên dụng."]},
                {"tag": "h3", "children": ["1. Đơn giản hóa quy trình xuất bản ấn phẩm truyền thông"]},
                {"tag": "p", "children": ["Người dùng có thể mở nhanh các tệp PSD, AI, thiết kế banner và xuất file ảnh dung lượng tối ưu ngay trong tích tắc. Đọc thêm đánh giá công nghệ tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://sapa-tour-3n2d.laocaiview-vn.workers.dev/danh-gia-thuat-toan-crypto-csprng-vongquaymayman-web-app.html"}, "children": ["👉 Đánh Giá Công Nghệ Đồ Họa Điện Toán Đám Mây Cloudflare Edge"]},
                    "."
                ]},
                {"tag": "h3", "children": ["2. Ứng dụng trong tiếp thị đa kênh"]},
                {"tag": "p", "children": ["Hình ảnh tối ưu giúp tăng tốc độ tải trang web và cải thiện điểm Core Web Vitals rõ rệt. Tham khảo tài liệu kỹ thuật tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://lao-cai-view-ve-fansipan-and-bat-dong.onrender.com/index.html"}, "children": ["👉 Tiêu Chuẩn Tối Ưu Hình Ảnh Đa Nền Tảng Render Cloud"]},
                    "."
                ]}
            ]
        },
        {
            "id": "t2-art-08",
            "title": "Bùng Nổ Thanh Toán Mã VietQR & Chuyển Đổi Số Cho Các Cửa Hàng Kinh Doanh 2026",
            "target_satellites": [
                {"name": "GitHub Pages (Nhà Đất Lào Cai)", "url": "https://nguyenhaithttsapa-rgb.github.io/nhadatlaocai-review/"},
                {"name": "Replit Engine (Hub)", "url": "https://newsvetinh--laocaiview.replit.app"}
            ],
            "content_nodes": [
                {"tag": "p", "children": ["Mã QR để bàn chuẩn VietQR đã trở thành hạ tầng thanh toán quen thuộc tại mọi quầy thu ngân từ nhà hàng, khách sạn đến quán cà phê trên toàn quốc."]},
                {"tag": "h3", "children": ["1. Tăng tốc độ phục vụ và giảm thiểu thất thoát thu ngân"]},
                {"tag": "p", "children": ["Việc tạo bảng mã VietQR có in sẵn logo thương hiệu và mã Wi-Fi giúp cửa hàng nâng tầm chuyên nghiệp trong mắt khách hàng. Đón đọc cẩm nang chuyển đổi số bán lẻ tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://nguyenhaithttsapa-rgb.github.io/nhadatlaocai-review/"}, "children": ["👉 Xu Hướng Số Hóa Điểm Bán Hàng & Mặt Bằng Kinh Doanh"]},
                    "."
                ]},
                {"tag": "h3", "children": ["2. Kết nối hạ tầng thương mại không biên giới"]},
                {"tag": "p", "children": ["Khám phá mạng lưới giải pháp số hỗ trợ doanh nghiệp kinh doanh đa lĩnh vực tại "]},
                {"tag": "p", "children": [
                    {"tag": "a", "attrs": {"href": "https://newsvetinh--laocaiview.replit.app"}, "children": ["👉 Trung Tâm Điều Phối Giải Pháp Số Master Hub"]},
                    "."
                ]}
            ]
        }
    ]

def publish_tier2_telegraph():
    """Xuất bản một bài viết Tầng 2 lên Telegra.ph và lưu vào lịch sử"""
    token = get_or_create_account()
    templates = get_tier2_templates()

    # Chọn luân phiên theo giờ hoặc số bài đã đăng
    curr_hour = datetime.now().hour
    idx = curr_hour % len(templates)
    art = templates[idx]

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # API createPage
    url = "https://api.telegra.ph/createPage"
    payload = urllib.parse.urlencode({
        "access_token": token,
        "title": art["title"],
        "author_name": "Lao Cai View & Satellite Mesh",
        "author_url": "https://newsvetinh.web.app",
        "content": json.dumps(art["content_nodes"]),
        "return_content": False
    }).encode("utf-8")

    req = urllib.request.Request(url, data=payload, headers={"User-Agent": "TelegraphTier2Bot/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=12, context=ctx) as r:
            res = json.loads(r.read())
            if res.get("ok"):
                telegraph_url = res["result"]["url"]
                published_item = {
                    "title": art["title"],
                    "url": telegraph_url,
                    "target_satellites": art["target_satellites"],
                    "published_at": now_str,
                    "platform": "Telegra.ph (Telegram API - DA 91)"
                }

                # Lưu vào lịch sử tier2_articles.json
                history = []
                if os.path.exists(TIER2_ARTICLES_FILE):
                    try:
                        with open(TIER2_ARTICLES_FILE, "r", encoding="utf-8") as f:
                            history = json.load(f)
                    except Exception:
                        history = []

                # Tránh trùng lặp URL
                if not any(h.get("url") == telegraph_url for h in history):
                    history.insert(0, published_item)

                with open(TIER2_ARTICLES_FILE, "w", encoding="utf-8") as f:
                    json.dump(history[:20], f, ensure_ascii=False, indent=2)

                print(f"\n[🏛️] ĐÃ XUẤT BẢN THÀNH CÔNG BÀI VIẾT TẦNG 2 TRÊN TELEGRA.PH (DA 91)!")
                print(f"  ✓ Tiêu đề: \"{published_item['title']}\"")
                print(f"  ✓ Link bài viết: {published_item['url']}")
                print(f"  ✓ Bơm lực trực tiếp về 2 vệ tinh: {', '.join([s['name'] for s in published_item['target_satellites']])}")
                return published_item
            else:
                print(f"[!] Lỗi xuất bản Telegra.ph: {res}")
                return None
    except Exception as e:
        print(f"[!] Ngoại lệ khi gọi Telegra.ph: {e}")
        return None

if __name__ == "__main__":
    print("=" * 70)
    print("🚀 CHẠY THỬ NGHIỆM XUẤT BẢN BÀI VIẾT TẦNG 2 (TELEGRA.PH API)...")
    print("=" * 70)
    res = publish_tier2_telegraph()
    if res:
        print(f"\n🎉 Hoàn tất! Đã tạo link Tầng 2: {res['url']}")
