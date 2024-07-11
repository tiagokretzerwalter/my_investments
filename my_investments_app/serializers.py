from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password', 'name', 'is_active', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8, 'required': True},
            'is_staff': {'required': False},
            'is_active': {'required': False}
            }

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(
            password=password,
            **validated_data
        )
        return user

    def update(self, instance, validated_data):
        """Update an user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)