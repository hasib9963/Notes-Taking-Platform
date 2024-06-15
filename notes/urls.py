from django.urls import path

from . import views

app_name="notes"
urlpatterns = [
    # path('home/',views.index,name='index'),
    path('',views.indexView.as_view(),name='index'),
    
    # path('notes/',views.notes,name='notes'),
    path('notes/',views.notesListView.as_view(),name='notes'),
    
    # path('note/<int:note_id>',views.note,name='note'),
    path('note/<int:id>',views.noteDetailView.as_view(),name='note'),
    
    # path('new_note/',views.new_note,name='new_note'),
    path('new_note/',views.newNoteCreateView.as_view(),name='new_note'),
    
    
]