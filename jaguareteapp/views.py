from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import CreateCustomerForm, OrderForm, CreateUserForm, ContactoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
import datetime


# Create your views here.
def index(request):
    return render(request, 'jaguareteapp/index.html')

def productos(request):
    return render(request, 'jaguareteapp/productos.html' )

def admin2(request):
    return render(request, 'jaguareteapp/admin2.html' )


def nosotros(request):
    return render(request, 'jaguareteapp/nosotros.html')

def contacto(request):
	data = {
		'form': ContactoForm()
	}
	
	if request.method == 'POST':
		formulario = ContactoForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data["mensaje"] = "Recibimos el mensaje, estaremos en contacto a la brevedad"
		else:
			data["form"] = formulario

	return render(request, 'jaguareteapp/contacto.html', data)


def home(request):
    return render(request, 'jaguareteapp/home.html')


def registro(request):
    form = CreateUserForm()
    form1 = CreateCustomerForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'La cuenta ha sido creada para ' + user)
        
            return redirect('loginn')
            
    context = {'form':form}
    return render(request, 'jaguareteapp/registro.html', context)


def loginn(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Contraña o usuario incorrecto')

		context = {}
		return render(request, 'jaguareteapp/loginn.html', context)

def logoutUser(request):
	logout(request)
	return redirect('loginn')


def store(request):
	if request.user.is_authenticated:
		# customer = request.user.customer
		order, created = Order.objects.get_or_create(complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items

	else:
		items = []
		order = {'get_cart_total' :0, 'get_cart_items':0}
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'jaguareteapp/store.html', context)

def cart(request):
	if request.user.is_authenticated:
		# customer = request.user.customer
		order, created = Order.objects.get_or_create(complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items

	else:
		items = []
		order = {'get_cart_total' :0, 'get_cart_items':0}
		cartItems = order['get_cart_items']
		

	context = {'items':items,'order':order, 'cartItems':cartItems}
	return render(request, 'jaguareteapp/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		# customer = request.user.customer
		order, created = Order.objects.get_or_create( complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items

	else:
		items = []
		order = {'get_cart_total' :0, 'get_cart_items':0}
		cartItems = order['get_cart_items']
		
		
	context = {'items':items,'order':order, 'cartItems':cartItems}
	return render(request, 'jaguareteapp/checkout.html', context)
	
	

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	print('Action:', action)
	print('productId:', productId)

	# customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	
	if action =='add':
		orderItem.quantity = (orderItem.quantity +1)
	elif action =='remove':
		orderItem.quantity = (orderItem.quantity -1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

		
	return JsonResponse('Item was added', safe=False)


def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)
	


	if request.user.is_authenticated:
		# customer = request.user.customer
		order, created = Order.objects.get_or_create(complete=False)
		total = float(str(data['form']['total']).strip().replace(',','.'))
		order.transaction_id = transaction_id

		if total == float(order.get_cart_total):
			order.complete= True
		order.save()

		if order.shipping == True:
			ShippingAddress.objects.create(
				
				order=order,
				address=data['shipping']['address'],
				city=data['shipping']['city'],
				state=data['shipping']['state'],
				zipcode=data['shipping']['zipcode'],
				
			

			)

		return JsonResponse('Payment complete!', safe=False)
			
	    

	
 

