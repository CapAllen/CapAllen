import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.capallen.top/atom.xml')
soup = BeautifulSoup(feed.content,'html.parser')
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}

with open('README.md', 'w') as f:
    f.write(r'''
```
                          ___       __       __       _______ .__   __.  __     _______.               
                         /   \     |  |     |  |     |   ____||  \ |  | (_ )   /       |               
                        /  ^  \    |  |     |  |     |  |__   |   \|  |  |/   |   (----`               
                       /  /_\  \   |  |     |  |     |   __|  |  . `  |        \   \                   
                      /  _____  \  |  `----.|  `----.|  |____ |  |\   |    .----)   |                  
                     /__/     \__\ |_______||_______||_______||__| \__|    |_______/                   
                                                                                                       
 _______       ___   .___________.    ___              _______.  ______  __   _______ .__   __.   ______  _______ 
|       \     /   \  |           |   /   \            /       | /      ||  | |   ____||  \ |  |  /      ||   ____|
|  .--.  |   /  ^  \ `---|  |----`  /  ^  \          |   (----`|  ,----'|  | |  |__   |   \|  | |  ,----'|  |__   
|  |  |  |  /  /_\  \    |  |      /  /_\  \          \   \    |  |     |  | |   __|  |  . `  | |  |     |   __|  
|  '--'  | /  _____  \   |  |     /  _____  \     .----)   |   |  `----.|  | |  |____ |  |\   | |  `----.|  |____ 
|_______/ /__/     \__\  |__|    /__/     \__\    |_______/     \______||__| |_______||__| \__|  \______||_______|
                                                                                                                  
```
## Latest blog posts
''')
    for entry in soup.find_all('entry')[:5]:
        text = entry.find('title').get_text()
        url = entry.find('link')['href']
        published = entry.find('published').get_text()[:10]
        f.write('- {} [{}]({})\n'.format(published, text, url))

    f.write('''
[>>> More blog posts](https://www.capallen.top)
## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=CapAllen)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=CapAllen&hide=ipynb,html&layout=compact)
''')
