import json

maintreeurl  = "https://api.github.com/repos/dnlrv/PyTest/git/trees/main?recursive=1"
basecripturl = "https://raw.githubusercontent.com/dnlrv/PyTest/main/"

maintree = requests.get(maintreeurl)

pyPaths = [i['path'] for i in (json.loads(maintree.text))['tree'] if i['path'].endswith('.py')]

for s in pyPaths:
  exec(requests.get(f'{basecripturl}{s}')).content.decode('utf-8')
