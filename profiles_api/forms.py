from django import forms
from .models import ImageUploadDwonload
class ImageForm(forms.ModelForm):
 class Meta:
      model = ImageUploadDwonload
      fields = ('video','image')
