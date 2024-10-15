from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoModels
from .forms import TodoForm

# Create your views here.
def todo_list(request):
    todos = TodoModels.objects.all()
    return render (request, 'todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_create.html', {'form': form})

def todo_update(request, pk):
    todo = get_object_or_404(TodoModels, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_update.html', {'form': form})

def todo_delete(request, pk):
    todo = get_object_or_404(TodoModels, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_delete.html', {'todo': todo})