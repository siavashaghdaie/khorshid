from django.contrib import admin
from django.urls import path
from cafe import urls
from cafe import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
    path('profileupdate/<str:pk>/', views.userProfileUpdate, name='profileupdate'),
    path('profiledelet/<str:pk>/', views.profileDelete, name='profiledelete'),
    path('menu/', views.menu, name='menu'),
    path('shop/', views.shop, name='shop'),
    path('product/<str:pk>/', views.product, name='product'),
    path('product_delete/<str:pk>/', views.product_delete, name='product_delete'),
    path('product_modify/<str:pk>/', views.product_modify, name='product_modify'),
    path('product_add/', views.product_add, name='product_add'),
    path('artist_add/', views.artist_add, name='artist_add'),
    path('artwork_add/', views.artwork_add, name='artwork_add'),
    path('modify/<str:pk>/', views.modify, name='modify'),
    path('factor/<str:pk>/', views.factor, name='factor'),
    path('sms/<str:pk>/', views.sms, name='sms'),
    path('payment/<str:pk>/', views.payment, name='payment'),
    path('mafia/', views.mafia, name='mafia'),
    path('gallery/', views.gallery, name='gallery'),
    path('artist/', views.artist, name='artist'),
    path('artwork/', views.artwork, name='artwork'),
    path('contact/', views.contact, name='contact'),
    path('social/', views.social, name='social'),
    path('events/', views.events, name='events'),
    
]