from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ("board_title",)


class UserInvitationForm(forms.Form):
    username = forms.CharField(label='Name of the user you want to add:')


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ("column_title",)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author", "comment_text",)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description", "lead_time",)