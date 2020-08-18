from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django.http import JsonResponse

from account.models import Account
from me.models import CollaborateModel, ProjectModel, CourseModel, SuggestionModel, MeAccountModel
from me.api.serializers import CollaborateSerializer, ProjectSerializer, CourseSerializer, SuggestionSerializer, MeAccountSerializer

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

# Headers: Authorization: Token <token>
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def account_read_view(request):
    try:
        meAccount = MeAccountModel.objects.get(
            userId=request.query_params.get('userId'))
    except CollaborateModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MeAccountSerializer(meAccount)
        return Response(serializer.data)

# Headers: Authorization: Token <token>
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def account_create_view(request):

    if request.method == 'POST':

        data = request.data
        data['author'] = request.user.pk
        serializer = MeAccountSerializer(data=data)

        data = {}
        if serializer.is_valid():
            account_detail = serializer.save()
            data['response'] = CREATE_SUCCESS
            data['about'] = account_detail.about
            data['primaryTrack'] = account_detail.primaryTrack
            data['userId'] = account_detail.userId

            return Response(data=data)
        if serializer.errors['userId'][0] == 'me account model with this userId already exists.':
            updateData = MeAccountModel.objects.get(userId=int(request.data['userId']))
            updateData.about = request.data['about']
            updateData.primaryTrack = request.data['primaryTrack']
            updateData.save()
            data['response'] = UPDATE_SUCCESS
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Headers: Authorization: Token <token>
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def collaborate_read_view(request):
    try:
        collaborate = CollaborateModel.objects.get(
            userId=request.query_params.get('userId'))
    except CollaborateModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CollaborateSerializer(collaborate)
        return Response(serializer.data)


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
        if serializer.errors['userId'][0] == 'collaborate model with this userId already exists.':
            updateData = CollaborateModel.objects.get(userId=int(request.data['userId']))
            updateData.workDuring = request.data['workDuring']
            updateData.otherWorkDuring = request.data['otherWorkDuring']
            updateData.workWith = request.data['workWith']
            updateData.communicateOver = request.data['communicateOver']
            updateData.communicateWith = request.data['communicateWith']
            updateData.workBy = request.data['workBy']
            updateData.otherWorkBy = request.data['otherWorkBy']
            updateData.workHours = request.data['workHours']
            updateData.otherWorkHours = request.data['otherWorkHours']
            updateData.projectDuration = request.data['projectDuration']
            updateData.save()
            data['response'] = UPDATE_SUCCESS
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Headers: Authorization: Token <token>
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def project_read_view(request):
    try:
        project = ProjectModel.objects.filter(userId=request.query_params.get('userId'))
    except ProjectModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project, many = True)
        return Response(serializer.data)

# Headers: Authorization: Token <token>
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def project_create_view(request):

    if request.method == 'POST':

        data = request.data
        data['author'] = request.user.pk
        serializer = ProjectSerializer(data=data)

        data = {}
        if serializer.is_valid():
            project_detail = serializer.save()
            data['response'] = CREATE_SUCCESS
            data['projectTitle'] = project_detail.projectTitle
            data['projectLink'] = project_detail.projectLink
            data['about'] = project_detail.about
            data['primaryTrack'] = project_detail.primaryTrack
            data['userId'] = project_detail.userId

            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Headers: Authorization: Token <token>
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def course_read_view(request):
    try:
        course = CourseModel.objects.filter(userId=request.query_params.get('userId'))
    except CourseModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course, many = True)
        return Response(serializer.data)

# Headers: Authorization: Token <token>
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def course_create_view(request):

    if request.method == 'POST':

        data = request.data
        data['author'] = request.user.pk
        serializer = CourseSerializer(data=data)

        data = {}
        if serializer.is_valid():
            course_detail = serializer.save()
            data['response'] = CREATE_SUCCESS
            data['courseTitle'] = course_detail.courseTitle
            data['courseLink'] = course_detail.courseLink
            data['coursePublisher'] = course_detail.coursePublisher
            data['primaryTrack'] = course_detail.primaryTrack
            data['rating'] = course_detail.rating
            data['difficulty'] = course_detail.difficulty
            data['userId'] = course_detail.userId

            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Headers: Authorization: Token <token>
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def suggestion_create_view(request):

    if request.method == 'POST':

        data = request.data
        data['userId'] = request.data.get('userId',0)
        data['category'] = request.data.get('category',0)
        data['message'] = request.data.get('message',0)
        serializer = SuggestionSerializer(data=data)

        data = {}
        if serializer.is_valid():
            course_detail = serializer.save()
            data['response'] = CREATE_SUCCESS
            return Response(data=data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
