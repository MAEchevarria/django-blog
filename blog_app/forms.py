from django.forms import ModelForm
from .models import Category, Post

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'description']