from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Pet


class PetTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='tester@email.com',
            password='pass'
        )

        self.pet = Pet.objects.create(
            name='pickle',
            description='puppy',
            human=self.user,
        )

    def test_string_representation(self):
        pet = Pet(name='Snickers')
        self.assertEqual(str(pet), pet.name)

    def test_pet_content(self):
        self.assertEqual(f'{self.pet.name}', 'pickle')
        self.assertEqual(f'{self.pet.human}', 'tester@email.com')
        self.assertEqual(f'{self.pet.description}', 'puppy')

    def test_pet_list_view(self):
        response = self.client.get(reverse('pet_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'pickle')
        self.assertTemplateUsed(response, 'pets/pet-list.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_pet_detail_view(self):
        response = self.client.get(reverse('pet_detail', args='1')) #'/pets/1/')
        no_response = self.client.get('/pets/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'puppy')
        self.assertTemplateUsed(response, 'pets/pet-detail.html')
        self.assertTemplateUsed(response, '_base.html')


    def test_pet_create_view(self):
        response = self.client.post(reverse('pet_create'), {
            'name': 'Burgers',
            'description': 'needy kitty',
            'human': self.user,
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Burgers')
        self.assertContains(response, 'needy kitty')
        self.assertTemplateUsed(response, 'pets/pet-create.html')
        self.assertTemplateUsed(response, '_base.html')


    def test_pet_update_view(self):
        response = self.client.post(reverse('pet_update',args='1'), {
            'name': 'Updated name',
            'description': 'Updated description',
        })
        self.assertEqual(response.status_code, 200)

    def test_pet_update_view_redirect(self):
        response = self.client.post(reverse('pet_update',args='1'), {
            'name': 'Updated name',
            'description': 'Updated description',
        }, follow=True)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Updated name')

        self.assertTemplateUsed('pets/pet-detail.html')


    def test_pet_delete_view(self):
        response = self.client.get(reverse('pet_delete',args='1'))
        self.assertEqual(response.status_code, 200)