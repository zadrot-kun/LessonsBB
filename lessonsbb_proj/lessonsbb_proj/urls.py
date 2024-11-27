from django.contrib import admin
from django.urls import path, include
from bb.views import index, IndexClass
from django.conf.urls.static import static
from lessonsbb_proj import settings
from customauth.views import Login

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('bb/', include('bb.bb_urls')),
    # path('', index, name="index"),
    path('', IndexClass.as_view(), name="index"),
    path('login/', Login.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
