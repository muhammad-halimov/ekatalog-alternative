from ekatalog_alternative.apps.base.models.user import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'name',
            'surname',
            'patronymic',
            'email',
            'avatar',
            'groups',
            'created',
            'updated',
        ]
