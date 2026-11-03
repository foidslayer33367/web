from decimal import Decimal
from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Order


class OrderTests(TestCase):
    def setUp(self):
        self.paid = Order.objects.create(customer_name='Оплаченный', total_amount='100.50',
                                        is_paid=True, delivery_address='Тестовый адрес')
        self.unpaid = Order.objects.create(customer_name='Неоплаченный', total_amount='50.00')

    def test_paid_filter_and_exclude(self):
        self.assertEqual(list(Order.objects.filter(is_paid=True)), [self.paid])
        self.assertEqual(list(Order.objects.exclude(is_paid=True)), [self.unpaid])

    def test_update_persists_exact_decimal(self):
        order = Order.objects.get(pk=self.unpaid.pk)
        order.total_amount = Decimal('10.10')
        order.is_paid = True
        order.save()
        order.refresh_from_db()
        self.assertEqual(order.total_amount, Decimal('10.10'))
        self.assertTrue(order.is_paid)

    def test_delete_persists(self):
        pk = self.unpaid.pk
        self.unpaid.delete()
        self.assertFalse(Order.objects.filter(pk=pk).exists())

    def test_invalid_amount_and_required_name(self):
        for name, amount in [('Имя', '-0.01'), ('', '20')]:
            with self.assertRaises(ValidationError):
                Order(customer_name=name, total_amount=amount).full_clean()

    def test_paid_page_filters_database_records(self):
        response = self.client.get('/?paid=1')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.paid.customer_name)
        self.assertNotContains(response, self.unpaid.customer_name)
        self.assertContains(self.client.get('/'), self.unpaid.customer_name)

    def test_admin_requires_login(self):
        response = self.client.get('/admin/orders/order/')
        self.assertRedirects(response, '/admin/login/?next=/admin/orders/order/', fetch_redirect_response=False)
