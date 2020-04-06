from django.contrib import admin
from .models import HealthCondition, HealthInfo


class HealthConditionAdmin(admin.ModelAdmin):
    list_display = ['name', 'url','keywords', 'published', 'created_at', 'updated_at']


class HealthInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'keywords', 'created_at', 'updated_at', 'health_condition_id']


admin.site.register(HealthCondition, HealthConditionAdmin)
admin.site.register(HealthInfo, HealthInfoAdmin)
