from rest_framework import serializers

from eaptekahack.models import MedicationAvailable, Products, TreatmentCourse


class TreatmentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentCourse
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class MedicationAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationAvailable
        fields = '__all__'
