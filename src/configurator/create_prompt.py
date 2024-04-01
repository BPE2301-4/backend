from openai import OpenAI
from src import TOKEN
from .schemas import Resume


client = OpenAI(
    api_key=f'{TOKEN}'
)


def get_prompt(prompt: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Ты знаешь ответ на любой вопрос !"},
                  {"role": "user", "content": prompt}]
    )
    return completion.choices[0].delta.content


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
        