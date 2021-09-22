from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ColumnForm
from .models import Column
from boards.models import Board
from tasks.models import Task


@login_required(login_url='/login')
def detail(request, column_id, board_id):
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

