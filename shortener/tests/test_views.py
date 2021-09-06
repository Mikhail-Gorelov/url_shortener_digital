import factory
import pytest
from django.urls import reverse

from shortener.forms import URLForm
from shortener.models import URL


class URLFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = URL


@pytest.mark.django_db
class TestMainView:
    path = reverse('shortener:main')

    def test_get(self, client):
        """Минимальный тест, что ответ ОК, содержит нужный список и форму"""
        session_key = client.session.session_key
        current_user_urls_count = 3
        URLFactory.create_batch(current_user_urls_count, session=session_key)
        URLFactory.create_batch(2)

        response = client.get(self.path)
        paginated_urls = response.context.get('paginated_urls')
        urls_list = paginated_urls.object_list if paginated_urls else []
        exists_form = bool(response.context.get('form'))

        assert response.status_code == 200
        assert len(urls_list) == current_user_urls_count
        assert exists_form is True

    def test_post(self, client):
        """Тест, что ответ ОК и объект в БД действительно создается"""
        data = {'url': 'google.com'}

        response = client.post(self.path, data)

        assert response.status_code == 200
        assert URL.objects.count() == 1
