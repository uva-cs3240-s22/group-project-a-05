from django.test import TestCase

# Create your tests here.
# Test comment
class DummyTest(TestCase):
    def testShouldWork(self):
        self.assertTrue(True)
    
    def testShouldFail(self):
        self.assertTrue(False)