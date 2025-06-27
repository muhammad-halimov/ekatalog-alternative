"""
URL configuration for ekatalog_alternative project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import ekatalog_alternative.apps.base.views.parse_wb_view
from ekatalog_alternative.apps.api.services.redirector import Redirector

urlpatterns = [
    path('', Redirector.admin_redirect, name='admin_redirect'),
    path('', include(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))),

    path('admin/', admin.site.urls),
    path('api/', Redirector.api_redirect, name='api_redirect'),
    path('api/', include('ekatalog_alternative.apps.api.urls')),

    path(
        route='parse-wb/',
        view=ekatalog_alternative.apps.base.views.parse_wb_view.parse_wb_view,
        name='parse_wb'
    ),
]
