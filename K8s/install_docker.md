## 一、 安装docker
# 环境：  Centos8.4

### 1，卸载旧版本
```
 sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
```
### 2,设置repository
```
 sudo yum install -y yum-utils

 sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
``` 
### 3,安装Docker Engine
```
sudo yum install docker-ce docker-ce-cli containerd.io
```
如果安装时遇到下面这个问题：
```
[root@Master ~]# sudo yum install docker-ce docker-ce-cli containerd.io
Docker CE Stable - x86_64                                                                                      11 kB/s | 3.5 kB     00:00
Docker CE Test - x86_64                                                                                        34 kB/s |  18 kB     00:00
Error:
 Problem 1: problem with installed package podman-3.0.1-7.module_el8.4.0+830+8027e1c4.x86_64
 ......
```
则说明Docker出现和Podman冲突
运行以下命令并重新安装：
```
yum erase podman buildah
```

### 4,启动docker
```
sudo systemctl start docker
```
### 5,启动docker service
```
systemctl enable docker.service
```

# 环境：s390x 
参考资料：  
https://docs.docker.com/engine/install/rhel/
