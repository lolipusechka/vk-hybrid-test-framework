import json
import requests

from src.api.models.comment import Comment
from src.api.models.like import Like
from src.api.models.photo import Photo
from src.api.models.post import Post
from src.utils.find_file import find
from src.utils.json_parser import get_config

__config = get_config("api_config.example.json")
__url = __config["url"]
__owner_id = __config["owner_id"]
__access_token = __config["access_token"]
__version = __config["v"]


def wall_post(msg: str) -> Post:
    response = requests.get(
        url=__url + 'wall.post',
        params={'owner_id': __owner_id,
                'access_token': __access_token,
                'v': __version,
                'message': msg}

    )
    return Post(response.text)


def wall_edit(photo: Photo, post: Post, msg: str):
    requests.get(
        url=__url + 'wall.edit',
        params={'owner_id': __owner_id,
                'access_token': __access_token,
                'v': __version,
                'message': msg,
                'attachments': f'photo{__owner_id}_{photo.id}',
                'post_id': post.id}
    )


def wall_create_comment(post: Post, msg: str) -> Comment:
    response = requests.get(
        url=__url + 'wall.createComment',
        params={'owner_id': __owner_id,
                'access_token': __access_token,
                'v': __version,
                'message': msg,
                'post_id': post.id}
    )
    return Comment(response.text)


def wall_delete(post: Post):
    requests.get(
        url=__url + 'wall.delete',
        params={'owner_id': __owner_id,
                'access_token': __access_token,
                'v': __version,
                'post_id': post.id}
    )


def wall_get_likes(post: Post) -> Like:
    response = requests.get(
        url=__url + 'wall.getLikes',
        params={'owner_id': __owner_id,
                'access_token': __access_token,
                'v': __version,
                'post_id': post.id}
    )
    return Like(response.text)


def save_wall_photo(name_of_file: str) -> Photo:
    upload_url = requests.get(
        url=__url + 'photos.getWallUploadServer',
        params={'access_token': __access_token,
                'v': __version}
    )

    upload_url = json.loads(upload_url.text)["response"]["upload_url"]
    files = {'photo': open(find(name_of_file), 'rb')}

    upload_photo_response = requests.post(url=upload_url, files=files).json()

    response = requests.get(
        url=__url + 'photos.saveWallPhoto',
        params={'owner_id': __owner_id,
                'access_token': __access_token,
                'v': __version,
                'server': int(upload_photo_response['server']),
                'hash': upload_photo_response['hash'],
                'photo': upload_photo_response['photo']}
    ).json()
    return Photo(int(response["response"][0]["id"]))
