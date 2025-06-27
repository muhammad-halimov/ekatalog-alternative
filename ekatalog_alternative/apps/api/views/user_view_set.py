from ekatalog_alternative.apps.base.models.user import User
from rest_framework import permissions, viewsets
from ekatalog_alternative.apps.api.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('created')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
