from django.urls import path,include, reverse_lazy
from missing_app import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.utils.translation import gettext_lazy



urlpatterns=[
path('home/',views.Home_page,name="Home_Page"),
path('sign_up/',views.Sign_up_page,name="sign_up_Page"),
path('login/',views.Login_page,name="Login_Page"),
path('found/',views.Found_page,name="Found_Page"),
path('found1/',views.Found1_page,name="Found1_Page"),
path('lost/',views.Lost_page,name="Lost_Page"),
path('profile/',views.Profile_page,name='Profile_Page'),
path('change_password/',auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('password_change_done')),name = "Change_Password"),
path('change_password/done/',auth_views.PasswordChangeDoneView.as_view(title = gettext_lazy('Password changed successfully. Please quit the browser and login again to continue. Thank You!')),name="password_change_done"),
path('contact/',views.Contact_page,name='Contact_Page'),
path('logout/',views.User_logout,name='Logout'),
path('test/',views.Test_page,name='Test_Page'),


]
