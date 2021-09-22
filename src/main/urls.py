from django.urls import path, include
from .views import *

urlpatterns = [
    path('', main, name='account_pages'),

    path('boards/<int:board_id>/', board_detail, name='board_detail'),
    path('boards/delete_board/<int:board_id>/', delete_board, name='delete_board'),
    path('boards/create_board', create_board, name="create_board"),
    path('boards/edit_board/<int:board_id>/', edit_board),
    path('boards/invite_user/<int:board_id>/', invite_user),

    path('<int:column_id>/<int:board_id>', column_detail, name='column_detail'),
    path('columns/create_column/<int:board_id>/', create_column, name="create_column"),
    path('columns/delete_column/<int:column_id>/<int:board_id>', delete_column),
    path('columns/edit_column/<int:column_id>/<int:board_id>', edit_column),

    path('register/', register, name='register'),

    # ???
    path('tasks/create_task/<int:column_id>/<int:board_id>', create_task,),
    path('tasks/delete_task/<int:task_id>/<int:column_id>/<int:board_id>', delete_task),
    path('tasks/edit_task/<int:task_id>/<int:column_id>/<int:board_id>', edit_task),
    path('tasks/complete_task/<int:task_id>/<int:column_id>/<int:board_id>', complete_task),
    # path('leave_comment/<int:task_id>/<int:board_id>', views.leave_comment),
    # path('leave', views.leave),
]
