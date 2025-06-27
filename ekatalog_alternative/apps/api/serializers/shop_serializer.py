from ekatalog_alternative.apps.base.models.shop import Shop
from rest_framework import serializers


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = [
            'id',
            'title',
            'address',
            'url',
            'image',
            'description',
            'created',
            'updated',
        ]
