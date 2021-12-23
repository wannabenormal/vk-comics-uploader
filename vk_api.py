import requests


def publish_image_on_group_wall(
        access_token, group_id, image_id, image_owner,
        message="", from_group=True):

    params = {
        "access_token": access_token,
        "v": "5.131",
        "owner_id": f"-{group_id}",
        "from_group": 1 if from_group else 0,
        "attachments": f"photo{image_owner}_{image_id}",
        "message": message,
    }

    response = requests.get(
        "https://api.vk.com/method/wall.post",
        params=params
    )
    response.raise_for_status()


def get_upload_server(access_token, group_id):
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


def upload_image(upload_url, image):
    files = {
        "photo": image
    }

    response = requests.post(upload_url, files=files)
    response.raise_for_status()

    return response.json()


def save_image(access_token, group_id, photo, server, hash):
    params = {
        "group_id": group_id,
        "access_token": access_token,
        "photo": photo,
        "server": server,
        "hash": hash,
        "v": "5.131",
    }

    save_response = requests.post(
        "https://api.vk.com/method/photos.saveWallPhoto",
        data=params
    )
    save_response.raise_for_status()

    return save_response.json()["response"][0]
