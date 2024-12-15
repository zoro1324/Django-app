from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('blog/',views.index,name="index"),
    path('post/<str:slug>',views.detail,name="detail"),
    path("old_url/",views.old_url_redirect,name="old_url"),
    path("new_url/",views.new_url_redirect,name="new_url"),
    path('contact/',views.contact,name="contact"),
    path('aboutus/',views.about,name='about_us'),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logout,name="logout"),
    path('forget_password/',views.forget_password,name="forget_password"),

]