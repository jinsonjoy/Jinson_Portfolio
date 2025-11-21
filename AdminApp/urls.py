from django.urls import path
from AdminApp import views
# from AdminApp.views import send_email_view

urlpatterns = [
    path('index_page/',views.index_page,name="index_page"),
    # path('send-email/', send_email_view, name='send_email'),

]