from django import forms
from app7.models import CousreModel,StudentModel,FacuiltyModel
import re
class CourseForm(forms.ModelForm):
    fee = forms.IntegerField(min_value=3000)
    class Meta:
      model = CousreModel
      fields="__all__"

    def clean_name(self):
        name = self.cleaned_data["name"]
        res = re.findall(r'^[A-Z a-z]*$',name)
        if res:
            return name
        else:
            raise forms.ValidationError("invalid name...will accept A-z or a-z")