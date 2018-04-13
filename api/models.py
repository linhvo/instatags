
from django.db import models


class InstagramUser(models.Model):
    access_token = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    instagram_id = models.BigIntegerField()

