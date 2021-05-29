from rest_framework import serializers

from eaptekahack.models import MedicationAvailable


class MedicationAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationAvailable
        fields = ['user', 'drug', 'number_of_pills']
