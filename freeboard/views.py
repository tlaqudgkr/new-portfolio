from django.shortcuts import render, redirect
from .models import Board, Comment, Category
from django.shortcuts import get_object_or_404
from .form import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

def board_list(request):
    # board = Board.objects.all()
    category = Category.objects.all()
    ctgry = request.GET.get('category')
    if ctgry != None:
        board = Board.objects.filter(category__name = ctgry).order_by('-created_date')
    else:
        board = Board.objects.all().order_by('-created_date')

    return render(request, 'freeboard/board_list.html', {'boards':board, 'categorys':category})


def board_detail(request, pk):
    category = Category.objects.all()
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'freeboard/board_detail.html', {'boards':board, 'categorys':category})

@login_required
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

@login_required
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

@login_required
def board_remove(request, pk):
    post = get_object_or_404(Board, pk=pk)
    post.delete()
    return redirect('board:board_list')

@login_required
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

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('board:board_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('board:board_detail', pk=comment.post.pk)