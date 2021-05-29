from rest_framework import serializers

from eaptekahack.models import MedicationAvailable, Products, TreatmentCourse


class TreatmentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentCourse
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='ID', read_only=True)
    name = serializers.CharField(source='NAME', read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'name']


class MedicationAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationAvailable
        fields = '__all__'
