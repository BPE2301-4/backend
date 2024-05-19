# import external libraries
from openai import OpenAI
import json
# import from folder 'src/' via __init__
from src import TOKEN


client = OpenAI(
    api_key=f'{TOKEN}'
)


def mist_correction(text: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты - бот , который отлично знает русский язык . Твоя задача - находить ошибки в полученном тобой тексте , исправлять их и отдельно выписывать те места и слова, в которых были допущены ошибки . Тебе следует JSON-объект , где по ключу text будет строка , содержащая исправленный текст , а по ключу mistakes - Python список , содержащий в сеебе все слова , в которых допущены ошибки , в виде строк ."},
            {"role": "user", "content": text}
        ]
    )
    response_text = completion.choices[0].message.content
    try:
        response = json.loads(response_text)
        return response
    except json.JSONDecodeError:
        return None
