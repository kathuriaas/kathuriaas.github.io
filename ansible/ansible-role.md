---
layout: default
parent: ANSIBLE
---
# Ansible Role

Ansible role is used to organise `ansible-playbook` code in a well defined directory structure.

A very simple directory structure can be like this as defined [here](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html#directory-layout).

```shell
roles/
  role_name/
    tasks/
      main.yml
    files/
      script.sh
    vars/
      main.yml
```

There can be other directories as needed. Also, we can remove directories, which are not needed.

We can move all tasks from playbook to `roles/role_name/tasks/main.yml`. This will keep playbook clean. Any scripts needed for play, can be stored under `roles/role_name/files` directory.
