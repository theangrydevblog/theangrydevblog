from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, ReadOnlyPasswordHashField
from theangrydev.models import Message
User = get_user_model()

class LoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                          'id':'inputEmail4'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                 'id':'inputPassword4'}))


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean_password(self):
        return self.initial["password"]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = (
            'first_name',
            'last_name',
            'email',
            'message'
        )
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
    email = forms.CharField(label='email', max_length=100)
    message = forms.CharField(label='message', max_length=1000)

