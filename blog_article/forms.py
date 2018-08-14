from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    def __init__(self, *args, **kwargs):
        self.article = kwargs.pop('article')  # the blog entry instance
        super().__init__(*args, **kwargs)


    def save(self):
        comment = super().save(commit=False)
        comment.article = self.article
        comment.save()
        return comment