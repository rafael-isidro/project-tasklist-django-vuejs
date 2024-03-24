from django.urls import path
from .views import (
    Login,
    ListCreateTasklist,
    RetrieveUpdateDestroyTasklist
    )

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('list-create-tasklist/', ListCreateTasklist.as_view(), name='list-create-tasklist'),
    path('retrieve-update-destroy-tasklist/<int:pk>/', RetrieveUpdateDestroyTasklist.as_view(), name="retrieve-update-destroy-tasklist")
]