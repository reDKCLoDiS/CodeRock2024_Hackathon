from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
import json
from .inputs import *
from django.core.cache import cache
import datetime

def get_login(request):
    
    if request.method == "POST":
        print('post')
        login_form = InputForm(request.POST)
        password_form = PasswordForm(request.POST)
        warehouse1_form = WarehousesForm1(request.POST)
        warehouse2_form = WarehousesForm2(request.POST)
        warehouse3_form = WarehousesForm3(request.POST)
        email_input_form = EmailInput(request.POST)
    else:
        print('get')
        login_form = InputForm()
        password_form = PasswordForm()
        warehouse1_form = WarehousesForm1()
        warehouse2_form = WarehousesForm2()
        warehouse3_form = WarehousesForm3()
        email_input_form = EmailInput()

    login_value, password_value = \
        login_form.data.get('login'), password_form.data.get('password')
    warehouse1_value, warehouse2_value, warehouse3_value, =\
        warehouse1_form.data.get('warehouse1'), warehouse2_form.data.get('warehouse2'), warehouse3_form.data.get('warehouse3')
    print(email_input_form.data)
    email_input_value = email_input_form.data.get('email')

    database_file = open(r'myapp1/DB.json')
    database = json.load(database_file)
    database_file.close()

    database_file_email = open(r'myapp1/DB_email.json')
    database_email = json.load(database_file_email)
    database_file_email.close()
    
    print(database_email.values(),email_input_value)
    if email_input_value != None and email_input_value != 'null' and email_input_value != '' and email_input_value in database_email.values(): 
        print(True)
    
    elif (login_value != None and password_value != None and email_input_value != None) and \
         (str(login_value) != 'null' and str(password_value) != 'null' and email_input_value != 'null') and \
        (str(login_value) != '' and str(password_value) != '' and email_input_value != ''):
        
            warehouses = []
            side = 'buyer'
            if warehouse1_value == 'on':
                warehouses.append('warehouse1')
            if warehouse2_value == 'on':
                warehouses.append('warehouse2')
            if warehouse3_value == 'on':
                warehouses.append('warehouse3')
                
            database_file = open(r'myapp1/DB.json', 'w')
            database_file_email = open(r'myapp1/DB_email.json', 'w')

            if warehouses:  
                database[login_value] = (password_value, email_input_value, warehouses)
            else:
                database[login_value] = (password_value, email_input_value, side)

            database_email[login_value] = email_input_value

            json.dump(database, database_file)
            json.dump(database_email, database_file_email)

            database_file_email.close()
            database_file.close()
    print('end')
    
    return render(request, 'main-page.html', \
            {'login_form': login_form, 'password_form': password_form, 
            'warehouse1_form': warehouse1_form, 'warehouse2_form': warehouse2_form, 
            'warehouse3_form': warehouse3_form, 'email_input_form': email_input_form})#, 'side_form': side_form


def get_login2(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(form.data)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    print(form.data)
    return render(request, "index.html", {"form": form})