from rest_framework import serializers

from me.models import CollaborateModel, ProjectModel, CourseModel, SuggestionModel


class CollaborateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CollaborateModel
        fields = ['userId', 'workDuring', 'otherWorkDuring', 'workWith', 'communicateOver',
                  'communicateWith', 'workBy', 'otherWorkBy', 'workHours', 'otherWorkHours', 'projectDuration']


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectModel
        fields = ['projectTitle', 'projectLink',
                  'about', 'primaryTrack', 'userId']


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseModel
        fields = ['courseTitle', 'courseLink', 'coursePublisher',
                  'primaryTrack', 'rating', 'difficulty', 'userId']

class SuggestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SuggestionModel
        fields = ['userId', 'category', 'message']
