---
layout: default
parent: NodeJS
---
# Install nodejs

***To install and use multiple versions of nodejs on same machine, click [here](./install_nvm.md)***

## Windows

1. Go to link <https://nodejs.org/en/download>
2. Page will display options to download LTS version (this is the latest stable version of nodejs).
3. Look for appropriate version as per your OS (32/64 bit).
4. Choose .msi OR .zip file and click to download.
5. Once downloaded, unzip the zip file (for installation using .msi skip this step).
6. zip file will extract all files and can be used directly without any installtion. Update your PATH environment variable to add the location, where you keep all unzipped files.
7. If you downloaded .msi, click on the file to install and follow simple installation steps.
8. This will install node and npm on the machine. npm is node package manager, used for download and install any module.
9. Check the version of node and npm using below commands:-  

```js
node -v
npm -v
```

## Ubuntu

### Add specific version (e.g. 12.x here) in repository and install using apt-get

```shell
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### If we do not have root access, we can download and untar nodejs tar file and use it

```shell
curl -o node-v12.18.0-linux-x64.tar.xz "https://nodejs.org/dist/v12.18.0/node-v12.18.0-linux-x64.tar.xz"

tar -xvf node-v12.18.0-linux-x64.tar.xz
```

Now add the path of above untar file (with ./bin path) to PATH environment variable.

## Linux

### If we do not have root access, we can download and untar nodejs tar file to use it

```shell
curl -o node-v12.18.0-linux-x64.tar.xz "https://nodejs.org/dist/v12.18.0/node-v12.18.0-linux-x64.tar.xz"

tar -xvf node-v12.18.0-linux-x64.tar.xz
```

Now add the path of above untar file (with ./bin path) to PATH environment variable.
