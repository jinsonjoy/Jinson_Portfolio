from django.urls import path
from AdminApp import views

urlpatterns = [
    path('',views.index_page,name="index_page"),

]