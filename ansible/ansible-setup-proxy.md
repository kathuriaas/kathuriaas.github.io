---
layout: default
parent: ANSIBLE
---
# Ansible Role

Ansible can update ssh proxy keys on existing target servers. Follow below steps on control node:-


```shell
mkdir $HOME/.ssh

chmod go-w $HOME $HOME/.ssh

cd $HOME/.ssh

ssh-keygen -t rsa -b 1024 -f key_file_name.rsa.openssh
```
