from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Info


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('date', 'detection_time', 'street_and_house', 'object', 'damage', )



admin.site.site_header = 'Бомбардировка Ленинграда'

#admin.site.unregister(Logs)  # нужно что бы снять с регистрации модель Logs
