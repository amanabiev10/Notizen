from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Note, Page
from django.contrib.auth.decorators import login_required

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