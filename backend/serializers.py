from rest_framework import serializers
from models import TtsEntry

class TtsEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TtsEntry
        field = '__all__'