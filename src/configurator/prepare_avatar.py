import requests
from fastapi import HTTPException
from ..core import Resume
from PIL import Image
from io import BytesIO


def avatar(resume: Resume):
    target_size = (400, 400)

    def crop_image(image):
        return image.resize(target_size, Image.Resampling.LANCZOS)

    try:
        if resume.avatar.file:
            try:
                avatar_image_bytes = resume.avatar.file
                avatar_image = Image.open(BytesIO(avatar_image_bytes))
                resized_avatar_image = crop_image(avatar_image)
                return resized_avatar_image
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Ошибка обработки аватара из файла: {e}")

        if resume.avatar.url:
            try:
                response = requests.get(resume.avatar.url)
                response.raise_for_status()
                avatar_image_bytes = response.content
                avatar_image = Image.open(BytesIO(avatar_image_bytes))
                resized_avatar_image = crop_image(avatar_image)
                return resized_avatar_image
            except requests.RequestException as e:
                raise HTTPException(status_code=404, detail=f"Ошибка загрузки аватара по URL: {e}")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Ошибка обработки аватара по URL: {e}")

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Произошла непредвиденная ошибка: {e}")
