import asyncio
import json
import httpx
import requests

file = 'file_5.jpg'


async def upload_document_to_glpi(filename: str) -> None:
    async with httpx.AsyncClient() as client:
        url = 'http://188.34.149.219/apirest.php/Document/'
        headers = {
            'Session-Token': 'cq94lptqusf0kk9t064ts21alj',
        }
        upload_dict = {
            "input": {
                "name": "Uploaded document", "_filename": [filename]
            }
        }
        files = {
            'uploadManifest': (None, json.dumps(upload_dict), 'application/json'),
            'filename[0]': (filename, open(f'/home/airguy/PycharmProjects/sandbox1/media/{filename}', 'rb'))
        }
        response = await client.post(headers=headers, url=url, files=files)
        return json.loads(response.text)


print(asyncio.run(upload_document_to_glpi(file)))
