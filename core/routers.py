from rest_framework.routers import SimpleRouter
from core.user.viewsets import UserViewSet, CurrentUserViewSet
from core.auth.viewsets import (
    LoginViewSet,
    RegistrationViewSet,
    RefreshViewSet,
)
from core.incident.viewsets import IncidentViewSet, IncidentNoteViewSet


routes = SimpleRouter()

# AUTHENTICATION
routes.register(r"login", LoginViewSet, basename="auth-login")
routes.register(r"register", RegistrationViewSet, basename="auth-register")
routes.register(r"refresh", RefreshViewSet, basename="auth-refresh")

# USER
routes.register(r"users", UserViewSet, basename="users")
routes.register(r"current-user", CurrentUserViewSet, basename="current-user")

routes.register(r"incidents", IncidentViewSet, basename="incident")
routes.register(r"incident-notes", IncidentNoteViewSet, basename="incident-notes")

urlpatterns = [*routes.urls]
