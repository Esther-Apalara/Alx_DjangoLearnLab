from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Create sample books
        self.book1 = Book.objects.create(
            title='Django for Beginners',
            author='William Vincent',
            publication_year=2020
        )

        self.book2 = Book.objects.create(
            title='Two Scoops of Django',
            author='Greenfeld',
            publication_year=2019
        )

        # API endpoints (adjust if your URLs differ)
        self.list_url = '/api/books/'
        self.create_url = '/api/books/create/'

    # ------------------------
    # READ (LIST)
    # ------------------------
    def test_get_books_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # ------------------------
    # CREATE (AUTH REQUIRED)
    # ------------------------
    def test_create_book_unauthenticated(self):
        data = {
            'title': 'Unauthorized Book',
            'author': 'No User',
            'publication_year': 2024
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass123')

        data = {
            'title': 'New Django Book',
            'author': 'Test Author',
            'publication_year': 2023
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # ------------------------
    # UPDATE
    # ------------------------
    def test_update_book(self):
        self.client.login(username='testuser', password='testpass123')

        url = f'/api/books/{self.book1.id}/update/'
        data = {
            'title': 'Updated Django Book',
            'author': 'William Vincent',
            'publication_year': 2021
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ------------------------
    # DELETE
    # ------------------------
    def test_delete_book(self):
        self.client.login(username='testuser', password='testpass123')

        url = f'/api/books/{self.book2.id}/delete/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ------------------------
    # FILTERING
    # ------------------------
    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + '?author=Greenfeld')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # ------------------------
    # SEARCH
    # ------------------------
    def test_search_books(self):
        response = self.client.get(self.list_url + '?search=Django')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    # ------------------------
    # ORDERING
    # ------------------------
    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)