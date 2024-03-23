from django.urls import path
from .views import ( ListCreateTasklist )

urlpatterns = [
    path('list-create-tasklist/', ListCreateTasklist.as_view(), name='list-create-tasklist'),
]