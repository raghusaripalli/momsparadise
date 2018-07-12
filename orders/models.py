from django.core.validators import MaxLengthValidator, MinLengthValidator, integer_validator, RegexValidator
from django.db import models


# Create your models here.
from shop.models import Product


class Order(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(validators=[MaxLengthValidator(10), MinLengthValidator(10)], max_length=10)
    pincode_regex = RegexValidator(regex='^\d{6}$', message="Pincode must be exactly 6 digits"
                                   , code="invalid_pincode")
    pincode = models.CharField(validators=[pincode_regex], max_length=6)
    email = models.EmailField(blank=True)
    landmark = models.CharField(max_length=50, blank=True)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
