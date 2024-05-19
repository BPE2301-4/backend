from ..core import Resume
from io import BytesIO
from fastapi.responses import StreamingResponse
from fastapi import HTTPException
from . import prepare_text, prepare_template, prepare_avatar
import datetime


def generate_pdf(resume: Resume, template_image: int):
    try:
        draw, template = prepare_template.prepare_template(template_image=template_image)
        left_column_x = 163
        right_column_x = 890
        y = 163
        if resume.avatar:
            try:
                avatar_image = prepare_avatar.avatar(resume=resume)
                template.paste(avatar_image, (left_column_x, y))
                y += 563
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Ошибка обработки аватара: {e}")

        try:
            text_to_write_left = prepare_text.left_column(resume=resume)
            text_to_write_right = prepare_text.right_column(resume=resume)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Ошибка подготовки текста: {e}")

        try:
            for item in text_to_write_left:
                draw.multiline_text((left_column_x, y), item.text, fill="black", font=item.text_font.value)
                y += item.text_padding * 2
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Ошибка при написании текста в левую колонку: {e}")

        y = 163
        try:
            for item in text_to_write_right:
                draw.multiline_text((right_column_x, y), item.text, fill="black", font=item.text_font.value)
                y += item.text_padding * 2
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Ошибка при написании текста в правую колонку: {e}")

        try:
            buffer = BytesIO()
            template.save(buffer, format="PDF")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Ошибка сохранения PDF: {e}")

        headers = {
            "Content-Disposition": f'attachment; filename="JobJotter{datetime.datetime.utcnow().date()}.pdf"',
            "Content-Type": "application/pdf"
        }
        return StreamingResponse([buffer.getvalue()], headers=headers)
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Произошла непредвиденная ошибка: {e}")
