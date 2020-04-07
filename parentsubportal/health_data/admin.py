from django.contrib import admin
from .models import HealthCondition, HealthInfo, PageLink
from .data_fetch.nhs import run_fetch_nhs


class HealthConditionAdmin(admin.ModelAdmin):
    list_display = ['name', 'url','keywords', 'published', 'created_at', 'updated_at']

    actions = ['update_info']

    def update_info(self, request, queryset):
        run_fetch_nhs()


class HealthInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'keywords', 'created_at', 'updated_at', 'health_condition_id']


class PageLinkAdmin(admin.ModelAdmin):
    list_display = ['url', 'name','keywords', 'published', 'description',  'source', 'created_at', 'updated_at']


admin.site.register(HealthCondition, HealthConditionAdmin)
admin.site.register(HealthInfo, HealthInfoAdmin)
admin.site.register(PageLink, PageLinkAdmin)
