from django.contrib import admin

from .models import InfojobUser

class InfouserAdmin(admin.ModelAdmin):
    # какие поля будут отображаться в админке
    list_display = ('id', 'username', 'email', 'user_role', 'created_at')
    # какие поля будут ссылками на соответствующие модели
    list_display_links = ('id', 'username', 'email')
    # какие поля будут участвовать в поиске
    search_fields = ('username', 'email', 'user_role')



admin.site.register(InfojobUser, InfouserAdmin)