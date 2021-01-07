from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post, Category, Tag, Comment
from django.utils import timezone
from django.contrib.auth.models import User


def create_category(name='result', description=''):
    category, is_created = Category.objects.get_or_create(
        name=name,
        description=description
    )

    category.slug = category.name.replace(' ', '-').replace('/', '')
    category.save()

    return category

class TestModel(TestCase):

        def test_category(self):
            category = create_category()

            post_000 = create_post(
                title='The first post',
                content='Hello World. We are the world.',
                author=self.author_000,
                category=category
            )

            self.assertEqual(category.post_set.count(), 1)


def test_post_list_by_category(self):
    category_results = create_category(name='결과 공유')

    post_000 = create_post(
        title='The first post',
        content='Hello World. We are the world.',
        author=self.author_000,
    )

    post_001 = create_post(
        title='The second post',
        content='Second Second Second',
        author=self.author_000,
        category=category_results
    )

    response = self.client.get(category_results.get_absolute_url())
    self.assertEqual(response.status_code, 200)

    soup = BeautifulSoup(response.content, 'html.parser')

    main_div = soup.find('div', id='main-div')
    self.assertNotIn('미분류', main_div.text)
    self.assertIn(category_results.name, main_div.text)


def test_post_list_no_category(self):
    category_results = create_category(name='결과 공유')

    post_000 = create_post(
        title='The first post',
        content='Hello World. We are the world.',
        author=self.author_000,
    )

    post_001 = create_post(
        title='The second post',
        content='Second Second Second',
        author=self.author_000,
        category=category_results
    )

    response = self.client.get('/blog/category/_none/')
    self.assertEqual(response.status_code, 200)

    soup = BeautifulSoup(response.content, 'html.parser')

    main_div = soup.find('div', id='main-div')
    self.assertIn('미분류', main_div.text)
    self.assertNotIn(category_results.name, main_div.text)