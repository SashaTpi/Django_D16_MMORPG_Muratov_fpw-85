from django_filters import FilterSet

from .models import Note, Response


class NoteFilter(FilterSet):
    class Meta:
        model = Note
        fields = ('category',) #'user',


class ResponseFilter(FilterSet):
    class Meta:
        model = Response
        fields = ('note_id',)