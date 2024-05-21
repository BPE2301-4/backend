import requests
from bs4 import BeautifulSoup
from ..core import session
from ..core import Resume, Url

resume_url = 'https://www.rabota.ru/v3_shop.html?group_id=1'


def parse_and_save_resume(resume_url):
    response = requests.get(resume_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        work_exp = soup.find('span', {'class': 'text_18 bold exp-years'}).text.strip()
        city = soup.find('span', {'class': 'region'}).text.strip()
        #citizenship = soup.find('span', {'class':'b-citizenship-info'}).text.strip()
        post = soup.find('span', {'class': 'text_24 bold position-name'}).text.strip()
        salary = soup.find('span', {'class': 'text_24 salary nobr'}).text.strip()
        
        education = soup.find('span', {'class': 'bold edu-type'}).text.strip()
        about = soup.find('p', {'class': 'mt_4 p-res-qua lh_20 aboutme-info'}).text.strip()


       
        resume = Resume(work_exp=work_exp,
                        city=city, #citizenship=citizenship,
                        post=post, salary=salary,
                        education=education, about=about)
        
        url = Url(url=resume_url)
        session.add(url)
        session.add(resume)
        session.commit()
        return("Резюме успешно сохранено в базу данных.")
    else:
        return("Не удалось получить резюме. Код состояния:", response.status_code)

