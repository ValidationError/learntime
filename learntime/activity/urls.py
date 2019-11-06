from django.urls import path

from learntime.activity import views

app_name = "activities"
urlpatterns = [

    path('', view=views.ActivityList.as_view(), name='activities'),
    path('activity-create', view=views.ActivityCreate.as_view(), name='activity_create'),
    path('activity-detail/<str:pk>/', view=views.ActivityDetail.as_view(), name='activity_detail'),
    path('activity-update/<str:pk>/', view=views.ActivityUpdate.as_view(), name='activity_update'),
    # path('student-create/', view=views.StudentCreate.as_view(), name='student_create'),

    # path("student-delete/<int:pk>/", view=views.StudentDelete.as_view(), name='student_delete'),

]
