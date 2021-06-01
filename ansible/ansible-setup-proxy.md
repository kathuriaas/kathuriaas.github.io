---
layout: default
parent: ANSIBLE
---
# Update proxy keys

Ansible can update ssh proxy keys on existing target servers. Follow below steps on control node:-

It is assumed that proxy keys are already working and need to be updated.

```shell
mkdir $HOME/.ssh

chmod go-w $HOME $HOME/.ssh

cd $HOME/.ssh

ssh-keygen -t rsa -b 1024 -f key_file_name.rsa.openssh
```
