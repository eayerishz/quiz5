from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account  

class UserSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(source='account.bio', allow_blank=True, required=False)
    profile_picture = serializers.ImageField(source='account.profile_picture', allow_null=True, required=False)
    phone_number = serializers.CharField(source='account.phone_number', allow_blank=True, required=False)
    address = serializers.CharField(source='account.address', allow_blank=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 'phone_number', 'address']
