from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

def home(request):
    subject="project mail"
    message="about project"
    from_email="jyotiade287@gmail.com"
    recipient_list=["himanshimate9@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)

    return HttpResponse("done......")

