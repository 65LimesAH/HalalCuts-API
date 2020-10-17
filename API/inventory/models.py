from django.db import models
from django.utils import timezone

class Items(models.Model):
    name = models.CharField(max_length=100)
    stockCount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    modifiedTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Printers(models.Model):
    printer = models.CharField(max_length=100, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return self.printer


class PriceType(models.Model):
    name = models.CharField(max_length=20, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return self.name


class Canonical(models.Model):
    canonical = models.CharField(max_length=100, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return self.canonical


class Attribute(models.Model):
    attribute = models.CharField(max_length=100, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return self.attribute


class Options(models.Model):
    name = models.CharField(max_length=100, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return self.name


class ItemGroup(models.Model):
    name = models.CharField(max_length=100, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return self.name


class TaxRates(models.Model):
    name = models.CharField(max_length=100)
    taxType = models.CharField(max_length=100, blank=True, null=True, )
    rate = models.IntegerField(default=0)
    isDefault = models.BooleanField(default=False)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    taxAmount = models.IntegerField(default=0)
    deletedTime = models.DateTimeField(default=timezone.now)
    modifiedTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Modifiers(models.Model):
    name = models.CharField(max_length=100)
    alternateName = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ModifierGroups(models.Model):
    name = models.CharField(max_length=100)
    alternateName = models.CharField(max_length=100)
    minRequired = models.IntegerField(default=0)
    maxAllowed = models.IntegerField(default=0)
    showByDefault = models.BooleanField(default=True)
    modifiers = models.ManyToManyField(Modifiers)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100)
    sortOrder = models.IntegerField(default=0)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    modifiedTime = models.DateTimeField(default=timezone.now)
    canonical = models.ManyToManyField(Canonical)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=100)
    showInReport = models.BooleanField(default=False)
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    printers = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ItemStock(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    stockCount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    modifiedTime = models.DateTimeField(default=timezone.now)
    deletedTime = models.DateTimeField(default=timezone.now)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.item


class Menu(models.Model):
    hidden = models.BooleanField(default=False)
    itemGroup = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    options = models.ForeignKey(Options, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    alternateName = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    priceType = models.ForeignKey(PriceType, on_delete=models.CASCADE)
    defaultTaxRates = models.BooleanField(default=True)
    unitName = models.CharField(max_length=100)
    cost = models.IntegerField(default=0)
    isRevenue = models.BooleanField(default=False)
    taxRate = models.ForeignKey(TaxRates, on_delete=models.CASCADE)
    modifierGroups = models.ManyToManyField(ModifierGroups)
    categories = models.ManyToManyField(Categories)
    tags = models.ManyToManyField(Tags)
    canonical = models.ForeignKey(Canonical, on_delete=models.CASCADE)
    itemStock = models.ForeignKey(ItemStock, on_delete=models.CASCADE)
    modifiedTime = models.DateTimeField(default=timezone.now)
    deletedTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
