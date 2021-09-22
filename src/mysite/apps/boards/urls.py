from django.urls import path, include
from . import views

app_name = 'boards'
urlpatterns = [
    path('<int:board_id>/', views.detail, name='detail'),
    path('<int:board_id>/columns/', include('columns.urls')),
    path('<int:board_id>/tasks/', include('tasks.urls')),
    path('delete_board/<int:board_id>/', views.delete_board, name='delete_board'),
    path('create_board', views.create_board, name="create_board"),
    path('edit_board/<int:board_id>/', views.edit_board),
    path('invite_user/<int:board_id>/', views.invite_user),
]
