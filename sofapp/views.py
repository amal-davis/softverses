import select
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from .models import *
import random
import string

# Create your views here.

def homepage(request):
    return render(request,'home.html')


def terms_and_condition(request):
    return render(request,'terms.html')


def about_us(request):
    return render(request,'about.html')


def service(request):
    return render(request,'service.html')


def technology(request):
    return render(request,'technology.html')


def blog(request):
    return render(request,'blog.html')


def contact(request):
    return render(request,'contact.html')


def web_services(request):
    return render(request,'webservice.html')


def digiatl_marketing(request):
    return render(request,'digital_marketing.html')


def branding(request):
    return render(request,'branding.html') 


def contact_details(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        messaage_email = request.POST['email']
        message = request.POST['comments']
        message_phnnum = request.POST['phone']

        send_mail(
         'message from'+ message_name, # Subject
         message + '\n from email:' + messaage_email + '\n Phone Number:' + message_phnnum, # Message
         messaage_email, # From email
         ['akhilakd5299@gmail.com']   # To email
        )
        mail = Contact_details(name=message_name,phone_no=message_phnnum,email=messaage_email,message=message)
        mail.save()

        success_message = "We will get back to you soon."
        return render(request,'contact.html',{'message_name':message_name,'success_message': success_message})
    else:
       return redirect('contact')

