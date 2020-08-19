from rest_framework import serializers

from course.models import CourseMLModel


class CourseMLSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseMLModel
        fields = ['courseId','courseTitle', 'courseLink', 'coursePublisher',
                  'primaryTrack', 'rating', 'difficulty', 'recommended']