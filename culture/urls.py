from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'culture'

urlpatterns = [
    path('', views.home, name='home'),
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
    path('lan-dieu/', views.lan_dieu_list, name='lan_dieu_list'),
    path('nghe-nhan/', views.nghe_nhan_list, name='nghe_nhan_list'),
    path('lang-quan-ho/', views.lang_quan_ho_list, name='lang_quan_ho_list'),
    path('tin-tuc/', views.danh_sach_bai_viet, name='danh_sach_bai_viet'),
    path('tin-tuc/<int:pk>/', views.chi_tiet_bai_viet, name='chi_tiet_bai_viet'),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('toggle-favorite/<int:pk>/', views.toggle_favorite, name='toggle_favorite'),
    path('profile/', views.user_profile, name='user_profile'),
    path('doi-mat-khau/', auth_views.PasswordChangeView.as_view(template_name='culture/password_change_form.html', success_url='/doi-mat-khau/xong/'), name='password_change'),
    path('doi-mat-khau/xong/', auth_views.PasswordChangeDoneView.as_view(template_name='culture/password_change_done.html'), name='password_change_done'),
]
