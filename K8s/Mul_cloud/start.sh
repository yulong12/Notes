#!/bin/sh
# docker run -it -v /root/tensor_mnt:/tmp --name tensorflowboard -p 8080:6006 tensorboard:x86

# docker run -it --name tensorflowboard -p 8080:6006 tensorboard:x86
# echo "login:http://9.30.215.42:8080/"
# echo "                                         "
# echo "begin to deploy"

# echo "###########build image : tensorboard:x86###########"
# echo "building......"
# sleep 5
# echo "sucess"

# echo "###########build image : sys-z-test-docker-local.artifactory.swg-devops.com/demo-serving:x86###########"
# echo "building......"
# sleep 5
# echo "sucess"

# echo "###########deployment the inference ###########"
# echo "deploying......"
# sleep 5
# echo "sucess"
# echo "now you can :"
# echo "login http://9.30.215.42:30080/ to see clusters"
# echo "login http://9.30.215.42:8080 to see inference"

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

sleep 5
kubectl get deployments

kubectl get services

kubectl get pods
