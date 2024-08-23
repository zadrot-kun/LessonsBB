from django.contrib import admin
from django.urls import path, include
from bb.views import index, IndexClass
from django.conf.urls.static import static
from lessonsbb_proj import settings

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('bb/', include('bb.bb_urls')),
    # path('', index, name="index"),
    path('', IndexClass.as_view(), name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
