from django.shortcuts import render

# Create your views here.

def aboutUs(req):
    return render(req,'about_us/index.html')