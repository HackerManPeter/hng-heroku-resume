from django.http import response
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'resume/home.html')

def send_gmail(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        form_subject = request.POST.get('subject')
        message = request.POST.get('message')
        # print(name, subject, email, message)

        subject = f'[Django Resume]-{form_subject}'
        message += f'\n\nName:\t{name.title()}\nEmail:\t{email}\nPhone:\t{phone}'
        send_mail(
            subject,
            message,
            'pebueku.test@gmail.com',
            ['pebueku@gmail.com']
            
        )


        reply_subject = 'Thanks for reaching out!'
        reply_message = f'Good day {name.title()},\nThank you for reaching out, I\'ll be sure to get back to you soon.'

        send_mail(
            reply_subject,
            reply_message,
            'pebueku.test@gmail.com',
            [email]

        )


        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponse('Invalid request')