---
layout: default
parent: NodeJS
nav_order: 7
---
# Functions in NodeJS

## Different ways to write a function in nodeJS

### Method 1:-

```js
function test_fn (param1,param2){
    console.log('param1 is: ', param1);
    console.log('param2 is: ', param2);
  }

test_fn ('p1','p2');
```

### Method 2:-

```js
const test_fn = function (param1,param2){
    console.log('param1 is: ', param1);
    console.log('param2 is: ', param2);
  }

test_fn ('p1','p2');
```

### Method 3:-

```js
const test_fn = (param1,param2)=>{
    console.log('param1 is: ', param1);
    console.log('param2 is: ', param2);
  }

test_fn ('p1','p2');
```
