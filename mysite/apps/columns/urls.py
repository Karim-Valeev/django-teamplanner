from django.contrib import admin
from django.urls import path
from columns import views

urlpatterns = [
    path('<int:column_id>/<int:board_id>', views.detail, name='detail'),
    path('create_column/<int:board_id>/', views.create_column, name="create_column"),
    path('delete_column/<int:column_id>/<int:board_id>', views.delete_column),
    path('edit_column/<int:column_id>/<int:board_id>', views.edit_column),
]
