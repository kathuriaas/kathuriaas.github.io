# Setup Chef-Server

Method here used to setup chef-server is by using docker image.

***Pre-requisites:-***

To install a docker image, docker must be installed. Follow [Install docker](https://kathuriaas.github.io/code-examples/docker/install_docker) link for this.

Chef-server docker image is available on Docker Hub [here](https://registry.hub.docker.com/r/base/chef-server/).

## Step 1 : Pull docker image

```shell
# Pull image from Docker Hub
docker pull base/chef-server

# Verify image is available locally
docker images
```

## Step 2 : Start container from image that will start chef-server

We will start a container using image base/chef-server.  
PORT 443 of container will be published to port 443 of host machine (`-p host_port:container_port`). So, chef-server page will be available at `localhost:443`.  

```shell
# Docker Run
docker run --privileged -t --name chef-server -d -p 443:443 base/chef-server
```

## Step 3 : Login to chef manage console

- Open link <https://localhost:443> in your browser.
- Enter username and password, available on the page.
- Login to the portal.
- You are now all set to use Chef-server.
