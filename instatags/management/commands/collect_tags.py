import os

import requests
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from api.models import *

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('tag_name', nargs='+')
        # parser.add_argument('loc_lat', nargs='+')
        # parser.add_argument('loc_long', nargs='+')

    def handle(self, *args, **options):
        tag_name = options['tag_name'][0]
        url = "https://api.instagram.com/v1/tags/%s/media/recent?access_token=%s" % (tag_name, ACCESS_TOKEN)
        res = requests.get(url)
        data = res.json()['data']
        for dt in data:
            location = dt['location']
            tag, _ = Tag.objects.get_or_create(tag_name=tag_name)
            try:
                user = InstagramUser.objects.get(username=dt['user']['username'])
            except ObjectDoesNotExist:
                # ToDo: Log this errors
                self.stdout.write('User %s is not registered' % dt['user']['username'])
                return
            media, _ = Media.objects.get_or_create(url=dt['images']['standard_resolution']['url'], instagram_user=user, tag=tag)
            if dt['type'] != 'image':
                media.is_photo = False
                media.save()
            Location.objects.get_or_create(loc_id=location['id'], loc_lat=location['latitude'], loc_long=location['longitude'], name=location['name'])
        print(data)
        self.stdout.write('Done')