from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from aero.models import Contact

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message, date = datetime.today())
        contact.save()
        return render(request, "base.html")
    else:
        return render(request, "base.html")