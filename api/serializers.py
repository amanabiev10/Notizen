from rest_framework import serializers
from notes.models import Note, Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'note', 'title', 'content', 'created_at', 'updated_at']

class NoteSerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'user', 'title', 'created_at', 'updated_at', 'pages']