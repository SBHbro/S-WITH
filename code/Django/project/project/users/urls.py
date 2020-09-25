from django.urls import path
from . import views

app_name = 'users'

urlpatterns =[
    path('user', views.user_insert, name='user_insert'),
    path('user/voca/<int:user_pk>', views.user_vocaList, name='user_vocaList'),
    path('voca', views.voca_list, name='voca_list'),
    path('voca/<int:voca_pk>', views.voca_detail, name='voca_detail')
]
