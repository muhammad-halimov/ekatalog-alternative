from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from ekatalog_alternative.apps.api.views.user_view_set import UserViewSet
# from ekatalog_alternative.apps.api.views.category_view_set import CategoryViewSet
from ekatalog_alternative.apps.api.views.group_view_set import GroupViewSet
# from ekatalog_alternative.apps.api.views.product_view_set importCategoryViewSet
# from ekatalog_alternative.apps.api.views.shop_view_set impCategoryViewSet
from ekatalog_alternative.apps.api.views.general_view_set import GeneralViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
# router.register(r'categories', CategoryViewSet)
# router.register(r'products', ProductViewSet)
# router.register(r'shops', ShopViewSet)
router.register(r'products', GeneralViewSet)

urlpatterns = [
    path('yaml-export/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
