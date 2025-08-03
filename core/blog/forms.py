from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    published_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'category', 'published_date']
