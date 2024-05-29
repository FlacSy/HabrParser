import requests
from bs4 import BeautifulSoup
import random
from typing import List, Tuple, Optional

class HabrParser:
    def __init__(self):
        self.base_url = "https://habr.com"
        self.cache = {}

    def _get_soup(self, url: str) -> BeautifulSoup:
        if url in self.cache:
            return self.cache[url]
        
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        self.cache[url] = soup
        
        return soup

    def _get_list_articles(self, category: Optional[str], page: int) -> Tuple[List[str], List[str]]:
        """
        Получает список статей из выбранной категории на Хабре.

        :param category: Категория на Хабре (например, "develop" или "popular_science").
        :param page: Номер страницы.
        :return: Списки заголовков и ссылок статей.
        """
        category_url = f"{self.base_url}/ru/flows/{category}/page{page}" if category else f"{self.base_url}/ru/articles/page{page}"
        soup = self._get_soup(category_url)

        articles = soup.find_all('h2', class_='tm-title tm-title_h2')
        articles_titles = [article.find('span').text.strip() for article in articles]
        articles_links = [self.base_url + article.find('a', class_='tm-title__link').get('href') for article in articles]

        return articles_titles, articles_links

    def get_random_article(self, category: Optional[str] = None, pages: int = 1) -> Tuple[str, str]:
        """
        Получает случайную статью из выбранной категории на Хабре.

        :param category: Категория на Хабре (например, "develop" или "popular_science").
        :param pages: Количество страниц для поиска случайной статьи.
        :return: Заголовок и ссылка случайной статьи.
        """
        articles_titles, articles_links = [], []
        for page in range(1, pages + 1):
            titles, links = self._get_list_articles(category, page)
            articles_titles.extend(titles)
            articles_links.extend(links)
        
        article_link, article_title = random.choice(list(zip(articles_links, articles_titles)))

        return article_title, article_link

    def get_article_by_id(self, article_id: int) -> Tuple[str, str, Optional[str]]:
        """
        Получает статью с выбранной статьи на Хабре по её ID.

        :param article_id: ID статьи на Хабре.
        :return: Заголовок, ссылка и краткое описание статьи.
        """
        article_url = f"{self.base_url}/ru/articles/{article_id}/"
        soup = self._get_soup(article_url)
        articles_title = soup.find('title').text.strip()
        articles_link = requests.get(article_url).url
        articles_image = soup.find('figure', class_='full-width').find('img').get('data-src') if soup.find('figure', class_='full-width') else None

        return articles_title, articles_link, articles_image
    
    def get_article_text_by_id(self, article_id: int) -> Tuple[str, str, str]:
        """
        Получает текст статьи с выбранной статьи на Хабре по её ID.

        :param article_id: ID статьи на Хабре.
        :return: Заголовок, ссылка и текст статьи.
        """
        article_url = f"{self.base_url}/ru/articles/{article_id}/"
        soup = self._get_soup(article_url)
        articles_text = soup.find('div', class_='tm-article-body').text.strip()

        return articles_text

    def get_random_article_id(self) -> int:
        """
        Получает случайный ID статьи на Хабре.

        :return: ID статьи на Хабре.
        """
        random_link = self.get_random_article()[1]
        article_id = random_link.split('/')[-2]

        return int(article_id)
    
    def get_random_article_image(self) -> Optional[str]:
        """
        Получает случайную картинку статьи на Хабре.

        :return: Ссылка на картинку статьи.
        """
        random_link = self.get_random_article()[1]
        article_id = random_link.split('/')[-2]
        article_image = self.get_article_by_id(article_id)[2]

        return article_image
    
    def get_random_article_title(self) -> str:
        """
        Получает случайный заголовок статьи на Хабре.

        :return: Заголовок статьи.
        """
        random_link = self.get_random_article()[1]
        article_id = random_link.split('/')[-2]

        article_title = self.get_article_by_id(article_id)[0]
        return article_title

    def search_articles_by_keyword(self, keyword: str, category: Optional[str] = None, pages: int = 1) -> List[Tuple[str, str]]:
        """
        Ищет статьи по ключевому слову.

        :param keyword: Ключевое слово для поиска.
        :param category: Категория на Хабре (например, "develop" или "popular_science").
        :param pages: Количество страниц для поиска.
        :return: Список заголовков и ссылок на статьи.
        """
        results = []
        for page in range(1, pages + 1):
            titles, links = self._get_list_articles(category, page)
            for title, link in zip(titles, links):
                if keyword.lower() in title.lower():
                    results.append((title, link))
        return results

    def get_comments_by_article_id(self, article_id: int) -> List[str]:
        """
        Получает комментарии к статье на Хабре по её ID.

        :param article_id: ID статьи на Хабре.
        :return: Список комментариев.
        """
        article_url = f"{self.base_url}/ru/articles/{article_id}/comments/"
        soup = self._get_soup(article_url)
        comments = soup.find_all('div', class_='tm-comment__body-content')
        comments_texts = [comment.text.strip() for comment in comments]

        return comments_texts
