from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import NoteViewSet, PageViewSet

# Router für Notes
router = DefaultRouter()
router.register(r'notes', NoteViewSet)

# Verschachtelter Router für Pages, die zu einer Note gehören
note_router = NestedDefaultRouter(router, r'notes', lookup='note')
note_router.register(r'pages', PageViewSet, basename='note-pages')

urlpatterns = [
    path('', include(router.urls)),  # Für Notes
    path('', include(note_router.urls)),  # Für verschachtelte Pages
]
