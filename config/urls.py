from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from config import settings
from eaptekahack.views import AnalogProductView, MedicationAvailableView, ProductView, TreatmentCourseViewSet

router = DefaultRouter()

router.register(r'course', TreatmentCourseViewSet, basename='treatment_course')

api_urlpatterns = router.urls + [
    path('products/<pk>/', ProductView.as_view(), name='products'),
    path('search_analog/<pk>/', AnalogProductView.as_view(), name='search_analog'),
    path('medication_available/<pk>/', MedicationAvailableView.as_view(), name='medication_available'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((api_urlpatterns, 'eaptekahack'), namespace='api')),
]

# swagger
openapi_info = openapi.Info(title="eaptekahack", default_version='v1', description="eaptekahack")
schema_view = get_schema_view(openapi_info, public=True, permission_classes=(permissions.AllowAny,),)
swagger_patterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += swagger_patterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
