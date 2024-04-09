from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
import json
from .inputs import InputForm, PasswordForm, SideForm, WarehousesForm

# Create your views here.
def define_account(request):
    return render(request, 'account_define.html')

def get_login(request):
        warehouses_value = ''
        login_form = InputForm(request.POST)
        password_form = PasswordForm(request.POST)
        side_form = SideForm(request.POST)
        warehousesform = WarehousesForm(request.POST)
        
        login_value, password_value, side_value = \
            login_form.data.get('login'), password_form.data.get('password'),  side_form.data.get('side')

        database_file = open(r'myapp1/DB.json')
        database = json.load(database_file)
        database_file.close()
        if login_value in database.keys():
            'user registered'
        else:
            database_file = open(r'myapp1/DB.json', 'w')
            database[login_value] = (password_value, side_value)
            json.dump(database, database_file)
            database_file.close()
            if side_value == 'buyer':
                pass
            elif side_value == 'seller':
                pass
        
        print(login_value, password_value)

        return render(request, 'account_define.html', \
                  {'login_form': login_form, 'password_form': password_form,})#, 'side_form': side_form

def settings(request):
    if request.method == "POST":
        warehousesform = WarehousesForm(request.POST)
        warehouses_value = dict(warehousesform.data)
        if 'warehouses' in warehouses_value.keys():
             print(warehouses_value['warehouses'])
        
        print(warehouses_value)
    return render(request, 'seller_settings.html', \
                  {'warehouses': warehousesform})
