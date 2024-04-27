from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from io import BytesIO


def prepare_template(template_image: int):
    path = Path(f'../core/resume_templates/bg{template_image}.jpeg').resolve()
    template_image_bytes = path.read()
    template = Image.open(BytesIO(template_image_bytes))
    draw = ImageDraw.Draw(template)
    font_path = Path(f"../core/resume_templates/font{template_image}.ttf").resolve()
    font_size = 12
    font = ImageFont.truetype(font_path, font_size)
    return draw, font, template
