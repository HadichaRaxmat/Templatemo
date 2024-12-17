from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class UserContact(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    title = models.CharField(max_length=50)
    last = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Header(models.Model):
    logo = models.CharField(max_length=20)

    def __str__(self):
        return self.logo


class Menu(models.Model):
    menu = models.CharField(max_length=20)

    def __str__(self):
        return self.menu


class Banner(models.Model):
    main = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=350)
    last = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Carousel(models.Model):
    title = models.CharField(max_length=15)
    text = models.CharField(max_length=20)

    def __str__(self):
        return self.title



class Meeting(models.Model):
    title = models.CharField(max_length=30)
    invitation = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    month = models.CharField(max_length=15)
    day = models.CharField(max_length=5)
    division = models.CharField(max_length=20)
    first_text = models.CharField(max_length=30)
    second_text = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='meeting_photos/', blank=True, null=True)

    def __str__(self):
        return self.title


class MeetingHeader(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class MeetingCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Middle(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=30)
    last = models.CharField(max_length=20)

    def __str__(self):
        return self.title



class About(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Popular(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='popular_photos/', blank=True, null=True)

    def __str__(self):
        return self.title



class Fact(models.Model):
    title = models.CharField(max_length=100)
    indicator = models.CharField(max_length=10)
    text = models.CharField(max_length=35)

    def __str__(self):
        return self.title


class Touch(models.Model):
    first_method = models.CharField(max_length=50)
    first = models.CharField(max_length=50)
    second_method = models.CharField(max_length=50)
    second = models.CharField(max_length=100)
    third_method = models.CharField(max_length=50)
    third = models.CharField(max_length=50)
    fourth_method = models.CharField(max_length=50)
    fourth = models.CharField(max_length=50)

    def __str__(self):
        return self.first_method


class End(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class MiddleFirst(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class MiddleSecond(models.Model):
    category = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    month = models.CharField(max_length=20)
    day = models.CharField(max_length=5)
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Last(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Detail(models.Model):
    price = models.CharField(max_length=10)
    month = models.CharField(max_length=20)
    day = models.CharField(max_length=5)
    head = models.CharField(max_length=30)
    title= models.CharField(max_length=30)
    text = models.CharField(max_length=300)
    hours = models.CharField(max_length=10)
    location = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    share = models.CharField(max_length=30)
    last = models.CharField(max_length=30)

    def __str__(self):
        return self.price