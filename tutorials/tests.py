from django.urls import reverse
import pytest
from django.urls import reverse
from tutorials.models import Tutorial


pytestmark = pytest.mark.django_db

@pytest.fixture
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username="test_username", password="test_password"
    )
    return "test_username", "test_password"

def test_login_user(client, test_user):
      test_username, test_password = test_user  # this unpacks the tuple
      login_result = client.login(username=test_username, password=test_password)
      assert login_result == True

def test_homepage_access():
          url = reverse('home')
          assert url == "/"

def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()

def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk