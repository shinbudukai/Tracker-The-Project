from django.urls import path,include
from . import views
from Fityfeed import views as efitty
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',efitty.home,name='home'),
    path('user/',efitty.userPage,name='userPage'), #userPage
    path('product/',efitty.fooditem,name='fooditem'),
    path('createfooditem/',efitty.createfooditem,name='createfooditem'),
    path('register/',efitty.registerPage,name='register'),
    path('login/',efitty.loginPage,name='login'),
    path('logout/',efitty.logoutUser,name='logout'),
    path('addFooditem/',efitty.addFooditem,name='addFooditem'),
     path('reset_password/',
         auth_views.PasswordResetView.as_view(),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
]