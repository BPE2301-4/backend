from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from ..core import Resume
from io import BytesIO
from fastapi.responses import StreamingResponse


def generate_pdf(resume: Resume, template_image: int):
    path = f'/Users/a1/PycharmProjects/mtuci/project/testname_summary/src/core/resume_templates/bg{template_image}.jpeg'
    template_image_bytes = path.read()
    template = Image.open(BytesIO(template_image_bytes))
    draw = ImageDraw.Draw(template)
    font_path = "/Users/a1/PycharmProjects/mtuci/project/testname_summary/src/core/resume_templates/font.ttf"
    font_size = 12
    font = ImageFont.truetype(font_path, font_size)
    left_column_x = 50
    right_column_x = 300
    y = 100
    text_to_write_left = f"""
    Имя: {resume.name}
    Телефон: {resume.phone}
    Email: {resume.email}
    Дата рождения: {resume.birth_date}
    """
    if resume.city:
        text_to_write_left += f"Город: {resume.city}\n"
    if resume.citizenship:
        text_to_write_left += f"Гражданство: {resume.citizenship}\n"
    text_to_write_right = f"""
    Опыт работы: {resume.work_experience}
    Должность: {resume.post}
    Заработная плата: {resume.salary}
    Занятость: {resume.employment}
    График: {resume.schedule}
    Образование: {resume.education}
    """
    if resume.about:
        text_to_write_right += f"О себе: {resume.about}\n"
    draw.multiline_text((left_column_x, y), text_to_write_left, fill="black", font=font)
    draw.multiline_text((right_column_x, y), text_to_write_right, fill="black", font=font)
    buffer = BytesIO()
    template.save(buffer, format="PDF")
    if resume.avatar:
        avatar_image_bytes = resume.avatar.read()
        avatar_image = Image.open(BytesIO(avatar_image_bytes))
        template.paste(avatar_image, (left_column_x, y))
    return StreamingResponse(buffer.getvalue(), media_type="application/pdf")
