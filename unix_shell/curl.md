# cURL (client for URLs) is tool to transfer data using different protocols

*curl is available on unix platform by default. It can also be used on windows with additional installation (e.g. git bash etc.). cURL can be used as a simple method to call **REST APIs** from command line. See man page of curl for more details.*

*This page uses github/NASA api for demo. Look for documentation of API needed to use curl. Most of the REST API docuemtation are created with curl example.*

## Sample curl requests:-

### A simple example without any option. Default is ```GET``` request:-

```shell
curl "https://api.github.com/users/kathuriaas"
```

### ```GET``` request returning head details (-I or --head):-

```shell
curl -I "https://api.github.com/users/kathuriaas"
```

### ```GET``` request with passing query parameters:-

```shell
curl -G -d 'api_key=DEMO_KEY' "https://api.nasa.gov/planetary/apod"
```

Above code is similar to:-

```shell
curl "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
```

More details for request and response headers can be viewed with ```-i (--include) and -v (--verbose)``` options.

***Following options are useful when making an HTTP request to a server:-***

- -X, --request - (Specify a custom request method e.g. ```GET,POST``` to use when communicating with the HTTP server)
- -H, --header - Send header information (e.g. "Content-Type: application/json")  
- -d, --data - Sends the specified data (can be json data, if -H has content type as json)  
- -i, --include - Display response headers

### ```POST``` request to create a github repo with token:-

```shell
curl -i -H "Authorization: token <paste github token here>" -d '{"name":"test_github_api", "auto_init": true, "private": true,
"gitignore_template": "nanoc"}' "https://api.github.com/user/repos"
```

### ```POST``` request to create a github repo with username & password:-

```shell
curl -i -u "username:password" -d '{"name":"test_github_api", "auto_init": true, "private": true,
"gitignore_template": "nanoc"}' "https://api.github.com/user/repos"
```

## Hide progress bar in a curl request:-

curl output can show progress which needs to be hidden, sometimes. This can be done with ```-s (--silent)``` option, as mentioned below:-

```shell
curl -s "https://api.github.com/users/kathuriaas"|python -c 'import sys,json;print (json.load(sys.stdin)["login"])'
```

## Download a binary file using curl [use ```-o ``` option]:-

```shell
curl -o node-v12.18.0-linux-x64.tar.xz "https://nodejs.org/dist/v12.18.0/node-v12.18.0-linux-x64.tar.xz"
```


## Save output to a file using curl [use ```-O (--output)``` option]:-

```shell
curl -O data.json "https://api.github.com/users/kathuriaas"|python -c 'import sys,json;print (json.load(sys.stdin))'
```
