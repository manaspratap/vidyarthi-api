from django.urls import path
from collaborate.api.views import(
    collaborate_view,
)

app_name = 'collaborate'

urlpatterns = [
    path('collaborate/read', collaborate_view, name="collaborate_read"),
]
