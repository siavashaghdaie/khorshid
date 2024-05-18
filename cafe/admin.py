from django.contrib import admin
from .models import Buy, Customer, MenuCat, MenuItem, Order, OrderItem, User, Product, Artist
admin.site.register(User)
admin.site.register(Buy)
admin.site.register(Product)
admin.site.register(Artist)
admin.site.register(MenuCat)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Customer)

 