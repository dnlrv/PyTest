# import requests; exec(requests.get('https://raw.githubusercontent.com/dnlrv/PyTest/refs/heads/main/example.py').content.decode('utf-8'))

import requests
import json

tree_url = 'https://api.github.com/repos/dnlrv/PyTest/git/trees/main?recursive=1'
maintree = requests.get(tree_url)
tree_data = json.loads(maintree.text)
print(tree_data)
py_paths = [
    p for p in tree_data['tree']
    if p['path'].endswith('.py') and p['path'] != 'main.py'
]

for s in py_paths:
    print(f'I am getting https://raw.githubusercontent.com/dnlrv/PyTest/main/{s}')
    script = requests.get(f'https://raw.githubusercontent.com/dnlrv/PyTest/main/{s}').content.decode('utf-8')
    print(script)
    exec(script)
