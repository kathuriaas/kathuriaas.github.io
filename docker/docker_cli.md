# Useful docker commands

Documentation of all commands can be found [here.](https://docs.docker.com/reference/)

Commands mentioned here may require `sudo` as per system configuration.

## Download/pull docker images

Docker Hub has pre-built images, which can be pulled. This base image can be used to create custom image, as per our need.

Click [here](https://hub.docker.com/_/node) for NodeJS images available on docker hub.

```shell
# Pull docker image for nodejs
docker pull node

# Pull nodejs image of specific version
docker pull node:14.4.0

# Pull ubuntu image
docker pull ubuntu
```

## Create custom image using pre-built image

To create a custom image on top of a pre-built image, we need to use Dockerfile (see below example)

```docker
FROM node:10.20.1

WORKDIR /usr/src/app

COPY . .

RUN wget https://ftp.postgresql.org/pub/source/v10.0/postgresql-10.0.tar.bz2

CMD [ "node", "app.js" ]
```

Now create a file with name "dockerfile" (without any extension) and run `docker build` command to create image. Syntax for docker build is:-

```shell
docker build [OPTIONS] PATH | URL
```

Dockerfile needs to be kept at PATH or GIT REPO, from where image is to be built.

```shell
# Build docker image from current directory
docker build --tag node_custom .

# Build docker image from git repo
docker build --tag node_custom https://github.com/kathuriaas/docker_example.git#develop

# Build docker image from git repo with code under a subfolder
docker build --tag node_custom <repo_link>#<branch_name>:<folder_name>
```

## List docker images

Images built as per above step can be listed as mentioned below:-

```shell
# List docker images
docker images
```

## Get docker images details

```shell
# Docker image details
docker image inspect <image_name or id>
```

## Run container from image

From an image, we can start a container and run the application needed.

```shell
# Docker run to create a container (npm start example)
docker run -t -i -d node_custom npm start

# Docker run to create a container (ubuntu example)
docker run -t -i -d --name my_ubuntu ubuntu /bin/bash

# Docker run to with port mapping (useful for web apps)
docker run -t -i -d -p host_port:container_port <NodeJS_image>

# Docker run to create a container (ubuntu example) without command, that will use CMD (from dockerfile, specified during image creation) as default command
docker run -t -i -d ubuntu

# Docker run to create a container with environment variables (-e)
docker run --name postgres_image -e POSTGRES_PASSWORD=test_password -d postgres

# Docker run to create a container with environment variables in a file (--env-file)
# Create a file env_file and add "POSTGRES_PASSWORD=test_password" to this file.
docker run --name postgres_image --env-file env_file -d postgres

```

Options specified above:-

```comment
-i is for interactive mode
-d for detached=true (run in background)
-t is used to allocate a tty
```

If you want the container to be removed automatically upon exit, use `--rm` option during docker run. e.g.

```shell
# container will be removed upon exit
docker run -t -i -d --rm ubuntu
```

## Create container without starting it

```shell
# Docker create container without starting it
docker create -t -i ubuntu
```

## Create image from container

```shell
# Docker commit to create a image from container, useful when container is started and modified and we want to same it to an image
docker commit <container ID>  <image name/tag>
```

## Start container

```shell
# Docker start container
docker start <container name or ID>
```

## Stop container

```shell
# Docker start container
docker stop container name or ID
```

## List docker containers

```shell
# List docker containers in running state
docker container ls

# List all docker containers
docker container ls -a

# PS command can also be used to list containers
docker ps -a
```

## Get docker container details

```shell
# Docker container details
docker container inspect <container name or id>

# We can look for IP address of container using above method. e.g.
docker container inspect <container ID>|python -c 'import sys,json;print (json.load(sys.stdin)[0]["NetworkSettings"]["Networks"]["bridge"]["IPAddress"])'
```

## Connect to a container

```shell
# Connect to a container
docker attach <container name or ID>
```

If container is used for running a web application (like node/jenkins server etc.), we might not be able to attach to it, as bash terminal may not be available. So, we can run `exec` command in such case to open a new terminal.

```shell
# Open a new terminal to connect to a container
docker exec -it <container ID> bash
```

## Run a command within a container

```shell
# Example to read a file within a container
docker exec -it <container ID> cat <file on container>
```

## Copy files between host machine and container

```shell
docker cp  <source_file> <container_id>:<dest file>
```

```shell
docker cp  <container_id>:<source_file> <dest file>
```

## Remove containers

```shell
# Remove container
docker rm <container name or ID>
```

## Remove image

```shell
# Remove container
docker rmi <Image name or ID>
```
