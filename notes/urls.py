from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('add_notebook/', views.add_notebook, name='add_notebook'),
    path('add_page/', views.add_page, name='add_page'),
    # andere URLs
]
