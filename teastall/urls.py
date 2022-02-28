from django.contrib import admin
from django.urls import path
from teastall import views


urlpatterns = [
    path('',views.index),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('menu/',views.menu,name='menu'),
    path('userlogout/',views.userlogout),
    #path('userlogout1/',views.userlogout1),
    path('addtocart/',views.addtocart,name='addtocart'),
    path('payment/',views.payment,name='payment'),
    path('updateprofile/',views.updateprofile,name='updateprofile'),
    path('suggestion/',views.suggestion,name='suggestion'),
    path('viewscart/',views.viewscart,name='viewscart'),
    path('details/',views.details,name='details'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.userlogin,name='login'),
    path('condelete/<int:id>',views.condelete,name='condelete'),
    path('paydelete/<int:id>',views.paydelete,name='paydelete'),
    path('sugdelete/<int:id>',views.sugdelete,name='sugdelete'),
]