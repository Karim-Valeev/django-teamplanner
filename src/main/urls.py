from django.urls import path, include
from .views import *

urlpatterns = [
    path('', main, name='account_pages'),

    path('<int:board_id>/', board_detail, name='detail'),
    # path('<int:board_id>/columns/', include('columns.urls')),
    # path('<int:board_id>/tasks/', include('tasks.urls')),
    path('delete_board/<int:board_id>/', delete_board, name='delete_board'),
    path('create_board', create_board, name="create_board"),
    path('edit_board/<int:board_id>/', edit_board),
    path('invite_user/<int:board_id>/', invite_user),

    path('<int:column_id>/<int:board_id>', column_detail, name='detail'),
    path('create_column/<int:board_id>/', create_column, name="create_column"),
    path('delete_column/<int:column_id>/<int:board_id>', delete_column),
    path('edit_column/<int:column_id>/<int:board_id>', edit_column),

    path('', register, name='register'),

    # ???
    path('', create_task),
    path('create_task/<int:column_id>/<int:board_id>', create_task,),
    path('delete_task/<int:task_id>/<int:column_id>/<int:board_id>', delete_task),
    path('edit_task/<int:task_id>/<int:column_id>/<int:board_id>', edit_task),
    path('complete_task/<int:task_id>/<int:column_id>/<int:board_id>', complete_task),
    # path('leave_comment/<int:task_id>/<int:board_id>', views.leave_comment),
    # path('leave', views.leave),
]
