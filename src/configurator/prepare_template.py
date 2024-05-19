from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from io import BytesIO
from fastapi import HTTPException


def prepare_template(template_image: int):
    try:
        path = Path(f'src/core/resume_templates/bg{template_image}.jpeg').resolve()
        if not path.exists():
            raise HTTPException(status_code=404, detail=f"Шаблон изображения bg{template_image}.jpeg не найден")

        try:
            template_image_bytes = path.open(mode='rb').read()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Ошибка чтения файла шаблона: {e}")

        try:
            template = Image.open(BytesIO(template_image_bytes))
            draw = ImageDraw.Draw(template)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Ошибка открытия изображения шаблона: {e}")

        return draw, template
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Произошла непредвиденная ошибка: {e}")
