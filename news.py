from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/section/world'

driver = webdriver.Chrome()
driver.get(url)
html_content = driver.page_source

soup = BeautifulSoup(html_content, 'html.parser')
articles = soup.find_all('li', class_='css-1l4spti')

for article in articles:
    title = article.find('h2').text.strip()
    link = article.find('a')['href']
    if link:
        print(title)
        print(link)

driver.quit()
