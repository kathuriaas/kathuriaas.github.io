---
layout: default
parent: DOCKER
nav_order: 1
---
# Docker Installation

## Ubuntu

### Using apt-get

*This approach will also install docker-compose.*

Remove old installations

```shell
sudo apt-get remove docker docker-engine docker.io containerd runc
```

Setup repo

```shell
sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

Install docker engine

```shell
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io
```

Verify Docker install

```shell
sudo docker run hello-world
```

Run docker as non-root

```shell
sudo groupadd docker

sudo usermod -aG docker $USER
```

Now logout and login again to use docker.

Configure docker to run on system startup:-

```shell
sudo systemctl enable docker
```

### Using snap package (snap should be pre-installed). This will install docker and start daemon

```shell
sudo snap install docker
```

Verify docker process

```shell
# Verify docker process
ps -ef|grep docker

# Check docker version
docker --version
```

We need to install docker-compose separately here. Please follow this [link](./docker-compose) for docker-compose.
