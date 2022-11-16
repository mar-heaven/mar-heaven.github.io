---
title: Fabric实践
date: 2022-11-15 10:44:48
tags:
    - Hyperledger
    - Fabric
categories: 区块链
author: Ginta
---

## 安装
参考[Install Fabric and Fabric Samples](https://hyperledger-fabric.readthedocs.io/en/latest/install.html)

### Fabric Samples 
第一步快速起一个Fabric测试网络，官方给了一个非常方便的项目用来学习 

```
# clone fabric-samples
git clone git@github.com:hyperledger/fabric-samples.git 

# 初始化数据仓库（用来放后续的peer、ca等数据）
mkdir ~/data/fabric-data
cd ~/data/fabric-data

# 脚本
要启动一个fabric测试网络需要下载相关镜像，还有一些工具放到了
[fabric-samples](https://github.com/hyperledger/fabric-samples) 这个仓库，官方给了一个一键执行的脚本
curl -sSLO https://raw.githubusercontent.com/hyperledger/fabric/main/scripts/install-fabric.sh && chmod +x install-fabric.sh
./install-fabric.sh -h 可以看一下有什么操作

# clone fabric-samples仓库，下载相关镜像
./install-fabric.sh docker samples

## 下载Fabric二进制执行文件
./install-fabric.sh --fabric-version 2.2.1 binary
```

### 运行网络
```
cd fabric-samples/test-network
# 先干掉之前运行的容器（如果是第一次运行就不用了）
./network.sh down
# 启动网络
./network.sh up

# 创建一个通道，第二个参数是名字，没写的话默认是mychannel
./network.sh createChannel
./network.sh createChannel -c channel1
./network.sh createChannel -c channel2
```

## 链码
### 部署
```
# 把链码安装到peer0.org1.example.com和peer0.org2.example.com两个peer
./network.sh deployCC -ccn basic -ccp ../asset-transfer-basic/chaincode-go -ccl go
```
### 交互
```
# 如果按照上边的步骤走下来会发现fabric-samples目录下有个bin文件夹，我们把它加到环境变量
export PATH=${PWD}/../bin:$PATH

# 设置环境变量FABRIC_CFG_PATH来指定core.yaml
export FABRIC_CFG_PATH=$PWD/../config/

# 现在来设置环境变量方便操作Org1
# Environment variables for Org1

export CORE_PEER_TLS_ENABLED=true
export CORE_PEER_LOCALMSPID="Org1MSP"
export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt
export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp
export CORE_PEER_ADDRESS=localhost:7051

# 初始化账本
peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile "${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem" -C mychannel -n basic --peerAddresses localhost:7051 --tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt" --peerAddresses localhost:9051 --tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt" -c '{"function":"InitLedger","Args":[]}'

# 查询账本资产
peer chaincode query -C mychannel -n basic -c '{"Args":["GetAllAssets"]}'

# 转移资产
peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile "${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem" -C mychannel -n basic --peerAddresses localhost:7051 --tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt" --peerAddresses localhost:9051 --tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt" -c '{"function":"TransferAsset","Args":["asset6","Christopher"]}'

# 同理我们设置Org2的环境变量
# Environment variables for Org2

export CORE_PEER_TLS_ENABLED=true
export CORE_PEER_LOCALMSPID="Org2MSP"
export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt
export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp
export CORE_PEER_ADDRESS=localhost:9051

# 使用Org2 peer来查询（注意上方的环境变量已经用Org2覆盖了之前的Org1的
peer chaincode query -C mychannel -n basic -c '{"Args":["ReadAsset","asset6"]}'
```

### 删除测试数据
```
这条命令会把我们的peer，order节点，volume(持久化文件)，还有CA证书，Org相关文件全部删掉
./network.sh down
```

至此我们已经简单走了一下Fabric的搭建流程！

