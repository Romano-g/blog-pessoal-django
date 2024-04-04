from django.contrib import admin
from site_configs.models import MenuLink


@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_or_path',
    list_display_links = 'id', 'text',
    search_fields = 'id', 'text', 'url_or_path',
