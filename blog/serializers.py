from rest_framework import serializers
from .models import (Header, Banner, Carousel, Contact, Meeting, Middle, About,
                     Popular, Fact, Touch, End, MiddleFirst, MiddleSecond, Last, Detail, Menu)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        read_only_fields = ('id' ,)
        fields = ['id', 'title', 'first_contact', 'second_contact', 'third_contact', 'fourth_contact', 'last']

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ['id', 'logo']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'menu']


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        read_only_fields = ('id' ,)
        fields = ['id', 'main', 'title', 'text', 'last']


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        read_only_fields = ('id' ,)
        fields = ['id', 'title', 'text']


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        read_only_fields = ('id',)
        fields = ['id', 'heading', 'title', 'category', 'invitation', 'price', 'month', 'day', 'division', 'first_text', 'second_text']


class MiddleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Middle
        read_only_fields = ('id' ,)
        fields = ['id', 'title', 'text', 'last']


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        read_only_fields = ('id' ,)
        fields = ['id', 'title', 'text']

class PopularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Popular
        read_only_fields = ('id', )
        fields = ['id', 'title', 'text', 'price']


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        read_only_fields = ('id', )
        fields = ['id', 'title', 'indicator', 'text']


class TouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Touch
        read_only_fields = ('id' ,)
        fields = ['id', 'first_method', 'second_method', 'third_method', 'fourth_method', 'first', 'second', 'third', 'fourth']


class EndSerializer(serializers.ModelSerializer):
    class Meta:
        model = End
        read_only_fields = ('id' ,)
        fields = ['id', 'title', 'text']


# Class Middle


class MiddleFirstSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiddleFirst
        read_only_fields = ('id' ,)
        fields = ['id', 'title', 'text']


class MiddleSecondSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiddleSecond
        read_only_fields = ('id' ,)
        fields = ['id', 'category', 'price', 'month', 'day', 'title', 'text']


# Class Last

class LastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Last
        read_only_fields = ('id' ,)
        fields = ['id', 'title', 'text']


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        read_only_fields = ('id' ,)
        fields = ['id', 'price', 'month', 'day', 'head', 'title', 'text', 'hours', 'location', 'contact', 'share', 'last']