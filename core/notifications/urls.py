from django.urls import path
from core.counter.views import ParameterUpdateView
from .views import (
    AddNotificationParameterView,
    DeleteNotificationParameterView,
    NotificationsParametersListView,
)
from core.user.viewsets import return_version
urlpatterns = [
    path(
        "version/",
         return_version,
        name="backend-version",         
         ),
    path(
        "notifications/add/",
        AddNotificationParameterView.as_view(),
        name="add_notification",
    ),
    path(
        "notifications/delete/<int:pk>/",
        DeleteNotificationParameterView.as_view(),
        name="delete_notification",
    ),
    path(
        "notifications/",
        NotificationsParametersListView.as_view(),
        name="list_notifications",
    ),
    path('parameters/<str:type>/', ParameterUpdateView.as_view(), name='update-parameter'),    
    path('parameters/', ParameterUpdateView.as_view(), name='list-parameters'),
]
