from django.urls import path
from bb.views import (CreateRubricController,
                      test_json_controller,
                      CreateBBController,
                      index_by_rubric,
                      create_bb,
                      update_bb,
                      update_bb_comments,
                      update_bb_images,
                      BBs_REST,
                      BB_REST)

urlpatterns = [
    path('create_rubric/', CreateRubricController.as_view(), name="create_rubric"),
    # path('create_bb/', CreateBBController.as_view(), name="create_bb",),
    path('create_bb/', create_bb, name="create_bb",),
    path('update_bb/<int:bb_pk>/', update_bb, name="update_bb",),
    path('update_bb/<int:bb_pk>/comments', update_bb_comments, name="update_bb_comments",),
    path('update_bb/<int:bb_pk>/images', update_bb_images, name="update_bb_images", ),
    path('test_json/', test_json_controller),
    path('rubrics/<int:rubric>/', index_by_rubric, name="bb_by_rubric"),
    path('bbs_rest/', BBs_REST.as_view()),
    path('bbs_rest/<int:bb_id>/', BB_REST.as_view()),
]
