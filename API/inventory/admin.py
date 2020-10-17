from django.contrib import admin

from .models import (Menu, Items, Printers, PriceType, Canonical, Attribute, Options, ItemGroup, TaxRates, Modifiers,
                     ModifierGroups, Categories, Tags, ItemStock)

admin.site.register(Menu)
admin.site.register(Items)
admin.site.register(ItemStock)
admin.site.register(ItemGroup)
admin.site.register(Modifiers)
admin.site.register(ModifierGroups)
admin.site.register(Categories)
admin.site.register(Canonical)
admin.site.register(Tags)
admin.site.register(Attribute)
admin.site.register(Options)
admin.site.register(TaxRates)
admin.site.register(PriceType)
admin.site.register(Printers)
