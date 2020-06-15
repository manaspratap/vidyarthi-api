from django.db import models
import account


class CollaborateModel(models.Model):
    userId = models.CharField(primary_key=True, max_length=512)
    workDuring = models.CharField(max_length=512)
    otherWorkDuring = models.CharField(max_length=512)
    workWith = models.CharField(max_length=512)
    communicateOver = models.CharField(max_length=512)
    communicateWith = models.CharField(max_length=512)
    workBy = models.CharField(max_length=512)
    otherWorkBy = models.CharField(max_length=512)
    workHours = models.CharField(max_length=512)
    otherWorkHours = models.CharField(max_length=512)
    projectDuration = models.CharField(max_length=512)

    def __str__(self):
        return self.userId


class ProjectModel(models.Model):

    projectId = models.AutoField(primary_key=True)
    projectTitle = models.CharField(max_length=512)
    projectLink = models.CharField(max_length=512)
    about = models.CharField(max_length=512)
    primaryTrack = models.CharField(max_length=512)
    userId = models.CharField(max_length=512)

    def __str__(self):
        return self.projectTitle


class CourseModel(models.Model):

    courseId = models.AutoField(primary_key=True)
    courseTitle = models.CharField(max_length=512)
    courseLink = models.CharField(max_length=512)
    coursePublisher = models.CharField(max_length=512)
    primaryTrack = models.CharField(max_length=512)
    rating = models.IntegerField()
    difficulty = models.IntegerField()
    userId = models.CharField(max_length=512)

    def __str__(self):
        return self.courseTitle
