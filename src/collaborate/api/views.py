from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from account.models import Account
from collaborate.models import CollaborateModel
from collaborate.api.serializers import CollaborateSerializer

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

# Headers: Authorization: Token <token>
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def collaborate_create_view(request):

    if request.method == 'POST':

        data = request.data
        data['author'] = request.user.pk
        serializer = CollaborateSerializer(data=data)

        data = {}
        if serializer.is_valid():
            collaborate_detail = serializer.save()
            data['response'] = CREATE_SUCCESS
            data['userId'] = collaborate_detail.userId
            data['workDuring'] = collaborate_detail.workDuring
            data['otherWorkDuring'] = collaborate_detail.otherWorkDuring
            data['workWith'] = collaborate_detail.workWith
            data['communicateOver'] = collaborate_detail.communicateOver
            data['communicateWith'] = collaborate_detail.communicateWith
            data['workBy'] = collaborate_detail.workBy
            data['otherWorkBy'] = collaborate_detail.otherWorkBy
            data['workHours'] = collaborate_detail.workHours
            data['otherWorkHours'] = collaborate_detail.otherWorkHours
            data['projectDuration'] = collaborate_detail.projectDuration

            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
