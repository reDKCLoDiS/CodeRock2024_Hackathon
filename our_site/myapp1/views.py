from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import json
from .inputs import *
from django.core.cache import cache

def set_cookies(request, login_falue):
    print(1)
    username = request.GET.get("login", login_falue)
    response = HttpResponse()
    #print(1, request.COOKIES.get('login'))
    response.delete_cookie('login')
    print(username, login_falue)
    response.set_cookie("login2", login_falue)

def get_login(request):
    
    if request.method == "POST":
        print('post')
        login_form = InputForm(request.POST)
        password_form = PasswordForm(request.POST)
        warehouse1_form = WarehousesForm1(request.POST)
        warehouse2_form = WarehousesForm2(request.POST)
        warehouse3_form = WarehousesForm3(request.POST)
    else:
        print('get')
        login_form = InputForm(request.GET)
        password_form = PasswordForm(request.GET)
        warehouse1_form = WarehousesForm1(request.GET)
        warehouse2_form = WarehousesForm2(request.GET)
        warehouse3_form = WarehousesForm3(request.GET)
    print(1)
    login_value, password_value = \
        login_form.data.get('login'), password_form.data.get('password')
    print(login_value)
    warehouse1_value, warehouse2_value, warehouse3_value, =\
        warehouse1_form.data.get('warehouse1'), warehouse2_form.data.get('warehouse2'), warehouse3_form.data.get('warehouse3')

    print(warehouse1_value)
    database_file = open(r'myapp1/DB.json')
    database = json.load(database_file)
    database_file.close()
    if login_value != None and password_value != None :
        if login_value in database.keys():
            if database[login_value][0] == password_value:
                request = set_cookies(request, login_value)
                return HttpResponseRedirect("/hello_world")
        else:
            warehouses = []
            side = 'buyer'
            if warehouse1_value == 'on':
                warehouses.append('warehouse1')
            if warehouse2_value == 'on':
                warehouses.append('warehouse2')
            if warehouse3_value == 'on':
                warehouses.append('warehouse3')
                
            database_file = open(r'myapp1/DB.json', 'w')
            if warehouses:  
                database[login_value] = (password_value, warehouses)
            else:
                database[login_value] = (password_value, side)
            json.dump(database, database_file)
            database_file.close()
            print(1, request.COOKIES.get('user_login'))
            request = set_cookies(request, login_value)
            return HttpResponseRedirect("/hello_world")
    
    
    return render(request, 'account_define.html', \
            {'login_form': login_form, 'password_form': password_form, 
            'warehouse1_form': warehouse1_form, 'warehouse2_form': warehouse2_form, 
            'warehouse3_form': warehouse3_form})#, 'side_form': side_form

def check_user(request):
    print(1, request.COOKIES.get('login2'))
    return render(request, 'index.html')
    
    