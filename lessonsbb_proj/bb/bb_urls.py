from django.urls import path
from bb.views import CreateRubricController, rubric_list

urlpatterns = [
    path('create_rubric/', CreateRubricController.as_view()),
    path('json_rubrics/', rubric_list)
]
