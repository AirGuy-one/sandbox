import json

import requests

url = 'http://188.34.149.219/apirest.php/Ticket/1/Document_Item/'
headers = {
    'Content-Type': 'multipart/form-data',
    'Session-Token': 'cq94lptqusf0kk9t064ts21alj',
}
files = {
    'uploadManifest': (None, '{"input": {"documents_id": 7, "items_id": 1, "itemtype": "Ticket"}}', 'application/json'),
    'filename[0]': ('file_5.jpg', open('/home/airguy/PycharmProjects/sandbox1/media/file_5.jpg', 'rb'))
}

response = requests.post(url, headers=headers, files=files)

print(response.text)