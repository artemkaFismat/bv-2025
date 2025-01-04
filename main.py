from googlesearch import search
import requests
from bs4 import BeautifulSoup

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def processing_text(text: str, lang='russian') -> str:
   stop_words = set(stopwords.words(lang))
   word_tokens = word_tokenize(text.strip())
   cleaned_text = [word for word in word_tokens if word.lower() not in stop_words]
   cleaned_text = ' '.join(cleaned_text)
   return cleaned_text

def search_google(reque: str, lang="ru", region="ru", num_results=1) -> list:
    search_list = []
    search_object = search(reque, lang=lang, num_results=num_results)
    for i in search_object:
        search_list.append(i)
    return search_list

def scraping_website(search_list: list) -> dict:
    website_data = {}
    search_pair = []
    text = ""
    count = 0
    for url in search_list:
        count += 1
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        all_tags = soup.find_all()
        for tag in all_tags:
            text += str(tag.get_text()) + ' '
        search_pair.append(url)
        search_pair.append(processing_text(text=text))
        website_data[count] = search_pair
    return website_data
   
print(scraping_website(search_list=search_google(reque="algol")))
