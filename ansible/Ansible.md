官方文档
https://docs.ansible.com/ansible/latest/getting_started/index.html

安装ansible
```
$ sudo pip install ansible
```
安装pip
```
https://www.runoob.com/w3cnote/python-pip-install-usage.html
```
编辑(或创建)/etc/ansible/hosts 并在其中加入一个或多个远程系统.你的public SSH key必须在这些系统的``authorized_keys``中:
```
9.30.189.182
9.30.211.96
9.30.216.220
```
ping 你的所有节点:
```
$ ansible all -m ping
```
![avatar](./images/ping.png)  

Ansible会像SSH那样试图用你的当前用户名来连接你的远程机器.要覆写远程用户名,只需使用’-u’参数. 如果你想访问 sudo模式,这里也有标识(flags)来实现:

现在对你的所有节点运行一个命令:
```

$ ansible all -a "/bin/echo hello"

```
![avatar](./images/hello.png)

## Inventories  
Inventories 在为 Ansible 提供系统信息和网络位置的集中文件中组织托管节点,使用inventory文件，Ansible 可以通过单个命令管理大量主机，通过减少需要指定的命令行选项的数量，inventory还可以帮助您更有效地使用 Ansible。  
inventory文件可以是 INI 或 YAML 格式。 出于演示目的，本节仅使用 YAML 格式。
- 1,打开一个终端  
- 2,创建inventory.yaml文件  
- 3,填写host内容  
```
virtualmachines:
  hosts:
    vm01:
      ansible_host: 9.30.189.182
    vm02:
      ansible_host: 9.30.211.96
    vm03:
      ansible_host: 9.30.216.220
```
- 4， 如果您在主目录以外的目录中创建清单，请使用 -i 选项指定完整路径。
```
ansible-inventory -i inventory.yaml --list
```
![avatar](./images/inventoryPing.png)

- 5,ping 清单中的受管节点。 在此示例中，group名称是 virtualmachines  
```
ansible virtualmachines -m ping -i inventory.yaml
```
![avatar](./images/inventoryPingResult.png)
## playbook
Playbook 是 YAML 格式的自动化蓝图，Ansible 使用它来部署和配置托管节点。
例子：
- 1 在控制节点打开一个终端
- 2 创建playbook文件playbook.yaml
- 3 添加以下内容
```
- name: My first play
  hosts: virtualmachines
  tasks:
   - name: Ping my hosts
     ansible.builtin.ping:
   - name: Print message
     ansible.builtin.debug:
       msg: Hello world
```
- 4 运行playbook
```
ansible-playbook -i inventory.yaml playbook.yaml
```
![avatar](./images/runPlaybookResult.png)
注意：
- 起的名字应便于验证和排除故障
- Gather Facts 任务隐式运行。 默认情况下，Ansible 会收集可以在 playbook 中使用的inventory信息。
- 每个任务的状态。 每个任务都有一个 ok 状态，这意味着它运行成功。
- 在这个例子中，有 3 个任务，所以 ok=3 表示每个任务都运行成功。

## 使用metagroups
可以使用metagroups来管理多个群组，语法如下：

```
metagroupname:
  children:
```