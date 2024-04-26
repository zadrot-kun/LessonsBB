from django.contrib import admin
from django.urls import path, include
from bb.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bb/', include('bb.bb_urls')),
    path('', index),
]
