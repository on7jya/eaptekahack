from django.urls import reverse

from eaptekahack.models import MedicationAvailable, ProductMNN, Products, TreatmentCourse


def test_products_detail_get(client):
    response = client.get(reverse('api:products', args=[1]), format='json')
    assert response.status_code == 404

    Products.objects.create(id=1, name="лекарство")
    response = client.get(reverse('api:products', args=[1]), format='json')
    assert response.status_code == 200


def test_course_list_get(client, course):
    response = client.get(reverse('api:treatment_course-list'), format='json')
    assert response.status_code == 200
    assert len(response.data) == 1


def test_course_list_without_data_get(client):
    response = client.get(reverse('api:treatment_course-list'), format='json')
    assert response.status_code == 200
    assert not len(response.data)


def test_course_list_post(client, product, user):
    assert TreatmentCourse.objects.count() == 0
    data = {
        "user": user.pk,
        "drug": product.pk,
        "schedule_info": {
            "time": ["08:00", "12:00", "20:00"],
            "start_date": "29.05.2021",
            "repeat_limit": {"date": "31.05.2021"},
        },
        "quantity": 30.0,
        "quantity_exists": 15.0,
    }

    response = client.post(reverse('api:treatment_course-list'), data=data, format='json')
    assert response.status_code == 201
    assert TreatmentCourse.objects.count() == 1


def test_course_detail_get(client, user, product, course):
    response = client.get(reverse('api:treatment_course-detail', args=[course.pk]), format='json')
    assert response.status_code == 200
    response = client.get(reverse('api:treatment_course-detail', args=[12345]), format='json')
    assert response.status_code == 404


def test_analog_products_detail_get(client):
    drug = Products.objects.create(id=1, name="Ацикловир мазь")
    Products.objects.create(id=2, name="Ацикловир гель")
    ProductMNN.objects.create(mnn_id=1, product_id=1, mnn_name="Ацикловир", mnn_code="atsiklovir")
    ProductMNN.objects.create(mnn_id=1, product_id=2, mnn_name="Ацикловир", mnn_code="atsiklovir")

    response = client.get(reverse('api:search_analog', args=[drug.pk]), format='json')
    assert response.status_code == 200
    assert len(response.data) == 2


def test_medical_available_detail_get(client, user, product, course):
    response = client.get(reverse('api:medication_available', args=[course.pk]), format='json')
    assert response.status_code == 404
    med_available = MedicationAvailable.objects.create(course=course, number_of_pills=30)
    response = client.get(reverse('api:medication_available', args=[course.pk]), format='json')
    assert response.status_code == 200
    assert response.data == {'id': med_available.pk, 'number_of_pills': 30, 'course': course.pk}
