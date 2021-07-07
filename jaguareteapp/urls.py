from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('home/', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('loginn/', views.loginn, name='loginn'),
    path('logout/', views.logoutUser, name='logout'),
    path('admin2/', views.admin2, name='admin2'),
    path('store', views.store, name="store"),
    path('contacto', views.contacto, name="contacto"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	
  
    
]