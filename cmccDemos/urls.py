from django.urls import path

from . import views

urlpatterns = [
    path('blog/', cmccDemos.views.blog, name='blog'),
]