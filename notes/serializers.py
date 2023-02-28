from rest_framework import serializers

from .models import Note


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'caption', 'content', 'reminder_time', 'tags']


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'caption', 'content', 'reminder_time', 'tag']
