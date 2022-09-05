from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('categories/new/', views.create_category, name="create_category"),
    path('categories/<int:id>/view', views.get_category, name="get_category"),
    path('categories/<int:id>/edit/', views.update_category, name="update_category"),
    path('categories/<int:id>/delete/', views.delete_category, name="delete_category"),
    path('categories/<int:id>/posts/', views.get_posts, name="get_posts"),
    path('categories/<int:id>/posts/new/', views.create_post, name="create_post"),
    path('categories/<int:id>/posts/<int:post_id>/', views.get_post, name="get_post"),
    path('categories/<int:id>/posts/<int:post_id>/edit/', views.update_post, name="update_post"),
    path('categories/<int:id>/posts/<int:post_id>/delete/', views.delete_post, name="delete_post"),
    
    path('categories/', views.categories_API),
    path('categories/<int:id>/', views.category_API),
    path('posts/', views.posts_API,),
    path('posts/<int:id>/', views.post_API,),
]