import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import logging


def buildFreqDist(url: str):
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
    except Exception as ex:
        logging.critical(ex)
        return "Entered URL link gave an access error : " + str(ex)

    # extracting the text from html
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(strip=True)

    # extracting the tokens
    tokens = [t for t in text.split()]

    sr = stopwords.words('english')
    clean_tokens = tokens[:]
    for token in tokens:
        if token in stopwords.words('english'):

            clean_tokens.remove(token)
    freq = nltk.FreqDist(clean_tokens)
    return freq


# for key,val in freq.items():
#     if val > 100:
#         print(str(key) + ':' + str(val))

# freq.plot(20, cumulative=False)
