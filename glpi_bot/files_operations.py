import aiohttp
import os


async def download_file(url, output_file):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(output_file, 'wb') as f:
                    async for chunk in response.content.iter_any():
                        f.write(chunk)
                print('File downloaded successfully')
            else:
                print(f'Failed to download file: {response.status}')


async def download_file_by_url(url: str):
    local_folder = os.getcwd() + '/media/'
    local_file_path = local_folder + url.split('/')[-1]
    await download_file(url, local_file_path)
