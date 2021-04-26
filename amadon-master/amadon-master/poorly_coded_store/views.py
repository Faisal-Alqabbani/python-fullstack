from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    if 'charge' in request.session: 
        request.session['total_charge']=0
        quantity_from_form = int(request.POST["quantity"])
        id = float(request.POST["product_id"]) 
        price_id=Product.objects.get(id=id) 
        request.session['total_charge'] = quantity_from_form * int(price_id.price) 
        request.session['charge']=request.session['charge']+request.session['total_charge'] 
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=request.session['total_charge'])
    if 'quantity' in request.session: 
        request.session['quantity']=request.session['quantity']+quantity_from_form 
    else: 
        request.session['charge']=0 
        request.session['quantity']=0 
        request.session['total_charge']=0
    return redirect("/checkout2")

def checkout2(request):
    return render(request, "store/checkout.html")