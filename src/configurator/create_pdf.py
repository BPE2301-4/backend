from ..core import Resume
from io import BytesIO
from fastapi.responses import StreamingResponse
from . import prepare_text, prepare_template, prepare_avatar


def generate_pdf(resume: Resume, template_image: int):
    draw, template = prepare_template.prepare_template(template_image=template_image)
    left_column_x = 163
    right_column_x = 890
    y = 163
    if resume.avatar:
        avatar_image = prepare_avatar.avatar(resume=resume)
        template.paste(avatar_image, (left_column_x, y))
        y += 563
    text_to_write_left = prepare_text.left_column(resume=resume)
    text_to_write_right = prepare_text.right_column(resume=resume)

    for item in text_to_write_left:
        draw.multiline_text((left_column_x, y), item.text, fill="black", font=item.text_font.value)
        y += item.text_padding*2
    y = 163
    for item in text_to_write_right:
        draw.multiline_text((right_column_x, y), item.text, fill="black", font=item.text_font.value)
        y += item.text_padding*2
    buffer = BytesIO()
    template.save(buffer, format="PDF")
    headers = {
        "Content-Disposition": 'attachment; filename="resume.pdf"',
        "Content-Type": "multipart/form-data"
    }
    return StreamingResponse([buffer.getvalue()], headers=headers)
