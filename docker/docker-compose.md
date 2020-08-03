---
layout: default
parent: DOCKER
---
# Docker compose

Docker compose is dependent upon docker engine. To install docker, follow [Install docker](./install_docker) link for this.

Docker compose is used to group multiple services using a single file. e.g., if we need to have two containers for our applications, one for nodejs and another one for postgres DB, we can create a single file to create/run containers using a single file.

## Install docker-compose

***For complete documentation, click [here](https://docs.docker.com/compose/install/)***

For linux, follow below steps:-

1. Download compose:-

    `sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`

2. Change executable permissions for docker-compose:-

    `sudo chmod +x /usr/local/bin/docker-compose`

3. Verify `docker-compose` is available now using below command. If not, check your PATH environment variable.

    `docker-compose -v`

## Create docker-compose.yml

`docker-compose.yml` is the file, which can be used to build multiple containers and start them in one go.

For docker-compose documentation, click [here](https://docs.docker.com/compose/)

An example repo is present [here](https://github.com/kathuriaas/docker-compose-examples) for sample docker-compose files for different type of services.
