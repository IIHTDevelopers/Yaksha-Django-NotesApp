from rest_framework.test import APITestCase
from notesapp.models import NotesModel
from test.TestUtils import TestUtils
class NotesAppAPIFunctionalTest(APITestCase):
    def test_get_request_for_all_records(self):
        url='http://127.0.0.1:8000/notes_crud/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetRequestForAllRecords", True, "functional")
            print("TestGetRequestForAllRecords = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForAllRecords", False, "functional")
            print("TestGetRequestForAllRecords = Failed")
    def test_get_request_for_single_record(self):
        url='http://127.0.0.1:8000/notes_crud_pk/101/'
        response=self.client.get(url)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestGetRequestForSingleRecord", True, "functional")
            print("TestGetRequestForSingleRecord = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestForSingleRecord", False, "functional")
            print("TestGetRequestForSingleRecord = Failed")

    def test_get_request_fail(self):
        url='http://127.0.0.1:8000/notes_crud/102123/'#Non existing id
        response=self.client.get(url)
        #self.assertEqual(response.status_code,404)
        test_obj = TestUtils()
        if response.status_code==404:
            test_obj.yakshaAssert("TestGetRequestFail", True, "functional")
            print("TestGetRequestFail = Passed")
        else:
            test_obj.yakshaAssert("TestGetRequestFail", False, "functional")
            print("TestGetRequestFail = Failed")

    def test_post_request(self):
        url='http://127.0.0.1:8000/notes_crud/'
        data={
            'title':'Java',
            'author':'Games Gosling',
            'description':'Python is a programming language',
            'status':'completed'
        }
        response=self.client.post(url,data,format='json')
        #self.assertEqual(response.status_code,201)
        test_obj = TestUtils()
        if response.status_code==201:
            test_obj.yakshaAssert("TestPostRequest", True, "functional")
            print("TestPostRequest = Passed")
        else:
            test_obj.yakshaAssert("TestPostRequest", False, "functional")
            print("TestPostRequest = Failed")

    def test_post_request_fail(self):
        url='http://127.0.0.1:8000/notes_crud/'
        data={
            'title':'Java',
            'author':'Games Gosling',
            'description':'Python is a programming language'
            #'status':'completed'   #skip status field to create
        }
        response=self.client.post(url,data,format='json')
        #self.assertEqual(response.status_code,400)
        test_obj = TestUtils()
        if response.status_code==400:
            test_obj.yakshaAssert("TestPostRequestFail", True, "functional")
            print("TestPostRequestFail = Passed")
        else:
            test_obj.yakshaAssert("TestPostRequestFail", False, "functional")
            print("TestPostRequestFail = Failed")

    def test_put_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/101/' #existing id
        data={
                'title':'Java',
                'author':'Games Gosling',
                'description':'Python is a programming language',
                'status':'completed'
            }
        response=self.client.put(url,data,format='json')
        #self.assertEqual(response.status_code,200)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestPutRequest", True, "functional")
            print("TestPutRequest = Passed")
        else:
            test_obj.yakshaAssert("TestPutRequest", False, "functional")
            print("TestPutRequest = Failed")

    def test_put_request_fail(self):
        url='http://127.0.0.1:8000/notes_crud_pk/12345/' #non existing id
        data={
            'title':'Java',
            'author':'Games Gosling',
            'description':'Python is a programming language',
            'status':'completed'
        }
        response=self.client.put(url,data,format='json')
        #self.assertEqual(response.status_code,500)
        #print(response.status_code)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestPutRequestFail", True, "functional")
            print("TestPutRequestFail = Passed")
        else:
            test_obj.yakshaAssert("TestPutRequestFail", False, "functional")
            print("TestPutRequestFail = Failed")

    def test_patch_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/101/' #existing id
        data={
                'status':'completed'
            }
        response=self.client.patch(url,data,format='json')
        #self.assertEqual(response.status_code,200)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestPatchRequest", True, "functional")
            print("TestPatchRequest = Passed")
        else:
            test_obj.yakshaAssert("TestPatchRequest", False, "functional")
            print("TestPatchRequest = Failed")

    def test_patch_request_fail(self):
        url='http://127.0.0.1:8000/notes_crud_pk/12345/' #non existing id
        data={
            'status':'completed'
           }
        response=self.client.patch(url,data,format='json')
        #self.assertEqual(response.status_code,500)
        #print(response.status_code)
        test_obj = TestUtils()
        if response.status_code==500:
            test_obj.yakshaAssert("TestPatchRequestFail", True, "functional")
            print("TestPatchRequestFail = Passed")
        else:
            test_obj.yakshaAssert("TestPatchRequestFail", False, "functional")
            print("TestPatchRequestFail = Failed")

    def test_delete_request(self):
        url='http://127.0.0.1:8000/notes_crud_pk/101/'
        response=self.client.delete(url)
        #self.assertEqual(response.status_code,200)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestDeleteRequest", True, "functional")
            print("TestDeleteRequest = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteRequest", False, "functional")
            print("TestDeleteRequest = Failed")

    def test_delete_request_fail(self):
        url='http://127.0.0.1:8000/notes_crud/10232/' #Non existing id
        response=self.client.delete(url)
        #self.assertEqual(response.status_code,404)
        test_obj = TestUtils()
        if response.status_code==404:
            test_obj.yakshaAssert("TestDeleteRequestFail", True, "functional")
            print("TestDeleteRequestFail = Passed")
        else:
            test_obj.yakshaAssert("TestDeleteRequestFail", False, "functional")
            print("TestDeleteRequestFail = Failed")

    def test_search_by_id(self):
        url='http://127.0.0.1:8000/search_by_id/?id=101'
        response=self.client.get(url)
        #print(response.status_code)
        #self.assertEqual(response.status_code,404)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestSearchById", True, "functional")
            print("TestSearchById = Passed")
        else:
            test_obj.yakshaAssert("TestSearchById", False, "functional")
            print("TestSearchById = Failed")

    def test_search_by_author(self):
        url='http://127.0.0.1:8000/search_by_author/?author=Guido Van Rossum'
        response=self.client.get(url)
        #self.assertEqual(response.status_code,404)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestSearchByAuthor", True, "functional")
            print("TestSearchByAuthor = Passed")
        else:
            test_obj.yakshaAssert("TestSearchByAuthor", False, "functional")
            print("TestSearchByAuthor = Failed")

    def test_search_by_status(self): #Note executing
        url='http://127.0.0.1:8000/search_by_status/?status=Completed'
        response=self.client.get(url)
        #self.assertEqual(response.status_code,404)
        test_obj = TestUtils()
        if response.status_code==200:
            test_obj.yakshaAssert("TestSearchByStatus", True, "functional")
            print("TestSearchByStatus = Passed")
        else:
            test_obj.yakshaAssert("TestSearchByStatus", False, "functional")
            print("TestSearchByStatus = Failed")
