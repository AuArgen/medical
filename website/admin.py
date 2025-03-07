from django.contrib import admin

from website.models import Website, Slider


# Register your models here.

@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone')
    search_fields = ('title',)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)