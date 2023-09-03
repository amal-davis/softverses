from django.urls import path
from  sofapp import views
from  django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('terms_and_condition',views.terms_and_condition,name='terms_and_condition'),
    path('about_us',views.about_us,name='about_us'),
    path('service',views.service,name='service'),
    path('technology',views.technology,name='technology'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('web_services',views.web_services,name='web_services'),
    path('digiatl_marketing',views.digiatl_marketing,name='digiatl_marketing'),
    path('branding',views.branding,name='branding'),
    path('contact_details',views.contact_details,name='contact_details'),
]