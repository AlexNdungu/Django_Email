import os
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from smtplib import SMTPException
from dotenv import load_dotenv

load_dotenv()

# Create your views here.

def home(request):
    return render(request,'Home.html')

def send_email(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(subject)
        print(message)
        try:
            result = send_mail(
                subject=subject,
                message=message,
                from_email= os.environ["EMAIL_HOST_USER"],
                recipient_list=['alexmeta517@gmail.com'],
                fail_silently=False,
            )

            if result == 1:
                return JsonResponse({'status': 'success', 'message': 'Email sent successfully'})
            else:
                return JsonResponse({'status': 'failed', 'message': 'Email not sent'})

        except SMTPException as e:
            return JsonResponse({'status': 'error', 'message': f'SMTP error: {str(e)}'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Unexpected error: {str(e)}'})