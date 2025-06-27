from ekatalog_alternative.apps.base.models.product import Product
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # Для записи - только ID
    category_id = serializers.IntegerField(
        write_only=True,
        required=False,
        allow_null=True
    )
    shop_id = serializers.IntegerField(
        write_only=True,
        required=False,
        allow_null=True
    )

    # Для просмотра - только название
    category = serializers.StringRelatedField()
    shop = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'category',
            'category_id',  # для записи
            'shop',
            'shop_id', # для записи
            'price',
            'url',
            'brand',
            'model',
            'specifications',
            'image',
            'created',
            'updated',
        ]
