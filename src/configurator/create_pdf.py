from ..core import Resume
from io import BytesIO
from fastapi.responses import StreamingResponse
from . import prepare_text, prepare_template, prepare_avatar


def generate_pdf(resume: Resume, template_image: int):
    draw, font, template = prepare_template.prepare_template(template_image=template_image)
    left_column_x = 50
    right_column_x = 300
    y = 100
    text_to_write_left = prepare_text.left_column(resume=resume)
    text_to_write_right = prepare_text.right_column(resume=resume)
    draw.multiline_text((left_column_x, y), text_to_write_left, fill="black", font=font)
    draw.multiline_text((right_column_x, y), text_to_write_right, fill="black", font=font)
    if resume.avatar:
        avatar_image = prepare_avatar.avatar(resume=resume)
        template.paste(avatar_image, (left_column_x, y))
    buffer = BytesIO()
    template.save(buffer, format="PDF")
    return StreamingResponse([buffer.getvalue()], media_type="application/pdf")
