from rest_framework import serializers
from bb.models import Bulletin as BulletinModel
from comments.models import Comment as CommentModel


class BulletinSerializer(serializers.ModelSerializer):

    class Meta:
        model = BulletinModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentModel
        exclude = ['bb']


class BulletinCommentsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = BulletinModel
        fields = '__all__'
