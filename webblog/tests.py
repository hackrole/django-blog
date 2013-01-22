"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from webblog.tests_bak import client
from django.utils import unittest
from webblog.models import Blog
from django.test.client import Client

class SimTest(TestCase):
    def test_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

# class FirstTest(TestCase):
#     def test_blog(self):
#         from webblog.models import Blog
#         b = Blog.objects.all()
#         self.assertEqual(len(b), 20)
class BlogTest(TestCase):
    # fixtures = ['sql/test_fixtures.json',]

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_blogIndex(self):
        c = Client()
        
        reponse = c.get("/blog/-1")
        self.assertEqual(reponse.status_code, 404)
        reponse = c.get("/blog/")
        self.assertEqual(reponse.status_code, 200)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(client.AboutTestCase('test_data_not_empty'))
    suite.addTest(SimTest('test_addition'))
    suite.addTest(BlogTest('test_blogIndex'))
    return suite
             
