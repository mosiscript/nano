from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote_plus
from django.utils import timezone
from django.db.models import Q

from .models import Post
from .forms import PostForm
import datetime

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    # if not request.user.is_authenticated():
    #     raise Http404
    form = PostForm(request.POST or None, request.FILES or None )
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, " Successfully Created ")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form' : form,
    }
    return render(request, "posts/post_form.html", context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    share_string = quote_plus(instance.content)
    context = {
        'title' : instance.title ,
        'instance' : instance,
        'share_string' : share_string,

    }
    return render(request, "posts/post_detail.html", context)

def post_list(request):
    queryset_list = Post.objects.filter(draft=False) #.filter(publish__lte=timezone.now())     #.all() # .order_by("-timestamp")

    query = request.GET.get("query")
    if query:
        # queryset_list = queryset_list.filter(title__icontains=query)
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
            ).distinct() # for avoid of duplicate search

    paginator = Paginator(queryset_list, 2)
    page_request_var = "page"
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        'object_list' : queryset ,
        'title' : 'List',
        'page_request_var' : page_request_var
    }
    return render(request, "posts/post_list.html", context)



def post_update(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, " Item Saved ", extra_tags='alert-success')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title' : instance.title ,
        'instance' : instance,
        'form' : form,
    }
    return render(request, 'posts/post_form.html', context)

def post_delete(request, id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, " Successfully Deleted ")
    return redirect("posts:post_list")
