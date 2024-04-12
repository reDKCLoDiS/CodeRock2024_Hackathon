from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
import json
from .inputs import *
from django.core.cache import cache
import datetime
from ipware import get_client_ip
from .dijkstra import Graph, Graph2
from random import choice

class User_Define:
    def __init__(self):
        self.ip_base = {}
        self.ip_base_pick_up_points = {} 
    
    def get_login(self, request):
        if request.method == "POST":
            email_input_form = EmailInput(request.POST)
            login_form = InputForm(request.POST)
            password_form = PasswordForm(request.POST)
            warehouse1_form = WarehousesForm1(request.POST)
            warehouse2_form = WarehousesForm2(request.POST)
            warehouse3_form = WarehousesForm3(request.POST)
        else:
            email_input_form = EmailInput()
            login_form = InputForm()
            password_form = PasswordForm()
            warehouse1_form = WarehousesForm1()
            warehouse2_form = WarehousesForm2()
            warehouse3_form = WarehousesForm3()
            
        email_input_value = email_input_form.data.get('email')
        database_file_email = open(r'myapp1/DB_email.json')
        database_email = json.load(database_file_email)
        database_file_email.close()
        
        nearest_pick_up_point = self.define_user_pick_up_point()

        if email_input_value != None and email_input_value != 'null' and email_input_value != '':
            client_ip, is_routable = get_client_ip(request)
            self.ip_base[str(client_ip)] = email_input_value
            self.ip_base_pick_up_points[str(client_ip)] = nearest_pick_up_point
            if email_input_value in database_email.keys():
                return HttpResponseRedirect('/main-page')
            else:
                return HttpResponseRedirect('/registration')
            
        return render(request, 'login-page.html', \
                {'email_input_form': email_input_form})#, 'side_form': side_form


    def registration(self, request):
        client_ip, is_routable = get_client_ip(request)
        email_input_value = self.ip_base[str(client_ip)]
        if request.method == "POST":
            login_form = InputForm(request.POST)
            password_form = PasswordForm(request.POST)
            warehouse1_form = WarehousesForm1(request.POST)
            warehouse2_form = WarehousesForm2(request.POST)
            warehouse3_form = WarehousesForm3(request.POST)
            warehouse4_form = WarehousesForm4(request.POST)
            warehouse5_form = WarehousesForm5(request.POST)
        else:
            login_form = InputForm()
            password_form = PasswordForm()
            warehouse1_form = WarehousesForm1()
            warehouse2_form = WarehousesForm2()
            warehouse3_form = WarehousesForm3()
            warehouse4_form = WarehousesForm4()
            warehouse5_form = WarehousesForm5()

        login_value, password_value = \
            login_form.data.get('login'), password_form.data.get('password')
        warehouse1_value, warehouse2_value, warehouse3_value, =\
            warehouse1_form.data.get('warehouse1'), warehouse2_form.data.get('warehouse2'), warehouse3_form.data.get('warehouse3')
        warehouse4_value, warehouse5_value = warehouse4_form.data.get('warehouse4'), warehouse5_form.data.get('warehouse5')

        
        database_file = open(r'myapp1/DB.json')
        database = json.load(database_file)
        database_file.close()

        database_file_email = open(r'myapp1/DB_email.json')
        database_email = json.load(database_file_email)
        database_file_email.close()

        if (login_value != None and password_value != None) and \
            (str(login_value) != 'null' and str(password_value) != 'null') and \
            (str(login_value) != '' and str(password_value) != ''):
            
            warehouses = []
            side = 'buyer'
            if warehouse1_value == 'on':
                warehouses.append('warehouse1')
            if warehouse2_value == 'on':
                warehouses.append('warehouse2')
            if warehouse3_value == 'on':
                warehouses.append('warehouse3')
            if warehouse4_value == 'on':
                warehouses.append('warehouse4')
            if warehouse5_value == 'on':
                warehouses.append('warehouse5')

            database_file_email = open(r'myapp1/DB_email.json', 'w')
            database_email[email_input_value] = login_value
            json.dump(database_email, database_file_email)
            database_file_email.close()

            if warehouses:  
                database[login_value] = (password_value, email_input_value, warehouses)
            else:
                database[login_value] = (password_value, email_input_value, side)

            database_file = open(r'myapp1/DB.json', 'w')
            json.dump(database, database_file)
            database_file.close()
            return HttpResponseRedirect('/main-page')

        return render(request, 'reg-page.html', \
            {'login_form': login_form, 'password_form': password_form, 
            'warehouse1_form': warehouse1_form, 'warehouse2_form': warehouse2_form, 
            'warehouse3_form': warehouse3_form})
    def main_page_function(self, request):
        return render(request, 'main-page.html')

    def define_user_pick_up_point(self):
        #в будущем местоположение клиента планируется определять по IP 
        #пока что код запускается локально, что лишает такой 
        
        return 30

    def order(self, request):
        if request.method == "POST":
            fastetst_way = Fastetst_way(request.POST)
            cheapest_way = Cheapest_way(request.POST)
        else:
            fastetst_way = Fastetst_way()
            cheapest_way = Cheapest_way()
        V = 2**18
        
        client_ip, is_routable = get_client_ip(request)
        nearest_pick_up_point = self.ip_base_pick_up_points[str(client_ip)]

        dist = Graph(V)
        cost = Graph2(V)
        data = open('myapp1/data.json')
        graph = json.load(data)
        data.close()
        for i in graph["distance"]:
            dist.addEdge(i['Graph_from'], i['Graph_to'], i['Length'], i['cost'])
        for i in graph["distance"]:
            cost.addEdge(i['Graph_from'], i['Graph_to'], i['cost'], i['Length'])
        
        ways_dict = {}
        storages = [26, 27, 28, 29, 31]
        for storage in storages:
            
            if cheapest_way.data.get('cheapest_way')=='on':
                _, price, _ = cost.shortestPath(storage, nearest_pick_up_point)
                ways_dict[price] = storage
            else:
                distance, _, _  = dist.shortestPath(storage, nearest_pick_up_point)
                ways_dict[distance] = storage
        
        best = min(ways_dict.keys())
        best_storage = ways_dict[best]
        _, price, _ = cost.shortestPath(best_storage, nearest_pick_up_point)
        
        return render(request, 'order-page.html', {'fastetst_way': fastetst_way, 'cheapest_way': cheapest_way, 'price': price})
    def info_page_function(self, request):
        return render(request, 'info-page.html')