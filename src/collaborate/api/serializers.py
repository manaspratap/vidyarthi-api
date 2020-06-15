from rest_framework import serializers

from collaborate.models import CollaborateModel


class CollaborateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CollaborateModel
        fields = ['userId', 'workDuring', 'otherWorkDuring', 'workWith', 'communicateOver',
                  'communicateWith', 'workBy', 'otherWorkBy', 'workHours', 'otherWorkHours', 'projectDuration']
