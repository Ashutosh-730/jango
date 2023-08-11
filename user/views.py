from rest_framework.views import APIView
from rest_framework.response import Response

class UserAPIView(APIView):
    def get(self, request):
        return Response({"message": "User API endpoint"})
    
class AuthAPIView(APIView):
    def get(self, request):
        return Response({"message": "Auth API endpoint"})