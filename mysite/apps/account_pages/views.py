from boards.models import Board
from columns.models import Column
from django.shortcuts import render


def main(request):
    board_list = Board.objects.order_by('pub_date')
    column_list = Column.objects.all()
    return render(request, 'account_pages/home.html', {'board_list': board_list, 'column_list': column_list})

