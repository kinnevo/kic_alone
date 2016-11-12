__author__ = 'jorgezavala'


from django import forms

from .models import Ideas, IdeaComment, IdeaCategory

class IdeaForm(forms.ModelForm):

    class Meta:
        model = Ideas
        fields = ['description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = IdeaComment
        fields = ['comment']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = IdeaCategory
        fields = ['category']
