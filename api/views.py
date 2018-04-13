import json
import os

import requests
from instagram import client
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from api.models import InstagramUser

CONFIG = {
    'client_id': os.environ.get('CLIENT_ID'),
    'client_secret': os.environ.get('CLIENT_SECRET'),
    'redirect_uri': 'http://127.0.0.1:8000/oauth_callback'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)


@api_view(['GET'])
def home(request):
    try:
        url = unauthenticated_api.get_authorize_url(scope=["basic", "public_content"])
        return Response(url)
    except Exception as e:
        print(e)


@api_view(['GET'])
def on_callback(request):
    code = request.GET.get("code")
    data = None
    if not code:
        return Response('Missing code')
    try:
        url = 'https://api.instagram.com/oauth/access_token'
        data = {
            'client_id': CONFIG['client_id'],
            'client_secret': CONFIG['client_secret'],
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri': CONFIG['redirect_uri']
        }

        response = requests.post(url, data=data)
        data = json.loads(response.content)
        print(data)
        InstagramUser.objects.create(access_toke=data['access_token'],
                                            username=data['user']['username'],
                                            instagram_id=data['user']['id'])
    except Exception as e:
        Response(status=HTTP_400_BAD_REQUEST, data="Error: %s" % e)
    return Response(data['user'])

#
# @api_view(['GET'])