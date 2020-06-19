# This file is used to generate index.md based on content of code-examples repo in github
# How to use:-
# python generate_index.py>index.md

import os
import json

user = ''
password = ''

#res = requests.get('https://api.github.com/repos/kathuriaas/code-examples/contents',auth=(user, password));
git_pages_link='https://kathuriaas.github.io/code-examples/'
#data_list = json.loads(res.text)

print ('# What are you looking for today:-')
print ('')
content = os.listdir('.')
content.sort()
for dir_file_name in content:
    if os.path.isdir(dir_file_name) and dir_file_name != '.git':
        dir_file_name_display = dir_file_name.replace('_',' ').upper()
        print('- ' + dir_file_name_display)
        file_list = os.listdir(dir_file_name)
        file_list.sort()
        for file_name in file_list:
            file_name_display = file_name.replace('.md','').replace('_',' ').capitalize()
            file_path = git_pages_link + dir_file_name + '/' + file_name.replace('.md','')
            print('  - [' + file_name_display + '](' + file_path + ')')
        print ('')