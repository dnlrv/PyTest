# import requests; exec(requests.get('https://raw.githubusercontent.com/dnlrv/PyTest/refs/heads/main/main.py').content.decode('utf-8'))

import requests
import json

tree_url = 'https://api.github.com/repos/dnlrv/PyTest/git/trees/main?recursive=1'
maintree = requests.get(tree_url)
tree_data = json.loads(maintree.text)
#print(tree_data)
py_paths = [
    entry['path']
    for entry in tree_data.get('tree', [])
    if entry.get('path', '').endswith('.py')
       and entry['path'] != 'main.py'
]

for s in py_paths:
    #print(f'I am getting https://raw.githubusercontent.com/dnlrv/PyTest/main/{s}')
    script = requests.get(f'https://raw.githubusercontent.com/dnlrv/PyTest/main/{s}').content.decode('utf-8')
    #print(script)
    exec(script)
