from rest_framework import serializers

from .models import Note, Tag


class NoteViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'caption', 'content', 'reminder_time', 'tags', 'user']


class NoteUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Note
        fields = ['id', 'caption', 'content', 'reminder_time', 'tag', 'user']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
