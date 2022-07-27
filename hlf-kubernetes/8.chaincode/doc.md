

peer节点启动成功之后，创建通道，并且使peer节点加入通道：  
1，创建channel，cli-peer0-org1执行  
```
sh scripts/createAppChannel.sh
```

2，其余三个peer节点分别加入channel：   
```
peer channel join -b ./channel-artifacts/mychannel.block 
```
3，更新   
```
sh scripts/updateAnchorPeer.sh Org1MSP
```
```
sh scripts/updateAnchorPeer.sh Org2MSP
```
```
sh scripts/updateAnchorPeer.sh Org3MSP
```



在package目录下面执行命令：
```
tar cfz code.tar.gz connection.json
tar cfz basic-org1.tgz code.tar.gz metadata.json
tar cfz basic-org2.tgz code.tar.gz metadata.json
tar cfz basic-org3.tgz code.tar.gz metadata.json
chmod 777 -R ./*
```
1，build chaincode,并且修改tag，push到ocp平台
在目录chaincode/basic下面编写Dockerfile，运行下面命令，创建chaincode镜像
```
docker build -t default-route-openshift-image-registry.apps.bj-prod-14.luban.cdl.ibm.com/demo/tcmpcc:v1.0 .

```
```
docker login -u $(oc whoami) -p $(oc whoami -t) default-route-openshift-image-registry.apps.bj-prod-14.luban.cdl.ibm.com
```
```
docker push default-route-openshift-image-registry.apps.bj-prod-14.luban.cdl.ibm.com/fabric/tcmpcc:v1.0
```

2,安装chaincode
```
cd /opt/gopath/src/github.com/chaincode/basic/packaging
ls 
peer lifecycle chaincode install basic-org1.tgz
```


```
peer0org1
basic:7df26f74ecb2f1e62c44c8358add49f982fa974fd0499358f278a0da853a2381
 peeroOrg2:
basic:82699333db3ddf87d38d46bc0f7543ac6e93aad055c298ab36a7823d94c60460
peer0Org3
basic:862d00d141cdbfff4573cef92f6c107d08c2577939f52b3d136133f5dab62db1
```

3,approve chaincode peer0-org1
```
peer lifecycle chaincode approveformyorg --channelID mychannel --name basic --version 1.0 --init-required --package-id basic:7df26f74ecb2f1e62c44c8358add49f982fa974fd0499358f278a0da853a2381 --sequence 1 -o orderer:7050 --tls --cafile $ORDERER_CA 

```
approve chaincode peer0-org2
```
peer lifecycle chaincode approveformyorg --channelID mychannel --name basic --version 1.0 --init-required --package-id basic:82699333db3ddf87d38d46bc0f7543ac6e93aad055c298ab36a7823d94c60460 --sequence 1 -o orderer:7050 --tls --cafile $ORDERER_CA 
```

approve chaincode peer0-org3
```
peer lifecycle chaincode approveformyorg --channelID mychannel --name basic --version 1.0 --init-required --package-id basic:862d00d141cdbfff4573cef92f6c107d08c2577939f52b3d136133f5dab62db1 --sequence 1 -o orderer:7050 --tls --cafile $ORDERER_CA 
```


checkcommitreadiness
```
peer lifecycle chaincode checkcommitreadiness --channelID mychannel --name basic --version 1.0 --init-required --sequence 1 -o -orderer:7050 --tls --cafile $ORDERER_CA
```

commit chaincode
```
peer lifecycle chaincode commit -o orderer:7050 --channelID mychannel --name basic --version 1.0 --sequence 1 --init-required --tls true --cafile $ORDERER_CA --peerAddresses peer0-org1:7051 --tlsRootCertFiles /organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses peer0-org2:7051 --tlsRootCertFiles /organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt --peerAddresses peer0-org3:7051 --tlsRootCertFiles /organizations/peerOrganizations/org3.example.com/peers/peer0.org3.example.com/tls/ca.crt

```

 InitLedger command
 ```
peer chaincode invoke -o orderer:7050 --isInit --tls true --cafile $ORDERER_CA -C mychannel -n basic --peerAddresses peer0-org1:7051 --tlsRootCertFiles /organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses peer0-org2:7051 --tlsRootCertFiles /organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt --peerAddresses peer0-org3:7051 --tlsRootCertFiles /organizations/peerOrganizations/org3.example.com/peers/peer0.org3.example.com/tls/ca.crt -c '{"Args":["InitLedger"]}' --waitForEvent

```

invoke command
```
peer chaincode invoke -o orderer:7050 --tls true --cafile $ORDERER_CA -C mychannel -n basic --peerAddresses peer0-org1:7051 --tlsRootCertFiles /organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses peer0-org2:7051 --tlsRootCertFiles /organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt --peerAddresses peer0-org3:7051 --tlsRootCertFiles /organizations/peerOrganizations/org3.example.com/peers/peer0.org3.example.com/tls/ca.crt -c '{"Args":["CreateAsset","demo4","blue","5","Tomoko","300","123","2022-3-25","2022-3-25","yulong","abe"]}' --waitForEvent

```







query command
```
peer chaincode query -C mychannel -n basic -c '{"Args":["GetAllAssets"]}'
```
```
peer chaincode query -C mychannel -n basic -c '{"Args":["ReadAsset","demo4"]}'
```
```
peer chaincode query -C mychannel -n basic -c '{"function":"ReadAsset","Args":["demo1"]}'
```

Accessing CouchDB
```
kubectl port-forward services/peer0-org1 5984:5984
```