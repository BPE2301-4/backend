from ..core import Resume
from PIL import Image
from io import BytesIO


def avatar(resume: Resume):
    if resume.avatar:
        avatar_image_bytes = resume.avatar.file.read()
        avatar_image = Image.open(BytesIO(avatar_image_bytes))
        return avatar_image
