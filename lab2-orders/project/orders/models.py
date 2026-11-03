from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class Order(models.Model):
    customer_name = models.CharField('Имя заказчика', max_length=150)
    order_date = models.DateField('Дата заказа', default=timezone.localdate)
    total_amount = models.DecimalField('Сумма заказа', max_digits=12, decimal_places=2,
                                      validators=[MinValueValidator(Decimal('0.00'))])
    is_paid = models.BooleanField('Оплачен', default=False)

    delivery_address = models.TextField('Адрес доставки', blank=True, default='')

    class Meta:
        ordering = ['id']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.pk} — {self.customer_name}'
