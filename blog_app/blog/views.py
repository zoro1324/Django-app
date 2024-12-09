from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse
import logging
from django.core.paginator import Paginator
from .models import Post,Catagory


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
    blog_title='Latest posts'

    paginator = Paginator(all_posts,6)
    page_no = request.GET.get("page")
    page_obj = paginator.get_page(page_no)

    return render(request,"blog/index.html",{"blog_title":blog_title,"page_obj":page_obj,"Catagories":catagories})

def detail(request,slug):
    #post=next((item for item in posts if item["id"] == int(post_id)),None)
    #logger=logging.getLogger("TESTING")
    try:

        post=Post.objects.get(slugs=slug)
        related_posts = Post.objects.filter(catagory_id=post.catagory_id).exclude(pk= post.catagory_id)

    except Post.DoesNotExist:
        raise Http404("Post Does not found")

    #logger.debug(f"The log is {post}")
    return render(request,"blog/detail.html",{"post":post,"related_posts":related_posts,"Catagories":catagories})

def old_url_redirect(request):
    return redirect(reverse("blog:new_url"))

def new_url_redirect(request):
    return HttpResponse("Redirected url")