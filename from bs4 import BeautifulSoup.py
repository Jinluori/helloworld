from bs4 import BeautifulSoup
import lxml
html = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;
   and their names were
<a herf="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
   and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
  # 根据html_doc创建BeautifulSoup类的对象，并指定使用lxml解析器解析文档
soup = BeautifulSoup(html, features='lxml')
print(soup.prettify())