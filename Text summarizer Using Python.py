import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

url = 'https://www.nwitimes.com/business/local/three-indiana-business-schools-rank-among-nations-best-according-to-u-s-news-world-report/article_9ed2ea50-c65d-5be2-ace5-0c3d951e8153.html'

article = Article(url)

article.download()
article.parse() # This will disect the article into the parts that it needs

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')

analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

