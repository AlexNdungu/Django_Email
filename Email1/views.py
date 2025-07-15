from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Home.html')

def send_email(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(subject)
        print(message)