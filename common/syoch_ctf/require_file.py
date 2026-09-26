import os
import requests

from pwn import process


def require_file(file_name: str, url: str, executable: bool = False) -> None:
    """
    ファイルを確認し、存在しない場合は指定されたURLからダウンロードする。
    また、executable が True の場合は、ファイルに実行権限を付与する。

    Args:
        file_name (str): 確認するファイル名
        url (str): ファイルをダウンロードするURL
        executable (bool): ファイルに実行権限を付与するかどうか

    Returns:
        None
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
        os.chmod(file_name, 0o755)  # NOSONAR
        print(f"Made {file_name} executable.")


def url_process(url: str) -> process:
    """
    指定されたURLからファイルをダウンロードし、実行可能にしてからプロセスとして起動する。

    Args:
        url (str): ファイルをダウンロードするURL

    Returns:
        process: 起動したプロセスのオブジェクト
    """

    require_file(
        "vuln",
        url,
        executable=True,
    )
    return process("./vuln")
