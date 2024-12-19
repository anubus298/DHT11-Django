from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NotificationsParameters
from .serializer import NotificationsParametersSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import ListAPIView


class NotificationsParametersListView(ListAPIView):
    queryset = NotificationsParameters.objects.all()
    serializer_class = NotificationsParametersSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Optionally filter the queryset by `type` query parameter.
        """
        queryset = super().get_queryset()
        notification_type = self.request.query_params.get(
            "type"
        )  # Get the `type` parameter from the query string
        if notification_type:
            queryset = queryset.filter(type=notification_type)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class AddNotificationParameterView(generics.CreateAPIView):
    queryset = NotificationsParameters.objects.all()
    serializer_class = NotificationsParametersSerializer
    permission_classes = (IsAdminUser,)


class DeleteNotificationParameterView(APIView):
    permission_classes = (IsAdminUser,)

    def delete(self, request, pk):
        try:
            parameter = NotificationsParameters.objects.get(pk=pk)
            parameter.delete()
            return Response(
                {"message": "Notification parameter deleted successfully."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except NotificationsParameters.DoesNotExist:
            return Response(
                {"error": "Notification parameter not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
