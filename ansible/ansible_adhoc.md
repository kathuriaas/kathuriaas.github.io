---
layout: default
parent: ANSIBLE
---
# Ansible Ad-hoc

Ansible adhoc uses `ansible` command to perform simple tasks on multiple nodes:-

```shell
ansible [pattern] -m [module] -a [module_options] -i <inventory_file/server_list> -u <user for ssh proxy>
```

Full list of ansible modules is available [here.](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)

## Example 1:-

```shell
# example of ping module:-
ansible all -m ping -i ssh_server, -u ssh_user
```

- Note a `comma` after server name list. When passing server list with `-i` option (not in a file), a comma is needed at the end of the list.
- `all` means, all servers listed as part of inventory.

## Example 2:-

```shell
# example of shell module:-
ansible all -m shell -i ssh_server, -u ssh_user -a 'date'
```

## Example 3:-

```shell
# example of script module:-
ansible all -m script -i ssh_server, -u ssh_user -a '/tmp/script1.ksh'
```

## Example 4:-

```shell
# example of find module:-
ansible all -m find -i ssh_server, -u ssh_user -a 'paths=~'
```
