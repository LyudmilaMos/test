from main_2 import upload_file_to_disk
import unittest
import requests

token_false = ''
token_true = ' '

class TestSomething(unittest.TestCase):

    def test_upload_file_to_disk(self):

        self.assertEqual((upload_file_to_disk(token_false, 'file_to_disk')).status_code, 401)        
        response = upload_file_to_disk(token_true, 'file_to_disk')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['href'], 'https://cloud-api.yandex.net/v1/disk/resources' + 'file_to_disk')
        r = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources",
            params={"path": 'file_to_disk'},
            headers={"Authorization": f"OAuth {token_true}"}
        )
        status = r.status_code

        self.assertEqual(status, 200)
        self.assertEqual((upload_file_to_disk(token_true, 'file_to_disk')).status_code, 409)