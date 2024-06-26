from django.shortcuts import render, get_object_or_404
from notes.models import Note, Page
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
import markdown


def index(request):
    pages_list = []
    notes = []

    if request.user.is_authenticated:
        notes = Note.objects.filter(user=request.user)
        for note in notes:
            pages = Page.objects.filter(note=note)
            for page in pages:
                page.content_html = markdown.markdown(page.content)
                page.content_html_safe = mark_safe(page.content_html)
                pages_list.append(page)

    context = {
        'notes': notes,
        'pages': pages_list
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
