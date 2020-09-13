from django.contrib import admin

# Register your models here.
from .models import CustomUrl1,CustomUrl2,CustomUrl3


class ProfileInline(admin.StackedInline):
    model = CustomUrl1
    model = CustomUrl2
    model = CustomUrl3

admin.site.register(CustomUrl1)
admin.site.register(CustomUrl2)
admin.site.register(CustomUrl3)