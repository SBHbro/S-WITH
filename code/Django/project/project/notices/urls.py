from django.urls import path
from . import views

# namespace: app별로 url를 나누기 위함
# notices/
app_name = 'notices'

urlpatterns =[
    path('notice/', views.notice_select, name='notice_select'),
    path('notice/<int:notice_pk>/', views.notice_detail, name='notice_detail'),
    path('notice/create/', views.notice_create, name='notice_create'),
    path('notice/update/<int:notice_pk>/', views.notice_update, name='notice_update'),
    path('notice/delete/<int:notice_pk>/', views.notice_delete, name='notice_delete'),
]
