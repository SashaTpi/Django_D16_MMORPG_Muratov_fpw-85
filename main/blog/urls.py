from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='main'), #mmorpg
    path('post/<int:pk>', PostDetails.as_view(), name='post_details'),
    path('create/', PostCreate.as_view(), name='create'),
    path('delete/<int:pk>', PostDelete.as_view(), name='delete'),
    path('edit/<int:pk>', PostEdit.as_view(), name='update'),
    path('replies/<int:pk>', ReplyDetails.as_view(), name='reply_details'),
    path('replies/create/', ReplyCreate.as_view(), name='reply_create'),
    path('replies/', ReplyList.as_view(), name='reply_list'),
    path('replies/edit/<int:pk>', ReplyEdit.as_view(), name='reply_edit'),
    path('replies/delete/<int:pk>', ReplyDelete.as_view(), name='reply_delete'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('login/', LoginAccount.as_view(), name='login_account'),
    path('login/delete/<int:pk>', ReplyDeleteByPostAuthor.as_view(), name='reply_delete_by_post_author'),
]