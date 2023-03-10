from django.contrib import admin
from .models import User, BotSettings

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'first_name', 'last_name', 'username', 'subscribed')
    list_filter = ('subscribed',)

@admin.register(BotSettings)
class BotSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'token', 'price')
