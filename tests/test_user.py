import pytest
from users.models import User

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create(
        name='test',
        email='test@test.com',
        password='test1234'
    )
    assert user.name == 'test'