from django.contrib import admin

from .models import Item, Inventory

admin.site.register([Item, Inventory])
