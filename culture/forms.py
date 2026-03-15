from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        label='Địa chỉ Email',
        help_text='Vui lòng cung cấp một địa chỉ email hợp lệ để khôi phục mật khẩu nếu bạn quên.'
    )

    class Meta:
        model = User
        fields = ['username', 'email']
