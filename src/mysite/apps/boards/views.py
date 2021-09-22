from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.utils import timezone
from boards.models import Board
from columns.models import Column
from tasks.models import Task
from .forms import BoardForm, UserInvitationForm


@login_required(login_url='/login')
def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    if request.user in board.users.all():
        columns_list = Column.objects.filter(board=board_id)
        task_list = Task.objects.all()
        return render(request, 'boards/detail.html',
                      {'board': board, 'columns_list': columns_list, 'task_list': task_list})
    else:
        return render(request, "account_pages/warning.html")


@login_required(login_url='/login')
def create_board(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.pub_date = timezone.now()
            board.save()
            board.users.add(request.user)
        return redirect("/")
    else:
        form = BoardForm()
    return render(request, "boards/create_board.html", {"form": form})


@login_required(login_url='/login')
def delete_board(request, board_id):
    board = Board.objects.get(id=board_id)
    if request.user in board.users.all():
        board.delete()
        return redirect("/")
    else:
        return render(request, "account_pages/warning.html")


@login_required(login_url='/login')
def edit_board(request, board_id):
    if request.method == "POST":
        board_prev = Board.objects.get(id=board_id)
        if request.user in board_prev.users.all():
            form = BoardForm(request.POST, instance=board_prev)
            if form.is_valid():
                board = form.save(commit=False)
                board.pub_date = timezone.now()
                board.save()
            return redirect('/boards/{}'.format(board_id))
        else:
            return render(request, "account_pages/warning.html")
    else:
        form = BoardForm()
    return render(request, "boards/create_board.html", {"form": form})


@login_required(login_url='/login')
def invite_user(request, board_id):
    if request.method == "POST":
        form = UserInvitationForm(request.POST)
        if form.is_valid():
            board = Board.objects.get(id=board_id)
            username = form.cleaned_data['username']
            try:
                user = User.objects.get(username=username)
                board.users.add(user.id)
            except ObjectDoesNotExist:
                return render(request, "account_pages/no_such_user.html")
        return redirect('/boards/{}'.format(board_id))
    else:
        form = UserInvitationForm()
    return render(request, "boards/invite_user.html", {"form": form})
