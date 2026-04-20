from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True,min_length=7)
    class Meta:
        model = User
        fields = ['username','email','password']
    def validate_username(self,value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Bu username var")
        return value
    def create(self,validate_data):
        return User.objects.create_user(**validate_data)
class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email',"date_joined"]
        read_only_fields = fields
    
class CustomTokenSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token
