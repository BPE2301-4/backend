# testname_summary
название будет редактироваться в процессе разработки

 
# 1. Цель проекта
Создать веб-приложение, которое поможет научиться писать резюме для трудоустройства в IT-сфере. Большая части функционала будет основана на нейросетях. В приложении будет реализован следующий функционал:
1) Список различных резюме, по которым люди нашли работу
2) Конструктор резюме, который будет предлагать вам готовое резюме по вашему набору параметров
3) Анализ вашего резюме на основе списка из успешных резюме

# 2. Описание проекта
## 2.1 Список резюме
Список резюме представляет собой список, выводящийся с реляционной базы данных, с возможностью фильтрации по различным параметрам.
База данных, содержащая резюме, будет наполнена резюме с различных фриланс-источников (hh.ru, upwork.com)

## 2.2 Конструктор резюме
Конструктор резюме представляет собой различные поля, обязательные и необязательные для заполнения.
При вводе информации и её подтверждения будет создаваться резюме с помощью нейросети ChatGPT.

### Примерный список полей
- Опыт работы
- Навыки
- Образование
- Языки
- Позиция
- ФИО
- Контактные данные

В ходе разработки список полей будет редактироваться

Пользователю возвращается текстовая версия резюме.

## 2.3 Анализатор резюме
Анализатор резюме представляет собой сравнение вашего резюме с уже готовыми примерными резюме с помощью нейросети TensorFlow.

Пользователь будет возвращать провалидированные данные, которые возвращает нейросеть после запроса.

# 3. Стек технологий
## 3.1 Предлагаемый стек технологий для Backend-разработки
Язык разработки - python
- FastAPI -- фреймворк для создания API
- SqlAlchemy 2.0 -- ORM
- asyncpg -- библиотека для асинхронного доступа к PostgreSQL
- PostgreSQL -- СУБД проекта
- Tensorflow -- для создания и конфигурации собственной нейросети
- OpenAI -- для использования нейросети ChatGPT 
- Alembic -- для миграций

## 3.2 Предлагаемый стек технологий для Frontend-разработки
Язык разработки - JavaScript
- React -- основно фреймворк для написания веб-приложения
- ChakraUI -- библиотека готовых компонентов

## 3.3 Предлагаемый стек технологий для UI/UX дизайна
- Figma -- для создания дизайна проекта
- Photoshop -- для создания элементов дизайна, например, логотипов

# 4. Дизайн проекта
тык ты тык 