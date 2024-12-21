from django.test import TestCase, Client
from django.urls import reverse
from .models import Member

class MemberViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.member1 = Member.objects.create(
            firstname="John",
            lastname="Doe",
            email="john.doe@example.com",
            phone="1234567890",
            joined_date="2023-01-01"
        )
        self.member2 = Member.objects.create(
            firstname="Jane",
            lastname="Doe",
            email="jane.doe@example.com",
            phone="0987654321",
            joined_date="2023-01-02"
        )

    def test_main_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_member_view(self):
        response = self.client.get(reverse('members'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'members.html')
        self.assertIn('members', response.context)
        self.assertEqual(len(response.context['members']), 2)

    def test_details_view(self):
        response = self.client.get(reverse('details', args=[self.member1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'details.html')
        self.assertEqual(response.context['members'], self.member1)

    def test_testing_view(self):
        response = self.client.get(reverse('testing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testing.html')
        self.assertIn('fruits', response.context)
        self.assertEqual(response.context['fruits'], ['Apple', 'Banana', 'Cherry'])

    def test_create_member_view(self):
        data = {
            'firstname': "Alice",
            'lastname': "Smith",
            'email': "alice.smith@example.com",
            'phone': "1122334455",
            'joined_date': "2024-03-01"
        }
        response = self.client.post(reverse('create_member'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Member.objects.filter(email="alice.smith@example.com").exists())

    def test_edit_member_view(self):
        data = {
            'firstname': "John Updated",
            'lastname': "Doe",
            'email': "john.doe@example.com",
            'phone': "1234567890",
            'joined_date': "2024-01-01"
        }
        response = self.client.post(reverse('edit_member', args=[self.member1.id]), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.member1.refresh_from_db()
        self.assertEqual(self.member1.firstname, "John Updated")

    def test_delete_members_view(self):
        data = {'members': [self.member1.id, self.member2.id]}
        response = self.client.post(reverse('delete_members'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertFalse(Member.objects.filter(id=self.member1.id).exists())
        self.assertFalse(Member.objects.filter(id=self.member2.id).exists())

    def test_select_member_to_edit_view(self):
        response = self.client.get(reverse('select_member_to_edit'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'select_member_to_edit.html')
        self.assertIn('members', response.context)
        self.assertEqual(len(response.context['members']), 2)