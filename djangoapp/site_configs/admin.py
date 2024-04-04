from django.contrib import admin
from django.http.request import HttpRequest
from site_configs.models import MenuLink, SiteSetup


class MenuLinkInine(admin.TabularInline):
    model = MenuLink
    extra = 1


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',
    inlines = MenuLinkInine,

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not SiteSetup.objects.exists()
