from django.shortcuts import render

def coustom_errorpage(request,exception):
    return render(request,"404.html",status=404)