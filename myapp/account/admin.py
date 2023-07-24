from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ('프로필', {'fields': ('username', 'password')}),
    ('개인정보', {'fiedls' : ('first_name', 'last_name', 'emial')}),
    ('권한', {'fields': ('is_active', 'is_staff','is_superuser')}),
    ('로그인정보',{'fields': ('last_login','date_joined')}),
