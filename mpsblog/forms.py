from django import forms
from .models import ThreadComment


class CommentBox(forms.ModelForm):
    class Meta:
        model = ThreadComment
        fields = ('body',)

class EditComment(forms.ModelForm):
    class Meta:
        model = ThreadComment
        fields = ('body',)