from django.contrib import admin

from finance.models import FeeType

# Register your models here.
@admin.register(FeeType)
class FeeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'amount')
    search_fields = ('name',)