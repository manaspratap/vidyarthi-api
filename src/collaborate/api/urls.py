from django.urls import path
from collaborate.api.views import(
    collaborate_create_view,
)

app_name = 'collaborate'

urlpatterns = [
    path('create', collaborate_create_view, name="collaborate_create"),
]
