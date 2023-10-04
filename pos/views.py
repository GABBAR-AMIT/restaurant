from django.shortcuts import render, redirect
from menu.models import Category, Menu, OrderItem, Order, Kitchen, KitchenItem
from django.contrib import messages # for showing the message.
from django.utils import timezone
from admin_p.models import UserDetails
# Create your views here.
def home(request):
    return render(request, 'table.html')

def menu(request, pk):
    table = pk
    item = Category.objects.all()
    
    return render(request, 't_menu.html', {'data':item, 'table':table})

def order(request, pk):
    if request.method=="POST":
        item = Menu.objects.get(id=pk)
        # print(item)
        quantity = int(request.POST.get('quantity', 0))
        table_number = request.POST.get('table_number')
        # Generate a unique order number
        current_time = timezone.now()
        order_number = f"{table_number}-{current_time.strftime('%Y%m%d')}"
        # print(order_number)
        # Create the order or retrieve it if it already exists
        order= Order.objects.get_or_create(table_number=table_number, order_number=order_number)
        # print(order)
        order, _ = order
        order_item, created = OrderItem.objects.get_or_create(item=item, order=order)
        order_item.quantity += quantity
        order_item.save()
        
        # for kitchen
        kitchen= Kitchen.objects.get_or_create(table_number=table_number, order_number=order_number)
        # print(order)
        kitchen, _ = kitchen
        order_item, created = KitchenItem.objects.get_or_create(item=item, kitchen=kitchen)
        order_item.quantity += quantity
        order_item.save()
        messages.success(request, "Added to order, for full order check the order tab !!" )
        return redirect('menu', pk=table_number)
    
def orders_for_table(request, pk):
    table=pk
    orders = Order.objects.filter(table_number=pk)

    # Retrieve messages
    messages_list = messages.get_messages(request)
    if orders:
        for order in orders:
            total_price = sum(item.quantity * item.item.item_price for item in order.orderitem_set.all())
        return render(request, 'orders_for_table.html', {'orders': orders, 'table':table, 'total':total_price, 'messages': messages_list})
    return render(request, 'orders_for_table.html',{'table':table})

def kit(request):
    items = Kitchen.objects.all()
    return render(request, 'kitchen.html',{'data':items})

def userdetails(request):
    if request.method=='POST':
        name= request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        user=UserDetails.objects.create(name=name, mobile=mobile, email=email)
        user.save()
    return render(request, 'userfrom.html')

def donee(request, pk):
    table = pk
    order = Kitchen.objects.filter(table_number=pk)
    order.delete()
    messages.success(request, f"Order for Table {table} is ready, Bon Appetit")
    return redirect('kitchen')

def pdonee(request, pk):
    table = pk
    order = Order.objects.filter(table_number=pk)
    order.delete()
    return redirect('bill')

def billDetails(request):
    items = Order.objects.all()
    if items:
        for order in items:
            total_price = sum(item.quantity * item.item.item_price for item in order.orderitem_set.all())
        return render(request, 'pos.html',{'data':items, 'total':total_price})
    return render(request, 'pos.html')