from rest_framework import serializers

from collaborate.models import CollaborateMLModel


class CollaborateMLSerializer(serializers.ModelSerializer):

    class Meta:
        model = CollaborateMLModel
        fields = ['collaborateId','collaborateName', 'collaboratePrimaryTrack', 'collaborateAbout',
                  'collaborateCScore', 'collaborateEScore', 'collaborateMScore']