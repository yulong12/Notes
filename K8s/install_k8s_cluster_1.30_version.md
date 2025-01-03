# 1 环境
- centos 8 armd64
- k8s 1.30
# 安装docker
为了防止docker版本冲突，需要将以前的版本删除

sudo sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*

sudo sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

sudo yum update -y

sudo dnf remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine

sudo dnf -y install dnf-plugins-core

sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

 sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl enable --now docker
sudo docker run hello-world

kubeadm init --cri-socket unix:///var/run/cri-dockerd.sock
kubeadm reset --cri-socket unix:///var/run/cri-dockerd.sock
kubeadm join 192.168.212.130:6443 --cri-socket unix:///var/run/cri-dockerd.sock --token wnvjr4.yybr6foca5g8ovkd \
	--discovery-token-ca-cert-hash sha256:1bf9c6ac9f257fc67a2e5492e44422f626a6a4877103bc4e3e092c348b7166d3

wget https://github.com/Mirantis/cri-dockerd/releases/download/v0.3.15/cri-dockerd-0.3.15.arm64.tgz
tar -zxvf cri-dockerd-0.3.15.arm64.tgz

cp cri-dockerd /usr/bin/
cri-dockerd --version
cd /usr/lib/systemd/system
参考https://github.com/Mirantis/cri-dockerd/tree/master/packaging/systemd
创建文件
cri-docker.service
cri-docker.socket

设置开机启动
systemctl daemon-reload
systemctl enable cri-dockerd.service
systemctl restart cri-dockerd.service


sudo setenforce 0
sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config

cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.30/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.30/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
EOF

sudo yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes


cat >> /etc/sysctl.d/k8s.conf << EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF

modprobe br_netfilter
modprobe overlay
sysctl -p /etc/sysctl.d/k8s.conf



# 创建containerd目录
mkdir /etc/containerd
​
# 恢复默认配置文件
containerd config default > /etc/containerd/config.toml
​
# 切换为国内源
sed -i 's/registry.k8s.io/registry.aliyuncs.com\/google_containers/' /etc/containerd/config.toml
​
# 重启服务
systemctl daemon-reload
systemctl restart containerd

find / -name "containerd.sock"
find / -name "cri-dockerd.sock"


ctr images ls
ctr c ls


3:20.10.0-3.el8

安装指定版本的docker
https://blog.csdn.net/skh2015java/article/details/127700161
