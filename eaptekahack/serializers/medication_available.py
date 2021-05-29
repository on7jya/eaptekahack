from rest_framework import serializers


class MedicationAvailableSerializer(serializers.Serializer):
    model_input = serializers.IntegerField()
