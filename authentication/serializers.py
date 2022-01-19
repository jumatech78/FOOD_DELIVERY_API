from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
 username=serializers.models.CharField(max_length=25)
 email=serializers.models.EmailField(max_length=80)
 phone_number=PhoneNumberField(allow_null=False,allow_blank=False)