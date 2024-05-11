import requests
from bs4 import BeautifulSoup
from ..core import session
from ..core import Resume, Url

resume_url = 'https://hh.ru/resume/abcdef123456'

# Функция для парсинга резюме и сохранения в базу данных
def parse_and_save_resume(resume_url):
    response = requests.get(resume_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Извлекаем данные из резюме
        # Здесь необходимо написать код для извлечения данных из HTML-кода страницы
        # Пример: full_name = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        name = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        phone = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        email = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        work_exp = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        birth_date = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        city = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        citizenship = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        post = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        salary = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        employment = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        schedule = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        education = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        about = soup.find('span', {'class': 'resume-header-name'}).text.strip()


        # Создаем экземпляр модели и сохраняем в базу данных
        resume = Resume(name=name, phone=phone, email=email, work_exp=work_exp,
                        birth_date=birth_date, city=city, citizenship=citizenship,
                        post=post, salary=salary, employment=employment, schedule=schedule,
                        education=education, about=about)
        
        url = Url(url=resume_url)
        session.add(url)
        session.add(resume)
        session.commit()
        return("Резюме успешно сохранено в базу данных.")
    else:
        return("Не удалось получить резюме. Код состояния:", response.status_code)

