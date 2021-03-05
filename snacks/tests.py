from django.test import TestCase
from django.urls import reverse

class SnackTest(TestCase):
# TO RUN TESTS, USE PYTHON MANAGE.PY TEST

# *******************LIST**********************
    def test_home_page(self):
        # naming convention 'home' MUST be the same as what's in snack url.py
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_page_template(self): 
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

# *******************DETAIL**********************
    # def test_detail_page(self):
    #     # naming convention 'home' MUST be the same as what's in snack url.py
    #     url = reverse('snack_detail')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # def test_detail_page_template(self): 
    #     url = reverse('snack_detail')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, 'snack_detail.html')


# XXX: Test Snack pages
# XXX: NOTE make sure test extends TestCase instead of SimpleTestCase used in previous class.
# XXX: verify status code
# XXX: verify correct template use url name instead of hard coded path TIP: django.urls.reverse will help with that.
# TODO: We can’t easily test SnackDetailView just yet. Can you figure out why?
#  Need to somehow pass a pk for snack_detail to work