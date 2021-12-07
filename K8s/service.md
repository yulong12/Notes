- Kubernetes 中 Pod 是随时可以消亡的（节点故障、容器内应用程序错误等原因）。如果使用 Deployment 运行应用程序，Deployment 将会在 Pod 消亡后再创建一个新的 Pod 以维持所需要的副本数。每一个 Pod 有自己的 IP 地址，因此pod的IP地址往往动态变化
- 解决方法：通过Service可以获得稳定的IP地址，且在Service的生命周期有效，与Pod的IP地址变化与否无关。  
例如一个无状态图像处理的后端部署了三个副本。这三个副本是相互可以替换的，前端并不关心他们使用的是哪个后端。虽然组成后端集的实际pod可能会发生变化，但前端客户端不需要知道这一点，也不需要跟踪后端集
----------------
## 定义service
在kubernetes中一个service是一个REST对象。像所有的REST对象一样，可以通过向APIserver post一个service定义去定义一个实例。
### 例子：
假设这里有一个Pods集合，监听TCP端口9376并且包含一个标签app=MyApp，则service可以这样定义：
```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
```
- 以上定义创建了一个名字为：my-service的service对象，它为目标TCP端口是9376和标签是app=MyApp的pod提供服务。
- 服务可以将任何传入端口映射到targetPort。默认情况下，为了方便起见，targetPort被设置为与port字段相同的值。
### 多端口的service
注意：必须设置ports的名称
```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 9376
    - name: https
      protocol: TCP
      port: 443
      targetPort: 9377

```
- 与Kubernetes名称一般一样，端口名称只能包含小写字母，数字和-。端口名还必须以字母数字开头和结尾。
- 例如，名称123-abc和web有效，但123_abc和-web无效。
--------
## Kube-proxy
Kube-proxy 是 kubernetes 工作节点上的一个网络代理组件，运行在每个节点上。  
Kube-proxy维护节点上的网络规则，实现了Kubernetes Service 概念的一部分 。它的作用是使发往 Service 的流量（通过ClusterIP和端口）负载均衡到正确的后端Pod。  
## kube-proxy的启动有三种模式
- User space（k8s v1.2后就已经被淘汰）
- ptables
- IPVS
## User space 代理模式

---
## 发布services
 - 对于应用程序的某些部分(例如前端)，您可能希望将服务公开到集群之外的外部IP地址。
 - Kubernetes ```ServiceTypes```允许您指定您想要的服务类型。默认为ClusterIP  
## type类型
- ClusterIP:暴露集群内部IP上的服务。选择此值将使服务只能从集群内部访问。这是默认的ServiceType。
- NodePort:以静态端口(NodePort)暴露每个节点的IP上的服务。自动创建一个ClusterIP服务，NodePort服务路由到该服务。
    - 在集群内部通过 $(ClusterIP): $(Port) 访问
    - 在集群外部通过 $(NodeIP): $(NodePort) 访问
-  LoadBalancer:使用云提供商的负载均衡器向外部公开服务。外部负载均衡器路由会自动创建到其中的NodePort和ClusterIP服务
    - 在集群内部通过 $(ClusterIP): $(Port) 访问
    - 在集群外部通过 $(NodeIP): $(NodePort) 访问
    - 在集群外部通过 $(LoadBalancerIP): $(Port) 访问
- ExternalName:通过返回带有其值的CNAME记录，将服务映射到ExternalName字段的内容(例如foo.bar.example.com)。没有建立任何形式的代理。

另外还可以使用ingress暴露服务端口。ingress不是一个服务类型但是是一个集群的入口。
## NodePort
```
apiVersion: v1
kind: Service
metadata:
  name: service-web
spec:
  ports:
  - port: 3000
    protocol: TCP
    targetPort: 443
    nodePort: 30080
  selector:
    run: pod-web
  type: NodePort
```
此时我们可以通过nodeip:30080 对pod-web访问。该端口有一定的范围（默认值：30000-32767）
## LoadBalancer
在支持外部负载均衡器的云环境中（例如 GCE、AWS、Azure 等），将 .spec.type 字段设置为 LoadBalancer，Kubernetes 将为该Service 自动创建一个负载均衡器。负载均衡器的创建操作异步完成，您可能要稍等片刻才能真正完成创建，负载均衡器的信息将被回写到 Service 的 .status.loadBalancer 字段。如下所示：
```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
  clusterIP: 10.0.171.239
  loadBalancerIP: 78.11.24.19
  type: LoadBalancer
status:
  loadBalancer:
    ingress:
      - ip: 146.148.47.155
```
发送到外部负载均衡器的网络请求就像被转发到 Kubernetes 中的后端 Pod 上。负载均衡的实现细节由各云服务上确定。

## ExternalName
ExternalName 类型的 Service 映射到一个外部的 DNS name，而不是一个 pod label selector。可通过 spec.externalName 字段指定外部 DNS name。
下面的例子中，名称空间 prod 中的 Service my-service 将映射到 my.database.example.com：
```
apiVersion: v1
kind: Service
metadata:
  name: my-service
  namespace: prod
spec:
  type: ExternalName
  externalName: my.database.example.com
```
执行 nslo.okup my-service.prod.svc.cluster.local 指令时，集群的 DNS 服务将返回一个 CNAME 记录，其对应的值为 my.database.example.com。访问 my-service 与访问其他类型的 Service 相比，网络请求的转发发生在 DNS level，而不是使用 proxy