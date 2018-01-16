from django.shortcuts import render, redirect
from .models import Orders, Item
from .forms import OrderForm, ItemForm
from django.contrib import messages

# Create your views here.
def index(request):
    orders = Orders.objects.all()
    instance = Orders.objects.first()
    return render(request, 'order\index.html', {'orders': orders})




def Neworder (request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/index', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('/index', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/index', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm()
    return render(request, 'order\order.html', {'form':form})
    


def index_items(request):
    Items = Item.objects.all()
    return render(request, 'order\index_items.html', {'items': items}) 




def Additem (request):
    if request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/index_items', messages.success(request, 'Product was successfully created.', 'alert-success'))
            else:
                return redirect('/index_items', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/index_items', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        product_form = ProductForm()
        return render(request, 'order\item.html', {'item_form':item_form}) 
