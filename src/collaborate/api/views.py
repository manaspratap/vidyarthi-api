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
from collaborate.models import CollaborateMLModel
from collaborate.api.serializers import CollaborateMLSerializer

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

# Headers: Authorization: Token <token>
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def collaborate_view(request):

    data = {}
    if request.method == 'POST':
        searchWord = request.data.get('search_word',0)
        collaborateData = projectCollaborate(searchWord, request)
        serializer = CollaborateMLSerializer(collaborateData, many = True)
        return Response(serializer.data)

import pandas as pd
from pandas import DataFrame
import random

def adjust_compat_team_attributes(attribute_name, user, collaborator):
    if user[attribute_name] == 0 or collaborator[attribute_name[5:]] == 0:
        return 0
    return abs(user[attribute_name] - collaborator[attribute_name[5:]]) * -5
        
def adjust_compat_standalone_attributes(attribute_name, user, collaborator):
    if user[attribute_name] == 0 or collaborator[attribute_name] == 0:
        return 0
    return abs(user[attribute_name] - collaborator[attribute_name]) * -5

    
def projectCollaborate(searchWord, request):    
    projectprofiles = pd.read_csv('./user-project-profiles.csv')
    user_id = request.user.pk 
    project_track = searchWord

    print('------12321------'+searchWord)

    matching_track_profiles = DataFrame(columns=projectprofiles.columns)
    k = 1

    for index, row in projectprofiles.iterrows():
        if row['User_ID'] == user_id:
            user_profile = row
            continue
        tracks = row['Tracks_Worked_On'].split('.')
        if project_track in tracks:
            matching_track_profiles.loc[k] = row
            k+=1
        
    matching_track_profiles["Compatibility_Score"] = 100

    compat_attributes = ['Team_Work_Time_Preference', 'Alignment_of_Work', 'Team_Learn_and_Work_Preference', 'Team_Working_Hours_Preference', 'Mode_of_Communication_Preference', 'Style_of_Communication_Preference']


    for index, row in matching_track_profiles.iterrows():
        compat_adjust = 0
        for attribute in compat_attributes:
            if attribute[0:4] == 'Team':
                compat_adjust += adjust_compat_team_attributes(attribute, user_profile, row)
            else:
                compat_adjust += adjust_compat_standalone_attributes(attribute, user_profile, row)
        row["Compatibility_Score"] = row["Compatibility_Score"] + compat_adjust
        matching_track_profiles.loc[index] = row

    matching_profiles_dict = list()

    for index, row in matching_track_profiles.iterrows():
        matching_profiles_dict.append({
            'collaborateId': row['User_ID'],
            'collaborateName': row['Name'],
            'collaboratePrimaryTrack': searchWord,
            'collaborateAbout': row['About'],
            'collaborateCScore': int(row['Compatibility_Score']),
            'collaborateEScore': int(row['eScore']),
            'collaborateMScore': int(row['Compatibility_Score'] * 0.5 + row['eScore'])
        })

    return(matching_profiles_dict)
