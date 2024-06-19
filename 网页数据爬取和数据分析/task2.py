import json

import requests
import unicodedata
from bs4 import BeautifulSoup, Comment
import re
from nltk import PorterStemmer
from nltk.corpus import stopwords

def task2(link_to_extract: str, json_filename: str):
    response = requests.get(link_to_extract)
    html_content = response.content
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(html_content, "html.parser")
    fulltext = soup.find("div", id="mw-content-text")

    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    remove_list = fulltext.find_all('th', {"class": "infobox-label"})
    for i in remove_list:
        i.decompose()

    remove_list = fulltext.find_all('div', {"class": "printfooter"})
    for i in remove_list:
        i.decompose()

    remove_list = fulltext.find_all('div', {"id": "toc"})
    for i in remove_list:
        i.decompose()

    ....

    # 找到所有文本单词,并剔除注释、html标签单词
    text_words = []
    for element in fulltext.find_all(text=True):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta']:
            continue
        if isinstance(element, str):
            text_words.append(element.strip())
        else:
            text_words.append(element.text.strip())

    # 将文本单词列表转换为字符串
    text_str = ' '.join(text_words)
    # 剔除所有非字母符号
    text_str = unicodedata.normalize('NFKD', text_str.casefold())
    text_str = re.sub(r"[^a-zA-Z\\]", ' ', text_str)
    text_str = re.sub(r'\s+', ' ', text_str)

    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()

    word_list = text_str.split()
    word_list = [w for w in word_list if not w in stop_words]
    word_list = [w for w in word_list if len(w) >= 2]
    word_list = [ps.stem(w) for w in word_list]

    output = {link_to_extract: word_list}

    with open(json_filename, "w") as json_file:
        json.dump(output, json_file)

    return output
