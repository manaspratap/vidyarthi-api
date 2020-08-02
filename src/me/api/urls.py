from django.urls import path
from me.api.views import(
    collaborate_read_view,
    collaborate_create_view,
    project_read_view,
    project_create_view,
    course_read_view,
    course_create_view,
    suggestion_create_view,
)

app_name = 'me'

urlpatterns = [
    path('collaborate/read', collaborate_read_view, name="collaborate_read"),
    path('collaborate/create', collaborate_create_view, name="collaborate_create"),
    path('project/read', project_read_view, name="project_read"),
    path('project/create', project_create_view, name="project_create"),
    path('course/read', course_read_view, name="course_read"),
    path('course/create', course_create_view, name="course_create"),
    path('suggestion/create', suggestion_create_view, name="suggestion_create")
]
