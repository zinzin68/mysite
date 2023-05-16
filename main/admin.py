from django.contrib import admin
#게시글(Post) Model을 불러옵니다.
from .models import Post

# Register your models here.
#관리자가 게시글에 접근 가능
admin.site.register(Post)