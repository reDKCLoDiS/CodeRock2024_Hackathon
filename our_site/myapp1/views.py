from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
import json
from .inputs import *

class get_login(request):
        warehouses_value = ''
        login_form = InputForm(request.POST)
        password_form = PasswordForm(request.POST)
        warehouse1_form = WarehousesForm1(request.POST)
        warehouse2_form = WarehousesForm2(request.POST)
        warehouse3_form = WarehousesForm3(request.POST)
        if login_form.is_valid():
            print(login_form.data)
            login_value, password_value = \
                login_form.data.get('login'), password_form.data.get('password')
            warehouse1_value, warehouse2_value, warehouse3_value, =\
                warehouse1_form.data.get('warehouse1'), warehouse2_form.data.get('warehouse2'), warehouse3_form.data.get('warehouse3')
            print(warehouse1_form.data)
            print(warehouse2_form.data)
            print(warehouse3_form.data)
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
        request.user.name = login_form
        return render(request, 'account_define.html', \
            {'login_form': login_form, 'password_form': password_form, 
             'warehouse1_form': warehouse1_form, 'warehouse2_form': warehouse2_form, 'warehouse3_form': warehouse3_form})#, 'side_form': side_form

def check_user(request):
    print(request.user)
    return render(request, 'index.html')