from django.contrib import admin

from eaptekahack.models import (
    EventForReminder,
    ProductMNN,
    Products,
    Property,
    PropertyMultipleValues,
    PropertyValues,
    TreatmentCourse,
    User,
)

admin.site.register(User)
admin.site.register(Products)
admin.site.register(Property)
admin.site.register(PropertyMultipleValues)
admin.site.register(PropertyValues)
admin.site.register(ProductMNN)
admin.site.register(TreatmentCourse)
admin.site.register(EventForReminder)
