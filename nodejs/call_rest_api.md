---
layout: default
parent: NodeJS
---
# Call REST API

## Different ways to call a REST API in NodeJS

Simplest way to call rest API is HTTP module. However, we rarely use this method. Most of the other modules, use HTTP, to simplify REST API call. So, we will use other modules here.

## *Request module*

***Example 1:-***

```js
# Code to fetch data from NASA API:-
const request = require('request');

request('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY', { json: true }, (err, res, body) => {
  if (err) { console.log(err); }
  console.log('Response is: ', res);
  console.log('Body is: ', body);
});
```

***Example 2:-***

```js
const request = require('request');

const options = {
  url: 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
};

request(options, (err, res, body) => {
  if (err) { console.log(err); }
  console.log('Response is: ', res);
  console.log('Body is: ', body);
});
```

***Example 3:-***

```js
const request = require('request');

const options = {
  url: 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY',
  method :'GET'
};

var callback = function(err, res, body){
    if (err) { console.log(err); }
    console.log('Response is: ', res);
    console.log('Body is: ', body);
  }

request(options, callback);
```

***Example 4 (Get Github Repo):-***

```js
const request = require('request');

const options = {
  url: 'https://api.github.com/user/repos',
  method :'GET',
  headers :{'User-Agent' :'kathuriaas' },
  'auth': {
    'user': 'kathuriaas',
    'pass': '<password>',
  }
};

var callback = function(err, res, body){
    if (err) { console.log(err); }
    console.log('Body is: ', JSON.parse(body));
  }

request(options, callback);
```

***Example 5 (Get Github Repo):-***

```js
const request = require('request');

const options = {
  url: 'https://api.github.com/user/repos',
  method :'GET',
  headers : { 'User-Agent' :'kathuriaas',
            "Authorization" : "Basic "+ new Buffer(username + ":" + password).toString("base64")
        }
};

var callback = function(err, res, body){
    if (err) { console.log(err); }
    console.log('Body is: ', JSON.parse(body));
  }

request(options, callback);
```

***Example 6 (Create Github Repo):-***

<span style="color:green"> *Here body option is equivalent to data parameter of curl. Since json is true, body must be a JSON object.* </span>

```js
const request = require('request');

const options = {
  url: 'https://api.github.com/user/repos',
  method :'POST',
  json : true,
  headers : {
            'User-Agent' :'kathuriaas',
            "Authorization" : "Basic "+ new Buffer(username + ":" + password).toString("base64")
        },
  body : {
            "name":"test_github_api",
            "auto_init": true,
            "private": true,
            "gitignore_template": "nanoc"
        }
};

var callback = function(err, res, body){
    if (err) { console.log(err); }
    console.log('Body is: ', body);
  }

request(options, callback);
```
