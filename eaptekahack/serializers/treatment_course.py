from rest_framework import serializers

from eaptekahack.models import Products, TreatmentCourse


class TreatmentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentCourse
        fields = ['user', 'drug', 'schedule_info', 'quantity', 'quantity_exists']


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='ID', read_only=True)
    name = serializers.CharField(source='NAME', read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'name']
