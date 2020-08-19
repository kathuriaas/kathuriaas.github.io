---
layout: default
parent: PYTHON
nav_order: 1
---
# Install Python

## Windows

1. Go to link <https://www.python.org/downloads/windows/>
2. Page will display options to download stable releases.
3. Click on Download button. If you are looking for a different version, scroll down on the page and select the version you need.
4. This will download an installable (exe file) for windows.
5. Click on downloaded ```.exe``` file to install python.
6. Follow on-screen steps.
7. Once installed, on command prompt, type ```python --version``` to check version of python installed.
8. In case, it is showing different version OR not working, update PATH environment variable.

## Ubuntu

Install python 3.7 using below steps:-

```shell
sudo apt install python3.7
```

Now, check python version using:-

```python
python --version
```

If output of above results in a different version, follow below steps to use this version as default python version on your machine:-

```shell
which python
which python3.7
```

This should give an output like:-

```shell
/usr/bin/python
/usr/bin/python3.7
```

Run below commands to point python to python3.7:-

```shell
ln -s /usr/bin/python3.7 /usr/bin/python
```

Check if pip is working fine using ```pip --version```. If any issue, install pip:-

```shell
sudo apt install python3-pip
```

## Linux
