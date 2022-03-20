class Translation(object):
    START_TEXT = """Chào {}, gửi link để tải video!"""
    FORMAT_SELECTION = "Chọn định dạng mong muốn để tải!"
    SET_CUSTOM_USERNAME_PASSWORD = """Để tải các video trả phí, nhập với định dạng:
URL | filename | username | password"""
    DOWNLOAD_START = "📥Đang download..."
    UPLOAD_START = "📤Đang upload..."
    RCHD_TG_API_LIMIT = "Tải xuống sau {} giây.\nKích thước tập tin: {}\nKhông thể tải video có dung lượng lớn hơn 2GB"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Đã hoàn tất</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Download sau {} 2 giây.\nUpload sau {} giây."
    SAVED_CUSTOM_THUMB_NAIL = "Đã lưu video/Ảnh thu nhỏ."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Đã xóa thumbnail"
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "Lỗi...\n<b>YouTubeDL</b> cho biết: {}"
    ABOUT_MSG = """ Thông tin Bot :
    
   ☞Tên  : DLC Media Downloader 

   ☞Language : Python3

   ☞Library  : <a href="https://docs.pyrogram.org/">Pyrogram 1.0.7</a>"""
    HELP_USER = """Các bước thực hiện!
    
1. Gửi liên kết cần tải
2. Gửi ảnh nền video cần thay thế (Tùy chọn).
3. Chọn định dạng
   SVideo - Nhận Video với ảnh chụp màn hình
   DFile  - Nhận Video dạng file với ảnh chụp màn hình
   Video  - Nhận Video với không có ảnh chụp màn hình
   File   - Nhận File không có ảnh chụp màn hình
"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Trả lời / tạo hình thu nhỏ tùy chỉnh cho album phương tiện, để tạo hình thu nhỏ tùy chỉnh "
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Album phương tiện chỉ có thể chứa hai ảnh. Vui lòng gửi lại."
Bạn có thể sử dụng lệnh /rename sau khi nhận được tệp để đổi tên tệp với hỗ trợ hình thu nhỏ tùy chỉnh .
"""
    CANCEL_STR = "Hủy tải về"
    ZIP_UPLOADED_STR = "Tập tin {} được tải lên sau {} giây"
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
