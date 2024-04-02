from rest_framework import serializers
from .models import Vote, Choice, Poll
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'

class UserSrializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_date):
        user = User(
            email=validated_date['email'],
            username=validated_date['username']
        )
        user.set_password(validated_date['password'])
        user.save()
        Token.objects.create(user=user)
        return user