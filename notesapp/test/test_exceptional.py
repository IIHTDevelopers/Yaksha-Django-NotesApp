from rest_framework.test import APITestCase
from notesapp.models import NotesModel
from notesapp.test.TestUtils import TestUtils
class NotesAppAPIExceptionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        NotesModel.objects.create(id=101,title="Python",description="Python is an easy programming language",author="Guido Van Rossum",status="Completed")

    def test_id_not_available_error_at_get_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/102111/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestIdNotAvailableErrorAtGetRequest", True, "exception")
            print("TestIdNotAvailableErrorAtGetRequest = Passed")
        else:
            test_obj.yakshaAssert("TestIdNotAvailableErrorAtGetRequest", False, "exception")
            print("TestIdNotAvailableErrorAtGetRequest = Failed")

    def test_id_not_available_error_at_put_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/11234/'
        response=self.client.put(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestIdNotAvailableErrorAtPutRequest", True, "exception")
            print("TestIdNotAvailableErrorAtPutRequest = Passed")
        else:
            test_obj.yakshaAssert("TestIdNotAvailableErrorAtPutRequest", False, "exception")
            print("TestIdNotAvailableErrorAtPutRequest = Failed")

    def test_id_not_available_error_at_patch_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/11234/'
        response=self.client.patch(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestIdNotAvailableErrorAtPatchRequest", True, "exception")
            print("TestIdNotAvailableErrorAtPatchRequest = Passed")
        else:
            test_obj.yakshaAssert("TestIdNotAvailableErrorAtPatchRequest", False, "exception")
            print("TestIdNotAvailableErrorAtPatchRequest = Failed")

    def test_id_not_available_error_at_delete_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/11234/'
        response=self.client.delete(url)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestIdNotAvailableErrorAtDeleteRequest", True, "exception")
            print("TestIdNotAvailableErrorAtDeleteRequest = Passed")
        else:
            test_obj.yakshaAssert("TestIdNotAvailableErrorAtDeleteRequest", False, "exception")
            print("TestIdNotAvailableErrorAtDeleteRequest = Failed")
