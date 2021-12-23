import requests


def publish_image_on_group_wall(
        access_token, group_id, image,
        message="", from_group=True):

    upload_server = get_wall_upload_server(access_token, group_id)
    saved_image = save_image_in_album(
        access_token,
        group_id,
        image,
        upload_server
    )

    params = {
        "access_token": access_token,
        "v": "5.131",
        "owner_id": f"-{group_id}",
        "from_group": 1 if from_group else 0,
        "attachments": f"photo{saved_image['owner_id']}_{saved_image['id']}",
        "message": message,
    }

    response = requests.get(
        "https://api.vk.com/method/wall.post",
        params=params
    )
    response.raise_for_status()


def get_wall_upload_server(access_token, group_id):
    params = {
        "access_token": access_token,
        "v": "5.131",
        "group_id": group_id
    }

    response = requests.get(
        "https://api.vk.com/method/photos.getWallUploadServer",
        params=params
    )

    response.raise_for_status()
    return response.json()["response"]["upload_url"]


def save_image_in_album(access_token, group_id, image, upload_url):
    files = {
            "photo": image,
        }

    upload_response = requests.post(upload_url, files=files)
    upload_response.raise_for_status()
    upload_meta = upload_response.json()

    save_params = {
        "group_id": group_id,
        "access_token": access_token,
        "photo": upload_meta["photo"],
        "server": upload_meta["server"],
        "hash": upload_meta["hash"],
        "v": "5.131",
    }

    save_response = requests.post(
        "https://api.vk.com/method/photos.saveWallPhoto",
        data=save_params
    )
    save_response.raise_for_status()

    return save_response.json()["response"][0]
