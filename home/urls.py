from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('notes/', views.notes_view, name='notes'),
    # path('notes/<int:note_id>/pages/', views.pages_view, name='pages'),
=======
    path('notes/<int:note_id>/', views.pages_view, name='pages_view'),
    path('notes/', views.notes_view, name='notes_view'),
    path('notes/<int:note_id>/pages/', views.pages_view, name='pages_view'),
>>>>>>> 6ac0723eb433918435eee0e3722d96435fdd1ee8
    # path('notes/<int:pk>/', views.note_detail, name='note_detail'),
    # path('notes/new/', views.note_new, name='note_new'),
    # path('notes/<int:pk>/edit/', views.note_edit, name='note_edit'),
    # path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),
]