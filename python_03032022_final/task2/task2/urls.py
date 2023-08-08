from django.contrib import admin
from django.urls import path
from it_digi import views
# from task2 import views
# from parking import views as ca
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('lg/', views.loginpage, name="loginpage"),
    path('rg/', views.register, name="registrationpage"),
    path('pg/', views.python, name="pythonpage"),
    path('jg/', views.java, name="javapage"),
    path('cg/', views.c, name="cpage"),
    path('ac/', views.ac, name="addcarpage"),
    path('book/', views.book, name="bookcargo"),
    path('fetch/', views.fetch, name='fetch'),
    path('car/', views.car),
    path('sh/', views.show, name="search"),

]