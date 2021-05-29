from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from eaptekahack.models import TreatmentCourse
from eaptekahack.serializers.treatment_course import TreatmentCourseSerializer


class TreatmentCourseViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = TreatmentCourseSerializer

    def get_queryset(self):
        queryset = TreatmentCourse.objects.filter(user=self.request.user)
        return queryset
