from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from config.settings import DEBUG
from eaptekahack.models import MedicationAvailable, ProductMNN, Products, TreatmentCourse
from eaptekahack.seriaizers import MedicationAvailableSerializer, ProductSerializer, TreatmentCourseSerializer


class TreatmentCourseViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = TreatmentCourseSerializer

    def get_queryset(self):
        if DEBUG:
            queryset = TreatmentCourse.objects.all()
        else:
            queryset = TreatmentCourse.objects.filter(user=self.request.user)
        return queryset


class ProductView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    def get_queryset(self):
        return Products.objects.all()


class AnalogProductView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        mnn_id = ProductMNN.objects.filter(product_id=self.kwargs['pk']).values_list('mnn_id', flat=True)
        analogs = ProductMNN.objects.filter(mnn_id__in=mnn_id).values_list('product_id', flat=True)
        return Products.objects.filter(pk__in=analogs)


class MedicationAvailableView(RetrieveAPIView):
    serializer_class = MedicationAvailableSerializer

    def get_queryset(self):
        return MedicationAvailable.objects.filter(course=self.kwargs['pk'])
