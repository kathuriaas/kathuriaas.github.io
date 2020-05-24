# Install nodejs

## Windows Installation

1. Go to link [https://nodejs.org/en/download](https://nodejs.org/en/download)
2. Page will display options to download LTS version (this is the latest stable version of nodejs).
3. Look for appropriate version as per your OS (32/64 bit).
4. Choose .msi OR .zip file and click to download.
5. Once downloaded, unzip the zip file (for installation using .msi skip this step).
6. zip file will extract all files and can be used directly without any installtion. Update your PATH environment variable to add the location, where you keep all unzipped files.
7. If you downloaded .msi, click on the file to install and follow simple installation steps.

## Ubuntu Installation

### Add specific version (e.g. 12.x here) in repository and install using apt-get

    curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
    sudo apt-get install -y nodejs

## Linux Installation
