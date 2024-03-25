from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile , Create_Post

class UserCreationForms(UserCreationForm):
    username = forms.CharField(label='اسم المستخدم' ,)
    first_name = forms.CharField(label='الأسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    email = forms.EmailField(label=' البريد الالكتروني')
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name' , 'email' , 'password1' , 'password2']


class Login_Form(forms.ModelForm):

    username = forms.CharField(label='اسم المستخدم' , max_length=50)
    password = forms.CharField(label= 'كلمة المرور' , widget= forms.PasswordInput , required=True)

    class Meta:
        model = User
        fields = ('username' , 'password')

class Update_User(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name' , 'last_name' , 'email']
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
        }


class Update_Profile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name',
                  'subtitle', 
                  'Specialist_doctor',
                  'address', 
                  'who_i', 
                  'price',
                  'Waiting_time',
                  'working_hours',
                  'number_phone',
                  'doctor_in',
                  'image',
                ]
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'subtitle' : forms.TextInput(attrs={'class':'form-control'}),
            'Specialist_doctor' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'who_i' : forms.Textarea(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'Waiting_time' : forms.NumberInput(attrs={'class':'form-control'}),
            'working_hours' : forms.NumberInput(attrs={'class':'form-control'}),
            'number_phone' : forms.TextInput(attrs={'class':'form-control'}),
            'doctor_in' : forms.Select(attrs={'class':'form-control'}),
            'image' : forms.FileInput(attrs={'class':'form-control'}),
        }

class Update_Post_Form(forms.ModelForm):

    class Meta:
        model = Create_Post()
        fields = ['title' , 'Introduction' , 'subject' , 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'Introduction': forms.Textarea(attrs={'class': 'form-control'}),
            'subject': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }