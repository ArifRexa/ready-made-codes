from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import CustomUser




class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    # Override the username field to customize help text
    username = forms.CharField(
        max_length=150,
        help_text='',  # Set an empty string to hide the help text
        # widget=forms.TextInput(attrs={'placeholder': 'Username'}),  # Optional: Add a placeholder to the input field
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'password', 'confirm_password']

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if CustomUser.objects.filter(username=username).exists():
    #         raise forms.ValidationError('This username is already taken.')
    #     return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user



class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)