from django.forms import ModelForm
from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'category']


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['post', 'author', 'text']