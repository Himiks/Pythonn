import requests, sys, webbrowser, bs4


print('Googling...')

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()


soup = bs4.BeautifulSoup(res.text, 'lxml')
linkElems = soup.select('a[href^="/url?q="]')
print(linkElems)


numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    print("open")
    

