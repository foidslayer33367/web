from django.shortcuts import render
from .models import Order


def order_list(request):
    paid_only = request.GET.get('paid') == '1'
    orders = Order.objects.filter(is_paid=True) if paid_only else Order.objects.all()
    return render(request, 'orders/list.html', {'orders': orders, 'paid_only': paid_only})
