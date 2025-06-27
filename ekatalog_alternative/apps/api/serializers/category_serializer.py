from ekatalog_alternative.apps.base.models.category import Category
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'description',
            'created',
            'updated',
        ]
