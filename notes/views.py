from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Note, Page
from django.contrib.auth.decorators import login_required
from markdown.extensions.fenced_code import FencedCodeExtension
import markdown

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


from django.shortcuts import render, get_object_or_404
from .models import Page


@login_required
def page_detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id, note__user=request.user)
    md = markdown.Markdown(extensions=[FencedCodeExtension()])
    page.content = md.convert(page.content)

    context = {
        'page': page,
    }
    return render(request, 'notes/page_detail.html', context)
