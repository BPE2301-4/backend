# import external libraries
from openai import OpenAI
# import from folder 'src/' via __init__
from src import TOKEN


client = OpenAI(
    api_key=f'{TOKEN}'
)


def mist_correction(text: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты - бот , который отлично знает русский язык. Твоя задача - находить ошибки в получеенном тобой тексте, исправлять их и отдельно выписывать те места и слова, в которых были допущены ошибки."},
            {"role": "user", "content": text}
        ]
    )
    if completion.choices[0].message is not None:
        return completion.choices[0].message.content
