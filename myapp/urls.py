from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('shop/',views.shop,name='shop'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
   
]