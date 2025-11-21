from django.shortcuts import render, redirect


# Create your views here.

def index_page(request):
    return render(request,"index.html")

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
import os

from django.http import JsonResponse

def send_email_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"""
You received a new contact form message:

Name: {name}
Email: {email}

Message:
{message}
"""

        try:
            send_mail(
                subject,
                full_message,
                os.environ.get("EMAIL_HOST_USER"),
                [os.environ.get("EMAIL_RECEIVER")],
                fail_silently=False,
            )
            return JsonResponse({"status": "success", "message": "Thank you for contacting us!"})
        except Exception:
            return JsonResponse({"status": "error", "message": "Email failed to send!"})

    return JsonResponse({"status": "error", "message": "Invalid request"})


