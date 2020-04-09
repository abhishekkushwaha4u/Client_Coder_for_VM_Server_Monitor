from rest_framework.views import APIView
from rest_framework.response import Response


class HealthCheckView(APIView):
    def get(self, request):
        Response.status_code = 200
        return Response({
            "status": "success",
            "message": "Server is working fine"
        })


choices = {
    1: 
}
