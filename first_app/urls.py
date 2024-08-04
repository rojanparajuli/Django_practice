from django.urls import path

from first_app.views import home

app_namee = 'first_name'

urlpatterns = [
    path('', home, name='home'),
]