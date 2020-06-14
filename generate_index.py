# This file is used to generate index.md based on content of code-examples repo in github
# How to use:-
# Update your github username/password in this script and run below command
# python generate_index.py>index.md

import requests
import json

user = '<user>'
password = '<password>'

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