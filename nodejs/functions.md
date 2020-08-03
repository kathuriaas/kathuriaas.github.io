---
layout: default
parent: NodeJS
---
# Different ways to write a function in nodeJS

## Method 1:-

```nodejs
function test_fn (param1,param2){
    console.log('param1 is: ', param1);
    console.log('param2 is: ', param2);
  }

test_fn ('p1','p2');
```

## Method 2:-

```nodejs
const test_fn = function (param1,param2){
    console.log('param1 is: ', param1);
    console.log('param2 is: ', param2);
  }

test_fn ('p1','p2');
```

## Method 3:-

```nodejs
const test_fn = (param1,param2)=>{
    console.log('param1 is: ', param1);
    console.log('param2 is: ', param2);
  }

test_fn ('p1','p2');
```
