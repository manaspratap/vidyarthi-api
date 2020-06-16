from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from account.models import Account
from me.models import CollaborateModel, ProjectModel, CourseModel
from me.api.serializers import CollaborateSerializer, ProjectSerializer, CourseSerializer

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

# Headers: Authorization: Token <token>
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def collaborate_view(request):
    try:
        collaborate = CollaborateModel.objects.get(
            userId=request.query_params.get('userId'))
    except CollaborateModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CollaborateSerializer(collaborate)
        return Response(serializer.data)
