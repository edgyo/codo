from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fields = ('nickname', 'email')
    list_display = ('nickname', 'id', 'registered_at')
admin.site.register(User, UserAdmin)