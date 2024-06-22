from django import forms
from django.forms import SelectDateWidget 
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Tasks
        fields = "__all__"

    assign_date = forms.DateField(
    widget=SelectDateWidget(),
    label="Assign Date",
    help_text="Please select the assign date"
    )