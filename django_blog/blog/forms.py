from django import forms
from .models import Post, Comment, Tag
from taggit.forms import TagWidget



class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
    
        tags = forms.CharField(widget=TagWidget()) 

