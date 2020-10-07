from django import forms
from.import models


class CreateStory(forms.ModelForm):
    class Meta:
        model = models.Story
        fields = {'title', 'body', 'slug', 'thumb'}
