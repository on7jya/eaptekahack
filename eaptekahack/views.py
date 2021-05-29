from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from config.settings import DEBUG
from eaptekahack.models import Products, TreatmentCourse
from eaptekahack.serializers.treatment_course import ProductSerializer, TreatmentCourseSerializer


class TreatmentCourseViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = TreatmentCourseSerializer

    def get_queryset(self):
        if DEBUG:
            queryset = TreatmentCourse.objects.all()
        else:
            queryset = TreatmentCourse.objects.filter(user=self.request.user)
        return queryset


#
# class MedicationAvailableViewSet(
#     GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
# ):
#     serializer_class = MedicationAvailableSerializer
#
#     def get_queryset(self):
#         if DEBUG:
#             queryset = MedicationAvailable.objects.all()
#         else:
#             queryset = MedicationAvailable.objects.filter(user=self.request.user)
#         return queryset
#
#
# class CourseProgressViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
#     serializer_class = CourseProgressSerializer
#
#     def get_queryset(self):
#         if DEBUG:
#             queryset = CourseProgress.objects.all()
#         else:
#             queryset = CourseProgress.objects.filter(user=self.request.user)
#         return queryset


class ProductView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    def get_queryset(self):
        return Products.objects.all()
