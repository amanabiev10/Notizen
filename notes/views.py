from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Note, Page
from django.contrib.auth.decorators import login_required
from markdown.extensions.fenced_code import FencedCodeExtension
from django.shortcuts import render, get_object_or_404
import markdown


@login_required
def notes_views(request, note_id):
    notes = Note.objects.filter(user=request.user)
    note = get_object_or_404(Note, pk=note_id, user=request.user)
    pages = Page.objects.filter(note=note)
    for page in pages:
        md = markdown.Markdown(extensions=[FencedCodeExtension()])
        page.content = md.convert(page.content)
    context = {
        'notes': notes,
        'pages': pages,
    }
    return render(request, 'notes/notes.html', context)


@login_required
def page_detail(request, page_id):
    notes = Note.objects.filter(user=request.user)
    page = get_object_or_404(Page, pk=page_id, note__user=request.user)
    md = markdown.Markdown(extensions=[FencedCodeExtension()])
    page.content = md.convert(page.content)

    context = {
        'notes': notes,
        'page': page,
    }
    return render(request, 'notes/page_detail.html', context)


@csrf_exempt
@login_required
def add_notebook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            note = Note.objects.create(user=request.user, title=title)
            return JsonResponse({'id': note.id, 'title': note.title})
    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
@login_required
def add_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        note_id = request.POST.get('note_id')
        if title and note_id:
            note = Note.objects.get(id=note_id, user=request.user)
            page = Page.objects.create(note=note, title=title)
            return JsonResponse({'id': page.id, 'title': page.title})
    return JsonResponse({'error': 'Invalid request'}, status=400)