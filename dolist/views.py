from django.shortcuts import render
import models import Todolist

#Create your views here.
def index(request):
    todo_items = Todolist.ogjects.order_by('id')
    context - {'todo_items' : todo_items}
    return render(request, "index.html", context)