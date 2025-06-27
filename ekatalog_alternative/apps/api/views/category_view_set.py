from ekatalog_alternative.apps.base.models.category import Category
from rest_framework import permissions, viewsets
from ekatalog_alternative.apps.api.serializers.category_serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('created')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
