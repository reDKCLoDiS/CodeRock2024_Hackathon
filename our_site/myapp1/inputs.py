from django import forms

class InputForm(forms.Form):
    login = forms.CharField(label="", max_length=20, required=False, widget=forms.TextInput(attrs={
        'id':"userNameInput",
        'class':"nav__modal-windowInput",
        'placeholder':"User"}))
class PasswordForm(forms.Form):
    password = forms.CharField(label="", max_length=20, required=False, widget=forms.TextInput(attrs={
        'id':"userPasswordInput",
        'class':"nav__modal-windowInput",
        'placeholder':"qwerty123"}))

class SideForm(forms.Form):
    side = forms.ChoiceField(choices={'seller':'seller', 'buyer':'buyer'}, required=False)

class WarehousesForm1(forms.Form):
    #warehouse = forms.CheckboxInput(attrs={})
    warehouse1 = forms.BooleanField(required=False,label='Склад 1')

class WarehousesForm2(forms.Form):
    #warehouse = forms.CheckboxInput(attrs={})
    warehouse2 = forms.BooleanField(required=False,label='Склад 2')

class WarehousesForm3(forms.Form):
    #warehouse = forms.CheckboxInput(attrs={})
    warehouse3 = forms.BooleanField(required=False,label='Склад 3')

class WarehousesForm4(forms.Form):
    #warehouse = forms.CheckboxInput(attrs={})
    warehouse4 = forms.BooleanField(required=False,label='Склад 4')

class WarehousesForm5(forms.Form):
    #warehouse = forms.CheckboxInput(attrs={})
    warehouse5 = forms.BooleanField(required=False,label='Склад 5')

class EmailInput(forms.Form):
    email = forms.CharField(label="", max_length=20, required=False, widget=forms.TextInput(attrs={\
        'type':"text",
        'class':"userLoginPasswordInput",
        'id':"userLoginPasswordInput",
        'placeholder':"example@mail.com"}))
    
class Fastetst_way(forms.Form):
    #warehouse = forms.CheckboxInput(attrs={})
    fastetst_way = forms.BooleanField(required=False,label='Самая быстрая')

class Cheapest_way(forms.Form):
    #warehouse = forms.CheckboxInput(attrs={})
    cheapest_way = forms.BooleanField(required=False,label='Самая дешёвая')