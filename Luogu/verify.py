"""
Filename: custom/verify.py
Author: ZnPdCo
"""

import requests
from app.config import config

# Please remove the below line if you need verification of the account credentials.
# pylint: disable=unused-argument
def verify_account(username, code):
    """
    If you wish to deploy this system, please write the `verify_account(username, code)` function
    within `app/custom/verify.py` yourself to implement user verification for your Online Judge.
    You need to make this function crawl description of `username` (or other relevant information)
    from the OJ and check if the description starts with the `code`. If it does, return `True`;
    otherwise, return `False`.

    Returns:
        True if the description of `username` starts with the `code`, False otherwise.
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36"
        + " (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    }
    url = "https://www.luogu.com.cn/user/" + username + "?_contentOnly"
    response = requests.get(url, headers=headers, timeout=5)
    if response.status_code != 200:
        return False
    data = response.json()
    if data["code"] != 200:
        return False

    ccf_level = data["currentData"]["user"]["ccfLevel"]
    if ccf_level < config["low_ccf_level"]:
        return False

    description = data["currentData"]["user"]["introduction"]
    if description.startswith(code):
        return True
    return False
