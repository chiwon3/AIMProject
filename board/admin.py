from django.contrib import admin
from .models import Post

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Post

    
admin.site.register(Post)