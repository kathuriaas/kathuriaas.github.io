---
layout: default
parent: PYTHON
---
# Get contents of repo on github

Get folder list on root of github repo and then list files under each directory. Output of this script can be saved as a markdown file (.md)

```python
import requests
import json

user = ''
password = ''

res = requests.get('https://api.github.com/repos/kathuriaas/code-examples/contents',auth=(user, password));
git_pages_link='https://kathuriaas.github.io/code-examples/'
data_list = json.loads(res.text)

print ('# What are you looking for today:-')
print ('')

for data_dict in data_list:
    if data_dict["type"] == "dir":
        dir_name = data_dict["name"].replace('_',' ').upper()
        dir_tree_link = data_dict["_links"]["self"]
        print('- ' + dir_name)
        dir_tree_contents = requests.get(dir_tree_link,auth=(user, password));
        dir_tree_data_list = json.loads(dir_tree_contents.text)
        for dir_tree_data_list_file in dir_tree_data_list:
            file_name = dir_tree_data_list_file["name"].replace('.md','').replace('_',' ').capitalize()
            file_path = dir_tree_data_list_file["path"].replace('.md','')
            print('  - [' + file_name + '](' + git_pages_link + file_path + ')')
        print ('')
```
