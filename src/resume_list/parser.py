import requests
from bs4 import BeautifulSoup
from ..core import session
from ..core import Resume, Url

resume_url = 'https://www.rabota.ru/v3_shop.html?group_id=1'


def parse_and_save_resume(resume_url):
    response = requests.get(resume_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        
        name = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        phone = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        email = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        work_exp = soup.find('span', {'class': 'text_18 bold exp-years'}).text.strip()
        birth_date = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        city = soup.find('span', {'class': 'region'}).text.strip()
        citizenship = soup.find('span', {'class':'b-citizenship-info'}).text.strip()
        post = soup.find('a', {'class': 'res-title'}).text.strip()
        salary = soup.find('span', {'class': 'text_24 salary nobr'}).text.strip()
        employment = soup.find('span', {'class': 'resume-header-name'}).text.strip()
        schedule = soup.find('div', {'class': 'pt12 1h_20 p-fs16 td2'}).text.strip()
        education = soup.find('span', {'class': 'bold edu-type'}).text.strip()
        about = soup.find('p', {'class': 'mb_10 lh_20'}).text.strip()


       
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

