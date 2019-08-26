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
