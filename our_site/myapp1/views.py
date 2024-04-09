from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
import json
from .inputs import *

# Create your views here.
def define_account(request):
    return render(request, 'account_define.html')

def get_login(request):
        warehouses_value = ''
        login_form = InputForm(request.POST)
        password_form = PasswordForm(request.POST)
        side_form = SideForm(request.POST)
        warehouse1_form = WarehousesForm1(request.POST)
        warehouse2_form = WarehousesForm2(request.POST)
        warehouse3_form = WarehousesForm3(request.POST)
        
        login_value, password_value, side_value = \
            login_form.data.get('login'), password_form.data.get('password'),  side_form.data.get('side')
        
        warehouse1_value, warehouse2_value, warehouse3_value, =\
              warehouse1_form.data.get('warehouse'), warehouse2_form.data.get('warehouse'), warehouse3_form.data.get('warehouse')

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
            {'login_form': login_form, 'password_form': password_form, 'warehouse1_form': warehouse1_form, \
             'warehouse2_form': warehouse2_form, 'warehouse3_form': warehouse3_form})#, 'side_form': side_form


