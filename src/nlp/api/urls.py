from django.urls import path
from nlp.api.views import(
    nlp_view,
)

app_name = 'nlp'

urlpatterns = [
    path('read', nlp_view, name="nlp_read"),
]
