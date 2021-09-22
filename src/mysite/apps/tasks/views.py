from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from tasks.forms import CommentForm, TaskForm
from columns.models import Column
from tasks.models import Comment, Task


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


