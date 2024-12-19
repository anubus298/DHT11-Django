from django.urls import path
from .views import (
    AddNotificationParameterView,
    DeleteNotificationParameterView,
    NotificationsParametersListView,
)

urlpatterns = [
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
]
