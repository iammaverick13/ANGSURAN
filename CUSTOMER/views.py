from django.shortcuts import render, redirect
from django.contrib.auth import	authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *
# Create your views here.
def loginView(request):
	user = None
	form = AdminForm()
	if request.method == 'POST':
		form = AdminForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			try:
				user = authenticate(username=username, password=password)
				if user:
					login(request, user)			
					return redirect('/')
				else:
					return redirect('/accounts/jsalert')
			except:
				return 

	context = {
		'form':form,
		'pageTitle':'LOGIN', 
	}
	return render(request, 'customer/login.html', context)

def logoutView(request):
	logout(request)
	return redirect('/')

def jsAlert(request):
	return render(request, 'customer/alert.html')

@login_required
def dashboard(request):
	list_customer = Customer.objects.all()
	context = {
		'list_customer':list_customer,
	}
	return render(request, 'customer/list_customer.html', context)

@login_required
def addCustomer(request):
	form = CustomerForm()
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			jumlah_utang = form.cleaned_data['jumlah_utang']
			add_customer = Customer(username=username, jumlah_utang=jumlah_utang)
			add_customer.save()
			return redirect('/accounts/dashboard')

	context = {
		'pageTitle':'ADD CUSTOMER',
		'form':form,
	}

	return render(request, 'customer/add.html', context)
@login_required
def updateCustomer(request):
	return redirect('/accounts/dashboard')

@login_required
def spesificCustomer(request, pk):
	user = Customer.objects.get(id=pk)
	bayar = UpdateUtang()

	if request.method == 'POST':
		bayar = UpdateUtang(request.POST)
		if bayar.is_valid():
			jumlah_bayar = bayar.cleaned_data.get('jumlah_bayar')
			user.jumlah_utang = user.jumlah_utang - jumlah_bayar
			user.save()
			return redirect('/accounts/dashboard/'+str(user.id))
	else:
		bayar = UpdateUtang()

	context = {
		'form':bayar,
		'user':user,
	}
	return render(request, 'customer/user.html', context)