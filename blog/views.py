from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from .models import (Header, Banner, Carousel, Meeting, Middle, About, Popular, Fact, Touch, End, MiddleFirst,
                     MiddleSecond, Last, Detail, Contact, UserContact, Menu)
from .serializers import (HeaderSerializer, ContactSerializer, BannerSerializer, CarouselSerializer, MeetingSerializer,
                          MiddleSerializer, AboutSerializer, PopularSerializer, FactSerializer, TouchSerializer,
                          EndSerializer, MiddleFirstSerializer, MiddleSecondSerializer, LastSerializer,
                          DetailSerializer, MenuSerializer)
from rest_framework.response import Response
from .forms import (HeaderForm, BannerForm, CarouselForm, MeetingForm, MiddleForm, AboutForm, PopularForm, FactForm,
                    TouchForm, EndForm, MiddleFirstForm, MiddleSecondForm, LastForm, DetailForm, ContactForm,
                    UserContactForm, MenuForm)


def admin_view(request):
    return render(request, 'admin/index.html')


def dashboard2_view(request):
    return render(request, 'admin/index2.html')


def dashboard3_view(request):
    return render(request, 'admin/index3.html')


def iframe_view(request):
    return render(request, 'admin/iframe.html')


def home_view(request):
    header = Header.objects.all()
    contact = Contact.objects.all()
    banners = Banner.objects.all()
    carousels = Carousel.objects.all()
    meetings = Meeting.objects.all()
    middles = Middle.objects.all()
    about = About.objects.all()
    popular = Popular.objects.all()
    facts = Fact.objects.all()
    touch = Touch.objects.all()
    end = End.objects.all()
    menu = Menu.objects.all()
    d = {
        'header': header,
        'contact': contact,
        'banners': banners,
        'carousels': carousels,
        'meetings': meetings,
        'middles': middles,
        'about': about,
        'popular': popular,
        'facts': facts,
        'touch': touch,
        'end': end,
        'menu': menu
    }
    return render(request, 'index.html', context=d)


def meetings_view(request):
    header = Header.objects.all()
    first = MiddleFirst.objects.all()
    second = MiddleSecond.objects.all()
    end = End.objects.all()
    d = {
        'header': header,
        'first': first,
        'second': second,
        'end': end
    }
    return render(request, 'meetings.html', context=d)


def meeting_details_view(request):
    header = Header.objects.all()
    last = Last.objects.all()
    detail = Detail.objects.all()
    end = End.objects.all()
    d = {
        'header': header,
        'last': last,
        'detail': detail,
        'end': end
    }
    return render(request, 'meeting-details.html', context=d)


def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        contact = UserContact.objects.create(name=data['name'], phone=data['phone'],
                                             email=data['email'], message=data['message'])
        contact.save()
        return redirect('/')
    return render(request, 'index.html')

def contact_list_view(request):
    user_contacts = UserContact.objects.all()
    return render(request, 'admin/user_contact_list.html', {'user_contacts': user_contacts})

def user_contact_update(request, pk):
    user_contact = get_object_or_404(UserContact, id=pk)
    if request.method == 'POST':
        form = UserContactForm(request.POST, instance=user_contact)
        if form.is_valid():
            form.save()
            return redirect('user_contact_list')
    else:
        form = UserContactForm(instance=user_contact)
    return render(request, 'admin/user_contact_update.html', {'form': form})


def user_contact_delete(request, pk):
    user_contact = get_object_or_404(UserContact, id=pk)
    if request.method == 'POST':
        user_contact.delete()
        return redirect('user_contact_list')
    return render(request, 'admin/user_contact_delete.html', {'user_contact': user_contact})



def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'admin/contact_create.html', {'form': form})


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'admin/contact_list.html', {'contacts': contacts})


def contact_update(request, pk):
    contact = get_object_or_404(Contact, id=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'admin/contact_update.html', {'form': form})


def contact_delete(request, pk):
    contact = get_object_or_404(Contact, id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'admin/contact_delete.html', {'contact': contact})


def header_create(request):
    if request.method == 'POST':
        form = HeaderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('header_list')
    else:
        form = HeaderForm()
        return render(request, 'admin/header_create.html', {'form': form})


def header_list(request):
    header = Header.objects.all()
    print(header)
    return render(request, 'admin/header_list.html', {'header': header})


