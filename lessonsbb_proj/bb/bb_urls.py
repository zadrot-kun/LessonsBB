from django.urls import path
from bb.views import (CreateRubricController,
                      test_json_controller,
                      CreateBBController,
                      index_by_rubric,
                      create_bb,
                      update_bb)

urlpatterns = [
    path('create_rubric/', CreateRubricController.as_view(), name="create_rubric"),
    # path('create_bb/', CreateBBController.as_view(), name="create_bb",),
    path('create_bb/', create_bb, name="create_bb",),
    path('update_bb/<int:bb_pk>/', update_bb, name="update_bb",),
    path('test_json/', test_json_controller),
    path('rubrics/<int:rubric>/', index_by_rubric, name="bb_by_rubric")
]
