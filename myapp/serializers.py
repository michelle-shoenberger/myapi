from rest_framework import serializers
from .models import Drink, User, Food
from rest_framework.authtoken.models import Token

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['name', 'price', 'description']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'price', 'description', 'bread']


class UserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'auth_token']
        read_only_fields = ('username', )

    def get_auth_token(self, obj):
        token = Token.objects.get(user=obj)
        return token.key

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)