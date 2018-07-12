from django.contrib import admin
from rango.models import Category, page



class PageAdmin(admin.ModelAdmin):
    list_display = ('title',  'category', 'url','views')
    list_filter=['category']


# Register your models here.
admin.site.register(Category)
admin.site.register(page,PageAdmin)
