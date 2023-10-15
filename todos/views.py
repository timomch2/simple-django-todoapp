from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
import os

# Create your views here.
def index(request):
    file = open(os.getcwd()+'/todos/files/todos.json')
    todos = json.load(file)
    context = {'todos':todos}
    return render(request, 'todos/index.html', context)

def addTodo(request):
    todos = getTodos()
    if request.method =='POST':
        last_id = ''
        if len(todos) > 1:
            items = todos[-1].items()
            for key, value in items:
                if key == 'id':
                    last_id = value + 1

        if last_id =='':
            last_id = 1
        new_todo = {
            'id': last_id,
            'title': request.POST['title'],
            'description': request.POST['description'],
            'status': 'pending'
        }

        file = os.getcwd() + '/todos/files/todos.json'
        with open(file, 'r+') as jfile:
            file_data = json.load(jfile)
            file_data.append(new_todo)
            jfile.seek(0)
            json.dump(file_data, jfile, indent=4)
        return redirect('/')
def getTodos():
    file = open(os.getcwd() + '/todos/files/todos.json')
    return json.load(file)

def editTodo(request, id):
    todos = getTodos()
    todo = todos[(int(id))-1]
    context = {'todo':todo}

    if request.method == 'POST':
        todo['id'] = id
        todo['title'] = request.POST['title']
        todo['description'] = request.POST['description']
        todo['status'] = request.POST['status']

        file = os.getcwd() + '/todos/files/todos.json'
        with open(file, 'w') as fp:
            json.dump(todos, fp, indent=4)
        return redirect('/')

    return render(request, 'todos/index.html', context)

def deleteTodo(request, id):
    index = int(id)
    file = file = os.getcwd() + '/todos/files/todos.json'
    todos = getTodos()
    del todos[index-1]
    with open(file, 'w') as fp:
        json.dump(todos, fp)
    return redirect('/')

def todoMarkCompleted(request, id):
    todos = getTodos()
    todo = todos[int(id)-1]
    todo['status'] = request.GET['status']
    file = os.getcwd() + '/todos/files/todos.json'
    with open(file, 'w') as fp:
        json.dump(todos, fp, indent=4)
    return redirect('/')
