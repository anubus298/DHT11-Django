from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Parameter
from .serializer import ParameterSerializer
from rest_framework.permissions import IsAdminUser

class ParameterUpdateView(APIView):
    permission_classes = ( IsAdminUser,)  
    
    def get(self, request):
        # Retrieve all parameters
        parameters = Parameter.objects.all()
        serializer = ParameterSerializer(parameters, many=True)
        return Response({"data" : serializer.data} , status=status.HTTP_200_OK)
    def put(self, request, type):
        try:
            # Retrieve the parameter by type
            parameter = Parameter.objects.get(type=type)
        except Parameter.DoesNotExist:
            return Response({"error": "Parameter not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Update the parameter value
        serializer = ParameterSerializer(parameter, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
