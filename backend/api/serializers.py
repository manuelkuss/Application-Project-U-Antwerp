from rest_framework import serializers
from .models import Note, MgfFile


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class MgfFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MgfFile
        fields = '__all__'