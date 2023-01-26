from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [

      path('', NoteMain.as_view(), name='main'),
      path('search/', NoteSearch.as_view(), name='search'),
      path('ckeditor', include('ckeditor_uploader.urls')),
      path('detail/<int:pk>/', NoteDetail.as_view(), name='detail'),

      path('create/', ProtectNoteCreate.as_view(), name='create'),
      path('delete/<int:pk>', ProtectNoteDelete.as_view(), name='delete'),
      path('edit/<int:pk>', ProtectNoteEdit.as_view(), name='edit'),
      path('response/', ProtectResponseList.as_view(), name='response'),
      path('response_accept/<int:pk>', ProtectResponseAccept.as_view(), name='accept'),
      path('response_remove/<int:pk>', ProtectResponseRemove.as_view(), name='remove'),

  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)