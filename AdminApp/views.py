from django.shortcuts import render, redirect


# Create your views here.

def index_page(request):
    return render(request,"Index_Page.html")




