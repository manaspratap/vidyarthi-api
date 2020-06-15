from django.urls import path
from me.api.views import(
    collaborate_create_view,
    project_create_view,
    course_create_view,
)

app_name = 'me'

urlpatterns = [
    path('collaborate/create', collaborate_create_view, name="collaborate_create"),
    path('project/create', project_create_view, name="project_create"),
    path('course/create', course_create_view, name="course_create"),
]
