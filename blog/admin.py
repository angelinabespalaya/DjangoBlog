from django.contrib import admin
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin

'''class BlogAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    description_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    description_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'
'''

@admin.register(Post)
class PostAdmin(TranslationAdmin):
    fields = ('title','author', 'body')