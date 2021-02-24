from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stock
from .forms import *
from stocks.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import csv
from django.db.models import Sum
# returns {'field_name__sum': 1000} for example

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'stocks/login.html', {})


def home(request):
    title = 'Home'
    context = {
    "header": title,
    }
    if request.user.is_authenticated:
        return render(request, "stocks/home.html",context)
    else:
        # render(request, "stocks/home.html",context)
        return render(request, "stocks/login.html",context)



@login_required
def list_items(request):
    title = 'List of Assets and Consumables'
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()
    total = ( Stock.objects
            .filter(rate__isnull=False)
            .aggregate(
                total=Sum('rate', field="rate*quantity")
             )['total']
         )
    context = {
        "header": title,
        "queryset": queryset,
        "total":total,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Stock.objects.filter(
        item_name__icontains=form['item_name'].value(),
            category__icontains=form['category'].value(),
        )

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY','SUB CATEGORY','PART NO',
             'ITEM NO','ITEM NAME', 'QUANTITY', 'UNITS','RATE', 'VALUE'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.category,stock.subcategory,stock.part_no,
                stock.item_no,stock.item_name, stock.quantity, stock.units,
                stock.rate, (stock.quantity * stock.rate)])
            return response

        context = {
        "form": form,
        "header": title,
        "queryset": queryset,
    }
    return render(request, "stocks/list_items.html", context)

@login_required
def add_items(request):
    form = StockCreateForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.updated_by = request.user.username
        instance.save()

        messages.success(request, 'Successfully Saved')
        return redirect('add_items')
    context = {
		"form": form,
		"header": "Add Assets or Consumables",
	}
    return render(request, "stocks/add_items.html", context)

@login_required
def update_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = StockUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully Saved')
			return redirect('list_items')

	context = {
		'form':form,
        "header": "Update Assets or Consumables",
	}
	return render(request, 'stocks/update_items.html', context)

@login_required
def delete_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Successfully Deleted')
		return redirect('list_items')
	return render(request, 'stocks/delete_items.html')

@login_required
def stock_detail(request, pk):
	queryset = Stock.objects.get(id=pk)
	context = {
		"queryset": queryset,
	}
	return render(request, "stocks/stock_detail.html", context)

@login_required
def issue_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity -= instance.issue_quantity
		# instance.issue_by = str(request.user)
		messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
		instance.save()

		return redirect('/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": 'Issue ' + str(queryset.item_name),
		"queryset": queryset,
		"form": form,
	    "username": 'Issue By: ' + str(request.user),
	}
	return render(request, "stocks/add_items.html", context)

@login_required
def receive_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = ReceiveForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity += instance.receive_quantity
		instance.save()
		messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name)+"s now in Store")

		return redirect('/stock_detail/'+str(instance.id))
		# return HttpResponseRedirect(instance.get_absolute_url())
	context = {
			"title": 'Reaceive ' + str(queryset.item_name),
			"instance": queryset,
			"form": form,
			"username": 'Receive By: ' + str(request.user),
		}
	return render(request, "stocks/add_items.html", context)
