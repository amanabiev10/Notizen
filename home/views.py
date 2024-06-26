from django.shortcuts import render, get_object_or_404
from notes.models import Note, Page
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import markdown2


def index(request):
    notes = Note.objects.all()
    pages = Page.objects.all()
    for page in pages:
        page.content = markdown2.markdown(page.content)

    context = {
        'notes': notes,
        'pages': pages
    }
    return render(request, 'home/index.html', context)


def notes_view(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'home/base.html', context)


def pages_view(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    pages = Page.objects.filter(note=note)
    pages_list = [{'id': page.id, 'title': page.title} for page in pages]
    return JsonResponse({'pages': pages_list})
