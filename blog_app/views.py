from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Post
from .forms import CategoryForm, PostForm
import json


def index(request):
    categories = Category.objects.all()
    return render(request, "craigslist_app/index.html", {"categories": categories})

def get_categories(request):
    categories = Category.objects.all()
    return render(request, "craigslist_app/index.html", {"categories": categories})
    
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'craigslist_app/category_new.html', {"form": form})

def get_category(request, id):
    try:
        posts = Post.objects.filter(category=id)
        category = Category.objects.get(id=id)
        data = {"posts": posts, "category": category}
    except:
        raise Http404("Hello, World! This category does not exist.")
    return render(request, "craigslist_app/category.html", data) 

def update_category(request, id):
    category = Category.objects.get(pk=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm(instance=category)
    return render(request, "craigslist_app/category_edit.html", {'form': form})

def delete_category(request, id):
    try:
        category = Category.objects.get(id=id)

        if request.method == 'POST':
            category.delete()
            return redirect('index')        
        
        return render(request, "craigslist_app/category_delete.html", {'category': category})

    except:
        return HttpResponse({"Category deletion:", False})

def get_posts(request):
    pass 

def create_post(request, id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'craigslist_app/post_new.html', {"form": form})

def get_post(request, id, post_id):
    try:
        post = Post.objects.get(category=id, id=post_id)
        category = Category.objects.get(id=id)
        data = {"post": post, "category": category}

    except:
        raise Http404("Hello, World! This post does not exist.")

    return render(request, "craigslist_app/post.html", data) 

def update_post(request, id, post_id):
    post = Post.objects.get(category=id, pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('get_post', id, post_id)

    else:
        form = PostForm(instance=post)
    return render(request, "craigslist_app/post_edit.html", {'form': form})

def delete_post(request, id, post_id):
    try:
        post = Post.objects.get(category_id=id, pk=post_id)
        category = Category.objects.get(id=id)
        data = {"post": post, "category": category}
        
        if request.method == 'POST':
            post.delete()
            return redirect('index')
        return render(request, "craigslist_app/post_delete.html", data)

    except Exception as e:
        return HttpResponse(f"Post deletion failed: {e}")
     




############ API ############

@csrf_exempt
def categories_API(request):
    if request.method == 'POST':
        user_request = request.body
        json_request = json.loads(user_request)
        name = json_request['name']
        category = Category(name=name)
        category.full_clean()
        category.save()
        category = Category.objects.get(name=name)
        response = serializers.serialize("json", [category])
        return HttpResponse(response)

    elif request.method == 'GET':
        categories = Category.objects.all()
        response = serializers.serialize("json", categories)
        return HttpResponse(response)

    return HttpResponse({"Category request success:": False})

@csrf_exempt
def category_API(request, id): 
    if request.method == "PUT":
        user_request = request.body
        json_request = json.loads(user_request)
        name = json_request['name']
        category = Category.objects.filter(id=id).update(name=name)
        category = Category.objects.get(name=name)
        response = serializers.serialize("json", [category])
        return HttpResponse(response)

    elif request.method == "GET":
        category = Category.objects.get(id=id)
        response = serializers.serialize("json", [category])
        return HttpResponse(response)

    elif request.method == "DELETE":
        try:
            category = Category.objects.get(id=id)
            category.delete()
            return HttpResponse({"Category deletion:", True })
        except:
            return HttpResponse({"Category deletion:", False })

    else:
        return HttpResponse({"Category_ID request success:": False})

@csrf_exempt
def posts_API(request):
    if request.method == "POST":
        user_request = request.body
        json_request = json.loads(user_request)
        category = json_request['category']
        title = json_request['title']
        description = json_request['description']
        post = Post(category_id=category, title=title, description=description)
        post.full_clean()
        post.save()
        response = serializers.serialize("json", [post])
        return HttpResponse(response)

    elif request.method == "GET":
        id = request.GET.get('id')
        if id == None:
            posts = Post.objects.all()
            response = serializers.serialize("json", posts)
            return HttpResponse(response)
        else:
            posts = Post.objects.filter(category=id)
            response = serializers.serialize("json", posts)
            return HttpResponse(response)

    else:
        return HttpResponse(f"Posts request success: {False}")

@csrf_exempt
def post_API(request, id):

    if request.method == "PUT":
        try:
            user_request = request.body
            json_request = json.loads(user_request)
            category = json_request['category']
            title = json_request['title']
            description = json_request['description']
            post = Post.objects.filter(category_id=category, id=id).update(title=title, description=description)
            post = Post.objects.get(category_id=category, id=id)
            response = serializers.serialize("json", [post])
            return HttpResponse(response)
        except Exception as e:
            return HttpResponse(f"Error occurred during post update: {e}")

    if request.method == "GET":
        post = Post.objects.all().filter(id=id)
        response = serializers.serialize("json", post)
        return HttpResponse(response)

    if request.method == "DELETE":
        try:
            post = Post.objects.get(id=id)
            print(post)
            post.delete()
            return HttpResponse("Post deleted successfully", True)
        except:
            return HttpResponse("Error occurred during post deletion")

    else:
        return HttpResponse(f"PostsID request success: {False}")