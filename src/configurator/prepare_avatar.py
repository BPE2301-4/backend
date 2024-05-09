import requests

from ..core import Resume
from PIL import Image
from io import BytesIO


def avatar(resume: Resume):
    # if resume.avatar_file.file != "":
    #     avatar_image_bytes = resume.avatar_file.file
    #     avatar_image = Image.open(BytesIO(avatar_image_bytes))
    #     return avatar_image
    if resume.avatar_url:
        avatar_image_bytes = requests.get(resume.avatar_url.url).content
        avatar_image = Image.open(BytesIO(avatar_image_bytes))
        return avatar_image
