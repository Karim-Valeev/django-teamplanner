from django import forms
from .models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ("board_title",)


class UserInvitationForm(forms.Form):
    username = forms.CharField(label='Name of the user you want to add:')
