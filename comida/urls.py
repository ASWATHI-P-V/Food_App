from django.urls import path
from comida import views



urlpatterns = [
	path('',views.index),
	path('contact/',views.register),
	path('index/',views.register),
	path('login/',views.login),
	path('logout/',views.logout),
	path('adminlogin/',views.adminlogin),
	path('addproduct/',views.addproduct),
	path('userlist/',views.userlist),
	path('adminindex/',views.adminindex),



]