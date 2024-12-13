from django.contrib import admin
from .models import Post,Catagory,AboutUS
# Register your models here.

class Postadmin(admin.ModelAdmin):
    list_display = ('title','content')
    search_fields = ('title', 'content')
    list_filter = ('created_at_time','catagory')


admin.site.register(Post,Postadmin)
admin.site.register(Catagory)
admin.site.register(AboutUS)