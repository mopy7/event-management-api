from rest_framework import serializers
from events.models import Event
from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
    model = Event
    fields = [
      'id',
      'title',
      'description',
      'location',
      'date',
      'is_active',
      'owner',
      'created_at',
      'updated_at',
    ]
    read_only_fields = ['owner']

class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'password']
  
  def create(self, validated_data):
    return User.objects.create_user(
      username=validated_data['username'],
      email=validated_data.get('email'),
      password=validated_data['password']
    )

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()
