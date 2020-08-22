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

## Example 1 (PING module):-

Create a file `test.yml` with below code for `ping` module.

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

## Example 2 (COMMAND module):-

Create a file `test.yml` with below code for `command` and `debug` modules. `ansible-playbook` does not print returned values. So, output is registered to a variable and printed.

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

You can use `msg` parameter as well in debug module as mentioned below. For `debug` module documentation, see details [here.](https://docs.ansible.com/ansible/latest/modules/debug_module.html)

{% raw %}

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
            msg:  "This is {{ cur_date.stdout }}"
```

{% endraw %}

Now, run below command to execute the playbook

```shell
ansible-playbook -i ssh_server, -u ssh_user test.yml
```

## Example 3 (SCRIPT module):-

Create a shell script /tmp/script1.sh on ansible control node with following lines of code.

```shell
date>>/tmp/script1.log
```

Create a file `test.yml` with below code for script module(used torun a local script on remote node).

```yml
---
    - name: Test Playbook
      hosts: all
      gather_facts: false
      tasks:
        - name: Test task
          script: /tmp/script1.sh
```

Now, run below command to execute the playbook

```shell
ansible-playbook -i ssh_server, -u ssh_user test.yml
```

Verify on target node (ssh_server), file /tmp/script1.log has been created with output of date command.

## Example 4 (SHELL module):-

Create a shell script /tmp/script2.sh on target node with following lines of code. Grant execute permission on script.

```shell
date>>/tmp/script2.log
```

Create a file `test.yml` with below code for script module to run a local script on remote node.

```yml
---
    - name: Test Playbook
      hosts: all
      gather_facts: false
      tasks:
        - name: Test task
          shell: /tmp/script2.sh
```

Now, run below command to execute the playbook

```shell
ansible-playbook -i ssh_server, -u ssh_user test.yml
```

Verify on target node (ssh_server), file /tmp/scrip2.log has been created with output of date command.
