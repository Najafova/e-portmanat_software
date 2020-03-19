from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ['pk', 'imei_code', 'longitude', 'latitude', 'battery']


class MobileDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MobileData
        fields = ['pk', 'imei_code', 'longitude', 'latitude', 'battery']


class  MobileDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MobileData
        fields = ['pk', 'imei_code', 'longitude', 'latitude', 'battery']
