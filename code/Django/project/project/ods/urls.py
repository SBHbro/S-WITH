from django.urls import path
from . import views


# namespace: app별로 url를 나누기 위함
# notices/
app_name = 'ods'

urlpatterns =[
    path('imageUpload/', views.imageUpload, name='imageUpload'),
]
