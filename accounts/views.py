from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenSerializer,RegisterSerializer,ProfileSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message":"Qeydiyyatdan ugurla kecdiniz"},status=status.HTTP_201_CREATED)
        return Response(serializer.error,status = status.HTTP_400_BAD_REQUEST)
    

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        serializer = ProfileSerializers
        return Response(serializer.data)

class UpdateEmailView(APIView):
    permission_classes=[IsAuthenticated]
    def patch(self,request):
        new_email = request.data.get('email')
        if not new_email:
            return Response({'error':'email vacibdir'},status=400)
        request.user.email = new_email
        request.user.save()
        return Response({'message':"Email yenilendir",'email':new_email})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'error':'Refresh token yoxdur'},status=400)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message':"Cixis olundu"})
        except Exception:
            return Response({"error":'Token etibarsiz ve ya artiq istifade edilib'},400)

class ProtectedDataView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        return Response({
            "message": f'Salam {request.user.username}, bu melumat yalniz sene gorunur',
            'user_id':request.user.id,
            'is_staff':request.user.is_staff
        }) 