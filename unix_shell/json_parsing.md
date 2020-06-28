# Parsing JSON data from standard input

When calling a REST API via command line (e.g. using curl), data is resulted in JSON format, although it is a string. So, we need to parse the data to get required fields. This can be achieved with python as mentioned in below example:-

```shell
curl "https://api.github.com/users/kathuriaas"|python -c 'import sys,json;print (json.load(sys.stdin))'
```

Data retrieved above can be further broken as needed, as mentioned below:-

```shell
curl "https://api.github.com/users/kathuriaas"|python -c 'import sys,json;print (json.load(sys.stdin)["login"])'
```
