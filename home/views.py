from django.shortcuts import render
from notes.models import Note, Page
import markdown2


def notes(request):
    notes = Page.objects.all()
    for note in notes:
        note.content = markdown2.markdown(note.content)
    context = {
        'notes': notes
    }
    return render(request, 'home/notiz.html', context)


def index(request):
    return render(request, 'home/index.html')