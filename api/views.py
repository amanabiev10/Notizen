from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from notes.models import Note, Page
from .serializers import NoteSerializer, PageSerializer
from django.shortcuts import get_object_or_404

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    # Custom GET method to retrieve a specific note
    def retrieve(self, request, pk=None):
        note = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Custom POST method to create a new note
    def create(self, request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Custom PUT method to update an existing note
    def update(self, request, pk=None):
        note = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Custom DELETE method to delete a note
    def destroy(self, request, pk=None):
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    # Überschreibe die `get_queryset` Methode, um die Pages basierend auf der Note zu filtern
    def get_queryset(self):
        note_pk = self.kwargs.get('note_pk')  # Hol den note_pk aus der URL
        if note_pk:
            return Page.objects.filter(note_id=note_pk)  # Filtere Pages nach Note
        return super().get_queryset()  # Standardverhalten, wenn kein note_pk vorhanden

    # Custom GET method for a specific page related to a note
    def retrieve(self, request, note_pk=None, pk=None):
        page = get_object_or_404(Page, note_id=note_pk, pk=pk)
        serializer = PageSerializer(page)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Custom POST method to create a new page for a specific note
    def create(self, request, note_pk=None):
        request.data['note'] = note_pk  # Associate the page with the note
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Custom PUT method to update a page for a specific note
    def update(self, request, note_pk=None, pk=None):
        page = get_object_or_404(Page, note_id=note_pk, pk=pk)
        serializer = PageSerializer(page, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Custom DELETE method to delete a page for a specific note
    def destroy(self, request, note_pk=None, pk=None):
        page = get_object_or_404(Page, note_id=note_pk, pk=pk)
        page.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
