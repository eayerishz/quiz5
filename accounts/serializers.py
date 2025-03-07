from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['bio', 'profile_picture', 'phone_number', 'address', 'createdAt', 'updatedAt']

class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()  # Nested AccountSerializer to include account fields

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'account']  # Include 'account' for profile data
