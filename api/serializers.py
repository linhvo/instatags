from rest_framework import serializers

from api.models import InstagramUser, Media


class InstagramUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    full_name = serializers.CharField()

    class Meta:
        model = InstagramUser
        fields = ('username', 'full_name',)

class MediaSerializer(serializers.Serializer):
    url = serializers.CharField()
    instagram_user = InstagramUserSerializer()
    created_date = serializers.DateTimeField()

    class Meta:
        model = Media
        fields = ('url', 'instagram_user', 'created_date',)