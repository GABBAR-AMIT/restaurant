from django.contrib import admin
from menu.models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
admin.site.register(Category,CategoryAdmin)

class menuAdmin(admin.ModelAdmin):
    list_display = ["category",'item_name',"item_description", "item_price"]
admin.site.register(Menu, menuAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ["table_number","order_number"]
admin.site.register(Order,OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order",'item',"quantity"]
admin.site.register(OrderItem, OrderItemAdmin)
