from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('',views.index,name="index"),
    path('post/<str:slug>',views.detail,name="detail"),
    path("old_url/",views.old_url_redirect,name="old_url"),
    path("new_url/",views.new_url_redirect,name="new_url"),
    path('contact/',views.contact,name="contact"),
    path('aboutus/',views.about,name='about_us')
]