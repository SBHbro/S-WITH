from django.urls import path
from. import views


app_name = 'articles'

# articles/
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),

    path('artists/', views.artist_list, name='artist_list'),
    path('artists/<int:artist_pk>/', views.artist_detail, name='artist_detail'),
    path('musics/', views.music_list, name='music_list'),
    path('musics/<int:music_pk>/', views.music_detail, name='music_detail'),
    path('musics/<int:music_pk>/comments/', views.comment_create, name='comment_create'),
    path('comments/<int:comment_pk>/', views.comment_update_and_delete, name='comment_update_and_delete'),
]

