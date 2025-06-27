from django.contrib.auth.models import Group, Permission
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    permissions = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'permissions',
        ]
