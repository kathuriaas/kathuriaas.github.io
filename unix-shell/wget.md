---
layout: default
parent: UNIX
---
# WGET in UNIX

wget is used to communicate with a web address via http/https/ftp etc

## How to use:-

***wget is available on unix platform***

A simple example to download static pages of a website:-

```shell
wget \
--recursive \
--no-clobber \
--page-requisites \
--html-extension \
--convert-links \
--restrict-file-names=windows \
--no-parent \
"https://kathuriaas.github.io/code-examples/"
```
