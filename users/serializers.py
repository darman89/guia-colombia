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

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'address', 'phone', 'password', 'confirm_password',
                  'username')

    def create(self, validated_data):
        # Validate the password
        # username = validated_data['email']
        # validated_data['username'] = username
        password = validated_data.get('password', None)
        confirm_password = validated_data.pop('confirm_password', None)
        if not has_valid_password(password, confirm_password):
            raise ValidationError('The password did not match with the confirm password field')
        return User.objects.create_user(**validated_data)

    def partial_update(self, instance, validated_data):
        if validated_data['password'] and validated_data['confirm_password']:
            password = validated_data.get('password', None)
            confirm_password = validated_data.pop('confirm_password', None)
            if not has_valid_password(password, confirm_password):
                raise ValidationError('The password did not match with the confirm password field')
            instance.password = validated_data.get('password', instance.password)
            instance.confirm_password = validated_data.get('confirm_password', instance.confirm_password)
        else:
            instance.email = validated_data.get('email', instance.email)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.address = validated_data.get('address', instance.address)
            instance.phone = validated_data.get('phone', instance.phone)
            instance.save()
        return instance
