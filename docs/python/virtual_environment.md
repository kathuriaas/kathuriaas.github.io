---
layout: default
parent: PYTHON
---
# Setup virtual environment

## Linux

In some of the linux flavours, we may be required to install python-virtualenv or pipenv etc., based on version of python.

Go to your directory, where you plan to create your project

```shell
cd <project_dir>
```

Setup virtual environment (this will create a folder [e.g. here myvenv] to hold files for python's virtual environment)

```shell
#For Python 2.x
virtualenv myvenv

#For Python 3.x
python3 -m venv myvenv
```

Activate virtual environment

```shell
source myvenv/bin/activate
```

Install packages in virtual environment

```shell
# This will now install packages available in virtaul environment
pip install <package name>
```
