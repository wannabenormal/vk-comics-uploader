import requests


def get_last_comic_num():
    response = requests.get("https://xkcd.com/info.0.json")
    response.raise_for_status()

    return response.json()["num"]


def fetch_comic(comic_num):
    response = requests.get(f"https://xkcd.com/{comic_num}/info.0.json")
    response.raise_for_status()

    return response.json()
