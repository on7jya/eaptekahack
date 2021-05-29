from django.urls import reverse

from eaptekahack.models import Products


def test_products_detail_get(client):
    response = client.get(reverse('api:products', args=[1]), format='json')
    assert response.status_code == 404

    Products.objects.create(ID=1, NAME="лекарство")
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


def test_course_detail_get(client, user, product, course):
    response = client.get(reverse('api:treatment_course-detail', args=[course.pk]), format='json')
    assert response.status_code == 200
    response = client.get(reverse('api:treatment_course-detail', args=[12345]), format='json')
    assert response.status_code == 404
