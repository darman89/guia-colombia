from users.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


# Create your views here.


def has_valid_password(password, confirm_password):
    return password is not None and len(password) > 0 and password == confirm_password


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)
    current_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'address', 'phone', 'password', 'confirm_password', 'current_password')

    def create(self, validated_data):
        # Validate the password
        username = validated_data['email']
        validated_data['username'] = username
        password = validated_data.get('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        if not has_valid_password(password, confirm_password):
            raise ValidationError('The password did not match with the confirm password field')
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        if validated_data.get('password') and validated_data.get('confirm_password'):
            current_password = validated_data.get("current_password")
            if not instance.check_password(current_password):
                raise ValidationError('The current password is wrong')
            password = validated_data.get('password', None)
            confirm_password = validated_data.pop('confirm_password', None)
            if not has_valid_password(password, confirm_password):
                raise ValidationError('The password did not match with the confirm password field')
            instance.set_password(password)
        else:
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.address = validated_data.get('address', instance.address)
            instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance
