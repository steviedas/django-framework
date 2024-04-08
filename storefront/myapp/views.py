from django.shortcuts import render, HttpResponse
from .models import Todoitem

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = Todoitem.objects.all()
    return render(request, "todos.html", {"todos": items})