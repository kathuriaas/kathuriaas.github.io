# Async, Await and Promise in NODEJS

```await``` is used to wait for a ```Promise```. It can be used only inside an ```async``` function.

```nodejs
async function func_nm(){
    return_value = await <expression>
    }
```

```return_value``` is the value fulfilled by Promise.

```expression``` is a Promise or any other value to wait for.
