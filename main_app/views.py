from main_app.forms import WidgetForm
from django.shortcuts import render, redirect
from .models import Widget

# Create your views here.
def index(request):
  widgets = Widget.objects.all()
  return render(request, 'index.html', {'widgets': widgets})

def create(request):
  new_widget = Widget(
    description = request.POST['description'],
    quantity = request.POST['quantity']
  )
  new_widget.save()
  return redirect('index')
