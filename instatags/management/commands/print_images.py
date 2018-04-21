import os

import requests
from PIL import Image
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
        try:
            tag = Tag.objects.get(tag_name=tag_name)
        except ObjectDoesNotExist:
            self.stdout.write('%s does not exist' % tag_name)
            return

        medias = Media.objects.filter(tag=tag, is_photo=True)
        for media in medias:
            img_data = requests.get(media.url).content
            with open('./instatags/picture_out.jpg', 'wb') as f:
                f.write(img_data)
            print('Printing')
            os.system("lpr /Users/trung/dev/instatags/picture_out.jpg")

        self.stdout.write('Done')


def compress(original_file, max_size, scale):
    assert(0.0 < scale < 1.0)
    orig_image = Image.open(original_file)
    cur_size = orig_image.size

    while True:
        cur_size = (int(cur_size[0] * scale), int(cur_size[1] * scale))
        resized_file = orig_image.resize(cur_size, Image.ANTIALIAS)

        with io.BytesIO() as file_bytes:
            resized_file.save(file_bytes, optimize=True, quality=95, format='jpeg')

            if file_bytes.tell() <= max_size:
                file_bytes.seek(0, 0)
                with open(original_file, 'wb') as f_output:
                    f_output.write(file_bytes.read())
                break

