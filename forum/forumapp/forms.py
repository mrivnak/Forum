from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
 
class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }),
        help_text='150 characters or fewer.'
    )

    first_name = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        })
    )

    last_name = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
    )

    user_department = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Department'
        })
    )

    email = forms.EmailField(
        max_length=64, 
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }),
        help_text='Enter a valid email address'
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        }),
        help_text='Passwords must match'
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'user_department', 'email', 'password1', 'password2', )

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150, 
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password')

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['board_title']
        widgets = { 
            'board_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                }),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_title']
        widgets = { 
            'category_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
                }),
        }