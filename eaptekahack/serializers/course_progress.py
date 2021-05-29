from rest_framework import serializers

from eaptekahack.models import CourseProgress


class CourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProgress
        fields = ['user', 'drug', 'date', 'has_taken']
