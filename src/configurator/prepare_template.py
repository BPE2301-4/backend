from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from io import BytesIO


def prepare_template(template_image: int):
    path = Path(f'src/core/resume_templates/bg{template_image}.jpeg').resolve()
    template_image_bytes = path.open(mode='rb').read()
    template = Image.open(BytesIO(template_image_bytes))
    draw = ImageDraw.Draw(template)
    return draw, template
