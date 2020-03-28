from bs4 import BeautifulSoup

SIMPLE_HTML = '''
<html>
<head>
</head>
<body>
<h1>This will be the title
</h1>
<p class="subtitle">
My name is Jaskiran Kaur.</p>
<p>p without class</p>
<ul>
  <li>Aman</li>
  <li>Sahil</li>
  <li>Prince</li>
  <li>Pari</li>
</ul>
</body>
</html>
'''
simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def findtitle():
    h1_tag=simple_soup.find('h1')
    print(h1_tag.string)

def find_list_items():
    list_items=simple_soup.find_all('li')
    friends_list=[e.string for e in list_items]
    print(friends_list)

def find_subtitle():
    paragraph=simple_soup.find('p', {'class':'subtitle'})
    print(paragraph.string)

def find_other_paragraphs():
    paragraphs=simple_soup.find_all('p')
    other_paragraphs= [p for p in paragraphs if 'subtitle' not in p.attrs.get('class',[])]
    print(other_paragraphs[0].string)

findtitle()
find_list_items()
find_subtitle()
find_other_paragraphs()