from django.contrib import admin
from django.urls import path

from bb.models import Rubric, Bulletin

print(Rubric, Bulletin)

urlpatterns = [
    path('admin/', admin.site.urls),
]
