import requests
from bs4 import BeautifulSoup

URL_STR = "https://www.goodreads.com/author/quotes/34583.Vincent_van_Gogh?page="

for x in range(100):
  URL=URL_STR+str(x+1)
  page = requests.get(URL)

  soup = BeautifulSoup(page.content, "html.parser")
  results = soup.find(class_="quotes")

  quotes =results.find_all("div", class_="quote")

  with open("quote.txt", "a") as f:
    for quote in quotes:
      quote_text = quote.find("div", class_="quoteText")
      f.write(str(quote_text).split("<br/>")[0].split("<div class=\"quoteText\">")[1].strip())
      f.write('\n\n')
