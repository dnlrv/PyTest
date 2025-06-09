import requests

maintreeurl  = "https://api.github.com/repos/dnlrv/PyTest/git/trees/main?recursive=1"
basecripturl = "https://raw.githubusercontent.com/dnlrv/PyTest/main/"

maintree = requests.get(maintreeurl)
