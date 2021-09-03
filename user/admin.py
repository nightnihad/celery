from django.contrib import admin
from .models import CustomUser
# Register your models here.
@admin.register(CustomUser)
class CustomAdmin(admin.ModelAdmin):
    class Meta:
        search_fields = ('first_name', 'email')
        list_display = (
        'first_name', 'last_name', 'email','date_joined'
        )

