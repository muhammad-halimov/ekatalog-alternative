from ekatalog_alternative.apps.base.models.shop import Shop
from rest_framework import permissions, viewsets
from ekatalog_alternative.apps.api.serializers.shop_serializer import ShopSerializer


class ShopViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Shop.objects.all().order_by('created')
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticated]
