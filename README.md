# bv-2025
https://habr.com/ru/articles/810721/
Создание промта
https://habr.com/ru/companies/lanit/articles/812261/

def split_text(article_text: str) -> int:
    n = article_text.split('\n')
    count = 0
    sum = 0
    for i in n:
        if len(i) > 100:
            count += 1
            sum += len(i)
    return sum // count
    #return article_text.split('\n')

summa = 0
count = 0
for i in range(0, 10):
    summa += split_text(article_text=article_list[i].__dict__['_Article__text'])
    count += 1

print(summa // count)
