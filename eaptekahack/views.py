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
# class MedicationAvailableViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin,
#                                  UpdateModelMixin):
#     serializer_class = MedicationAvailableSerializer
#
#     def get_queryset(self):
#         # def get_medication_available(med_id, user_id):
#         initial_value, number_per_time = TreatmentCourse.objects.filter(user=self.request.user,
#                                                                         drug=self.request.drug).values_list(
#             'quantity_exists',
#             'quantity',
#             flat=True)
#         times_medication_was_taken = len(
#             CourseProgress.objects.filter(user=self.request.user, drug=self.request.drug, has_taken=True))
#         sum_quantity_of_purchased_drug = Orders.objects.filter(user=self.request.user,
#                                                                drug=self.request.drug).aggregate(Sum('quantity'))
#         number_per_package = PropertyValues.objects.filter(IBLOCK_ELEMENT_ID=self.request.drug).values_list(
#             'PROPERTY_540', flat=True)
#         return initial_value - times_medication_was_taken * number_per_time + sum_quantity_of_purchased_drug * number_per_package
#
#
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


class ProductView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    def get_queryset(self):
        return Products.objects.all()
