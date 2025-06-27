from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets
from ekatalog_alternative.apps.api.serializers.group_serializer import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
