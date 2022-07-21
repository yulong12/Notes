1, 关闭防火墙和selinux
```
sed -i  "s/SELINUX=enforcing/SELINUX=permissive/g" /etc/selinux/config
systemctl stop firewalld
systemctl disable firewalld
```
2,安装docker  

3,开始安装openshift

```
./openshift-install --dir /opt/software/openshift/installDir wait-for bootstrap-complete  --log-level=info
 ```
 安装网址：
 https://blog.51cto.com/zhangxueliang/3000227


创建新项目
```
oc new-project my-project
```
创建新应用程序
```
oc new-app https://github.com/sclorg/cakephp-ex
```
查看当前项目的 pod
```
oc get pods -o wide
```
使用oc logs命令查看特定 pod 的日志。
```
oc logs cakephp-ex-1-deploy
```
使用oc project命令查看当前项目
```
oc project
```
使用 oc status 命令查看有关当前项目的信息，如服务、部署和构建配置。
```
oc status
```
使用oc api-resources命令查看服务器上支持的 API 资源列表。
```
oc api-resources
```
注销 OpenShift CLI 以结束当前会话。
```
oc logout
```
