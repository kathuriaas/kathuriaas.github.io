# This file is used to generate README.md based on content of code-examples repo in github
# How to use:-
# python generate_readme.py>README.md

import os

print('# Code Examples')
print('')
print('Website:- <https://kathuriaas.github.io/code-examples>')
print('')
print('Single source of code examples of multiple programming languages.')
print('Directory is added for each language/technology for example codes.')
print('')
print('Click on technology name below to go to code examples of that technology/language.')
print('')
content = os.listdir('.')
content_to_remove = ['.git','_layouts']
content = list(set(content) - set(content_to_remove))
content.sort()
for dir_file_name in content:
    if os.path.isdir(dir_file_name):
        dir_file_name_display = dir_file_name.replace('_',' ').upper()
        print('- [' + dir_file_name_display + '](' + dir_file_name + ')')
        