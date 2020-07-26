from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.create_task),
    path('create_task/<int:column_id>/<int:board_id>', views.create_task,),
    path('delete_task/<int:task_id>/<int:column_id>/<int:board_id>', views.delete_task),
    path('edit_task/<int:task_id>/<int:column_id>/<int:board_id>', views.edit_task),
    path('complete_task/<int:task_id>/<int:column_id>/<int:board_id>', views.complete_task),
    # path('leave_comment/<int:task_id>/<int:board_id>', views.leave_comment),
    # path('leave', views.leave),
]
