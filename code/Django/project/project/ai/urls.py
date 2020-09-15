from django.urls import path
from . import views


# namespace: app별로 url를 나누기 위함
# notices/
app_name = 'ai'

urlpatterns =[
    path('textDetection/', views.textDetection, name='textDetection'),
    path('objectDetection/', views.objectDetection, name='objectDetection'),
]
