from django.test.client import Client
from django.utils import unittest
from webblog.models import *
from webblog.form import *

class AboutTestCase(unittest.TestCase):
    """
    test for about
    """
    fixtures = ['',]
    # urls = ''
    # multi_db = True

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_data_not_empty(self):
        """
        test about database is not empty
        """
        about = About.objects.all()
        self.assertNotEqual(len(about), 2)
        
    def test_about_post(self):
        c = Client()
        response = c.post('/blog/about/', {
                'name':'hackrole', 
                'email':'daipeng123456@gmail.com', 
                'website':'', 
                'content':'',
                })
        self.assertEqual(response.status_code, 200)

        print response.templates


def suite():
    pass
    #suite = unittest.TestSuite()
