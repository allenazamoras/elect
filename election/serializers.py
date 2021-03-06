from election.models import Party, User, Vote

from rest_framework import serializers
from rest_framework.response import Response


class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'name', 'detail')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'firstname', 'lastname')


class LoginSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class AppointSerializer(serializers.ModelSerializer):
    firstname = serializers.ReadOnlyField()
    lastname = serializers.ReadOnlyField()
    username = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'username', 'firstname',
                  'lastname', 'party', 'position')


class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'party', 'position')


class VoteAllSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    detail = serializers.ReadOnlyField()

    class Meta:
        model = Party
        fields = ('id', 'name', 'detail')
