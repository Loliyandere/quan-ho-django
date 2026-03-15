from django.db import models
from django.contrib.auth.models import User
import re

class LanDieu(models.Model):
    ten = models.CharField(max_length=200, verbose_name="Tên làn điệu")
    mo_ta_y_nghia = models.TextField(blank=True, null=True, verbose_name="Mô tả ý nghĩa")
    nguon_goc = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nguồn gốc")

    def __str__(self):
        return self.ten

    class Meta:
        verbose_name = "Làn điệu"
        verbose_name_plural = "Các Làn điệu"

class NgheNhan(models.Model):
    ten = models.CharField(max_length=200, verbose_name="Tên nghệ nhân")
    nam_sinh = models.IntegerField(blank=True, null=True, verbose_name="Năm sinh")
    danh_hieu = models.CharField(max_length=100, blank=True, null=True, verbose_name="Danh hiệu") # VD: NSND, NSƯT
    tieu_su = models.TextField(blank=True, null=True, verbose_name="Tiểu sử")
    anh_dai_dien = models.ImageField(upload_to='nghe_nhan/', blank=True, null=True, verbose_name="Ảnh đại diện")

    def __str__(self):
        danh_hieu_str = f" - {self.danh_hieu}" if self.danh_hieu else ""
        return f"{self.ten}{danh_hieu_str}"

    class Meta:
        verbose_name = "Nghệ nhân"
        verbose_name_plural = "Các Nghệ nhân"

class BaiHat(models.Model):
    ten_bai = models.CharField(max_length=255, verbose_name="Tên bài hát")
    loi_bai_hat = models.TextField(blank=True, null=True, verbose_name="Lời bài hát")
    file_audio = models.URLField(blank=True, null=True, verbose_name="Link Audio/YouTube") # Hoặc FileField nếu upload file
    audio_file = models.FileField(upload_to='audios/', blank=True, null=True, verbose_name="File Audio (MP3/WAV)")
    youtube_url = models.URLField(blank=True, null=True, verbose_name="Link YouTube (để nhúng video)")
    lan_dieu = models.ForeignKey(LanDieu, on_delete=models.SET_NULL, null=True, blank=True, related_name='bai_hats', verbose_name="Làn điệu")
    nghe_nhan = models.ForeignKey(NgheNhan, on_delete=models.SET_NULL, null=True, blank=True, related_name='bai_hats', verbose_name="Nghệ nhân trình bày")
    favorites = models.ManyToManyField(User, related_name='favorite_songs', blank=True, verbose_name="Lượt yêu thích")

    @property
    def get_youtube_id(self):
        if not self.youtube_url:
            return None
        # Extract YouTube ID
        regex = r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})'
        match = re.search(regex, self.youtube_url)
        if match:
            return match.group(1)
        return None

    def __str__(self):
        return self.ten_bai

    class Meta:
        verbose_name = "Bài hát"
        verbose_name_plural = "Các Bài hát"


class BaiViet(models.Model):
    tieu_de = models.CharField(max_length=255, verbose_name="Tiêu đề")
    hinh_anh = models.ImageField(upload_to='bai_viet/%Y/%m/', null=True, blank=True, verbose_name="Hình ảnh bìa")
    tom_tat = models.TextField(blank=True, null=True, verbose_name="Tóm tắt")
    noi_dung = models.TextField(verbose_name="Nội dung")
    nguoi_dang = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Người đăng")
    ngay_dang = models.DateTimeField(auto_now_add=True, verbose_name="Ngày đăng")
    
    def __str__(self):
        return self.tieu_de

    class Meta:
        verbose_name = "Bài viết (Tin tức)"
        verbose_name_plural = "Các Bài viết"
