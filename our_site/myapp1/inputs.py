from django import forms
class InputForm(forms.Form):
    login = forms.CharField(label="", max_length=20, widget=forms.TextInput(attrs={
        'id':"userNameInput",
        'class':"nav__modal-windowInputUserName",
        'placeholder':"User"}))
class PasswordForm(forms.Form):
    password = forms.CharField(label="", max_length=20, widget=forms.TextInput(attrs={
        'id':"userNameInput",
        'class':"nav__modal-windowInputUserPassword",
        'placeholder':"qwerty123"}))

class SideForm(forms.Form):
    side = forms.ChoiceField(choices={'seller':'seller', 'buyer':'buyer'}, required=False)

class WarehousesForm(forms.Form):
    warehouses = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices={str(i): str(i) for i in range(3)})

