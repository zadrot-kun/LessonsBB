from django.contrib import admin
from django.urls import path, include
from bb.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bb/', include('bb.bb_urls')),
    path('', index, name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
