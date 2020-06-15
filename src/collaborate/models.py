from django.db import models


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
