from django.urls import path
from bb.views import CreateRubricController

urlpatterns = [
    path('create_rubric/', CreateRubricController.as_view())
]
