from django.urls import path
from . import views

# namespace: app별로 url를 나누기 위함
# notices/
app_name = 'notices'

urlpatterns =[
    path('notice', views.notice_list, name='notice_list'),
    path('notice/<int:notice_pk>', views.notice_detail, name='notice_detail'),
]
