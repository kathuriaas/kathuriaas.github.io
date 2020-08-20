---
layout: default
parent: ANSIBLE
---
# Ansible Playbook

Ansible playbooks can be run using `ansible-playbook` command as follows:-

```shell
ansible-playbook -i <inventory_file/server_list> -u <user for ssh proxy> <playbook>
```

More cli options are listed [here.](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html)

## Example 1:-

Create a file `test.yml` with below code for ping module.

```yml
---
    - name: Test Playbook
      hosts: all
      gather_facts: false
      tasks:
        - name: Test task
          ping:
```

Now, run below command to execute the playbook

```shell
ansible-playbook -i ssh_server, -u ssh_user test.yml
```

## Example 2:-

Create a file `test.yml` with below code for `command` module. `ansible-playbook` does not print returned values. So, output is registered to a variable and printed.

```yml
---
    - name: Test Playbook
      hosts: all
      gather_facts: false
      tasks:
        - name: Test task
          command: date
          register: cur_date

        - name: Print Output
          debug:
            var: cur_date.stdout
```

Now, run below command to execute the playbook

```shell
ansible-playbook -i ssh_server, -u ssh_user test.yml
```

You can use `msg` parameter as well in debug module. For `debug` module, see details [here.](https://docs.ansible.com/ansible/latest/modules/debug_module.html)
