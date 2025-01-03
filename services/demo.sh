curl -LO "https://dl.k8s.io/release/v1.32.0/bin/linux/amd64/kubectl"
curl -LO "https://dl.k8s.io/release/v1.32.0/bin/linux/amd64/kube-apiserver"
curl -LO "https://dl.k8s.io/release/v1.32.0/bin/linux/amd64/kube-controller-manager"
curl -LO "https://dl.k8s.io/release/v1.32.0/bin/linux/amd64/kube-scheduler"
curl -LO "https://dl.k8s.io/release/v1.32.0/bin/linux/amd64/kubelet"
curl -LO "https://dl.k8s.io/release/v1.32.0/bin/linux/amd64/kube-proxy"

cfssl gencert -ca=/etc/kubernetes/pki/ca/ca.pem -ca-key=/etc/kubernetes/pki/ca/ca-key.pem -config=/etc/kubernetes/pki/ca/ca-config.json -profile=kubernetes kubelet-csr.json | cfssljson -bare kubelet


sudo kubectl config set-cluster kubernetes \
     --certificate-authority=/etc/kubernetes/pki/ca/ca.pem \
     --embed-certs=true \
     --server=https://192.168.237.130:6443 \
     --kubeconfig=/etc/kubernetes/kubelet.kubeconfig
sudo kubectl config set-credentials system:kubelet \
     --client-certificate=/etc/kubernetes/pki/kubelet/kubelet.pem \
     --client-key=/etc/kubernetes/pki/kubelet/kubelet-key.pem \
     --embed-certs=true \
     --kubeconfig=/etc/kubernetes/kubelet.kubeconfig

sudo kubectl config set-context system:kubelet@kubernetes \
     --cluster=kubernetes \
     --user=system:kubelet \
     --kubeconfig=/etc/kubernetes/kubelet.kubeconfig

sudo kubectl config use-context system:kubelet@kubernetes \
     --kubeconfig=/etc/kubernetes/kubelet.kubeconfig

sudo systemctl daemon-reload
sudo systemctl start kubelet.service
sudo systemctl enable kubelet.service
sudo systemctl status kubelet.service

sudo cfssl gencert \
   -ca=/etc/kubernetes/pki/ca/ca.pem \
   -ca-key=/etc/kubernetes/pki/ca/ca-key.pem \
   -config=/etc/kubernetes/pki/ca/ca-config.json \
   -profile=kubernetes \
   kube-proxy-csr.json | sudo cfssljson -bare kube-proxy

sudo kubectl config set-cluster kubernetes \
  --certificate-authority=/etc/kubernetes/pki/ca/ca.pem \
  --embed-certs=true \
  --server=https://192.168.237.139:6443 \
  --kubeconfig=/etc/kubernetes/kube-proxy.kubeconfig

sudo kubectl config set-credentials kube-proxy \
  --client-certificate=/etc/kubernetes/pki/proxy/kube-proxy.pem \
  --client-key=/etc/kubernetes/pki/proxy/kube-proxy-key.pem \
  --embed-certs=true \
  --kubeconfig=/etc/kubernetes/kube-proxy.kubeconfig

sudo kubectl config set-context kube-proxy@kubernetes \
  --cluster=kubernetes \
  --user=kube-proxy \
  --kubeconfig=/etc/kubernetes/kube-proxy.kubeconfig

sudo kubectl config use-context kube-proxy@kubernetes \
  --kubeconfig=/etc/kubernetes/kube-proxy.kubeconfig

sudo systemctl daemon-reload
sudo systemctl start kube-proxy.service
sudo systemctl enable kube-proxy.service
sudo systemctl status kube-proxy.service

wget https://raw.githubusercontent.com/projectcalico/calico/v3.27.3/manifests/tigera-operator.yaml


kubectl get namespace tigera-operator -o json | tr -d "\n" | sed "s/\"finalizers\": \[[^]]\+\]/\"finalizers\": []/" | kubectl replace --raw /api/v1/namespaces/tigera-operator/finalize -f -

sudo systemctl daemon-reload
sudo systemctl enable kube-apiserver
sudo systemctl restart kube-apiserver
sudo systemctl enable kube-controller-manager
sudo systemctl restart kube-controller-manager
sudo systemctl enable kube-scheduler
sudo systemctl restart kube-scheduler

sudo systemctl status kube-apiserver
sudo systemctl status kube-scheduler
sudo systemctl status kube-controller-manager

sudo systemctl daemon-reload
sudo systemctl enable kubelet
sudo systemctl restart kubelet
sudo systemctl enable kube-proxy
sudo systemctl restart kube-proxy
sudo systemctl status kube-proxy

# 输入命令
kubectl get namespaces tigera-operator -o json | tr -d "\n" | sed "s/\"finalizers\": \[[^]]\+\]/\"finalizers\": []/" | kubectl replace --raw /api/v1/namespaces/tigera-operatorfinalize -f -

sudo apt-get install firewalld firewall-config

sudo firewall-cmd --add-port=40006/tcp --permanent
sudo firewall-cmd --reload
sudo firewall-cmd --list-port