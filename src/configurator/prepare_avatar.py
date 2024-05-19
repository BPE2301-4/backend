import requests

from ..core import Resume
from PIL import Image
from io import BytesIO


def avatar(resume: Resume):

    target_size = (400, 400)

    def crop_image(image):
        return image.resize(target_size, Image.Resampling.LANCZOS)

    if resume.avatar.file:
        avatar_image_bytes = resume.avatar.file
        avatar_image = Image.open(BytesIO(avatar_image_bytes))
        resized_avatar_image = crop_image(avatar_image)
        return resized_avatar_image
    if resume.avatar.url:
        avatar_image_bytes = requests.get(resume.avatar.url).content
        avatar_image = Image.open(BytesIO(avatar_image_bytes))
        resized_avatar_image = crop_image(avatar_image)
        return resized_avatar_image
