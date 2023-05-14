
from bs4 import BeautifulSoup
import requests

import sys

arg = sys.argv[1:]
arg2 = arg[0].replace(" ", "+")
print(arg2)
link_sp = []

x = 1

while True:
    if x == 1:
        url = "https://filmot.com/search/" + str(arg2) + "/1/?"

    else:
        url = "https://filmot.com/search/" + str(arg2) + "/1/" + str(x) + "?"

    request = requests.get(url)

    soup = BeautifulSoup(request.text, "html.parser")

    teme = soup.find("div", {"id": "videoresults"})

    for temes in teme:
        temes = temes.find("img")
        if "https://img.youtube.com/" in str(temes):
            link = temes.get('src')
            it_link = "https://www.youtube.com/watch?v=" + str(link[27: 38])
            link_sp.append(it_link)

    x += 1
    if x == 4:
        break

with open("link.txt", "w") as file:
    print(*link_sp, file=file, sep="\n")
