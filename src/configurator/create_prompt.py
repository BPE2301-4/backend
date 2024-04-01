# import external libraries
from openai import OpenAI
# import from folder 'src/' via __init__
from src import TOKEN
# import from folder 'src/core' via __init__
from ..core import Resume


client = OpenAI(
    api_key=f'{TOKEN}'
)


def get_resume(resume_param: Resume):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты - бот , который очень хорошо разбирается в создании резюме , и можешь "
                                          "составить подходящее резюме для любой профессии"},
            {"role": "user", "content": resume_param.configue_prompt()}
        ]
    )
    if completion.choices[0].message is not None:
        return completion.choices[0].message.content
        