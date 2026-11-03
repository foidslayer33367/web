from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'order_date', 'total_amount', 'is_paid')
    list_filter = ('is_paid', 'order_date')
    search_fields = ('customer_name', 'delivery_address')
