from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from core.auth.serializers import RegisterSerializer


class RegistrationViewSet(ViewSet):
    serializer_class = RegisterSerializer
    permission_classes = (IsAdminUser,)
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }        
        return Response(
            {
                "data": {
                    "user": serializer.data,
                    "refresh": res["refresh"],
                    "token": res["access"],                    
                }
            },
            status=status.HTTP_201_CREATED,
        )


# non superuser = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM0ODEzNTc1LCJqdGkiOiJlNjBmODQ0ZjE2Zjg0OTZlODliZjRlNTk4YWUxMWNkZiIsInVzZXJfaWQiOjR9.AQYNjJehDQPc_Z7owvpvDyhaLgnYpg82JelGmaONAzk
# superuser =  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM0ODEzNTUzLCJqdGkiOiI5OWMyZjJiOTc1NDk0OWE0YmUzM2ViZGNmZDRkYmFiZiIsInVzZXJfaWQiOjJ9.eWBwU8pFujSK3JmNrGfbm0icfL6V1e0zbRbEK3Lmups