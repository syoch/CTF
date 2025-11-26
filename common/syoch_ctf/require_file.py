import os
import requests

from pwn import process


def require_file(file_name: str, url: str, executable: bool = False) -> None:
    """
    Ensure that a file exists by downloading it from the specified URL if it does not exist.

    :param file_name: The name of the file to check or download.
    :param url: The URL to download the file from if it does not exist.
    """
    if not os.path.exists(file_name):
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        with open(file_name, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {file_name} from {url}")
    else:
        print(f"{file_name} already exists.")

    if executable and not os.access(file_name, os.X_OK):
        os.chmod(file_name, 0o755)
        print(f"Made {file_name} executable.")

def url_process(url: str) -> process:
    """
    Start a process for the given URL.

    :param url: The URL to process.
    :return: The process object.
    """

    require_file(
        "vuln",
        url,
        executable=True,
    )
    return process("./vuln")
