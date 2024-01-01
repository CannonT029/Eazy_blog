from django import forms
from .models import Comment
from .models import Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control form-control-lg',"autocomplete":"off", 'placeholder': 'Name'}),
            'body': forms.Textarea(attrs={'class':'form-control form-control-lg', "autocomplete":"off", 'placeholder': 'Write something'}),
        }

class PostEdit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'category', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control form-control-lg', "autocomplete":"off", 'placeholder': 'Title'}),
            'body' : forms.Textarea(attrs={'class': 'form-control form-control-lg', "autocomplete":"off"}),
        }


