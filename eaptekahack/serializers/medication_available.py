from abc import ABC

from rest_framework import serializers


class MedicationAvailableSerializer(serializers.Serializer, ABC):
    model_input = serializers.IntegerField()

