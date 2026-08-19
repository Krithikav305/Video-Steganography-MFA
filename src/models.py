from django.db import models


class AuthDetails(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    audio = models.CharField(max_length=255)
    video_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
