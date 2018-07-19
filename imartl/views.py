
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf.urls import include
from django.template import loader
from .models import Imartl
from django.http import Http404
from .forms import SignUpForm,AddBookForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
import pymysql.cursors
# Create your views here.
@login_required
def home(request):
    return render(request, 'home1.html')

def signup_success(request):
    return render(request,'signup_success1.html')

def add_book(request):
    return render(request,'add_product.html')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			cname = form.cleaned_data.get('librarian_name')
			email = form.cleaned_data.get('email')
			phoneno = form.cleaned_data.get('phone_number')
			user.refresh_from_db()
			user.save()
			passwd = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=passwd)
			login(request, user)

	else:
		form = SignUpForm()
	return render(request, 'signup1.html', {'form': form})


def add_product(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data.get('product')
            b = form.cleaned_data.get('company')
            c = form.cleaned_data.get('description')
            d = form.cleaned_data.get('price')
            e = form.cleaned_data.get('category')
            count = 0
            connection = pymysql.connect(host='localhost',
                                         user='dodmise',
                                         password='dodmise123',
                                         db='shubham',
                                         )

            with connection.cursor() as cursor:
                    sql = "INSERT INTO `stud_data` (`product_name`, `company`,`description`,`product_id`,`category`) VALUES (%s, %s,%s,%s,%s)"
                    sql1 = "INSERT INTO `sale` (`product_name`,`category`,`count`) VALUES(%s,%s,%s)"
                    cursor.execute(sql, (a, b, c,d,e))
                    #sql1 = "INSERT INTO `sale` (`product_name`,`count`) VALUES(%s,%s)"
                    cursor.execute(sql1, (a,e, count))
                    connection.commit()
                    return render(request, 'psuccess.html', {'form': form})




    else:
        form = AddBookForm()
    return render(request, 'addp.html', {'form': form})


