from django.urls import path

from . import views

urlpatterns = [
    path('blog/', cmccDemos.views.blog, name='blog'),
    path('contact/', cmccDemos.views.contact, name='contact'),
    path('products/', cmccDemos.views.products, name='products'),
]