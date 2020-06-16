from django.urls import path
from course.api.views import(
    course_view,
)

app_name = 'course'

urlpatterns = [
    path('course/read', course_view, name="course_read"),
]
