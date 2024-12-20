from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import action
from core.user.models import User
from core.user.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "put", "patch", "delete"]  # Allow PUT, PATCH, DELETE
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)  # Only admin can delete or update
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["updated"]
    ordering = ["-updated"]

    def get_queryset(self):
        return User.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]
        obj = User.objects.get(id=lookup_field_value)
        self.check_object_permissions(self.request, obj)
        return obj
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data})
    # Admin-specific method to delete a user
    def destroy(self, request, *args, **kwargs):
        """
        This method allows the admin to delete a user.
        """
        # Get the user object to be deleted
        user = self.get_object()
        # user must not be the current user
        if user == request.user:
            return Response(
                {"detail": "You cannot delete your own account."},
                status=status.HTTP_400_BAD_REQUEST,)
        
        # Delete the user
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    # Admin-specific method to update a user
    def update(self, request, *args, **kwargs):
        """
        This method allows the admin to update user information.
        """
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)        
        
        #declare a variable that take the /users/ => id
        user_id = self.kwargs["pk"]

        #make sure if the user is_staff he doesnt downgrade himself
        
        print(request.user.id)
        print(user_id)
        if  "is_staff" in request.data and request.data["is_staff"] == False and str(user_id) == str(request.user.id) :
            return Response(
                {"detail": "You cannot downgrade your own account."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if the provided data is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentUserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def current_user(self, request):
        serializer = UserSerializer(request.user)
        return Response({"data": serializer.data})
