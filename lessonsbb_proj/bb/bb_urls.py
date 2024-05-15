from django.urls import path
from bb.views import CreateRubricController, rubric_list, CreateBBController, index_by_rubric

urlpatterns = [
    path('create_rubric/', CreateRubricController.as_view(), name="create_rubric"),
    path('create_bb/', CreateBBController.as_view(), name="create_bb",),
    path('json_rubrics/', rubric_list),
    path('rubrics/<int:rubric>/', index_by_rubric, name="bb_by_rubric")
]
