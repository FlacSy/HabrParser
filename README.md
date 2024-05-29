# HabrParser

## Обзор
Библиотека `HabrParser` предоставляет инструменты для скрапинга и получения статей, комментариев и другого контента с веб-сайта Habr. В этой документации подробно описано использование и функциональность каждого метода в классе `HabrParser`.

## Установка
Чтобы установить библиотеку `HabrParser`, воспользуйтесь pip:
[PyPi]()
```bash
pip install HabrParser
```
[GitHub]()
```bash
pip install git+https://github.com/FlacSy/HabrParser
```

## Использование

### Инициализация
Чтобы использовать `HabrParser`, сначала импортируйте библиотеку и создайте экземпляр класса `HabrParser`:
```python
from habr_parser import HabrParser

parser = HabrParser()
```

### Методы

#### `_get_soup(url: str) -> BeautifulSoup`
Это закрытый метод, который получает содержимое указанного URL и возвращает объект BeautifulSoup для разбора HTML.
- **Параметры**:
  - `url` (str): URL веб-страницы для получения содержимого.
- **Возвращает**: Объект `BeautifulSoup`.

#### `_get_list_articles(category: Optional[str], page: int) -> Tuple[List[str], List[str]]`
Получает список статей из указанной категории и страницы на сайте Habr.
- **Параметры**:
  - `category` (Optional[str]): Категория на Habr (например, "develop" или "popular_science").
  - `page` (int): Номер страницы для получения статей.
- **Возвращает**: Кортеж, содержащий списки заголовков статей и ссылок на них.

#### `get_random_article(category: Optional[str] = None, pages: int = 1) -> Tuple[str, str]`
Получает случайную статью из указанной категории и диапазона страниц на сайте Habr.
- **Параметры**:
  - `category` (Optional[str]): Категория на Habr (по умолчанию `None`).
  - `pages` (int): Количество страниц для поиска случайной статьи (по умолчанию `1`).
- **Возвращает**: Кортеж, содержащий заголовок и ссылку на случайную статью.

#### `get_article_by_id(article_id: int) -> Tuple[str, str, Optional[str]]`
Получает статью с Habr по её ID.
- **Параметры**:
  - `article_id` (int): ID статьи на Habr.
- **Возвращает**: Кортеж, содержащий заголовок, ссылку и, при наличии, ссылку на изображение статьи.

#### `get_article_text_by_id(article_id: int) -> str`
Получает текст статьи с Habr по её ID.
- **Параметры**:
  - `article_id` (int): ID статьи на Habr.
- **Возвращает**: Текст статьи.

#### `get_random_article_id() -> int`
Получает случайный ID статьи с Habr.
- **Возвращает**: ID случайной статьи на Habr.

#### `get_random_article_image() -> Optional[str]`
Получает ссылку на изображение случайной статьи на Habr.
- **Возвращает**: Ссылка на изображение случайной статьи.

#### `get_random_article_title() -> str`
Получает заголовок случайной статьи на Habr.
- **Возвращает**: Заголовок случайной статьи.

#### `search_articles_by_keyword(keyword: str, category: Optional[str] = None, pages: int = 1) -> List[Tuple[str, str]]`
Ищет статьи на Habr по ключевому слову.
- **Параметры**:
  - `keyword` (str): Ключевое слово для поиска.
  - `category` (Optional[str]): Категория на Habr (по умолчанию `None`).
  - `pages` (int): Количество страниц для поиска (по умолчанию `1`).
- **Возвращает**: Список кортежей, содержащих заголовки и ссылки на статьи.

#### `get_comments_by_article_id(article_id: int) -> List[str]`
Получает комментарии к статье на Habr по её ID.
- **Параметры**:
  - `article_id` (int): ID статьи на Habr.
- **Возвращает**: Список комментариев к статье.

## Примеры:


1. **get_random_article(category: Optional[str] = None, pages: int = 1) -> Tuple[str, str]**
```python
from habr_parser import HabrParser

parser = HabrParser()

# Пример получения случайной статьи из категории "develop" с первой страницы
title, link = parser.get_random_article(category="develop", pages=1)
print(f"Title: {title}\nLink: {link}")
```

2. **get_article_by_id(article_id: int) -> Tuple[str, str, Optional[str]]**
```python
from habr_parser import HabrParser

parser = HabrParser()

# Пример получения статьи по её ID
article_id = 123456
title, link, image = parser.get_article_by_id(article_id)
print(f"Title: {title}\nLink: {link}\nImage: {image}")
```

3. **get_article_text_by_id(article_id: int) -> str**
```python
from habr_parser import HabrParser

parser = HabrParser()

# Пример получения текста статьи по её ID
article_id = 123456
article_text = parser.get_article_text_by_id(article_id)
print(article_text)
```

4. **get_random_article_id() -> int**
```python
from habr_parser import HabrParser

parser = HabrParser()

# Пример получения случайного ID статьи
article_id = parser.get_random_article_id()
print(article_id)
```

5. **get_random_article_image() -> Optional[str]**
```python
from habr_parser import HabrParser

parser = HabrParser()

# Пример получения ссылки на изображение случайной статьи
image_url = parser.get_random_article_image()
print(image_url)
```

6. **get_random_article_title() -> str**
```python
from habr_parser import HabrParser

parser = HabrParser()

# Пример получения заголовка случайной статьи
article_title = parser.get_random_article_title()
print(article_title)
```

7. **search_articles_by_keyword(keyword: str, category: Optional[str] = None, pages: int = 1) -> List[Tuple[str, str]]**
```python
from habr_parser import HabrParser

parser = HabrParser()

# Пример поиска статей по ключевому слову "Python"
results = parser.search_articles_by_keyword(keyword="Python", pages=2)
for title, link in results:
    print(f"Title: {title}\nLink: {link}\n")
```

8. **get_comments_by_article_id(article_id: int) -> List[str]**
```python
from habr_parser import HabrParser

parser = HabrParser()

# Пример получения комментариев к статье по её ID
article_id = 123456
comments = parser.get_comments_by_article_id(article_id)
for comment in comments:
    print(comment)
```
