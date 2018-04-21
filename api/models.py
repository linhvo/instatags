
from django.db import models


class InstagramUser(models.Model):
    access_token = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    instagram_id = models.BigIntegerField()
    created_date = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    tag_name = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now=True)

class Media(models.Model):
    url = models.CharField(max_length=1000)
    instagram_user = models.ForeignKey(InstagramUser, related_name='media')
    tag = models.ForeignKey(Tag, related_name='media_tag')
    is_photo = models.BooleanField(default=True)
    created_time = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)


class Location(models.Model):
    loc_id = models.BigIntegerField()
    loc_lat = models.DecimalField(decimal_places=6, max_digits=9)
    loc_long = models.DecimalField(decimal_places=6, max_digits=9)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)

