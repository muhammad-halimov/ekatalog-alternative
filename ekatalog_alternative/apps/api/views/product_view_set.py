from ekatalog_alternative.apps.base.models.product import Product
from rest_framework import permissions, viewsets
from ekatalog_alternative.apps.api.serializers.product_serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('created')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
