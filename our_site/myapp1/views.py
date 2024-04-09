from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import json
from .inputs import *
from django.core.cache import cache


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

    database_file = open(r'myapp1/DB.json')
    database = json.load(database_file)
    database_file.close()
    if login_value in database.keys():
        'user registered'
    else:
        database_file = open(r'myapp1/DB.json', 'w')
        database[login_value] = (password_value)
        json.dump(database, database_file)
        database_file.close()
    print(login_value, password_value)
    if login_value != None and password_value != None:
        #return render(request, 'index.html')
        return HttpResponseRedirect("/admin/")
    #set_cookie(request, login_value)
    return render(request, 'account_define.html', \
            {'login_form': login_form, 'password_form': password_form, 
            'warehouse1_form': warehouse1_form, 'warehouse2_form': warehouse2_form, 'warehouse3_form': warehouse3_form})#, 'side_form': side_form

def check_user(request):
    print(request.content_params)
    #return render(request, 'index.html')
    return HttpResponseRedirect("/admin/")