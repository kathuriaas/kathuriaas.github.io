# Dockerfile examples

Dockerfile is used to create custom docker images by specifying instructions in file exactly named as `dockerfile` (case -Insensitive, without extention). Openshift custom images with `docker` strategy can also be created using `dockerfile`.

After creating the dockerfile, follow [docker cli documentation](https://kathuriaas.github.io/code-examples/docker/docker_cli) to create the image and start the container.

## Example 1:- ubuntu image with postgresql client

```dockerfile
FROM ubuntu

WORKDIR /usr/src/app

RUN apt-get update

RUN apt-get install -y postgresql-client

CMD [ "/bin/bash" ]
```

## Example 2:- NodeJS image with postgresql client

```dockerfile
FROM node:10.20.1

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

RUN apt-get update

RUN apt-get install -y postgresql-client

CMD [ "node", "app.js" ]
```

Above dockerfile can be kept along with your NodeJS application code. To test this, simple `Hello World` nodejs app is available on github [here](https://github.com/kathuriaas/docker_example.git).
