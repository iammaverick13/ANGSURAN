from django.urls import path

from .views import *

urlpatterns = [
	path('login/', loginView, name='login'),
	path('logout/', logoutView, name='logout'),
	path('jsalert/', jsAlert, name='alert'),
	path('dashboard/<int:pk>/', spesificCustomer, name='customer'),
	path('dashboard/', dashboard, name='dashboard'),
	path('add/', addCustomer, name='add'),
	path('update/', updateCustomer, name='update'),
]