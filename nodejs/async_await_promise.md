# Async, Await and Promise in NODEJS

```await``` is used to wait for a ```Promise```. It can be used only inside an ```async``` function.

```nodejs
async function func_nm(){
    return_value = await <expression>
    }
```

```return_value``` is the value fulfilled by Promise.

```expression``` is a Promise or any other value to wait for.

```await``` pauses the async function execution, until a ```Promise``` is resolved or rejected.

***Example 1:-***

```nodejs
function resolvePromise() {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve('resolved after await');
    }, 3000);
  });
}

async function func() {
  console.log(Date.now());
  var ret_val = await resolvePromise();
  console.log(Date.now());
  console.log(ret_val);
}

func();
```

***Example 2:-***

```nodejs
const request = require('request');

function resolvePromise() {
  return new Promise((resolve,reject) => {
        request('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY', { json: true }, (err, res, body) => {
        if (err) { reject(err) }
          resolve(body);
    });
    });
  }

async function waitPromise(){
    var ret_val = await resolvePromise();
    console.log(ret_val);
}

waitPromise();
```

## Difference between callback based function and promise based function

- A callback based function may return undefined value.
- If a callback based function is converted to a promise based function, it will, for sure return some value (resolved promise).
- Below example is to convert a callback based function to promise

***callback example (it returns undefined)***

```nodejs
const request = require('request');


function withoutPromise() {
        request('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY', { json: true }, (err, res, body) => {
        if (err) { reject(err) }
                return(body);
    });
  }

async function waitReturn(){
    var ret_val = await withoutPromise();
    console.log(ret_val);
}

waitReturn();
```

***conversion to promise example (it returns promised value)***

```nodejs
const request = require('request');

function withPromise() {
  return new Promise((resolve,reject) => {
        request('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY', { json: true }, (err, res, body) => {
        if (err) { reject(err) }
          resolve(body);
    });
    });
  }

async function waitReturn(){
    var ret_val = await withPromise();
    console.log(ret_val);
}

waitReturn();
```
