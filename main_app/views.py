from main_app.forms import WidgetForm
from django.shortcuts import render, redirect
from .models import Widget

# Create your views here.
def index(request):
  widgets = Widget.objects.all()
  sum = 0
  for widget in widgets:
    sum += widget.quantity
  return render(request, 'index.html', {'widgets': widgets, 'sum': sum})

def create(request):
  new_widget = Widget(
    description = request.POST['description'],
    quantity = request.POST['quantity']
  )
  new_widget.save()
  return redirect('index')

def delete(request, widget_id):
  Widget.objects.get(id=widget_id).delete()
  return redirect('/')