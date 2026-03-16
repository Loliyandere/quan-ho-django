from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from .models import LanDieu, NgheNhan, BaiHat, BaiViet, LangQuanHo

# --- CUSTOM USER ADMIN ---
admin.site.unregister(User) # Hủy đăng ký User mặc định
admin.site.unregister(Group) # Ẩn luôn phần Quản lý Group cho đỡ rối phố

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Ghi đè fieldsets để quyết định những trường nào được hiện trong form Edit
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Thông tin cá nhân', {'fields': ('email',)}),  # Bỏ first_name, last_name
        ('Quyền Quản trị viên', {'fields': ('is_active', 'is_superuser')}),
        # Đã loại bỏ hoàn toàn dòng 'groups', 'user_permissions' và 'is_staff'
        ('Ngày tháng', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Ở trang dánh sách, hiển thị các cột cơ bản
    list_display = ('username', 'email', 'is_superuser')
    list_filter = ('is_superuser', 'is_active')
    search_fields = ('username', 'email')


# --- QUAN HO ADMIN ---
@admin.register(LanDieu)
class LanDieuAdmin(admin.ModelAdmin):
    list_display = ('ten', 'nguon_goc')
    search_fields = ('ten', 'mo_ta_y_nghia')

@admin.register(LangQuanHo)
class LangQuanHoAdmin(admin.ModelAdmin):
    list_display = ('ten_lang', 'huyen')
    search_fields = ('ten_lang', 'huyen', 'mo_ta')

@admin.register(NgheNhan)
class NgheNhanAdmin(admin.ModelAdmin):
    list_display = ('ten', 'nam_sinh', 'danh_hieu', 'lang_que')
    search_fields = ('ten', 'tieu_su')
    list_filter = ('danh_hieu', 'lang_que')
    autocomplete_fields = ['lang_que']

@admin.register(BaiHat)
class BaiHatAdmin(admin.ModelAdmin):
    list_display = ('ten_bai', 'lan_dieu', 'nghe_nhan', 'youtube_url')
    search_fields = ('ten_bai', 'loi_bai_hat', 'youtube_url')
    list_filter = ('lan_dieu', 'nghe_nhan')
    autocomplete_fields = ['lan_dieu', 'nghe_nhan'] # Cần search_fields ở Model tương ứng (đã có ở trên)

@admin.register(BaiViet)
class BaiVietAdmin(admin.ModelAdmin):
    list_display = ('tieu_de', 'nguoi_dang', 'ngay_dang')
    search_fields = ('tieu_de', 'tom_tat')
    list_filter = ('ngay_dang',)
