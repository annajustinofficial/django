from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')
from .models import Item
from django.shortcuts import redirect

def add_item(request):
    if request.method == "POST":
        item_name = request.POST['item_name']
        brand = request.POST['brand']
        quantity = request.POST['quantity']
        price = request.POST['price']

        if item_name and brand and quantity and price:
            Item.objects.create(
                item_name=item_name,
                brand=brand,
                quantity=quantity,
                price=price
            )

            return redirect('view_items')

    return render(request,'add_item.html')
def view_items(request):
    items = Item.objects.all()
    return render(request, "view_items.html", {"items": items})
def edit_item(request, id):

    item = Item.objects.get(id=id)

    if request.method == "POST":

        item.item_name = request.POST.get("item_name")
        item.brand = request.POST.get("brand")
        item.quantity = request.POST.get("quantity")
        item.price = request.POST.get("price")

        item.save()

        return redirect("view_items")

    return render(request, "edit_item.html", {"item": item})
def delete_item(request, id):

    item = Item.objects.get(id=id)

    item.delete()

    return redirect("view_items")