from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.forms import ClearableFileInput

from column.models import articles
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class UploadForm(forms.ModelForm):
    class Meta:
        model = articles
        exclude = ['uploader_id', 'click', 'likes', 'upload_time', 'status']
        widgets = {
            'catalog': forms.Select(attrs={'class': 'form-control'}),
            'article_name': forms.TextInput(attrs={'class': 'form-control'}),
            'img_url': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'content': CKEditorUploadingWidget(attrs={'class': 'form-control'}),
        }
