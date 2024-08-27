from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required



def index(request):
    '''Домашняя страница.'''
    return render(request, 'notes_app/index.html')



@login_required()
def notes(request):
    '''Страница со всеми заметками.'''
    notes = Note.objects.filter(owner=request.user).order_by('-date_add')
    context = {'notes':notes}
    return render(request, 'notes_app/notes.html', context)



@login_required()
def note(request, note_id):
    '''Выводит отдельную заметку.'''
    note = Note.objects.get(id=note_id)
    if note.owner != request.user:
        return render(request, 'notes_app/error.html')
    context = {'note':note}
    return render(request, 'notes_app/note.html', context)



@login_required()
def new_note(request):
    '''Создает новую заметку.'''
    if request.method != 'POST':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.owner = request.user
            new_note.fixed_note()
            new_note.save()
            return redirect('notes_app:notes')

    context = {'form':form}
    return render(request, 'notes_app/new_note.html', context)


@login_required()
def edit_note(request, note_id):
    '''Редактирует существующую запись.'''
    note = Note.objects.get(id=note_id)
    if request.method != 'POST':
        form = NoteForm(instance=note)
    else:
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            note.fixed_note()
            form.save()
            return redirect('notes_app:note', note_id=note.id)
    context = {'note':note, 'form':form}
    return render(request, 'notes_app/edit_note.html', context)