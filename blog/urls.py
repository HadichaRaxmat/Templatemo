from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import (home_view, meetings_view, meeting_details_view, header_create, header_update, header_list,
                    header_delete, menu_delete, menu_create, menu_update, menu_list, banner_list, banner_create,
                    banner_update, banner_delete, carousel_create, login_view, signup_view,
                    carousel_list, carousel_update, carousel_delete, meeting_create, meeting_list, meeting_update,
                    meeting_delete, meeting_header_create, meeting_header_delete, meeting_header_list,
                    meeting_header_update, user_update, user_delete, users_list, logout_view,
                    middle_create, middle_delete, middle_list, middle_update, popular_delete,
                    popular_list, popular_create, popular_update, fact_create, fact_update, fact_delete, fact_list,
                    touch_create, touch_delete, touch_list, touch_update, end_create, end_list, end_delete, end_update,
                    middlefirst_create, middlefirst_delete, middlefirst_update, middlefirst_list, middlesecond_create,
                    middlesecond_list, middlesecond_delete, middlesecond_update, last_list, last_delete,
                    last_update, last_create, detail_update, detail_create, detail_list, detail_delete, about_update,
                    about_list, about_delete, about_create, dashboard2_view, dashboard3_view, iframe_view,
                    contact_create, contact_delete, contact_update, contact_view, contact_list, contact_list_view,
                    user_contact_update, user_contact_delete, HeaderListAPIView, HeaderDetailAPIView, admin_logout,
                    ContactListAPIView, ContactDetailAPIView, BannerListAPIView, BannerDetailAPIView,
                    CarouselListAPIView, CarouselDetailAPIView, MeetingListAPIView, MeetingDetailAPIView, admin_create,
                    MiddleListAPIView, MiddleDetailAPIView, AboutDetailAPIView, AboutListAPIView, PopularListAPIView,
                    PopularDetailAPIView, FactDetailAPIView,FactListAPIView, TouchDetailAPIView, TouchListAPIView,
                    EndDetailAPIView, EndListAPIView, MiddleFirstDetailAPIView, MiddleFirstListAPIView, admin_list, admin_delete,
                    MiddleSecondListAPIView, MiddleSecondDetailAPIView, LastDetailAPIView, LastListAPIView, admin_update,
                    DetailListAPIView, DetailDetailAPIView, MenuDetailAPIView, MenuListAPIView, admin_view)


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Документация API для вашего проекта",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your.email@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # HTML
    path('', home_view),
    path('dashboard/', admin_view, name='dashboard'),
    path('dashboard2/', dashboard2_view),
    path('dashboard3', dashboard3_view),
    path('iframe/', iframe_view),
    path('meetings/', meetings_view),
    path('meeting/details', meeting_details_view),
    path('contact/', contact_view, name='contact'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    #admin
    path('admin/list/', admin_list, name='admin_list'),
    path('admin/create/', admin_create, name='admin_create'),
    path('admin/update/<int:user_id>/', admin_update, name='admin_update'),
    path('admin/delete/<int:user_id>/', admin_delete, name='admin_delete'),
    path('admin/logout/', admin_logout, name='admin_logout'),
    #user
    path('users/', users_list, name='users'),
    path('user/update/<int:pk>/', user_update, name='user_update'),
    path('user/delete/<int:pk>/', user_delete, name='user_delete'),
    #user contact
    path('user/contact/list/', contact_list_view, name='user_contact_list'),
    path('user/contact/update/<int:pk>/', user_contact_update, name='user_contact_update'),
    path('user/contact/delete/<int:pk>/', user_contact_delete, name='user_contact_delete'),
    #contact
    path('contact/create/', contact_create, name='contact_create'),
    path('contact/list/', contact_list, name='contact_list'),
    path('contact/update/<int:pk>/', contact_update, name='contact_update'),
    path('contact/delete/<int:pk>/', contact_delete, name='contact_delete'),
    # Header
    path('header/create/', header_create, name='header_create'), #create
    path('header/list/', header_list, name='header_list'), # Header list
    path('header/update/<int:pk>/', header_update, name='header_update'), #update
    path('header/delete/<int:pk>/', header_delete, name='header_delete'), #delete
    #menu
    path('menu/create/', menu_create, name='menu_create'), #create
    path('menu/list/', menu_list, name='menu_list'), # Header list
    path('menu/update/<int:pk>/', menu_update, name='menu_update'), #update
    path('menu/delete/<int:pk>/', menu_delete, name='menu_delete'), #delete
    # Banner
    path('banner/create/', banner_create, name='banner_create'), #create
    path('banner/list/', banner_list, name='banner_list'), #list
    path('banner/update/<int:pk>/', banner_update, name='banner_update'), # update
    path('banner/delete/<int:pk>/', banner_delete, name='banner_delete'), # delete
    # Carousel
    path('carousel/create/', carousel_create, name='carousel_create'),
    path('carousel/list/', carousel_list, name='carousel_list'),
    path('carousel/update/<int:pk>/', carousel_update, name='carousel_update'),
    path('carousel/delete/<int:pk>/', carousel_delete, name='carousel_delete'),
    # Meeting
    path('meeting/create/', meeting_create, name='meeting_create'),
    path('meeting/list/', meeting_list, name='meeting_list'),
    path('meeting/update/<int:pk>/', meeting_update, name='meeting_update'),
    path('meeting/delete/<int:pk>/', meeting_delete, name='meeting_delete'),
    #meeting header
    path('meeting/header/create/', meeting_header_create, name='meeting_header_create'),
    path('meeting/header/list/', meeting_header_list, name='meeting_header_list'),
    path('meeting/header/update/<int:pk>/', meeting_header_update, name='meeting_header_update'),
    path('meeting/header/delete/<int:pk>/', meeting_header_delete, name='meeting_header_delete'),
    #middle
    path('middle/create/', middle_create, name='middle_create'),
    path('middle/list/', middle_list, name='middle_list'),
    path('middle/update/<int:pk>/', middle_update, name='middle_update'),
    path('middle/delete/<int:pk>/', middle_delete, name='middle_delete'),
    #popular
    path('popular/create/', popular_create, name='popular_create'),
    path('popular/list/', popular_list, name='popular_list'),
    path('popular/update/<int:pk>/', popular_update, name='popular_update'),
    path('popular/delete/<int:pk>/', popular_delete, name='popular_delete'),
    #fact
    path('fact/create/', fact_create, name='fact_create'),
    path('create/list/', fact_list, name='fact_list'),
    path('fact/update/<int:pk>/', fact_update, name='fact_update'),
    path('fact/delete/<int:pk>/', fact_delete, name='fact_delete'),
    #touch
    path('touch/create/', touch_create, name='touch_create'),
    path('touch/list/', touch_list, name='touch_list'),
    path('touch/update/<int:pk>/', touch_update, name='touch_update'),
    path('touch/delete/<int:pk>/', touch_delete, name='touch_delete'),
    #end
    path('end/create/', end_create, name='end_create'),
    path('end/list/', end_list, name='end_list'),
    path('end/update/<int:pk>/', end_update, name='end_update'),
    path('end/delete/<int:pk>/', end_delete, name='end_delete'),
    #middlefirst
    path('middlefirst/create/', middlefirst_create, name='middlefirst_create'),
    path('middlefirst/list/', middlefirst_list, name='middlefirst_list'),
    path('middlefirst/update/<int:pk>/', middlefirst_update, name='middlefirst_update'),
    path('middlefirst/delete/<int:pk>/', middlefirst_delete, name='middlefirst_delete'),
    #middlesecond
    path('middlesecond/create/', middlesecond_create, name='middlesecond_create'),
    path('middlesecond/list/', middlesecond_list, name='middlesecond_list'),
    path('middlesecond/update/<int:pk>/', middlesecond_update, name='middlesecond_update'),
    path('middlesecond/delete/<int:pk>/', middlesecond_delete, name='middlesecond_delete'),
    #last
    path('last/create/', last_create, name='last_create'),
    path('last/list/', last_list, name='last_list'),
    path('last/update/<int:pk>/', last_update, name='last_update'),
    path('last/delete/<int:pk>/', last_delete, name='last_delete'),
    #detail
    path('detail/create/', detail_create, name='detail_create'),
    path('detail/list/', detail_list, name='detail_list'),
    path('detail/update/<int:pk>/', detail_update, name='detail_update'),
    path('detail/delete/<int:pk>/', detail_delete, name='detail_delete'),
    #about
    path('about/create/', about_create, name='about_create'),
    path('about/list/', about_list, name='about_list'),
    path('about/update/<int:pk>/', about_update, name='about_update'),
    path('about/delete/<int:pk>/', about_delete, name='about_delete'),



    # API
    re_path(r'^swagger(?P<format>\.json|\.yml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('header/', HeaderListAPIView.as_view(), name='header-list'), #header list
    path('header/<int:pk>/', HeaderDetailAPIView.as_view(), name='header-detail'), #header detail
    path('contact/', ContactListAPIView.as_view(), name='contact-list'), #contact list
    path('contact/<int:pk>/', ContactDetailAPIView.as_view(), name='contact-detail'), #contact detail
    path('banner/', BannerListAPIView.as_view(), name='banner-list'), #banner list
    path('banner/<int:pk>/', BannerDetailAPIView.as_view(), name='banner-detail'), #banner detail
    path('carousel/', CarouselListAPIView.as_view(), name='carousel-list'), #carousel list
    path('carousel/<int:pk>/', CarouselDetailAPIView.as_view(), name='carousel-detail'), #carousel detail
    path('meeting/', MeetingListAPIView.as_view(), name='meeting-list'), #meeting list
    path('meeting/<int:pk>/', MeetingDetailAPIView.as_view(), name='meeting-detail'), #meeting detail
    path('middle/', MiddleListAPIView.as_view(), name='middle-list'),# middle list
    path('middle/<int:pk>/', MiddleDetailAPIView.as_view(), name='middle-detail'), #middle detail
    path('about/', AboutListAPIView.as_view(), name='about-list'), #about list
    path('about/<int:pk>/', AboutDetailAPIView.as_view(), name='about-detail'), #about detail
    path('popular/', PopularListAPIView.as_view(), name='popular-list'), #popular list
    path('popular/<int:pk>/', PopularDetailAPIView.as_view(), name='popular-detail'), #popular detail
    path('fact/', FactListAPIView.as_view(), name='fact-list'),
    path('fact/<int:pk>/', FactDetailAPIView.as_view(), name='fact-detail'),
    path('touch/', TouchListAPIView.as_view(), name='touch-list'),
    path('touch/<int:pk>/', TouchDetailAPIView.as_view(), name='touch-detail'),
    path('end/', EndListAPIView.as_view(), name='end-list'),
    path('end/<int:pk>/', EndDetailAPIView.as_view(), name='end-detail'),
    path('middlefirst/', MiddleFirstListAPIView.as_view(), name='middlefirst-list'),
    path('middlefirst/<int:pk>/', MiddleFirstDetailAPIView.as_view(), name='middlefirst-detail'),
    path('middlesecond/', MiddleSecondListAPIView.as_view(), name='middlesecond-list'),
    path('middlesecond/<int:pk>/', MiddleSecondDetailAPIView.as_view(), name='middlesecond-detail'),
    path('last/', LastListAPIView.as_view(), name='last-list'),
    path('last/<int:pk>/', LastDetailAPIView.as_view(), name='last-detail'),
    path('detail/', DetailListAPIView.as_view(), name='detail-list'),
    path('detail/<int:pk>/', DetailDetailAPIView.as_view(), name='detail-detail'),
    path('menu/', MenuListAPIView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', MenuDetailAPIView.as_view(), name='menu-detail'),
]







