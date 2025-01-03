 1  ls
    2  vi /etc/sysconfig/network-scripts/ifcfg-ens160
    3  hostnamectl set-hostname worker01
    4  vi /etc/hosts
    5  reboot
    6  systemctl stop firewalld
    7  systemctl disable firewalld
    8  nc 127.0.0.1 6443 -v
    9  vim /etc/fstab
   10  swapoff -a
   11  mkdir software
   12  cd software/
   13  ls
   14  wget https://github.com/containerd/containerd/releases/download/v1.7.24/containerd-1.7.24-linux-arm64.tar.gz
   15  tar Cxzvf /usr/local containerd-1.7.24-linux-arm64.tar.gz
   16  vi /usr/local/lib/systemd/system/containerd.service
   17  touch /usr/local/lib/systemd/system/containerd.service
   18  mkdir -p /usr/local/lib/systemd/system/
   19  touch /usr/local/lib/systemd/system/containerd.service
   20  vi /usr/local/lib/systemd/system/containerd.service
   21  cat /usr/local/lib/systemd/system/containerd.service
   22  systemctl daemon-reload
   23  systemctl enable --now containerd
   24  systemctl status containerd.service
   25  wget https://github.com/opencontainers/runc/releases/download/v1.2.3/runc.arm64
   26  install -m 755 runc.arm64 /usr/local/sbin/runc
   27  wget https://github.com/containernetworking/plugins/releases/download/v1.6.1/cni-plugins-linux-arm64-v1.6.1.tgz
   28  mkdir -p /opt/cni/bin
   29  tar Cxzvf /opt/cni/bin cni-plugins-linux-arm64-v1.6.1.tgz
   30  containerd config default > /etc/containers/config.toml
   31  vi /etc/containers/config.toml
   32  cat /etc/containers/config.toml
   33  systemctl restart containerd
   34  systemctl status containerd.service
   35  yum erase podman buildah
   36  sudo systemctl restart containerd
   37  sudo systemctl status containerd
   38  sudo setenforce 0
   39  sudo sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
   40  cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.32/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.32/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
EOF

   41  sudo sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
   42  sudo sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
   43  vim /etc/sysctl.d/k8s.conf
   44  yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
   45  systemctl enable --now kubelet
   46  systemctl status kubelet
   47  kubeadm join 192.168.212.140:6443 --token abcdef.0123456789abcdef --discovery-token-ca-cert-hash sha256:c499ba880944154ba7bf65f3524b92b24ebec6cb2d5a4524aebe1cd484f99cc0 --ignore-preflight-errors=SystemVerification
   48  vim /etc/sysctl.d/k8s.conf
   49  sysctl -p /etc/sysctl.d/k8s.conf
   50  modprobe br_netfilter
   51  sysctl -p /etc/sysctl.d/k8s.conf
   52  kubeadm join 192.168.212.140:6443 --token abcdef.0123456789abcdef --discovery-token-ca-cert-hash sha256:c499ba880944154ba7bf65f3524b92b24ebec6cb2d5a4524aebe1cd484f99cc0 --ignore-preflight-errors=SystemVerification
   53  kubelet get nodes
   54  clear
   55  ls
   56  history