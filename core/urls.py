from django.contrib import admin
from django.urls import path
from .views import (
    HomeView,
    AboutView,
    ServicesView,
    ServiceDetailView,
    BlogView,
    BlogDetailView,
    ContactView,
    CareerView,
    ApplyView,
    PrivacyView,
    ReviewsView,
    RequestQuoteApiView,
    Subscribe,
    robots
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about-us/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('services/<slug:slug>/', ServiceDetailView.as_view(), name='service_detail'),
    path('blog/', BlogView.as_view(), name='blogs'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('career/', CareerView.as_view(), name='career'),
    path('apply/', ApplyView.as_view(), name='apply'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('reviews/', ReviewsView.as_view(), name='reviews'),
    path('api/request/', RequestQuoteApiView.as_view(), name='request'),
    path('subscribe/',Subscribe,name="subscribe"),
    path('robots.txt', robots, name='robots'),
    
]