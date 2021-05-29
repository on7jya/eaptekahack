from rest_framework import serializers

from eaptekahack.models import TreatmentCourse


class TreatmentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentCourse
        fields = ['user', 'drug', 'schedule_info', 'quantity', 'quantity_exists']

    # @transaction.atomic
    # def update(self, instance: Segment, validated_data):
    #     super().update(instance, validated_data)
    #     categories_ids = self.initial_data.get('categories')
    #     SegmentController.update_segment(instance, categories_ids)
    #     return instance
