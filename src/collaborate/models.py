from django.db import models

# Create your models here.
class CollaborateMLModel(models.Model):

    collaborateId = models.AutoField(primary_key=True)
    collaborateName = models.CharField(max_length=512)
    collaboratePrimaryTrack = models.CharField(max_length=512)
    collaborateAbout = models.CharField(max_length=512)
    collaborateCScore = models.IntegerField()
    collaborateEScore = models.IntegerField()
    collaborateMScore = models.IntegerField()

    def __str__(self):
        return self.courseTitle