from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from .forms import *


def main(request):
    board_list = Board.objects.order_by('pub_date')
    column_list = Column.objects.all()
    return render(request, 'account_pages/home.html', {'board_list': board_list, 'column_list': column_list})


""" Board views """
@login_required(login_url='/login')
def board_detail(request, board_id):
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


""" Column views """
@login_required(login_url='/login')
def column_detail(request, column_id, board_id):
    a = Column.objects.get(id=column_id)
    board = Board.objects.get(id=board_id)
    if a in board.column.all():
        return render(request, 'columns/detail.html', {'column': a})
    else:
        return render(request, "account_pages/warning.html")


@login_required(login_url='/login')
def create_column(request, board_id):
    if request.method == "POST":
        board = Board.objects.get(id=board_id)
        form = ColumnForm(request.POST)
        if form.is_valid():
            column = form.save(commit=False)
            column.board = board
            column.save()
            board.column.add(column)
            return redirect('/boards/{}'.format(board_id))
    else:
        form = ColumnForm()
    return render(request, "columns/create_column.html", {"form": form})


@login_required(login_url='/login')
def delete_column(request, column_id, board_id):
    column = Column.objects.get(id=column_id)
    board = Board.objects.get(id=board_id)
    if column in board.column.all():
        column.delete()
        return redirect('/boards/{}'.format(board_id))
    else:
        return render(request, "account_pages/warning.html")


@login_required(login_url='/login')
def edit_column(request, column_id, board_id):
    if request.method == "POST":
        column_prev = Column.objects.get(id=column_id)
        board = Board.objects.get(id=board_id)
        if column_prev in board.column.all():
            form = ColumnForm(request.POST, instance=column_prev)
            if form.is_valid():
                column = form.save(commit=False)
                column.save()
                # board.column.add(column)
                return redirect('/boards/{}'.format(board_id))
        else:
            return render(request, "account_pages/warning.html")
    else:
        form = ColumnForm()
    return render(request, "columns/create_column.html", {"form": form})


""" Registration """
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(request, username=form.cleaned_data['username'],

                                password=form.cleaned_data['password1'],
                                )
            login(request, user)
            form.save()
            return render(request, "account_pages/home.html", {})
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})


""" Task views """
@login_required(login_url='/login')
def create_task(request, column_id, board_id):
    if request.method == "POST":
        column = Column.objects.get(id=column_id)
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.column = column
            task.author = request.user
            task.pub_date = timezone.now()
            task.save()
            column.task.add(task)
        return redirect('/boards/{}'.format(board_id))
    else:
        form = TaskForm()
    return render(request, "tasks/create_task.html", {'form': form})


@login_required(login_url='/login')
def delete_task(request, task_id, column_id, board_id):
    task = Task.objects.get(id=task_id)
    column = Column.objects.get(id=column_id)
    if task in column.task.all():
        task.delete()
        return redirect('/boards/{}'.format(board_id))
    else:
        return render(request, "account_pages/warning.html")


@login_required(login_url='/login')
def edit_task(request, task_id, column_id, board_id):
    if request.method == "POST":
        task_prev = Task.objects.get(id=task_id)
        column = Column.objects.get(id=column_id)
        if task_prev in column.task.all():
            form = TaskForm(request.POST, instance=task_prev)
            if request.user == task_prev.author:
                if form.is_valid():
                    task = form.save(commit=False)
                    # task.column = column
                    task.pub_date = timezone.now()
                    # task.author = request.user
                    # task.lead_time = ...
                    task.save()
                    # column.task.add(task)
                return redirect('/boards/{}'.format(board_id))
            else:
                return render(request, "account_pages/warning.html")
        else:
            return render(request, "account_pages/warning.html")
    else:
        form = TaskForm()
        return render(request, "tasks/create_task.html", {'form': form})


@login_required(login_url='/login')
def complete_task(request, task_id, column_id, board_id):
    task = Task.objects.get(id=task_id)
    column = Column.objects.get(id=column_id)
    if task in column.task.all():
        task.is_completed = True
        task.save()
        return redirect('/boards/{}'.format(board_id))
    else:
        return render(request, "account_pages/warning.html")


# @login_required(login_url='/login')
# def leave_comment(request, task_id, board_id):
#     task = Task.objects.get(id=board_id)
#     task.comment_set.create(author=request.user, comment_text="jgfj")


