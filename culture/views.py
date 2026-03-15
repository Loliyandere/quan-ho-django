from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import BaiHat, LanDieu, NgheNhan, BaiViet
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Đăng ký thành công! Chào mừng {user.username}.')
            return redirect('culture:home')
        else:
            messages.error(request, 'Lỗi đăng ký. Vui lòng kiểm tra lại thông tin.')
    else:
        form = UserRegisterForm()
    return render(request, 'culture/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Xin chào, {username}!')
                return redirect('culture:home')
        else:
            messages.error(request, 'Sai tên đăng nhập hoặc mật khẩu.')
    else:
        form = AuthenticationForm()
    return render(request, 'culture/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'Bạn đã đăng xuất thành công.')
    return redirect('culture:home')

@login_required
def toggle_favorite(request, pk):
    bai_hat = get_object_or_404(BaiHat, pk=pk)
    if bai_hat.favorites.filter(id=request.user.id).exists():
        bai_hat.favorites.remove(request.user)
        is_favorited = False
    else:
        bai_hat.favorites.add(request.user)
        is_favorited = True
    return JsonResponse({'is_favorited': is_favorited})

@login_required
def user_profile(request):
    favorite_songs = request.user.favorite_songs.all()
    context = {
        'favorite_songs': favorite_songs
    }
    return render(request, 'culture/profile.html', context)

def home(request):
    query = request.GET.get('q', '')
    lan_dieu_id = request.GET.get('lan_dieu', '')

    bai_hats = BaiHat.objects.all()

    if query:
        bai_hats = bai_hats.filter(
            Q(ten_bai__icontains=query) | Q(loi_bai_hat__icontains=query)
        )
    
    if lan_dieu_id:
        bai_hats = bai_hats.filter(lan_dieu_id=lan_dieu_id)

    lan_dieus = LanDieu.objects.all()

    context = {
        'bai_hats': bai_hats,
        'lan_dieus': lan_dieus,
        'search_query': query,
        'selected_lan_dieu': lan_dieu_id,
    }
    return render(request, 'culture/index.html', context)

def song_detail(request, pk):
    bai_hat = get_object_or_404(BaiHat, pk=pk)
    context = {'bai_hat': bai_hat}
    return render(request, 'culture/song_detail.html', context)

def lan_dieu_list(request):
    lan_dieus = LanDieu.objects.all().order_by('ten')
    return render(request, 'culture/lan_dieu_list.html', {'lan_dieus': lan_dieus})

def nghe_nhan_list(request):
    nghe_nhans = NgheNhan.objects.all().order_by('ten')
    return render(request, 'culture/nghe_nhan_list.html', {'nghe_nhans': nghe_nhans})

def danh_sach_bai_viet(request):
    bai_viets = BaiViet.objects.all().order_by('-ngay_dang')
    return render(request, 'culture/danh_sach_bai_viet.html', {'bai_viets': bai_viets})

def chi_tiet_bai_viet(request, pk):
    bai_viet = get_object_or_404(BaiViet, pk=pk)
    return render(request, 'culture/chi_tiet_bai_viet.html', {'bai_viet': bai_viet})
