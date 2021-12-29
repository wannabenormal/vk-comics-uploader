import os
import random

from dotenv import load_dotenv

from comics_api import get_last_comic_num, fetch_comic
from files_operations import get_extension_from_url, download_image
from vk_api import (get_upload_server, upload_image, save_image,
                    publish_image_on_group_wall)


def main():
    load_dotenv()
    last_comic_num = get_last_comic_num()
    rand_comic_num = random.randint(1, last_comic_num)

    comic = fetch_comic(rand_comic_num)
    comic_url = comic["img"]
    comic_extension = get_extension_from_url(comic_url)
    comic_title = comic["alt"]
    comic_filename = f"comic{comic_extension}"

    download_image(comic_url, comic_filename)

    vk_access_token = os.getenv("VK_ACCESS_TOKEN")
    vk_group_id = os.getenv("VK_GROUP_ID")

    try:
        vk_upload_url = get_upload_server(vk_access_token, vk_group_id)

        with open(comic_filename, 'rb') as comic:
            uploaded_image = upload_image(vk_upload_url, comic)

        saved_image = save_image(
            vk_access_token,
            vk_group_id,
            uploaded_image["photo"],
            uploaded_image["server"],
            uploaded_image["hash"]
        )

        publish_image_on_group_wall(
            vk_access_token,
            vk_group_id,
            saved_image["id"],
            saved_image["owner_id"],
            message=comic_title
        )

    finally:
        os.remove(comic_filename)


if __name__ == "__main__":
    main()
