from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('/<int:note_id>/', views.notes_views, name='notes_views'),
    path('page/<int:page_id>/', views.page_detail, name='page_detail'),
    path('add_notebook/', views.add_notebook, name='add_notebook'),
    path('add_page/', views.add_page, name='add_page'),
    # andere URLs
]
