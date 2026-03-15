import os
import django

# Thiết lập môi trường Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quan_ho_project.settings')
django.setup()

from culture.models import LanDieu, NgheNhan, BaiHat

def seed_data():
    print("Đang nạp dữ liệu mẫu...")

    # Tạo Làn điệu
    ld_vặt, _ = LanDieu.objects.get_or_create(
        ten="Giọng vặt", 
        mo_ta_y_nghia="Những bài hát có nội dung tự do, phong phú, thường được hát ở nhiều hoàn cảnh.", 
        nguon_goc="Dân gian Bắc Ninh"
    )
    ld_huong, _ = LanDieu.objects.get_or_create(
        ten="Giọng sổng", 
        mo_ta_y_nghia="Hát với âm điệu cao, vang, thường dùng để gọi bạn.", 
        nguon_goc="Dân gian Bắc Ninh"
    )
    ld_la_rang, _ = LanDieu.objects.get_or_create(
        ten="Giọng La Giằng",
        mo_ta_y_nghia="Làn điệu lề lối, hát chậm rãi, trang trọng.",
        nguon_goc="Dân gian Bắc Ninh"
    )

    # Tạo Nghệ nhân
    nn_thuy, _ = NgheNhan.objects.get_or_create(
        ten="Thúy Cải", 
        nam_sinh=1953, 
        danh_hieu="NSND", 
        tieu_su="Là một trong những giọng ca Quan họ tiêu biểu, có nhiều đóng góp trong việc bảo tồn và phát triển dân ca Quan họ."
    )
    nn_quy, _ = NgheNhan.objects.get_or_create(
        ten="Quý Trọng",
        nam_sinh=1945,
        danh_hieu="NSƯT",
        tieu_su="Nghệ nhân nổi tiếng với giọng ca trầm ấm, biểu cảm."
    )

    # Bài hát 1
    BaiHat.objects.get_or_create(
        ten_bai="Mười nhớ",
        loi_bai_hat="Một thương tóc bỏ đuôi gà...\nHai thương ăn nói mặn mà có duyên...",
        file_audio="https://www.youtube.com/watch?v=dQw4w9WgXcQ", # Placeholder link
        lan_dieu=ld_vặt,
        nghe_nhan=nn_thuy
    )

    # Bài hát 2
    BaiHat.objects.get_or_create(
        ten_bai="Người ơi người ở đừng về",
        loi_bai_hat="Người ơi người ở đừng về...\nNgười về em vẫn khóc thầm...\nĐôi bên vạt áo ướt đầm như mưa...",
        file_audio="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        lan_dieu=ld_vặt,
        nghe_nhan=nn_thuy
    )

    # Bài hát 3
    BaiHat.objects.get_or_create(
        ten_bai="Ngồi tựa mạn thuyền",
        loi_bai_hat="Trăng thanh gió mát trăng thanh...\nNăm canh nhặt cả năm canh ai thời...\nNgồi tựa mạn thuyền, gối hận phòng không...",
        file_audio="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        lan_dieu=ld_huong,
        nghe_nhan=nn_quy
    )

    # Bài hát 4
    BaiHat.objects.get_or_create(
        ten_bai="Tương phùng tương ngộ",
        loi_bai_hat="Tương phùng là tương phùng tương ngộ...\nĐôi phen như nước đục trong...",
        file_audio="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        lan_dieu=ld_vặt,
        nghe_nhan=nn_thuy
    )

    # Bài hát 5
    BaiHat.objects.get_or_create(
        ten_bai="Trống cơm",
        loi_bai_hat="Tình bằng có cái trống cơm...\nKhen ai khéo vỗ, ố mấy bông mà nên bông...",
        file_audio="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        lan_dieu=ld_vặt,
        nghe_nhan=nn_quy
    )

    print("Đã nạp thành công 5 bài Dân ca Quan họ và các dữ liệu liên quan!")

if __name__ == "__main__":
    seed_data()
