from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
    
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@app.com',
            password = 'admin123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'user@app.com',
            password = 'user123',
            name = 'test user full name'
        )

    def test_for_user_listed(self):
        """ Test that user are listed on admin page """

        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)
        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """ Test that the user edit page works """

        url = reverse('admin:core_user_change', args=[self.user.id]) # /admin/core/user/1
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the user page works """

        url = reverse('admin:core_user_add') 
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
 