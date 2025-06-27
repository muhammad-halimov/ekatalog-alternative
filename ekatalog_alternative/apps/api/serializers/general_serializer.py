from ekatalog_alternative.apps.base.models.general import General
from rest_framework import serializers


class GeneralSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = General
        fields = [
            'id',
            'wb_id',
            'title',
            'category',
            'price_discount',
            'price_original',
            'rating',
            'review',
            'link',
            'photo',
            'created',
            'updated',
        ]
