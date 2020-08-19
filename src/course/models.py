from django.db import models

# Create your models here.
class CourseMLModel(models.Model):

    courseId = models.AutoField(primary_key=True)
    courseTitle = models.CharField(max_length=512)
    courseLink = models.CharField(max_length=512)
    coursePublisher = models.CharField(max_length=512)
    primaryTrack = models.CharField(max_length=512)
    rating = models.IntegerField()
    difficulty = models.IntegerField()
    recommended = models.IntegerField()

    def __str__(self):
        return self.courseTitle