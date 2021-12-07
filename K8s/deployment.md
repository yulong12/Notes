docker tag sys-z-test-docker-local.artifactory.swg-devops.com/demo-serving:x86 localhost:5000/sys-z-test-docker-local.artifactory.swg-devops.com/demo-serving:x86

docker push localhost:5000/sys-z-test-docker-local.artifactory.swg-devops.com/demo-serving:x86



docker pull registry



docker run --detach --publish 5000:5000 --name registry-container --hostname registry registry
```
[root@Master Mul_cloud]# docker run --detach --publish 5000:5000 --name registry-container --hostname registry registry
```

查看当前registry镜像仓库
```
curl -X GET http://9.30.215.42:5000/v2/_catalog
```

```
# cat /etc/docker/daemon.json
{
  "registry-mirror": [
    "https://registry.docker-cn.com"
  ],
  "insecure-registries": [
    "9.30.215.42:5000:5000"
  ]
}
```

```
# systemctl stop docker
# systemctl start docker
```
sudo systemctl start docker.socket