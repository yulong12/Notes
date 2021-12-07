
```
docker pull tensorflow/tensorflow:2.3.3
```

```
docker run -it -v /root/tensor_mnt:/tmp --name tensorflowboard -p 8080:6006 tensorflow/tensorflow:2.3.3
```

```
pip3 install sklearn
pip3 install -U tensorboard-plugin-profile
```
```
tensorboard --logdir=/tmp/dumps_logs_new --load_fast=false --port 6006 --bind_all
```
/Users/yulong/Documents/yyds/dataCollect-and-train/saved_model/dumpsModel

http://9.30.215.42:8080


tensorboard --logdir=/Users/yulong/Documents/yyds/dataCollect-and-train/dumps_logs_new --load_fast=false --port 6006 --bind_all


tensorboard --inspect --logdir /Users/yulong/Documents/yyds/dataCollect-and-train/saved_model/dumpsModel

```
 docker build -f dockerFile.yaml -t tensorboard:x86 .
 ```