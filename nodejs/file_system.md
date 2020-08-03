---
layout: default
parent: NodeJS
---
# File System Module

## FS (file system) module in nodejs

Following are steps to import and use file system module to interact with files on server. We need fs module, which is part of default installation of nodejs

***Please note:-** NodeJS should be already installed. If not, follow the [installation steps](./install_nodejs.md)*

Now, create a file `sample.html` at any location on your computer and add below content to it:

```html
<html>
<body>
<h1>Hello World</h1>
</body>
</html>
```

Create a file `app.js` at the same location on your computer and add below code to it:

```nodejs
var http = require('http');
var fs = require('fs');

httpServer = http.createServer(function(req,res){
    data = fs.readFileSync('sample.html')
    res.writeHead(200,{'Content-Type':'text/html'});
    res.write(data);
    res.end();
    });

httpServer.listen(3000);
```

Above code will create an http server.

Now, start your nodejs server using following command:-

```nodejs
node app.js
```

Now, open link <http://localhost:3000/> in your favourite browser and you should see "Hello World" on the page.
