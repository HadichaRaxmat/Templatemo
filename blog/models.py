from django.db import models


class UserContact(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    title = models.CharField(max_length=50)
    first_contact = models.CharField(max_length=20)
    second_contact = models.CharField(max_length=20)
    third_contact = models.CharField(max_length=20)
    fourth_contact = models.CharField(max_length=20)
    last = models.CharField(max_length=30)

    def __str__(self):
        return self.first_contact


class Header(models.Model):
    logo = models.CharField(max_length=20)
    menu = models.CharField(max_length=15)

    def __str__(self):
        return self.menu


class Banner(models.Model):
    main = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    text = models.TextField()
    last = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Carousel(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title



class Meeting(models.Model):
    heading = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    invitation = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    day = models.IntegerField()
    division = models.CharField(max_length=100)
    first_text = models.TextField()
    second_text = models.TextField()

    def __str__(self):
        return self.heading



class Middle(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    last = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class About(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.title


class Popular(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Fact(models.Model):
    title = models.CharField(max_length=500)
    indicator = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    last = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Touch(models.Model):
    first_method = models.CharField(max_length=20)
    first = models.CharField(max_length=20)
    second_method = models.CharField(max_length=30)
    second = models.CharField(max_length=20)
    third_method = models.CharField(max_length=20)
    third = models.CharField(max_length=20)
    fourth_method = models.CharField(max_length=20)
    fourth = models.CharField(max_length=20)

    def __str__(self):
        return self.first_method


class End(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title


class MiddleFirst(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class MiddleSecond(models.Model):
    category = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    month = models.CharField(max_length=250)
    day = models.IntegerField()
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.category


class Last(models.Model):
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Detail(models.Model):
    price = models.CharField(max_length=250)
    month = models.CharField(max_length=250)
    day = models.IntegerField()
    head = models.CharField(max_length=300)
    title= models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    hours = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    contact = models.CharField(max_length=50)
    share = models.CharField(max_length=250)
    last = models.CharField(max_length=250)

    def __str__(self):
        return self.price