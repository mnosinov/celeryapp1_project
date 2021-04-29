from django.urls import path
from celeryapp.views import IndexView, SayHelloView, SendEmailView

urlpatterns = [
    path('', IndexView.as_view()),
    path('hello', SayHelloView.as_view(), name='sayhello'),
    path('sendemail', SendEmailView.as_view(), name='sendemail'),
    path('last2minstaskresult', SendEmailView.as_view(), name='last2minstaskresult'),
]
