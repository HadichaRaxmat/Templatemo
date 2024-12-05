from django.urls import path
from .views import (home_view, meetings_view, meeting_details_view, HeaderCreateApiView,
                    BannerCreateApiView, CarouselCreateApiView, MeetingCreateApiView,
                    MiddleCreateApiView, AboutCreateApiView, PopularCreateApiView, FactCreateApiView,
                    TouchCreateApiView, EndCreateApiView, MiddleSecondCreateApiView, MiddleFirstCreateApiView,
                    LastCreateApiView, DetailCreateApiView, header_create, header_update, header_list,
                    header_delete, banner_list, banner_create, banner_update, banner_delete, carousel_create,
                    carousel_list, carousel_update, carousel_delete, meeting_create, meeting_list, meeting_update,
                    meeting_delete, middle_create, middle_delete, middle_list, middle_update, popular_delete,
                    popular_list, popular_create, popular_update, fact_create, fact_update, fact_delete, fact_list,
                    touch_create, touch_delete, touch_list, touch_update, end_create, end_list, end_delete, end_update,
                    middlefirst_create, middlefirst_delete, middlefirst_update, middlefirst_list, middlesecond_create,
                    middlesecond_list, middlesecond_delete, middlesecond_update, last_list, last_delete,
                    last_update, last_create, detail_update, detail_create, detail_list, detail_delete, about_update,
                    about_list, about_delete, about_create, dashboard2_view, dashboard3_view, iframe_view,
                    contact_create, contact_delete, contact_update, contact_view, contact_list, contact_list_view,
                    user_contact_update, user_contact_delete)


urlpatterns = [

    # HTML
    path('', home_view),
    path('dashboard2/', dashboard2_view),
    path('dashboard3', dashboard3_view),
    path('iframe/', iframe_view),
    path('meetings/', meetings_view),
    path('meeting/details', meeting_details_view),
    path('contact/', contact_view, name='contact'),
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
    path('api/header/', HeaderCreateApiView.as_view(), name='header-create'), # create
    path('api/header/<int:header_id>/', HeaderCreateApiView.as_view(), name='header-update'), #update
    path('api/banner/', BannerCreateApiView.as_view(), name='banner-create'),  # create
    path('api/banner/<int:banner_id>/', BannerCreateApiView.as_view(), name='banner-update'),#update
    path('api/carousel/', CarouselCreateApiView.as_view(), name='carousel-create'),  # create
    path('api/carousel/<int:carousel_id>/', CarouselCreateApiView.as_view(), name='carousel-update'), #update
    path('api/meeting/', MeetingCreateApiView.as_view(), name='meeting-create'),  # create
    path('api/meeting/<int:meeting_id>/', MeetingCreateApiView.as_view(), name='meeting-update'), #update
    path('api/middle/', MiddleCreateApiView.as_view(), name='middle-create'),  # create
    path('api/middle/<int:middle_id>/', MiddleCreateApiView.as_view(), name='middle-update'), #update
    path('api/about/', AboutCreateApiView.as_view(), name='about-create'),  # create
    path('api/about/<int:about_id>/', AboutCreateApiView.as_view(), name='about-update'), #update
    path('api/popular/', PopularCreateApiView.as_view(), name='popular-create'),   # create
    path('api/popular/<int:popular_id>/', PopularCreateApiView.as_view(), name='popular-update'), #update
    path('api/fact/', FactCreateApiView.as_view(), name='fact-create'),  # create
    path('api/fact/<int:fact_id>/', FactCreateApiView.as_view(), name='fact-update'), #update
    path('api/touch/', TouchCreateApiView.as_view(), name='touch-create'),  # create
    path('api/touch/<int:touch_id>/', TouchCreateApiView.as_view(), name='touch-update'), #update
    path('api/end/', EndCreateApiView.as_view(), name='end-create'),    # create
    path('api/end/<int:end_id>/', EndCreateApiView.as_view(), name='end-update'), #update

    # middle api
    path('api/first/', MiddleFirstCreateApiView.as_view(), name='first-create'),  # create
    path('api/first/<int:first_id>/', MiddleFirstCreateApiView.as_view(), name='first-update'), #update
    path('api/second/', MiddleSecondCreateApiView.as_view(), name='second-create'),  # create
    path('api/second/<int:second_id>/', MiddleSecondCreateApiView.as_view(), name='second-update'), #update

    # Last api
    path('api/last/', LastCreateApiView.as_view(), name='last-create'),  # create
    path('api/last/<int:last_id>/', LastCreateApiView.as_view(), name='last-update'), #update
    path('api/detail/', DetailCreateApiView.as_view(), name='detail-create'),  # create
    path('api/detail/<int:last_id>/', DetailCreateApiView.as_view(), name='detail-update'), #update
]