def header_update(request, pk):
    header = get_object_or_404(Header, id=pk)
    if request.method == 'POST':
        form = HeaderForm(request.POST, instance=header)
        if form.is_valid():
            form.save()
            return redirect('header_list')
    else:
        form = HeaderForm(instance=header)
    return render(request, 'admin/header_update.html', {'form': form, 'header': header})


def header_delete(request, pk):
    header = get_object_or_404(Header, id=pk)

    if request.method == 'POST':
        header.delete()
        return redirect('header_list')
    return render(request, 'admin/header_delete.html', {'header': header})


def menu_create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm()
        return render(request, 'admin/menu_create.html', {'form': form})


def menu_list(request):
    menu = Menu.objects.all()
    return render(request, 'admin/menu_list.html', {'menu': menu})


def menu_update(request, pk):
    menu = get_object_or_404(Menu, id=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'admin/menu_update.html', {'form': form, 'menu': menu})


def menu_delete(request, pk):
    menu = get_object_or_404(Menu, id=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('menu_list')
    return render(request, 'admin/menu_delete.html', {'menu': menu})


def banner_create(request):
    if request.method == 'POST':
        form = BannerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('banner_list')
    else:
        form = BannerForm()
    return render(request, 'admin/banner_create.html', {'form': form})


def banner_list(request):
    banners = Banner.objects.all()
    return render(request, 'admin/banner_list.html', {'banners': banners})


def banner_update(request, pk):
    banner = get_object_or_404(Banner, id=pk)
    if request.method == 'POST':
        form = BannerForm(request.POST, instance=banner)
        if form.is_valid():
            form.save()
            return redirect('banner_list')
    else:
        form = BannerForm(instance=banner)

    return render(request, 'admin/banner_update.html', {'form': form, 'banner': banner})


def banner_delete(request, pk):
    banner = get_object_or_404(Banner, id=pk)
    if request.method == 'POST':
        banner.delete()
        return redirect('banner_list')

    return render(request, 'admin/banner_delete.html', {'banner': banner})


def carousel_create(request):
    if request.method == 'POST':
        form = CarouselForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carousel_list')
    else:
        form = CarouselForm()

    return render(request, 'admin/carousel_create.html', {'form': form})


def carousel_list(request):
    carousels = Carousel.objects.all()
    return render(request, 'admin/carousel_list.html', {'carousels': carousels})


def carousel_update(request, pk):
    carousel = get_object_or_404(Carousel, id=pk)
    if request.method == 'POST':
        form = CarouselForm(request.POST, instance=carousel)
        if form.is_valid():
            form.save()
            return redirect('carousel_list')
    else:
        form = CarouselForm(instance=carousel)

    return render(request, 'admin/carousel_update.html', {'form': form, 'carousel': carousel})


def carousel_delete(request, pk):
    carousel = get_object_or_404(Carousel, id=pk)
    if request.method == 'POST':
        carousel.delete()
        return redirect('carousel_list')

    return render(request, 'admin/carousel_delete.html', {'carousel': carousel})


def meeting_create(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meeting_list')
    else:
        form = MeetingForm()

    return render(request, 'admin/meeting_create.html', {'form': form})


def meeting_list(request):
    meetings = Meeting.objects.all()
    return render(request, 'admin/meeting_list.html', {'meetings': meetings})


def meeting_update(request, pk):
    meeting = get_object_or_404(Meeting, id=pk)

    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('meeting_list')
    else:
        form = MeetingForm(instance=meeting)

    return render(request, 'admin/meeting_update.html', {'form': form, 'meeting': meeting})


def meeting_delete(request, pk):
    meeting = get_object_or_404(Meeting, id=pk)

    if request.method == 'POST':
        meeting.delete()
        return redirect('meeting_list')

    return render(request, 'admin/meeting_delete.html', {'meeting': meeting})


def middle_create(request):
    if request.method == 'POST':
        form = MiddleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('middle_list')
    else:
        form = MiddleForm()
    return render(request, 'admin/middle_create.html', {'form': form})


def middle_list(request):
    middle_objects = Middle.objects.all()
    return render(request, 'admin/middle_list.html', {'middle_objects': middle_objects})


def middle_update(request, pk):
    middle = Middle.objects.get(id=pk)
    if request.method == 'POST':
        form = MiddleForm(request.POST, instance=middle)
        if form.is_valid():
            form.save()
            return redirect('middle_list')
    else:
        form = MiddleForm(instance=middle)
    return render(request, 'admin/middle_update.html', {'form': form})


def middle_delete(request, pk):
    middle = get_object_or_404(Middle, id=pk)
    if request.method == 'POST':
        middle.delete()
        return redirect('middle_list')
    return render(request, 'admin/middle_delete.html', {'middle': middle})


def popular_create(request):
    if request.method == 'POST':
        form = PopularForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('popular_list')
    else:
        form = PopularForm()  # Пустая форма при GET-запросе
    return render(request, 'admin/popular_create.html', {'form': form})


def popular_list(request):
    popular = Popular.objects.all()
    return render(request, 'admin/popular_list.html', {'popular': popular})


def popular_update(request, pk):
    popular = Popular.objects.get(id=pk)
    if request.method == 'POST':
        form = PopularForm(request.POST, instance=popular)
        if form.is_valid():
            form.save()
            return redirect('popular_list')
    else:
        form = PopularForm(instance=popular)
    return render(request, 'admin/popular_update.html', {'form': form})


def popular_delete(request, pk):
    popular = get_object_or_404(Popular, id=pk)
    if request.method == 'POST':
        popular.delete()
        return redirect('popular_list')
    return render(request, 'admin/popular_delete.html', {'popular': popular})


def fact_create(request):
    if request.method == 'POST':
        form = FactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fact_list')
    else:
        form = FactForm()

    return render(request, 'admin/fact_create.html', {'form': form})


def fact_list(request):
    facts = Fact.objects.all()
    return render(request, 'admin/fact_list.html', {'facts': facts})


def fact_update(request, pk):
    fact = get_object_or_404(Fact, id=pk)
    if request.method == 'POST':
        form = FactForm(request.POST, instance=fact)
        if form.is_valid():
            form.save()
            return redirect('fact_list')
    else:
        form = FactForm(instance=fact)

    return render(request, 'admin/fact_update.html', {'form': form, 'fact': fact})


def fact_delete(request, pk):
    fact = get_object_or_404(Fact, id=pk)
    if request.method == 'POST':
        fact.delete()
        return redirect('fact_list')

    return render(request, 'admin/fact_delete.html', {'fact': fact})


def touch_create(request):
    if request.method == 'POST':
        form = TouchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('touch_list')
    else:
        form = TouchForm()
    return render(request, 'admin/touch_create.html', {'form': form})


def touch_list(request):
    touches = Touch.objects.all()
    return render(request, 'admin/touch_list.html', {'touches': touches})


def touch_update(request, pk):
    touch = get_object_or_404(Touch, id=pk)
    if request.method == 'POST':
        form = TouchForm(request.POST, instance=touch)
        if form.is_valid():
            form.save()
            return redirect('touch_list')
    else:
        form = TouchForm(instance=touch)
    return render(request, 'admin/touch_update.html', {'form': form, 'touch': touch})


def touch_delete(request, pk):
    touch = get_object_or_404(Touch, id=pk)
    if request.method == 'POST':
        touch.delete()
        return redirect('touch_list')
    return render(request, 'admin/touch_delete.html', {'touch': touch})


def end_create(request):
    if request.method == 'POST':
        form = EndForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('end_list')
    else:
        form = EndForm()
    return render(request, 'admin/end_create.html', {'form': form})


def end_list(request):
    ends = End.objects.all()
    return render(request, 'admin/end_list.html', {'ends': ends})


def end_update(request, pk):
    end = get_object_or_404(End, id=pk)
    if request.method == 'POST':
        form = EndForm(request.POST, instance=end)
        if form.is_valid():
            form.save()
            return redirect('end_list')
    else:
        form = EndForm(instance=end)
    return render(request, 'admin/end_update.html', {'form': form, 'end': end})


def end_delete(request, pk):
    end = get_object_or_404(End, id=pk)
    if request.method == 'POST':
        end.delete()
        return redirect('end_list')
    return render(request, 'admin/end_delete.html', {'end': end})


def middlefirst_create(request):
    if request.method == 'POST':
        form = MiddleFirstForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('middlefirst_list')
    else:
        form = MiddleFirstForm()
    return render(request, 'admin/middlefirst_create.html', {'form': form})


def middlefirst_list(request):
    middlefirsts = MiddleFirst.objects.all()
    return render(request, 'admin/middlefirst_list.html', {'middlefirsts': middlefirsts})


def middlefirst_update(request, pk):
    middlefirst = get_object_or_404(MiddleFirst, id=pk)
    if request.method == 'POST':
        form = MiddleFirstForm(request.POST, instance=middlefirst)
        if form.is_valid():
            form.save()
            return redirect('middlefirst_list')
    else:
        form = MiddleFirstForm(instance=middlefirst)
    return render(request, 'admin/middlefirst_update.html', {'form': form, 'middlefirst': middlefirst})


def middlefirst_delete(request, pk):
    middlefirst = get_object_or_404(MiddleFirst, id=pk)
    if request.method == 'POST':
        middlefirst.delete()
        return redirect('middlefirst_list')
    return render(request, 'admin/middlefirst_delete.html', {'middlefirst': middlefirst})


def middlesecond_create(request):
    if request.method == 'POST':
        form = MiddleSecondForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('middlesecond_list')
    else:
        form = MiddleSecondForm()
    return render(request, 'admin/middlesecond_create.html', {'form': form})


def middlesecond_list(request):
    middleseconds = MiddleSecond.objects.all()
    return render(request, 'admin/middlesecond_list.html', {'middleseconds': middleseconds})


def middlesecond_update(request, pk):
    middlesecond = get_object_or_404(MiddleSecond, id=pk)
    if request.method == 'POST':
        form = MiddleSecondForm(request.POST, instance=middlesecond)
        if form.is_valid():
            form.save()
            return redirect('middlesecond_list')
    else:
        form = MiddleSecondForm(instance=middlesecond)
    return render(request, 'admin/middlesecond_update.html', {'form': form, 'middlesecond': middlesecond})


def middlesecond_delete(request, pk):
    middlesecond = get_object_or_404(MiddleSecond, id=pk)
    if request.method == 'POST':
        middlesecond.delete()
        return redirect('middlesecond_list')
    return render(request, 'admin/middlesecond_delete.html', {'middlesecond': middlesecond})


def last_create(request):
    if request.method == 'POST':
        form = LastForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('last_list')
    else:
        form = LastForm()
    return render(request, 'admin/last_create.html', {'form': form})


def last_list(request):
    lasts = Last.objects.all()
    return render(request, 'admin/last_list.html', {'lasts': lasts})


def last_update(request, pk):
    last = get_object_or_404(Last, id=pk)
    if request.method == 'POST':
        form = LastForm(request.POST, instance=last)
        if form.is_valid():
            form.save()
            return redirect('last_list')
    else:
        form = LastForm(instance=last)
    return render(request, 'admin/last_update.html', {'form': form, 'last': last})


def last_delete(request, pk):
    last = get_object_or_404(Last, id=pk)
    if request.method == 'POST':
        last.delete()
        return redirect('last_list')
    return render(request, 'admin/last_delete.html', {'last': last})


def detail_create(request):
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail_list')
    else:
        form = DetailForm()
    return render(request, 'admin/detail_create.html', {'form': form})


def detail_list(request):
    details = Detail.objects.all()
    return render(request, 'admin/detail_list.html', {'details': details})


def detail_update(request, pk):
    detail = get_object_or_404(Detail, id=pk)
    if request.method == 'POST':
        form = DetailForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect('detail_list')
    else:
        form = DetailForm(instance=detail)
    return render(request, 'admin/detail_update.html', {'form': form, 'detail': detail})


def detail_delete(request, pk):
    detail = get_object_or_404(Detail, id=pk)
    if request.method == 'POST':
        detail.delete()
        return redirect('detail_list')
    return render(request, 'admin/detail_delete.html', {'detail': detail})


def about_create(request):
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about_list')
    else:
        form = AboutForm()
    return render(request, 'admin/about_create.html', {'form': form})


def about_list(request):
    abouts = About.objects.all()
    return render(request, 'admin/about_list.html', {'abouts': abouts})


def about_update(request, pk):
    about = get_object_or_404(About, id=pk)
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            return redirect('about_list')
    else:
        form = AboutForm(instance=about)
    return render(request, 'admin/about_update.html', {'form': form, 'about': about})


def about_delete(request, pk):
    about = get_object_or_404(About, id=pk)
    if request.method == 'POST':
        about.delete()
        return redirect('about_list')
    return render(request, 'admin/about_delete.html', {'about': about})


# API
class HeaderListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get all Header items",
        responses={200: HeaderSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        headers = Header.objects.all()
        serializer = HeaderSerializer(headers, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Header item",
        request_body=HeaderSerializer,
        responses={201: HeaderSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        serializer = HeaderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HeaderDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Header item",
        request_body=HeaderSerializer,
        responses={200: HeaderSerializer(many=True)},
    )
    def put(self, request, *args, **kwargs):
        try:
            header = Header.objects.get(id=kwargs['pk'])
        except Header.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HeaderSerializer(header, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Header item",
        request_body=HeaderSerializer,
        responses={200: HeaderSerializer(many=True)},
    )
    def patch(self, request, *args, **kwargs):
        try:
            header = Header.objects.get(id=kwargs['pk'])
        except Header.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = HeaderSerializer(header, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Header item",
        responses={204: 'No Content'},
    )
    def delete(self, request, *args, **kwargs):
        try:
            header = Header.objects.get(id=kwargs['pk'])
        except Header.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        header.delete()  # Удаляем объект
        return Response(status=status.HTTP_204_NO_CONTENT)



class MenuListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get all Menu items",
        responses={200: MenuSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Menu item",
        request_body=MenuSerializer,
        responses={201: MenuSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Menu item",
        request_body=MenuSerializer,
        responses={200: MenuSerializer(many=True)},
    )
    def put(self, request, *args, **kwargs):
        try:
            menu = Menu.objects.get(id=kwargs['pk'])
        except Menu.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Menu item",
        request_body=MenuSerializer,
        responses={200: MenuSerializer(many=True)},
    )
    def patch(self, request, *args, **kwargs):
        try:
            menu = Menu.objects.get(id=kwargs['pk'])
        except Menu.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = MenuSerializer(menu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Menu item",
        responses={204: 'No Content'},
    )
    def delete(self, request, *args, **kwargs):
        try:
            menu = Menu.objects.get(id=kwargs['pk'])
        except Menu.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ContactListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get all Contact items",
        responses={200: ContactSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Contact item",
        request_body=ContactSerializer,
        responses={201: ContactSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetailAPIView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(
        operation_description="Update a Contact item",
        request_body=ContactSerializer,
        responses={200: ContactSerializer(many=True)},
    )
    def put(self, request, *args, **kwargs):
        try:
            contact = Contact.objects.get(id=kwargs['pk'])
        except Contact.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Contact item",
        request_body=ContactSerializer,
        responses={200: ContactSerializer(many=True)},
    )
    def patch(self, request, *args, **kwargs):
        try:
            contact = Contact.objects.get(id=kwargs['pk'])
        except Contact.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Contact item",
        responses={204: 'No Content'},
    )
    def delete(self, request, *args, **kwargs):
        try:
            contact = Contact.objects.get(id=kwargs['pk'])
        except Contact.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class BannerListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получить все баннеры",
        responses={200: BannerSerializer(many=True)},  # Ответ с сериализатором для списка баннеров
    )
    def get(self, request, *args, **kwargs):
        banners = Banner.objects.all()
        serializer = BannerSerializer(banners, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создать новый баннер",
        request_body=BannerSerializer,
        responses={201: BannerSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        serializer = BannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BannerDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Обновить баннер",
        request_body=BannerSerializer,
        responses={200: BannerSerializer(many=True)},
    )
    def put(self, request, *args, **kwargs):
        try:
            banner = Banner.objects.get(id=kwargs['pk'])
        except Banner.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BannerSerializer(banner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Частичное обновление баннера",
        request_body=BannerSerializer,
        responses={200: BannerSerializer(many=True)},
    )
    def patch(self, request, *args, **kwargs):
        try:
            banner = Banner.objects.get(id=kwargs['pk'])
        except Banner.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = BannerSerializer(banner, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удалить баннер",
        responses={204: 'No Content'},
    )
    def delete(self, request, *args, **kwargs):
        try:
            banner = Banner.objects.get(id=kwargs['pk'])
        except Banner.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        banner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarouselListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получить все элементы Carousel",
        responses={200: CarouselSerializer(many=True)},  # Ответ с сериализатором для списка каруселей
    )
    def get(self, request, *args, **kwargs):
        carousels = Carousel.objects.all()
        serializer = CarouselSerializer(carousels, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создать новый элемент Carousel",
        request_body=CarouselSerializer,
        responses={201: CarouselSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        serializer = CarouselSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarouselDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Обновить элемент Carousel",
        request_body=CarouselSerializer,
        responses={200: CarouselSerializer(many=True)},
    )
    def put(self, request, *args, **kwargs):
        try:
            carousel = Carousel.objects.get(id=kwargs['pk'])
        except Carousel.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarouselSerializer(carousel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Частичное обновление элемента Carousel",
        request_body=CarouselSerializer,
        responses={200: CarouselSerializer(many=True)},
    )
    def patch(self, request, *args, **kwargs):
        try:
            carousel = Carousel.objects.get(id=kwargs['pk'])
        except Carousel.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarouselSerializer(carousel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удалить элемент Carousel",
        responses={204: 'No Content'},
    )
    def delete(self, request, *args, **kwargs):
        try:
            carousel = Carousel.objects.get(id=kwargs['pk'])
        except Carousel.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        carousel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MeetingListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получить все элементы Meeting",
        responses={200: MeetingSerializer(many=True)},  # Ответ с сериализатором для списка встреч
    )
    def get(self, request, *args, **kwargs):
        meetings = Meeting.objects.all()
        serializer = MeetingSerializer(meetings, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создать новый элемент Meeting",
        request_body=MeetingSerializer,
        responses={201: MeetingSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeetingDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Обновить элемент Meeting",
        request_body=MeetingSerializer,
        responses={200: MeetingSerializer(many=True)},
    )
    def put(self, request, *args, **kwargs):
        try:
            meeting = Meeting.objects.get(id=kwargs['pk'])
        except Meeting.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MeetingSerializer(meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Частичное обновление элемента Meeting",
        request_body=MeetingSerializer,
        responses={200: MeetingSerializer(many=True)},
    )
    def patch(self, request, *args, **kwargs):
        try:
            meeting = Meeting.objects.get(id=kwargs['pk'])
        except Meeting.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MeetingSerializer(meeting, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удалить элемент Meeting",
        responses={204: 'No Content'},
    )
    def delete(self, request, *args, **kwargs):
        try:
            meeting = Meeting.objects.get(id=kwargs['pk'])
        except Meeting.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MiddleListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get all Middle items",
        responses={200: MiddleSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        middle = Middle.objects.all()
        serializer = MiddleSerializer(middle, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Middle item",
        request_body=MiddleSerializer,
        responses={201: MiddleSerializer(many=True)}
    )
    def post(self, request, *args, **kwargs):
        serializer = MiddleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MiddleDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Middle item",
        request_body=MiddleSerializer,
        responses={200: MiddleSerializer(many=True)}
    )
    def put(self, request, *args, **kwargs):
        try:
            middle = Middle.objects.get(id=kwargs['pk'])
        except Middle.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MiddleSerializer(middle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Middle item",
        request_body=MiddleSerializer,
        responses={200: MiddleSerializer(many=True)}
    )
    def patch(self, request, *args, **kwargs):
        try:
            middle = Middle.objects.get(id=kwargs['pk'])
        except Middle.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MiddleSerializer(middle, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Middle item",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        try:
            middle = Middle.objects.get(id=kwargs['pk'])
        except Middle.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        middle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AboutListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get all About items",
        responses={200: AboutSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        about = About.objects.all()
        serializer = AboutSerializer(about, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new About item",
        request_body=AboutSerializer,
        responses={201: AboutSerializer(many=True)}
    )
    def post(self, request, *args, **kwargs):
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AboutDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update an About item",
        request_body=AboutSerializer,
        responses={200: AboutSerializer(many=True)}
    )
    def put(self, request, *args, **kwargs):
        try:
            about = About.objects.get(id=kwargs['pk'])
        except About.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AboutSerializer(about, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update an About item",
        request_body=AboutSerializer,
        responses={200: AboutSerializer(many=True)}
    )
    def patch(self, request, *args, **kwargs):
        try:
            about = About.objects.get(id=kwargs['pk'])
        except About.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AboutSerializer(about, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description="Delete an About item",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        try:
            about = About.objects.get(id=kwargs['pk'])
        except About.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        about.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PopularListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get all Popular items",
        responses={200: PopularSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        popular_items = Popular.objects.all()
        serializer = PopularSerializer(popular_items, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Popular item",
        request_body=PopularSerializer,
        responses={201: PopularSerializer(many=True)}
    )
    def post(self, request, *args, **kwargs):
        serializer = PopularSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PopularDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Popular item",
        request_body=PopularSerializer,
        responses={200: PopularSerializer(many=True)}
    )
    def put(self, request, *args, **kwargs):
        try:
            popular_item = Popular.objects.get(id=kwargs['pk'])
        except Popular.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PopularSerializer(popular_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Popular item",
        request_body=PopularSerializer,
        responses={200: PopularSerializer(many=True)}
    )
    def patch(self, request, *args, **kwargs):
        try:
            popular_item = Popular.objects.get(id=kwargs['pk'])
        except Popular.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PopularSerializer(popular_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Popular item",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        try:
            popular_item = Popular.objects.get(id=kwargs['pk'])
        except Popular.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        popular_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FactListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get all Fact items",
        responses={200: FactSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        facts = Fact.objects.all()
        serializer = FactSerializer(facts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Fact item",
        request_body=FactSerializer,
        responses={201: FactSerializer(many=True)}
    )
    def post(self, request, *args, **kwargs):
        serializer = FactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FactDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Fact item",
        request_body=FactSerializer,
        responses={200: FactSerializer(many=True)}
    )
    def put(self, request, *args, **kwargs):
        try:
            fact = Fact.objects.get(id=kwargs['pk'])
        except Fact.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = FactSerializer(fact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Fact item",
        request_body=FactSerializer,
        responses={200: FactSerializer(many=True)}
    )
    def patch(self, request, *args, **kwargs):
        try:
            fact = Fact.objects.get(id=kwargs['pk'])
        except Fact.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = FactSerializer(fact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Fact item",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        try:
            fact = Fact.objects.get(id=kwargs['pk'])
        except Fact.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        fact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TouchListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get all Touch items",
        responses={200: TouchSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        touches = Touch.objects.all()
        serializer = TouchSerializer(touches, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Touch item",
        request_body=TouchSerializer,
        responses={201: TouchSerializer(many=True)}
    )
    def post(self, request, *args, **kwargs):
        serializer = TouchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TouchDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Touch item",
        request_body=TouchSerializer,
        responses={200: TouchSerializer(many=True)}
    )
    def put(self, request, *args, **kwargs):
        try:
            touch = Touch.objects.get(id=kwargs['pk'])
        except Touch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TouchSerializer(touch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Touch item",
        request_body=TouchSerializer,
        responses={200: TouchSerializer(many=True)}
    )
    def patch(self, request, *args, **kwargs):
        try:
            touch = Touch.objects.get(id=kwargs['pk'])
        except Touch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TouchSerializer(touch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Touch item",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        try:
            touch = Touch.objects.get(id=kwargs['pk'])
        except Touch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        touch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EndListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get all End items",
        responses={200: EndSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        ends = End.objects.all()
        serializer = EndSerializer(ends, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new End item",
        request_body=EndSerializer,
        responses={201: EndSerializer(many=True)}
    )
    def post(self, request, *args, **kwargs):
        serializer = EndSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EndDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update an End item",
        request_body=EndSerializer,
        responses={200: EndSerializer(many=True)}
    )
    def put(self, request, *args, **kwargs):
        try:
            end = End.objects.get(id=kwargs['pk'])
        except End.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = EndSerializer(end, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update an End item",
        request_body=EndSerializer,
        responses={200: EndSerializer(many=True)}
    )
    def patch(self, request, *args, **kwargs):
        try:
            end = End.objects.get(id=kwargs['pk'])
        except End.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = EndSerializer(end, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete an End item",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        try:
            end = End.objects.get(id=kwargs['pk'])
        except End.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        end.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MiddleFirstListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get all MiddleFirst items",
        responses={200: MiddleFirstSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        middlefirsts = MiddleFirst.objects.all()
        serializer = MiddleFirstSerializer(middlefirsts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new MiddleFirst item",
        request_body=MiddleFirstSerializer,
        responses={201: MiddleFirstSerializer(many=True)}
    )
    def post(self, request, *args, **kwargs):
        serializer = MiddleFirstSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MiddleFirstDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a MiddleFirst item",
        request_body=MiddleFirstSerializer,
        responses={200: MiddleFirstSerializer(many=True)}
    )
    def put(self, request, *args, **kwargs):
        try:
            middlefirst = MiddleFirst.objects.get(id=kwargs['pk'])
        except MiddleFirst.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MiddleFirstSerializer(middlefirst, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a MiddleFirst item",
        request_body=MiddleFirstSerializer,
        responses={200: MiddleFirstSerializer(many=True)}
    )
    def patch(self, request, *args, **kwargs):
        try:
            middlefirst = MiddleFirst.objects.get(id=kwargs['pk'])
        except MiddleFirst.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MiddleFirstSerializer(middlefirst, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a MiddleFirst item",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        try:
            middlefirst = MiddleFirst.objects.get(id=kwargs['pk'])
        except MiddleFirst.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        middlefirst.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MiddleSecondListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get all MiddleSecond items",
        responses={200: MiddleSecondSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        middleseconds = MiddleSecond.objects.all()
        serializer = MiddleSecondSerializer(middleseconds, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new MiddleSecond item",
        request_body=MiddleSecondSerializer,
        responses={201: MiddleSecondSerializer(many=True)}
    )
    def post(self, request, *args, **kwargs):
        serializer = MiddleSecondSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MiddleSecondDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a MiddleSecond item",
        request_body=MiddleSecondSerializer,
        responses={200: MiddleSecondSerializer(many=True)}
    )
    def put(self, request, *args, **kwargs):
        try:
            middlesecond = MiddleSecond.objects.get(id=kwargs['pk'])
        except MiddleSecond.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MiddleSecondSerializer(middlesecond, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a MiddleSecond item",
        request_body=MiddleSecondSerializer,
        responses={200: MiddleSecondSerializer(many=True)}
    )
    def patch(self, request, *args, **kwargs):
        try:
            middlesecond = MiddleSecond.objects.get(id=kwargs['pk'])
        except MiddleSecond.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MiddleSecondSerializer(middlesecond, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a MiddleSecond item",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        try:
            middlesecond = MiddleSecond.objects.get(id=kwargs['pk'])
        except MiddleSecond.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        middlesecond.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class LastListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get all Last items",
        responses={200: LastSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        lasts = Last.objects.all()
        serializer = LastSerializer(lasts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Last item",
        request_body=LastSerializer,
        responses={201: LastSerializer(many=True)}
    )
    def post(self, request, *args, **kwargs):
        serializer = LastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LastDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Last item",
        request_body=LastSerializer,
        responses={200: LastSerializer(many=True)}
    )
    def put(self, request, *args, **kwargs):
        try:
            last = Last.objects.get(id=kwargs['pk'])
        except Last.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = LastSerializer(last, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Last item",
        request_body=LastSerializer,
        responses={200: LastSerializer(many=True)}
    )
    def patch(self, request, *args, **kwargs):
        try:
            last = Last.objects.get(id=kwargs['pk'])
        except Last.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = LastSerializer(last, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Last item",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        try:
            last = Last.objects.get(id=kwargs['pk'])
        except Last.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        last.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DetailListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Get all Detail items",
        responses={200: DetailSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        details = Detail.objects.all()
        serializer = DetailSerializer(details, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Detail item",
        request_body=DetailSerializer,
        responses={201: DetailSerializer(many=True)}
    )
    def post(self, request, *args, **kwargs):
        serializer = DetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Detail item",
        request_body=DetailSerializer,
        responses={200: DetailSerializer(many=True)}
    )
    def put(self, request, *args, **kwargs):
        try:
            detail = Detail.objects.get(id=kwargs['pk'])
        except Detail.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DetailSerializer(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Detail item",
        request_body=DetailSerializer,
        responses={200: DetailSerializer(many=True)}
    )
    def patch(self, request, *args, **kwargs):
        try:
            detail = Detail.objects.get(id=kwargs['pk'])
        except Detail.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DetailSerializer(detail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Detail item",
        responses={204: 'No Content'}
    )
    def delete(self, request, *args, **kwargs):
        try:
            detail = Detail.objects.get(id=kwargs['pk'])
        except Detail.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)