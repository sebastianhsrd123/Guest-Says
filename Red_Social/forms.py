from django import forms
from .models import SocialPost, SocialComment


class SocialPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md',
            'rows': '3',
            'placeholder': 'Say Something...'
            }),
        required=True)
    
    calification = forms.DecimalField(widget=forms.NumberInput (attrs={
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md',
            'rows': '1',
            'placeholder': 'Value'
            }),
        required=True)


    image = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': 'relative dark:text-dark-txt dark:bg-dark-second cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500',
        'multiple': True
        }),
        required=False
        )

    class Meta:
        model=SocialPost
        fields=['body', 'calification']
        
        
class SocialCommentForm(forms.ModelForm):
    comment = forms.CharField(
    widget=forms.Textarea(attrs={
        'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md',
        'rows': '1',
        'placeholder': 'Comment Something...'
        }),
    required=True
    )

    class Meta:
        model=SocialComment
        fields=['comment']