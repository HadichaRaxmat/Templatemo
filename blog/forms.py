from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import (Header, Banner, Carousel, Meeting, Middle, About, Popular, Fact, Touch, End, MiddleFirst,
                     MiddleSecond, Last, Detail, Contact, UserContact, Menu, MeetingHeader, MeetingCategory, CustomUser)




class CustomUserCreationUserForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'})
    )


    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')
        exclude = ('username',)



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )

    class Meta:
        email = forms.EmailField(required=True,
                                 widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'}))
        model = CustomUser
        fields = ('username', 'password')



class AdminUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'}),
        label="Username"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter admin email'}),
        label="Email"
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}),
        label="First Name"
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}),
        label="Last Name"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.is_admin = True
        if commit:
            user.save()
        return user


class AdminUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username or email'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username_or_email and password:
            user = authenticate(username=username_or_email, password=password)
            if user is None:
                raise forms.ValidationError("Invalid credentials.")
            if not (user.is_staff or user.is_superuser):
                raise forms.ValidationError("You do not have permission to access the admin panel.")

        return cleaned_data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar']


class HeaderForm(forms.ModelForm):
    class Meta:
        model = Header
        fields = ['logo']


class MeetingHeaderForm(forms.ModelForm):
    class Meta:
        model = MeetingHeader
        fields = ['title']


class MeetingCategoryForm(forms.ModelForm):
    class Meta:
        model = MeetingCategory
        fields = ['title']


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['menu']


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['main', 'title', 'text', 'last']


class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ['title', 'text']


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = [
            'title', 'photo', 'invitation', 'price', 'month',
            'day', 'division', 'first_text', 'second_text'
        ]


class MiddleForm(forms.ModelForm):
    class Meta:
        model = Middle
        fields = ['title', 'text', 'last']


class PopularForm(forms.ModelForm):
    class Meta:
        model = Popular
        fields = ['title', 'price', 'photo']


class FactForm(forms.ModelForm):
    class Meta:
        model = Fact
        fields = ['title', 'indicator', 'text']


class TouchForm(forms.ModelForm):
    class Meta:
        model = Touch
        fields = ['first_method', 'second_method', 'third_method', 'fourth_method', 'first', 'second', 'third',
                  'fourth']


class EndForm(forms.ModelForm):
    class Meta:
        model = End
        fields = ['title', 'text']


class MiddleFirstForm(forms.ModelForm):
    class Meta:
        model = MiddleFirst
        fields = ['title', 'text']


class MiddleSecondForm(forms.ModelForm):
    class Meta:
        model = MiddleSecond
        fields = ['category', 'price', 'month', 'day', 'title', 'text']


class LastForm(forms.ModelForm):
    class Meta:
        model = Last
        fields = ['title', 'text']


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = [
            'price', 'month', 'day', 'head', 'title', 'text',
            'hours', 'location', 'contact', 'share', 'last'
        ]


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'text']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'last']


class UserContactForm(forms.ModelForm):
    class Meta:
        model = UserContact
        fields = ['name', 'phone', 'email', 'message']
