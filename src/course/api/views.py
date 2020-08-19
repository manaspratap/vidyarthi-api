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
from course.models import CourseMLModel
from course.api.serializers import CourseMLSerializer

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

# Headers: Authorization: Token <token>
@api_view(['POST', ])
@permission_classes((IsAuthenticated, ))
def course_view(request):

    data = {}
    if request.method == 'POST':
        searchWord = request.data.get('search_word',0)
        recommendCourseData = recommendCourse(searchWord)
        serializer = CourseMLSerializer(recommendCourseData, many = True)
        return Response(serializer.data)

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import random

def feature_combination(row):
    return row["course_title"] + " " + row["platform"] + " " + str(row["course_index"]) + " " + str(row["difficulty"])

def tokenize_remove_stopwords(sentence, _stopwords):
    word_tokens = word_tokenize(sentence)
    word_tokens_cleaned = {word for word in word_tokens if word not in _stopwords}
    return ' '.join(list(word_tokens_cleaned))

def recommendCourse(searchWord):

    dataset = pd.read_csv("all-course-data.csv")

    dataset["difficulty"] = dataset["level"].map({"Advanced":100, "advanced":90, "All Levels":50, "Mixed":60, "Expert Level":80, "Intermediate": 40, "intermediate ":40, "intermediate":40, "Intermediate Level":45, "beginner":10, "Beginner":20, "Beginner Level":30})
    dataset.drop("level", axis=1, inplace=True)

    features = ["course_title", "course_index", "difficulty", "platform"]

    dataset["cumulative_features"] = dataset.apply(feature_combination, axis = 1)

    cv = CountVectorizer()
    _stopwords = stopwords.words('english')

    user_preference = searchWord
    user_difficulty = 40

    user_preference_string = tokenize_remove_stopwords(user_preference, _stopwords).title()

    required_data = dataset[features]
    required_data.loc[len(required_data)] = [user_preference_string, len(required_data), user_difficulty, "None"] 
    word_bag = cv.fit_transform(required_data["course_title"])
    word_list = word_bag.toarray()
    csim = cosine_similarity(word_list)

    similar_courses = list(enumerate(csim[len(required_data) - 1]))
    sorted_similar_courses = sorted(similar_courses,key=lambda x:x[1],reverse=True)[1:50]
    i=0
    recommended_courses = list()
    for element in sorted_similar_courses:
        course = dataset.loc[element[0]]
        if(course["difficulty"] >= user_difficulty - 15 and course["difficulty"] <= user_difficulty + 15 and element[0] != len(required_data) - 1):
            recommended_courses.append(
            {
                'courseId': course["course_index"], 
                'courseTitle': course["course_title"], 
                'courseLink': course["url"], 
                'coursePublisher': course["platform"], 
                'primaryTrack': "All Developement", 
                'rating': random.randint(71, 100), 
                'difficulty': course["difficulty"],
                'recommended': 100 - abs(user_difficulty - course["difficulty"])            
            })
    
    return recommended_courses
