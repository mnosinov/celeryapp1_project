from django.urls import path
from celeryapp.views import IndexView, SayHelloView, SendEmailView, \
        GetLast2minsTaskResultView, AuthView, AddView

urlpatterns = [
    path('', IndexView.as_view()),
    path('hello', SayHelloView.as_view(), name='sayhello'),
    path('sendemail', SendEmailView.as_view(), name='sendemail'),
    path('last2minstaskresult', GetLast2minsTaskResultView.as_view(),
         name='last2minstaskresult'),
    path('authenticate', AuthView.as_view(), name='authenticate'),
    path('add', AddView.as_view(), name='add'),
]
