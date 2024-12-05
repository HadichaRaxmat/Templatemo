from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from .models import (Header, Banner, Carousel, Meeting, Middle, About, Popular, Fact, Touch, End, MiddleFirst,
                     MiddleSecond, Last, Detail, Contact, UserContact)
from .serializers import (HeaderSerializer, ContactSerializer, BannerSerializer, CarouselSerializer,
                          MeetingSerializer, MiddleSerializer, AboutSerializer, PopularSerializer,
                          FactSerializer, TouchSerializer, EndSerializer, MiddleFirstSerializer,
                          MiddleSecondSerializer, LastSerializer, DetailSerializer)
from rest_framework.response import Response
from rest_framework import status
from .forms import (HeaderForm, BannerForm, CarouselForm, MeetingForm, MiddleForm, AboutForm, PopularForm, FactForm,
                    TouchForm, EndForm, MiddleFirstForm, MiddleSecondForm, LastForm, DetailForm, ContactForm,
                    UserContactForm)


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
        'end': end
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
        form = ContactForm(instance=user_contact)
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
class ApiContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeaderCreateApiView(APIView):
    def get_object(self, header_id):
        try:
            return Header.objects.get(id=header_id)
        except Header.DoesNotExist:
            raise Http404("Header not found")

    def get(self, **kwargs):
        header_id = kwargs.get('header_id')
        header = self.get_object(header_id)
        serializer = HeaderSerializer(header)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = HeaderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        header_id = kwargs.get('header_id')
        header = self.get_object(header_id)
        serializer = HeaderSerializer(header, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        header_id = kwargs.get('header_id')
        header = self.get_object(header_id)
        serializer = HeaderSerializer(header, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        header_id = kwargs.get('header_id')
        header = self.get_object(header_id)
        header.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BannerCreateApiView(APIView):
    def get_object(self, banner_id):
        try:
            return Banner.objects.get(id=banner_id)
        except Banner.DoesNotExist:
            raise Http404("Not found")

    def get(self, **kwargs):
        banner_id = kwargs.get('banner_id')
        banner = self.get_object(banner_id)
        serializer = BannerSerializer(banner)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        banner_id = kwargs.get('banner_id')
        banner = self.get_object(banner_id)
        serializer = BannerSerializer(banner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        banner_id = kwargs.get('banner_id')
        banner = self.get_object(banner_id)
        serializer = BannerSerializer(banner, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        banner_id = kwargs.get('banner_id')
        banner = self.get_object(banner_id)
        banner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarouselCreateApiView(APIView):
    def get_object(self, carousel_id):
        try:
            return Carousel.objects.get(id=carousel_id)
        except Carousel.DoesNotExist:
            raise Http404("Not found")

    def get(self, **kwargs):
        carousel_id = kwargs.get('carousel_id')
        carousel = self.get_object(carousel_id)
        serializer = CarouselSerializer(carousel)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CarouselSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        carousel_id = kwargs.get('carousel_id')
        carousel = self.get_object(carousel_id)
        serializer = CarouselSerializer(carousel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        carousel_id = kwargs.get('carousel_id')
        carousel = self.get_object(carousel_id)
        serializer = CarouselSerializer(carousel, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        carousel_id = kwargs.get('carousel_id')
        carousel = self.get_object(carousel_id)
        carousel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MeetingCreateApiView(APIView):
    def get_object(self, meeting_id):
        try:
            return Meeting.objects.get(id=meeting_id)
        except Meeting.DoesNotExist:
            raise Http404("Not found")

    def get(self, **kwargs):
        meeting_id = kwargs.get('meeting_id')
        meeting = self.get_object(meeting_id)
        serializer = CarouselSerializer(meeting)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        meeting_id = kwargs.get('meeting_id')
        meeting = self.get_object(meeting_id)
        serializer = MeetingSerializer(meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        meeting_id = kwargs.get('meeting_id')
        meeting = self.get_object(meeting_id)
        serializer = MeetingSerializer(meeting, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        meeting_id = kwargs.get('meeting_id')
        meeting = self.get_object(meeting_id)
        meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MiddleCreateApiView(APIView):
    def get_object(self, middle_id):
        try:
            return Middle.objects.get(id=middle_id)
        except Middle.DoesNotExist:
            raise Http404("Not found")

    def get(self, **kwargs):
        middle_id = kwargs.get('middle_id')
        meeting = self.get_object(middle_id)
        serializer = MiddleSerializer(meeting)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MiddleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        middle_id = kwargs.get('middle_id')
        middle = self.get_object(middle_id)
        serializer = MiddleSerializer(middle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        middle_id = kwargs.get('middle_id')
        middle = self.get_object(middle_id)
        serializer = MiddleSerializer(middle, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        middle_id = kwargs.get('middle_id')
        middle = self.get_object(middle_id)
        middle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AboutCreateApiView(APIView):
    def get_object(self, about_id):
        try:
            return About.objects.get(id=about_id)
        except About.DoesNotExist:
            raise Http404("Not found")

    def get(self, **kwargs):
        about_id = kwargs.get('about_id')
        about = self.get_object(about_id)
        serializer = AboutSerializer(about)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        about_id = kwargs.get('about_id')
        about = self.get_object(about_id)
        serializer = AboutSerializer(about, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        about_id = kwargs.get('about_id')
        about = self.get_object(about_id)
        serializer = AboutSerializer(about, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        about_id = kwargs.get('about_id')
        about = self.get_object(about_id)
        about.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PopularCreateApiView(APIView):
    def get_object(self, popular_id):
        try:
            return Popular.objects.get(id=popular_id)
        except Popular.DoesNotExist:
            raise Http404("Not found")

    def get(self, **kwargs):
        popular_id = kwargs.get('popular_id')
        popular = self.get_object(popular_id)
        serializer = PopularSerializer(popular)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PopularSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        popular_id = kwargs.get('popular_id')
        popular = self.get_object(popular_id)
        serializer = PopularSerializer(popular, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        popular_id = kwargs.get('popular_id')
        popular = self.get_object(popular_id)
        serializer = PopularSerializer(popular, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        popular_id = kwargs.get('popular_id')
        popular = self.get_object(popular_id)
        popular.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FactCreateApiView(APIView):
    def get_object(self, fact_id):
        try:
            return Fact.objects.get(id=fact_id)
        except Fact.DoesNotExist:
            raise Http404("Not found")

    def get(self, **kwargs):
        fact_id = kwargs.get('fact_id')
        fact = self.get_object(fact_id)
        serializer = FactSerializer(fact)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        fact_id = kwargs.get('fact_id')
        fact = self.get_object(fact_id)
        serializer = FactSerializer(fact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        fact_id = kwargs.get('fact_id')
        fact = self.get_object(fact_id)
        serializer = FactSerializer(fact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        fact_id = kwargs.get('fact_id')
        fact = self.get_object(fact_id)
        fact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TouchCreateApiView(APIView):
    def get_object(self, touch_id):
        try:
            return Touch.objects.get(id=touch_id)
        except Touch.DoesNotExist:
            raise Http404("Not found")

    def get(self, **kwargs):
        touch_id = kwargs.get('touch_id')
        touch = self.get_object(touch_id)
        serializer = TouchSerializer(touch)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TouchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        touch_id = kwargs.get('touch_id')
        touch = self.get_object(touch_id)
        serializer = TouchSerializer(touch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        touch_id = kwargs.get('touch_id')
        touch = self.get_object(touch_id)
        serializer = TouchSerializer(touch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        touch_id = kwargs.get('touch_id')
        touch = self.get_object(touch_id)
        touch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EndCreateApiView(APIView):
    def get_object(self, end_id):
        try:
            return End.objects.get(id=end_id)
        except End.DoesNotExist:
            raise Http404("Not found")

    def get(self, **kwargs):
        end_id = kwargs.get('end_id')
        end = self.get_object(end_id)
        serializer = EndSerializer(end)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EndSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        end_id = kwargs.get('end_id')
        end = self.get_object(end_id)
        serializer = EndSerializer(end, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        end_id = kwargs.get('end_id')
        end = self.get_object(end_id)
        serializer = EndSerializer(end, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        end_id = kwargs.get('end_id')
        end = self.get_object(end_id)
        end.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# middle view

class MiddleFirstCreateApiView(APIView):
    def get_object(self, first_id):
        try:
            return MiddleFirst.objects.get(id=first_id)
        except MiddleFirst.DoesNotExist:
            raise Http404("Not found")

    def get(self, **kwargs):
        first_id = kwargs.get('first_id')
        first = self.get_object(first_id)
        serializer = MiddleFirstSerializer(first)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MiddleFirstSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        first_id = kwargs.get('first_id')
        first = self.get_object(first_id)
        serializer = MiddleFirstSerializer(first, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        first_id = kwargs.get('first_id')
        first = self.get_object(first_id)
        serializer = MiddleFirstSerializer(first, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        first_id = kwargs.get('first_id')
        first = self.get_object(first_id)
        first.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MiddleSecondCreateApiView(APIView):
    def get_object(self, first_id):
        try:
            return MiddleSecond.objects.get(id=first_id)
        except MiddleSecond.DoesNotExist:
            raise Http404("Not found")

    def get(self, **kwargs):
        second_id = kwargs.get('second_id')
        second = self.get_object(second_id)
        serializer = MiddleFirstSerializer(second)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MiddleSecondSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        second_id = kwargs.get('second_id')
        second = self.get_object(second_id)
        serializer = MiddleSecondSerializer(second, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        second_id = kwargs.get('second_id')
        second = self.get_object(second_id)
        serializer = MiddleSecondSerializer(second, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        second_id = kwargs.get('second_id')
        second = self.get_object(second_id)
        second.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Last View

class LastCreateApiView(APIView):
    def get_object(self, last_id):
        try:
            return Last.objects.get(id=last_id)
        except Last.DoesNotExist:
            raise Http404("Not found")

    def get(self, **kwargs):
        last_id = kwargs.get('last_id')
        last = self.get_object(last_id)
        serializer = LastSerializer(last)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        last_id = kwargs.get('last_id')
        last = self.get_object(last_id)
        serializer = LastSerializer(last, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        last_id = kwargs.get('last__id')
        last = self.get_object(last_id)
        serializer = LastSerializer(last, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        last_id = kwargs.get('last_id')
        last = self.get_object(last_id)
        last.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DetailCreateApiView(APIView):
    def get_object(self, detail_id):
        try:
            return Detail.objects.get(id=detail_id)
        except Detail.DoesNotExist:
            raise Http404("Not found")

    def get(self, **kwargs):
        detail_id = kwargs.get('detail_id')
        detail = self.get_object(detail_id)
        serializer = DetailSerializer(detail)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        detail_id = kwargs.get('detail_id')
        detail = self.get_object(detail_id)
        serializer = DetailSerializer(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, **kwargs):
        detail_id = kwargs.get('detail_id')
        detail = self.get_object(detail_id)
        serializer = DetailSerializer(detail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        detail_id = kwargs.get('detail_id')
        detail = self.get_object(detail_id)
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)