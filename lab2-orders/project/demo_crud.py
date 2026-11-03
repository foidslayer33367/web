"""Выполнить: python manage.py shell < demo_crud.py. Изменения примера откатываются."""
from datetime import date
from decimal import Decimal
from django.db import transaction
from orders.models import Order

with transaction.atomic():
    first = Order(customer_name='Демо: Анна', order_date=date(2026, 11, 2),
                  total_amount=Decimal('1500.00'), is_paid=True,
                  delivery_address='Ставрополь, ул. Мира, 1')
    first.full_clean()
    first.save()
    second = Order.objects.create(customer_name='Демо: Иван', total_amount=Decimal('750.50'),
                                  is_paid=False, delivery_address='Ставрополь, ул. Ленина, 2')
    print('CREATE: созданы два заказа:', first.customer_name, second.customer_name)
    print('READ all():', list(Order.objects.all().values_list('customer_name', flat=True)))
    print('FILTER is_paid=True:', list(Order.objects.filter(is_paid=True).values_list('customer_name', flat=True)))
    print('GET:', Order.objects.get(pk=first.pk))
    print('EXCLUDE is_paid=True:', list(Order.objects.exclude(is_paid=True).values_list('customer_name', flat=True)))
    second.is_paid = True
    second.total_amount = Decimal('800.00')
    second.save()
    second.refresh_from_db()
    assert second.is_paid and second.total_amount == Decimal('800.00')
    print('UPDATE:', second.customer_name, second.total_amount, second.is_paid)
    deleted_pk = second.pk
    second.delete()
    assert not Order.objects.filter(pk=deleted_pk).exists()
    print('DELETE: второй демонстрационный заказ удалён')
    print('CRUD успешно проверен. Демонстрационные изменения откатываются.')
    transaction.set_rollback(True)
