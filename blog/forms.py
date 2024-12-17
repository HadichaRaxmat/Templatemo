from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import (Header, Banner, Carousel, Meeting, Middle, About, Popular, Fact, Touch, End, MiddleFirst,
                     MiddleSecond, Last, Detail, Contact, UserContact, Menu, MeetingHeader, MeetingCategory, CustomUser)


class CustomUserCreationUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')



class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


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
        fields = ['first_method', 'second_method', 'third_method', 'fourth_method', 'first', 'second', 'third', 'fourth']


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