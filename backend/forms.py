from django import forms


class UploadFileForm(forms.Form):
     file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'your-cool-css-class'}))