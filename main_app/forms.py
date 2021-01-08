from django.forms import ModelForm
from .models import Widget

class WidgetForm(ModelForm):
  class meta:
    model = Widget
    fields = '__all__'