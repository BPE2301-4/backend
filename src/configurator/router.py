# import external libraries
from fastapi import APIRouter
from . import create_pdf
from ..core import Resume

router = APIRouter(
    prefix='/configurator',
    tags=['Create your own resume and download it as PDF-file']
)


@router.post('/create')
def create_resume(resume: Resume, template_image: int):
    return create_pdf.generate_pdf(resume=resume, template_image=template_image)
