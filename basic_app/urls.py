from django.urls import path
from . import views


# Template tagging
app_name = 'basic_app' # important for url mapping.

urlpatterns = [
    path('', views.index, name='index'),
    path('relative/', views.relative, name='relative'), #  http://127.0.0.1:8000/basic_app/relative
    path('other/', views.other, name='other') #  http://127.0.0.1:8000/basic_app/other
]