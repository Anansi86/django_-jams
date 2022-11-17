#from django.contrib.auth.models import User, Group
from .models import song
from rest_framework import serializers






# class JamappSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = jamapp
#         fields = "__all__"


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']