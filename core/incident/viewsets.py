from .serializers import IncidentSerializer
from .models import Incident
from rest_framework import filters
from .models import IncidentNote
from .serializers import IncidentNoteSerializer
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from django_filters import rest_framework as filters


class IncidentViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "delete"]
    serializer_class = IncidentSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return Incident.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs["pk"]  # Default is "pk" for primary key
        try:
            obj = Incident.objects.get(id=lookup_field_value)
            self.check_object_permissions(self.request, obj)

            return obj
        except Incident.DoesNotExist:
            raise NotFound(f"Incident with id {lookup_field_value} not found.")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


# create a viewset for incident notes


class IncidentNoteViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "delete"]
    serializer_class = IncidentNoteSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return IncidentNote.objects.all()

    def get_object(self):
        # fk of the incident
        lookup_field_value = self.kwargs["pk"]  # Default is "pk" for primary key

        try:
            obj = IncidentNote.objects.get(id=lookup_field_value)
            self.check_object_permissions(self.request, obj)
            return obj
        except IncidentNote.DoesNotExist:
            raise NotFound(f"Incident Note with id {lookup_field_value} not found.")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getIncidentNoteByIncidentId(request):
    # sort by created_at here
    incident_id = int(request.GET.get("incident_id", 0))

    if incident_id == 0:
        return Response(
            {"error": "incident_id is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    incident_notes = IncidentNote.objects.filter(incident=incident_id).order_by(
        "-created_at"
    )
    serializer = IncidentNoteSerializer(incident_notes, many=True)
    return Response({"data": serializer.data}, status=status.HTTP_200_OK)
