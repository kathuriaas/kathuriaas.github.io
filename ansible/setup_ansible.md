---
layout: default
parent: ANSIBLE
nav_order: 1
---
# Setup Ansible

Ansible can be installed locally. However, quickest method is to use docker image. So, we will follow this approach.

***Pre-requisites:-***

To install a docker image, docker must be installed. Follow [Install docker](../docker/install_docker) link for this.

For docker-compose documentation, click [here](https://docs.docker.com/compose/)

## Step 1 : Create docker-compose file with name `docker-compose.yml`

There is no image on docker hub with ansible installed. So, we will install ansible on python image

```yml
version: '3'
services:
    ansible-service:
        image: ansible_image
        container_name: ansible_container
        build:
            context: .
        networks:
            - ansible_network
        tty: true
networks:
    ansible_network:
```

## Step 2 : Create dockerfile with name `dockerfile`

```dockerfile
FROM python:latest

RUN apt -y update && \
    pip install ansible --upgrade

CMD ["/bin/bash"]
```

## Step 3 : Build ansible image and start container

Keep both docker-compose.yml and dockerfile in same directory. Now run following commands from same directory (via shell):-

```shell
docker-compose build
```

```shell
docker-compose up -d
```

## Step 4 : Connect ansible container and verify ansible

```shell
docker exec -it ansible_container bash
```

Now, you are in a container. Verify ansible installation:

```shell
ansible --version
```
