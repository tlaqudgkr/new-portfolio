from django.shortcuts import render, redirect
from .models import Board, Comment, Category
from django.shortcuts import get_object_or_404
from .form import PostForm, CommentForm
from django.utils import timezone
# Create your views here.

def board_list(request):
    # board = Board.objects.all()
    category = Category.objects.all()
    ctgry = request.GET.get('category')
    if ctgry != None:
        board = Board.objects.filter(category__name = ctgry)
    else:
        board = Board.objects.all()

    return render(request, 'freeboard/board_list.html', {'boards':board, 'categorys':category})


def board_detail(request, pk):
    category = Category.objects.all()
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'freeboard/board_detail.html', {'boards':board, 'categorys':category})


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


def board_edit(request, pk):
    post = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.modified_date = timezone.now()
            post.save()
            return redirect('board:board_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'freeboard/board_edit.html', {'form':form})


def board_remove(request, pk):
    post = get_object_or_404(Board, pk=pk)
    post.delete()
    return redirect('board:board_list')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('board:board_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'freeboard/add_comment_to_post.html', {'form':form})