from django import forms
from .models import Board, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('title', 'text', 'category')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)