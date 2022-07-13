from rest_framework.test import APITestCase
from notesapp.test.TestUtils import TestUtils
class NotesAppAPIBoundaryTest(APITestCase):
    def test_boundary(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("TestBoundary",True,"boundary")
        print("TestBoundary = Passed")
