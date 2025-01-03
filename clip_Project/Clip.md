# clip在Ray环境上搭建

1,创建clip环境
```
conda create --name clip_ray python=3.10
```
```
conda remove -n your_env_name(虚拟环境名称) --all
```
# 将ray的dashboard的port转发到本地
先查看对应service的名字  
```
kubectl get service
```
转发接口
```
kubectl port-forward service/raycluster-sample-head-svc 8265:8265
```

```
serve run serve_quickstart:clip_app
```