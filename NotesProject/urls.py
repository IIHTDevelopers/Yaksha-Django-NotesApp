
from django.contrib import admin
from django.urls import path,re_path
#from django.conf.urls import url
from notesapp.views import NotesCRUDView,SearchNotesByIdView,SearchNotesByAuthorView,SearchNotesByStatusView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes_crud/',NotesCRUDView.as_view()),
    path('notes_crud_pk/<int:pk>/',NotesCRUDView.as_view()),
    #url(r'^notes_crud/',NotesCRUDView.as_view()),# wont works
    #url(r'^notes_crud/<int:pk>/',NotesCRUDView.as_view()),# wont works
    re_path(r'^search_by_id/',SearchNotesByIdView.as_view()),
    re_path(r'^search_by_author/',SearchNotesByAuthorView.as_view()),
    re_path(r'^search_by_status/',SearchNotesByStatusView.as_view()),
]

#http://127.0.0.1:8000/search_by_id/?id=102/
