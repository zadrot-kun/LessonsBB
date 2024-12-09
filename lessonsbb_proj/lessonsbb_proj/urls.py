from django.contrib import admin
from django.urls import path, include
from bb.views import index, IndexClass
from django.conf.urls.static import static
from lessonsbb_proj import settings
from customauth.views import Login, PasswordChange, PasswordChangeDone
from django.contrib.auth.views import LogoutView
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator
from rest_framework import permissions
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="BBoard API",
        default_version=f'v0.1',
        description="API проекта доски объявлений",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('bb/', include('bb.bb_urls')),
    # path('', index, name="index"),
    path('', IndexClass.as_view(), name="index"),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDone.as_view(), name='password_change_done'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
