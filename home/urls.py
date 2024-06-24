from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.notes, name='notes'),
    # path('notes/<int:pk>/', views.note_detail, name='note_detail'),
    # path('notes/new/', views.note_new, name='note_new'),
    # path('notes/<int:pk>/edit/', views.note_edit, name='note_edit'),
    # path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),
]