from django.contrib import admin
from .models import Article


admin.site.register(Article)
admin.site.site_header='Veencent Admin'
admin.site.site_title= 'Admins Only Site'

