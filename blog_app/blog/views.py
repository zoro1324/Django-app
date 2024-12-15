from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse
import logging
from django.core.paginator import Paginator
from .models import Post,Catagory,AboutUS
from .forms import ContactDetail,RegisterForms
from django.contrib import messages

# Create your views here.
#posts=[
#        {"id":1,"title":"Post-1","content":"Content of post 1"},
#       {"id":2,"title":"Post-2","content":"Content of post 2"},
#       {"id":3,"title":"Post-3","content":"Content of post 3"},
#       {"id":4,"title":"Post-4","content":"Content of post 4"},
#   ]

all_posts= Post.objects.all()
catagories = Catagory.objects.all()


def index(request):
    title='Latest posts'

    paginator = Paginator(all_posts,6)
    page_no = request.GET.get("page")
    page_obj = paginator.get_page(page_no)

    return render(request,"blog/index.html",{"title":title,"page_obj":page_obj,"Catagories":catagories})

def detail(request,slug):
    #post=next((item for item in posts if item["id"] == int(post_id)),None)
    
    try:

        post=Post.objects.get(slugs=slug)
        related_posts = Post.objects.filter(catagory_id=post.catagory_id).exclude(pk= post.catagory_id)

    except Post.DoesNotExist:
        raise Http404("Post Does not found")

    
    return render(request,"blog/detail.html",{"post":post,"related_posts":related_posts,"Catagories":catagories})

def old_url_redirect(request):
    return redirect(reverse("blog:new_url"))

def new_url_redirect(request):
    return HttpResponse("Redirected url")

def contact(request):
    form = ContactDetail()
    if request.method == 'POST':
        form = ContactDetail(request.POST)
        if form.is_valid():
            messages.success(request,"Your responce has been recorded")
            #logger=logging.getLogger("TESTING")
            #logger.debug(f"name = {form.cleaned_data['name']} email = {form.cleaned_data['email']} message = {form.cleaned_data['message']}")
    return render(request,"blog/contact.html",{'title':'Contact us','form':form})

def about(request):
    about_content = AboutUS.objects.first()
    if about_content is None or not about_content.content:
        about_content = "This content is currently unavailable"
    else:
        about_content = about_content.content
    return render(request,"blog/about.html",{'about_content':about_content,'title':'About us'})

def register(request):
    form = RegisterForms()
    if request.method == 'POST':
        form = RegisterForms(request.POST)
        if form.is_valid():
            user_data=form.save(commit=False)
            user_data.set_password(form.cleaned_data['password'])
            user_data.save()
            success_message = "You have sucessfully registered!"
            messages.success(request,"You have successfully registered!")
    return render(request,"blog/register.html",{'form':form,'title':'Register'})