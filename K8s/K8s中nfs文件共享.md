Kubernetes Volume（数据卷）主要解决了如下两方面问题：

- 数据持久性：通常情况下，容器运行起来之后，写入到其文件系统的文件是暂时性的。当容器崩溃后或者人为杀死后，如果kubelet重启该容器，此时原容器运行时写入的文件将丢失，因为容器将重新从镜像创建。
- 数据共享：同一个 Pod（容器组）中运行的容器之间，经常会存在共享文件/文件夹的需求


nfs 类型的数据卷可以加载 NFS（Network File System）到容器组/容器。容器组被移除时，将仅仅 umount（卸载）NFS 数据卷，NFS 中的数据仍将被保留。  
- 可以在加载 NFS 数据卷前就在其中准备好数据；
- 可以在不同容器组之间共享数据；
- 可以被多个容器组加载并同时读写；

-----------------
- 1.主服务器安装以下工具((主节点作为文件共享服务器)：
```
yum install -y nfs-utils rpcbind
```
- 2.创建存放文件数据的文件夹
```
mkdir -p /root/tensor_mnt
vim /etc/exports
```
将以下信息写入exports中  
```
/root/tensor_mnt *(insecure,rw,sync,no_root_squash)
```
(192.168.0.101为主节点ip，24为子掩码，rw表示可读写,sync表示同步信息)

- 3.启动nfs-utils和rpcbind并设置开机启动
```
systemctl start nfs-server
systemctl start rpcbind
systemctl enable rpcbind
systemctl enable nfs-server
```
- 4 验证是否已经共享了文件

```
[root@Master Mul_cloud]# exportfs
/root/tensor_mnt
		
```
出现上述信息代表已经共享  
如果没有出现以上信息，请检查/etc/exports文件是否书写正确，空格是否正确，逗号是否正确。  
检查完毕之后，执行以下命令让上述代码生效

```
[root@localhost data]# exportfs -r

```
- 5 每个节点需要安装

```
yum install -y nfs-utils
systemctl start nfs-server
systemctl enable nfs-server

```
- 6.从客户端节点查看是否挂载
```
[root@Master Mul_cloud]# showmount -e 9.30.215.42
Export list for 9.30.215.42:
/root/tensor_mnt *
```
表示挂载成功
- 7.从节点挂载主节点文件
```
mount -t nfs 9.30.215.42:/root/tensor_mnt /root/tensor_mnt
```
(9.30.215.42表示主节点IP地址，第一个/root/tensor_mnt表示主节点映射地址，第二个/root/tensor_mnt表示当前主机存放文件位置)

在主节点/root/tensor_mnt写文件如果能在从节点看到当前文件就表示NFS部署成功

- 8.取消的挂在命令
```
umount /root/tensor_mnt
```
/root/tensor_mnt表示当前主机存放文件位置
- 9.修改deployment的yaml文件
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: inference
  labels:
    app: inference
spec:
  replicas: 3
  selector:
    matchLabels:
      app: inference
      run: inference
  template:
    metadata:
      labels:
        app: inference
        run: inference
    spec:
      volumes:
      - name: mlata
        hostPath:
          path: /root/tensor_mnt
      containers:
      - name: demo-serving
        image: sys-z-test-docker-local.artifactory.swg-devops.com/demo-serving:x86
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 6666
      - name: tensorboard
        image: tensorboard:x86
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 6006
        volumeMounts:
        - name: mlata
          mountPath: /tmp
```
- 10 执行命令生效
```
kubectl apply -f deployment.yaml
```