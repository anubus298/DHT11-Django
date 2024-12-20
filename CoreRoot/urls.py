"""CoreRoot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from core.dht import api
from core.incident import viewsets

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("auth/", include(("core.routers", "core"), namespace="core-api")),
    path("api/dht/post", api.dlist, name="api_json"),
    path("api/incident/close", api.closeManuallyIncident, name="close_incident"),
    path("api/dht/statistics", api.getStatistics, name="statistics_json"),
    path("api/dht/avg/months", api.getMonthsAverage, name="avg_months_json"),
    path("api/dht/avg/days", api.getDailyAverage, name="avg_days_json"),
    path("api/dht/avg/range", api.getRangeAverage, name="avg_days_json"),
    path("api/dht/diff", api.getDateDifference, name="avg_days_json"),
    path("api/dht/diff", api.getDateDifference, name="avg_days_json"),
    path(
        "api/get-incidents-by-id",
        viewsets.getIncidentNoteByIncidentId,
        name="by_incident_id",
    ),
    path(
        "", include("core.notifications.urls")
    ),  # Replace 'your_app_name' with your app's name
]
