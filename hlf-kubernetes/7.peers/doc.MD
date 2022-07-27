
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