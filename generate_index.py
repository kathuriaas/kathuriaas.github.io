# This file is used to generate index.md based on content of code-examples repo in github
# How to use:-
# python generate_index.py>index.md

import os

print ('# What are you looking for today:-')
print ('')
content = os.listdir('.')
content.sort()
for dir_file_name in content:
    if os.path.isdir(dir_file_name) and dir_file_name != '.git' and dir_file_name != '_layouts':
        dir_file_name_display = dir_file_name.replace('_',' ').upper()
        print('- ' + dir_file_name_display)
        file_list = os.listdir(dir_file_name)
        file_list.sort()
        for file_name in file_list:
            file_name_display = file_name.replace('.md','').replace('_',' ')
            file_path = dir_file_name + '/' + file_name.replace('.md','')
            print('  - [' + file_name_display + '](' + file_path + ')')
        print ('')