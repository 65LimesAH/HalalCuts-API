from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Menu(models.Model):

    SCALE_CHOICES = (
        ('lbs', 'Pound'),
        ('oz', 'Ounces')
    )

    item = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.IntegerField(default=0)
    scale = models.CharField(max_length=3)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    primary_category = models.ForeignKey(
        Category, related_name='primary_products', blank=True, null=True, on_delete=models.CASCADE)
    secondary_categories = models.ManyToManyField(Category, blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse("cart:product-detail", kwargs={'slug': self.slug})

    # def get_update_url(self):
    #     return reverse("staff:product-update", kwargs={'pk': self.pk})

    # def get_delete_url(self):
    #     return reverse("staff:product-delete", kwargs={'pk': self.pk})

    def get_price(self):
        return "{:.2f}".format(self.price / 100)

    @property
    def in_stock(self):
        return self.stock > 0
