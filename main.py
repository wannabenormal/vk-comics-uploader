import os
import random

import requests
from dotenv import load_dotenv

from files_operations import get_extension_from_url, download_image
from vk_api import publish_image_on_group_wall


def main():
    load_dotenv()
    last_comic_response = requests.get("https://xkcd.com/info.0.json")
    last_comic_response.raise_for_status()
    last_comic = last_comic_response.json()
    last_comic_num = last_comic["num"]
    rand_comic_num = random.randint(1, last_comic_num)

    random_comic_response = requests.get(
        f"https://xkcd.com/{rand_comic_num}/info.0.json"
    )
    random_comic_response.raise_for_status()
    rand_comic = random_comic_response.json()

    comic_url = rand_comic["img"]
    comic_extension = get_extension_from_url(comic_url)
    comic_title = rand_comic["alt"]

    download_image(comic_url, f"comic{comic_extension}")

    vk_access_token = os.getenv("VK_ACCESS_TOKEN")
    vk_group_id = os.getenv("VK_GROUP_ID")

    with open(f"comic{comic_extension}", 'rb') as comic:
        publish_image_on_group_wall(
            vk_access_token,
            vk_group_id,
            comic,
            message=comic_title,
        )

    os.remove(f"comic{comic_extension}")


if __name__ == "__main__":
    main()
