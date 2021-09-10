from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Car
from .serializers import CarSerializer
from django.contrib.auth.models import User

# class CarsList(APIView):

#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         cars = Car.objects.all()
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_cars(request):
    # user = User.objects.get(username=request.user)

    # print('User', f"{user.id} {user.email} {user.username}")
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)
