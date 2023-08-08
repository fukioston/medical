from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.forms import ClearableFileInput

from column.models import Upload
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        exclude = ['author', 'views', 'slug', 'pub_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': CKEditorUploadingWidget(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'multi-checkbox'}),
        }
