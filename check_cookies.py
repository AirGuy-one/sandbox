import asyncio

import aiohttp


async def main():
    urls = [
        "https://fake-json-api.mock.beeceptor.com/users",
        "https://fake-json-api.mock.beeceptor.com/users",
        "https://fake-json-api.mock.beeceptor.com/users",
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        results = [await response.json() for response in responses]
        for result in results:
            print(result)


asyncio.run(main())
