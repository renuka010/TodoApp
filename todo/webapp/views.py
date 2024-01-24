from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginUserForm

from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

from .models import TodoItem

#homepage
def home(request):
    return render(request, 'webapp/index.html')

#register a user
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() # save user to database
            return redirect('webapp:login')
    else:
        form = CreateUserForm()
    return render(request, 'webapp/register.html', {'form': form})

#login a user
def login(request):
    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            #check if user exists
            if user is not None:
                auth.login(request, user)
                return redirect('webapp:notes')
    else:
        form = LoginUserForm()
    context = {'form': form}
    return render(request, 'webapp/login.html', context=context)

#logout a user
def logout(request):
    auth.logout(request)
    return redirect('webapp:login')

#create a note/view notes
@login_required(login_url='webapp:login')
def notes(request):
    if request.method == 'POST':
        description = request.POST['description']
        if description.strip() != '':
            TodoItem.objects.create(user=request.user, description=description)
            
    my_notes = TodoItem.objects.order_by('completed','id').filter(user=request.user)
    context = {'todonotes': my_notes, 'user': request.user}
    return render(request, 'webapp/note.html', context=context)

#edit note
@login_required(login_url='webapp:login')
def edit(request, note_id):
    if request.method == 'POST':
        note = TodoItem.objects.get(pk=note_id)
        description = request.POST['description']
        if description.strip() != '':
            note.description = description
            note.save()
            return redirect('webapp:notes')
        else:
            return redirect('webapp:edit', note_id=note_id)
    
    note = get_object_or_404(TodoItem, pk=note_id)
    context = {'note': note}
    return render(request, 'webapp/edit.html', context=context)

#delete note
@login_required(login_url='webapp:login')
def delete(request, note_id):
    note = get_object_or_404(TodoItem, pk=note_id)
    note.delete()
    return redirect('webapp:notes')

#complete note
@login_required(login_url='webapp:login')
def complete(request, note_id):
    note = get_object_or_404(TodoItem, pk=note_id)
    if note.completed == True:
        note.completed = False
    else:
        note.completed = True
    note.save()
    return redirect('webapp:notes')