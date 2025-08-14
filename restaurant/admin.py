from django.contrib import admin
from .models import Menu, MenuCategory, Booking

admin.site.register(Menu)
admin.site.register(MenuCategory)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'guests', 'phone', 'email')
    list_filter = ('date', 'time')
    search_fields = ('name', 'email', 'phone')
