from .views import ComposeEmail
from django.urls import path


urlpatterns = [
    path('sendmail/', ComposeEmail.as_view(), name='send_mail'),
]
