from django.contrib import admin
from .models import Item, Storage, Place, Order, OrderType, Session, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(Storage)
admin.site.register(Place)
admin.site.register(Order)
admin.site.register(OrderType)
admin.site.register(Session)

