from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)  # db_index = True provides faster lookup in database tables
    slug = models.SlugField(max_length=50, db_index=True)

    class Meta:
        ordering = ['name']  # Sort Asc based on name column
        verbose_name = 'category'  # Name of singular object of this model
        verbose_name_plural = 'categories'  # Name of plural objects of this models

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list', args=[self.slug])


class Product(models.Model):
    # CASCADE reflects the changes made in parent table
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add assign timestamp of creation of object
    modified = models.DateTimeField(auto_now=True)  # auto_now assign timestamp of recent modification of object

    class Meta:
        ordering = ['name']
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.id, self.slug])
