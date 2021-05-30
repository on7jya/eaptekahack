import pytest
from rest_framework.test import APIClient

from eaptekahack.models import Products, TreatmentCourse, User


@pytest.fixture(autouse=True)
def _automatic_django_db(db):
    """
    Mark all tests as tests that require database access
    """


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture()
def user():
    return User.objects.create(username='vasya@eapteka.ru')


@pytest.fixture()
def product():
    return Products.objects.create(id=461364, name="Виагра, таблетки 50 мг, 2 шт.")


@pytest.fixture()
def course(user, product):
    schedule_info = {
        "start_date": "29.05.2021",
        "time": ["08:00", "12:00", "20:00",],
        "repeat_limit": {
            "date": "31.05.2021",
            # "count": "number"
        },
    }
    course = TreatmentCourse.objects.create(
        pk=1, user=user, drug=product, schedule_info=schedule_info, quantity=20, quantity_exists=30
    )
    return course
