from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# namespace: app별로 url를 나누기 위함
# notices/
app_name = 'notices'

urlpatterns =[
    path('notice', views.notice_list, name='notice_list'),
    path('notice/<int:notice_pk>', views.notice_detail, name='notice_detail'),
    path('notice/reply/<int:notice_pk>', views.notice_reply, name='notice_reply'),
    path('reply', views.reply_insert, name='reply_insert'),
    path('reply/<int:reply_pk>', views.reply_detail, name='reply_detail'),
    path('upload', views.upload, name='upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
