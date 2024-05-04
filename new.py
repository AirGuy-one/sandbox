import json
import requests


url = 'http://188.34.149.219/apirest.php/Ticket/1/Document/'

headers = {
    'Content-Type': 'multipart/form-data',
    'Session-Token': 'omues57e3b3vf3figl6o5jcumr',
}

files = {
    'uploadManifest': (None, json.dumps({
        "input": {
            "name": "Uploaded document",
            "_filename": ["file.txt"]
        }
    }), 'application/json'),
    'filename[0]': ('file.txt', open('file.txt', 'rb'))
}

response = requests.post(url, headers=headers, files=files)

print(response.json())
