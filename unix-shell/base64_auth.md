---
layout: default
parent: UNIX
---
# Base64 command

`base64` command in UNIX can be used to generate auth headers from a username and password combination. Same command can be used to decode username and passwords. These auth headers are generally used in REST API calls in format of `Basic <auth header>`.

## Generate auth headers:-

```shell
# Pass correct username and password combination as per need
echo -n "user:pass"|base64
```

This will generate a auth header as below (output is from above values):-

```shell
dXNlcjpwYXNz
```

## Generate user:password from auth headers:-

```shell
# Pass auth header as per need
echo "dXNlcjpwYXNz"|base64 -d
```

This will generate credentials as below (output is from above values):-

```shell
user:pass
```
