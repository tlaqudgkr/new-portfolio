from django.shortcuts import render, redirect
from .models import Board, Comment
from django.shortcuts import get_object_or_404
from .form import PostForm, CommentForm
from django.utils import timezone
# Create your views here.

def board_list(request):
    board = Board.objects.all()
    return render(request, 'freeboard/board_list.html', {'boards':board})


def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'freeboard/board_detail.html', {'boards':board})


def board_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.modified_date = timezone.now()
            post.save()
            return redirect('board:board_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'freeboard/board_edit.html', {'form':form})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'freeboard/add_comment_to_post.html',{'form':form})