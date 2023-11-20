from django import forms

class AddCommentForm(forms.Form):
    message = forms.CharField(label="Comment", widget=forms.TextInput)

