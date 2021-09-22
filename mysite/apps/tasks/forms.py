from django import forms
from tasks.models import Comment
from tasks.models import Task


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author", "comment_text",)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("title", "description", "lead_time",)