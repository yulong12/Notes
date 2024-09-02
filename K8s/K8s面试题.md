
## 1. 什么k8s，谈谈你的理解   
   K8s是kubernetes的简称，其本质是一个开源的容器编排系统，主要用于管理容器化的应用，
其目标是让部署容器化的应用简单并且高效（powerful）,Kubernetes提供了应用部署，规划，更新，维护的一种机制。   
说简单点：k8s就是一个编排容器的系统，一个可以管理容器应用全生命周期的工具，从创建应用，应用的部署，应用提供服务，扩容缩容应用，应用更新，都非常的方便，而且还可以做到故障自愈，
所以，k8s是一个非常强大的容器编排系统。

##  2. k8s的组件有哪些，作用分别是什么？   
- k8s主要由master节点和node节点构成。
- master节点负责管理集群，node节点是容器应用真正运行的地方。
- master节点包含的组件有：kube-api-server、kube-controller-manager、kube-scheduler、etcd。
- node节点包含的组件有：kubelet、kube-proxy、container-runtime。

#### kube-api-server：   
- api-server是k8s最重要的核心组件之一，它是k8s集群管理的统一访问入口，提供了RESTful API接口, 实现了认证、授权和准入控制等安全功能；
- api-server还是其他组件之间的数据交互和通信的枢纽，其他组件彼此之间并不会直接通信，其他组件对资源对象的增、删、改、查和监听操作都是交由api-server处理后，api-server再提交给etcd数据库做持久化存储，只有api-server才能直接操作etcd数据库，其他组件都不能直接操作etcd数据库，其他组件都是通过api-server间接的读取，写入数据到etcd。

#### kube-controller-manager：
- controller-manager是k8s中各种控制器的的管理者，是k8s集群内部的管理控制中心，也是k8s自动化功能的核心；
- controller-manager内部包含replication controller、node controller、deployment controller、endpoint controller等各种资源对象的控制器，每种控制器都负责一种特定资源的控制流程，而controller-manager正是这些controller的核心管理者。

#### kube-scheduler：

- scheduler负责集群资源调度，其作用是将待调度的pod通过一系列复杂的调度算法计算出最合适的node节点，然后将pod绑定到目标节点上。
- shceduler会根据pod的信息，全部节点信息列表，过滤掉不符合要求的节点，过滤出一批候选节点，然后给候选节点打分，选分最高的就是最佳节点，scheduler就会把目标pod安置到该节点。

#### Etcd：

- etcd是一个分布式的键值对存储数据库，主要是用于保存k8s集群状态数据，比如，pod，service等资源对象的信息；
- etcd可以是单个也可以有多个，多个就是etcd数据库集群，
- etcd通常部署奇数个实例，在大规模集群中，etcd有5个或7个节点就足够了；
- 另外说明一点，etcd本质上可以不与master节点部署在一起，只要master节点能通过网络连接etcd数据库即可。

#### kubelet：

- 每个node节点上都有一个kubelet服务进程，kubelet作为连接master和各node之间的桥梁，负责维护pod和容器的生命周期，当监听到master下发到本节点的任务时，比如创建、更新、终止pod等任务，kubelet 即通过控制docker来创建、更新、销毁容器；
- 每个kubelet进程都会在api-server上注册本节点自身的信息，用于定期向master汇报本节点资源的使用情况。

#### kube-proxy：

- kube-proxy运行在node节点上，在Node节点上实现Pod网络代理，维护网络规则和四层负载均衡工作，
- kube-proxy会监听api-server中从而获取service和endpoint的变化情况，创建并维护路由规则以提供服务IP和负载均衡功能。
- 简单理解此进程是Service的透明代理兼负载均衡器，其核心功能是将到某个Service的访问请求转发到后端的多个Pod实例上。

#### container-runtime
容器运行时环境，即运行容器所需要的一系列程序，目前k8s支持的容器运行时有很多，如docker、rkt或其他，比较受欢迎的是docker，但是新版的k8s已经宣布弃用docker。

## 3.简述k8s的相关概念
#### master:
k8s集群的管理节点，负责管理集群，提供集群的资源数据访问入口。拥有Etcd存储服务（可选），运行Api Server进程，Controller Manager服务进程及Scheduler服务进程；
#### node
Node（worker）是Kubernetes集群架构中运行Pod的服务节点，是Kubernetes集群操作的单元，用来承载被分配Pod的运行，是Pod运行的宿主机。运行docker eninge服务，守护进程kunelet及负载均衡器kube-proxy；

#### pod
运行于Node节点上，若干相关容器的组合。Pod内包含的容器运行在同一宿主机上，使用相同的网络命名空间、IP地址和端口，能够通过localhost进行通信。Pod是Kurbernetes进行创建、调度和管理的最小单位，它提供了比容器更高层次的抽象，使得部署和管理更加灵活。一个Pod可以包含一个容器或者多个相关容器；

#### label：
Kubernetes中的Label实质是一系列的Key/Value键值对，其中key与value可自定义。Label可以附加到各种资源对象上，如Node、Pod、Service、RC等。一个资源对象可以定义任意数量的Label，同一个Label也可以被添加到任意数量的资源对象上去。Kubernetes通过Label Selector（标签选择器）查询和筛选资源对象；

#### Replication Controller：

- Replication Controller用来管理Pod的副本，保证集群中存在指定数量的Pod副本。
- 集群中副本的数量大于指定数量，则会停止指定数量之外的多余容器数量。反之，则会启动少于指定数量个数的容器，保证数量不变。
- Replication Controller是实现弹性伸缩、动态扩容和滚动升级的核心；

#### Deployment：

Deployment在内部使用了RS来实现目的，Deployment相当于RC的一次升级，其最大的特色为可以随时获知当前Pod的部署进度；

#### HPA（Horizontal Pod Autoscaler）：

Pod的横向自动扩容，也是Kubernetes的一种资源，通过追踪分析RC控制的所有Pod目标的负载变化情况，来确定是否需要针对性的调整Pod副本数量；

#### Service：

- Service定义了Pod的逻辑集合和访问该集合的策略，是真实服务的抽象。

- Service提供了一个统一的服务访问入口以及服务代理和发现机制，关联多个相同Label的Pod，用户不需要了解后台Pod是如何运行；

#### Volume：

Volume是Pod中能够被多个容器访问的共享目录，Kubernetes中的Volume是定义在Pod上，可以被一个或多个Pod中的容器挂载到某个目录下；

#### Namespace：

Namespace用于实现多租户的资源隔离，可将集群内部的资源对象分配到不同的Namespace中，形成逻辑上的不同项目、小组或用户组，便于不同的Namespace在共享使用整个集群的资源的同时还能被分别管理；

## 4.简述Kubernetes和Docker的关系?
Docker开源的容器引擎，一种更加轻量级的虚拟化技术；
K8s，容器管理工具，用来管理容器pod的集合，它可以实现容器集群的自动化部署、自动扩缩容、维护等功能；

## 5.简述Kubernetes如何实现集群管理?
- 在集群管理方面，Kubernetes将集群中的机器划分为一个Master节点和一群工作节点Node。
- 其中，在Master节点运行着集群管理相关的一组进程kube-apiserver、kube-controller-manager和kube-scheduler，这些进程实现了整个集群的资源管理、Pod调度、弹性伸缩、安全控制、系统监控和纠错等管理能力，并且都是全自动完成的；

## 6.简述Kubernetes的优势、适应场景及其特点?

- 优势：容器编排、轻量级、开源、弹性伸缩、负载均衡；

- 场景：快速部署应用、快速扩展应用、无缝对接新的应用功能、节省资源，优化硬件资源的使用；
- 特点：

    - 可移植: 支持公有云、私有云、混合云、多重云（multi-cloud）、

    - 可扩展: 模块化,、插件化、可挂载、可组合、

    - 自动化: 自动部署、自动重启、自动复制、自动伸缩/扩展；

## 7.简述Kubernetes的缺点或当前的不足之处?
- 安装过程和配置相对困难复杂、
- 管理服务相对繁琐、
- 运行和编译需要很多时间、
- 它比其他替代品更昂贵、
- 对于简单的应用程序来说，可能不需要涉及Kubernetes即可满足；

## 8.简述Kubernetes中什么是Minikube、Kubectl、Kubelet?
- Minikube 是一种可以在本地轻松运行一个单节点 Kubernetes 群集的工具；
- Kubectl 是一个命令行工具，可以使用该工具控制Kubernetes集群管理器，如检查群集资源，创建、删除和更新组件，查看应用程序；
- Kubelet 是一个代理服务，它在每个节点上运行，并使从服务器与主服务器通信；

## 9.kubelet的功能、作用是什么？（重点，经常会问）
kubelet部署在每个node节点上的，它主要有4个功能：

- 1、节点管理。   
kubelet启动时会向api-server进行注册，然后会定时的向api-server汇报本节点信息状态，资源使用状态等，这样master就能够知道node节点的资源剩余，节点是否失联等等相关的信息了。master知道了整个集群所有节点的资源情况，这对于 pod 的调度和正常运行至关重要。

- 2、pod管理。   
kubelet负责维护node节点上pod的生命周期，当kubelet监听到master的下发到自己节点的任务时，比如要创建、更新、删除一个pod，kubelet 就会通过CRI（容器运行时接口）插件来调用不同的容器运行时来创建、更新、删除容器；常见的容器运行时有docker、containerd、rkt等等这些容器运行时，我们最熟悉的就是docker了，但在新版本的k8s已经弃用docker了，k8s1.24版本中已经使用containerd作为容器运行时了。

- 3、容器健康检查。   
pod中可以定义启动探针、存活探针、就绪探针等3种，我们最常用的就是存活探针、就绪探针，kubelet 会定期调用容器中的探针来检测容器是否存活，是否就绪，如果是存活探针，则会根据探测结果对检查失败的容器进行相应的重启策略；

- 4、Metrics Server资源监控。   
在node节点上部署Metrics Server用于监控node节点、pod的CPU、内存、文件系统、网络使用等资源使用情况，而kubelet则通过Metrics Server获取所在节点及容器的上的数据。

## 10.kube-api-server的端口是多少？各个pod是如何访问kube-api-server的？
kube-api-server的端口是8080和6443，前者是http的端口，后者是https的端口，以我本机使用kubeadm安装的k8s为例：

在命名空间的kube-system命名空间里，有一个名称为kube-api-master的pod，

这个pod就是运行着kube-api-server进程，它绑定了master主机的ip地址和6443端口，但是在default命名空间下，存在一个叫kubernetes的服务，该服务对外暴露端口为443，目标端口6443，

这个服务的ip地址是clusterip地址池里面的第一个地址，同时这个服务的yaml定义里面并没有指定标签选择器，

也就是说这个kubernetes服务所对应的endpoint是手动创建的，该endpoint也是名称叫做kubernetes，该endpoint的yaml定义里面代理到master节点的6443端口，也就是kube-api-server的IP和端口。

这样一来，其他pod访问kube-api-server的整个流程就是：pod创建后嵌入了环境变量，pod获取到了kubernetes这个服务的ip和443端口，请求到kubernetes这个服务其实就是转发到了master节点上的6443端口的kube-api-server这个pod里面。

## 11.kubernetes的namespace的作用是什么？
- namespace是kubernetes系统中的一种非常重要的资源，namespace的主要作用是用来实现多套环境的资源隔离，或者说是多租户的资源隔离。

- k8s通过将集群内部的资源分配到不同的namespace中，可以形成逻辑上的隔离，以方便不同的资源进行隔离使用和管理。

- 不同的命名空间可以存在同名的资源，命名空间为资源提供了一个作用域。

- 可以通过k8s的授权机制，将不同的namespace交给不同的租户进行管理，这样就实现了多租户的资源隔离，还可以结合k8s的资源配额机制，限定不同的租户能占用的资源，例如CPU使用量、内存使用量等等来实现租户可用资源的管理。

## 12.k8s提供了大量的REST接口，其中有一个是Kubernetes Proxy API接口，简述一下这个Proxy接口的作用，以及怎么使用。
- kubernetes proxy api接口，从名称中可以得知，proxy是代理的意思，其作用就是代理rest请求；
- Kubernets API server 将接收到的rest请求转发到某个node上的kubelet守护进程的rest接口，由该kubelet进程负责响应。
- 我们可以使用这种Proxy接口来直接访问某个pod，这对于逐一排查pod异常问题很有帮助。

## 13 pod是什么？
在kubernetes的世界中，k8s并不直接处理容器，而是使用多个容器共存的理念，这组容器就叫做pod。

pod是k8s中可以创建和管理的最小单元，是资源对象模型中由用户创建或部署的最小资源对象模型，其他的资源对象都是用来支撑pod对象功能的，比如，pod控制器就是用来管理pod对象的，service或者ingress资源对象是用来暴露pod引用对象的，persistent volume资源是用来为pod提供存储等等，

简而言之，k8s不会直接处理容器，而是pod，pod才是k8s中可以创建和管理的最小单元，也是基本单元。

## 14. pod原理是什么？
在微服务的概念里，一般的，一个容器会被设计为运行一个进程，除非进程本身产生子进程，
这样，由于不能将多个进程聚集在同一个单独的容器中，所以需要一种更高级的结构将容器绑定在一起，并将它们作为一个单元进行管理，这就是k8s中pod的背后原理。

## 15。 pod有什么特点？
- 1、每个pod就像一个独立的逻辑机器，k8s会为每个pod分配一个集群内部唯一的IP地址，所以每个pod都拥有自己的IP地址、主机名、进程等；
- 2、一个pod可以包含1个或多个容器，1个容器一般被设计成只运行1个进程，1个pod只可能运行在单个节点上，即不可能1个pod跨节点运行，pod的生命周期是短暂，也就是说pod可能随时被消亡（如节点异常，pod异常等情况）；
- 3、每一个pod都有一个特殊的被称为"根容器"的pause容器，也称info容器，pause容器对应的镜像属于k8s平台的一部分，除了pause容器，每个pod还包含一个或多个跑业务相关组件的应用容器；
- 4、一个pod中的容器共享network命名空间；
- 5、一个pod里的多个容器共享pod IP，这就意味着1个pod里面的多个容器的进程所占用的端口不能相同，否则在这个pod里面就会产生端口冲突；既然每个pod都有自己的IP和端口空间，那么对不同的两个pod来说就不可能存在端口冲突；
- 6、应该将应用程序组织到多个pod中，而每个pod只包含紧密相关的组件或进程；
- 7、pod是k8s中扩容、缩容的基本单位，也就是说k8s中扩容缩容是针对pod而言而非容器。

## 16. pod的重启策略有哪些
pod重启容器策略是指针对pod内所有容器的重启策略，不是重启pod，其可以通过restartPolicy字段配置pod重启容器的策略，如下：   
- Always: 当容器终止退出后，总是重启容器，默认策略就是Always。
- OnFailure: 当容器异常退出，退出状态码非0时，才重启容器。
- Never: 当容器终止退出，不管退出状态码是什么，从不重启容器。

## 17. pod的镜像拉取策略有哪几种？
pod镜像拉取策略可以通过imagePullPolicy字段配置镜像拉取策略，   

主要有3中镜像拉取策略，如下：   
- IfNotPresent: 默认值，镜像在node节点宿主机上不存在时才拉取。
- Always: 总是重新拉取，即每次创建pod都会重新从镜像仓库拉取一次镜像。
- Never: 永远不会主动拉取镜像，仅使用本地镜像，需要你手动拉取镜像到node节点，如果node节点不存在镜像则pod启动失败。

## 18. kubenetes针对pod资源对象的健康监测机制?（必须记住3重探测方式，重点，经常问）
提供了三类probe（探针）来执行对pod的健康监测：   

- livenessProbe探针 （存活探针）:

    -  目的：
        - 检查容器是否还活着，即是否处于正常运行状态。
        - 如果容器被认为是不健康的，Kubernetes 会杀死这个容器，并根据容器的重启策略（如 Always 或 OnFailure）来决定是否重启它。
    - 触发时机：
        - 在容器运行期间定期执行。

- ReadinessProbe探针（就绪探针）:
    - 目的：
        - 检查容器是否已经准备好接收流量。
        - 只有当容器通过就绪探针检查时，Kubernetes 才会将其加入到 Service 的后端列表中。
    - 触发时机：
        - 在容器运行期间定期执行。
- startupProbe探针 （启动探针）:
    - 目的：
        - 检查容器是否成功启动并进入就绪状态。
        - 这种探针主要用于那些启动时间较长的应用程序，以避免在容器启动完成之前就执行 livenessProbe 或 readinessProbe。
    - 触发时机：
        - 在容器启动后立即执行，并在容器被认为已准备好之前一直执行。

- 探针配置参数
    - httpGet：  
        - 通过 HTTP GET 请求来检查容器状态。
        - 需要指定路径和端口。
    - tcpSocket：
        - 检查容器内的 TCP 端口是否打开。
        - 需要指定端口号。
    - exec：
        - 在容器内执行命令。
        - 需要指定要执行的命令。
    - initialDelaySeconds：
        - 探针开始执行前等待的秒数。
    - periodSeconds：
        - 探针执行间隔的秒数。
    - timeoutSeconds：
        - 探针执行的最大等待时间。
    - successThreshold：
        - 探针连续成功执行的次数。
    - failureThreshold：
        - 探针连续失败执行的次数，超过此次数后将采取行动。

## 19. 就绪探针（ReadinessProbe探针）与存活探针（livenessProbe探针）区别是什么？
两者作用不一样，   

- 存活探针是将检查失败的容器杀死，创建新的启动容器来保持pod正常工作；

- 就绪探针是，当就绪探针检查失败，并不重启容器，而是将pod移出endpoint，就绪探针确保了service中的pod都是可用的，确保客户端只与正常的pod交互并且客户端永远不会知道系统存在问题。


## 20 三种探针执行顺序
- 在容器启动时，Kubernetes会按照以下顺序进行探针检查：

    - StartupProbe：如果定义了StartupProbe，它会首先被执行。StartupProbe用于判断容器是否已经启动并准备接受请求。如果StartupProbe检查失败，Kubernetes会认为容器启动失败，并且不会执行LivenessProbe和ReadinessProbe。
    - ReadinessProbe：当StartupProbe成功或者未定义时，ReadinessProbe将开始执行。ReadinessProbe用于检查容器是否已经准备好接收外部流量。如果ReadinessProbe检查失败，Kubernetes会将Pod从服务中移除，不会再将新的流量发送到该Pod。
    - LivenessProbe：最后执行的是LivenessProbe。LivenessProbe用于检查容器是否还在运行。如果LivenessProbe检查失败，Kubernetes会杀死容器并尝试重启它。

## 21. k8s 创建一个pod的详细流程，涉及的组件怎么通信的？

- 1）客户端提交创建请求，可以通过 api-server 提供的 restful 接口，或者是通过 kubectl 命令行工具，支持的数据类型包括 JSON 和 YAML；

- 2）api-server 处理用户请求，将 pod 信息存储至 etcd 中；

- 3）kube-scheduler 通过 api-server 提供的接口监控到未绑定的 pod，尝试为 pod 分配 node 节点，主要分为两个阶段，预选阶段和优选阶段，其中预选阶段是遍历所有的 node 节点，根据策略筛选出候选节点，而优选阶段是在第一步的基础上，为每一个候选节点进行打分，分数最高者胜出；

- 4）选择分数最高的节点，进行 pod binding 操作，并将结果存储至 etcd 中；

- 5）随后目标节点的 kubelet 进程通过 api-server 提供的接口监测到 kube-scheduler 产生的 pod 绑定事件，然后从 etcd 获取 pod 清单，下载镜像并启动容器；

## 21. 简单描述一下pod的终止过程
- 1、用户向apiserver发送删除pod对象的命令；
- 2、apiserver中的pod对象信息会随着时间的推移而更新，在宽限期内（默认30s），pod被视为dead；
- 3、将pod标记为terminating状态；
- 4、kubectl在监控到pod对象为terminating状态了就会启动pod关闭过程；
- 5、endpoint控制器监控到pod对象的关闭行为时将其从所有匹配到此endpoint的server资源endpoint列表中删除；
- 6、如果当前pod对象定义了preStop钩子处理器，则在其被标记为terminating后会意同步的方式启动执行；
- 7、pod对象中的容器进程收到停止信息；
- 8、宽限期结束后，若pod中还存在运行的进程，那么pod对象会收到立即终止的信息；
- 9、kubelet请求apiserver将此pod资源的宽限期设置为0从而完成删除操作，此时pod对用户已不可见。

## 22. pod的生命周期有哪几种？
pod生命周期有的5种状态（也称5种相位），如下：  

    - Pending（挂起）：Kubernetes 已经开始创建 Pod，但由于 Pod 中的容器还未创建成功，所以 Pod 还处于挂起的状态。这时 Pod 可能在等待被调度，或者在等待下载镜像。

    - Running（运行中）：Pod 已经被调度到某个节点上了，Pod 中的所有容器都已被成功创建，并且至少有一个容器正处于 启动、重启、运行 这 3 个状态中的 1 个。

    - Succeed（成功）：Pod内所有容器均已退出，且不会再重启；

    - Failed（失败）：Pod内所有容器均已退出，且至少有一个容器为退出失败状态

    -  Unknown（未知）：某于某种原因apiserver无法获取该pod的状态，可能由于网络通行问题导致；

## 23. pod一直处于pending状态一般有哪些情况，怎么排查？（重点，持续更新）
（这个问题被问到的概率非常大）
- 一个pod一开始创建的时候，它本身就是会处于pending状态，这时可能是正在拉取镜像，正在创建容器的过程。

- 如果等了一会发现pod一直处于pending状态，那么我们可以使用`kubectl describe`命令查看一下pod的Events详细信息。一般可能会有这么几种情况导致pod一直处于pending状态：
    - 1、调度器调度失败。   
    Scheduer调度器无法为pod分配一个合适的node节点。而这又会有很多种情况，比如，
        - node节点处在cpu、内存压力，导致无节点可调度；
        - pod定义了资源请求，没有node节点满足资源请求；
        - node节点上有污点而pod没有定义容忍；
        - pod中定义了亲和性或反亲和性而没有节点满足这些亲和性或反亲和性；
    以上是调度器调度失败的几种情况。
    - 2、pvc、pv无法动态创建。
        - 如果因为pvc或pv无法动态创建，那么pod也会一直处于pending状态，比如要使用StatefulSet 创建redis集群，因为粗心大意，定义的storageClassName名称写错了，那么会造成无法创建pvc，这种情况pod也会一直处于pending状态，或者，即使pvc是正常创建了，但是由于某些异常原因导致动态供应存储无法正常创建pv，那么这种情况pod也会一直处于pending状态。
## 24. DaemonSet类型的资源特性有哪些
在Kubernetes（K8S）中，DaemonSet是一种控制器资源对象，它具有一系列独特的资源特性，这些特性使得DaemonSet特别适用于在集群的每个节点上运行守护进程或服务。以下是DaemonSet类型资源特性的详细阐述：
- 1. 确保每个节点上运行Pod副本
        - 节点级部署：DaemonSet确保集群中的每个节点（或满足特定条件的节点）上都运行一个Pod副本。这意味着无论何时创建或加入新的节点到集群中，DaemonSet都会自动为新节点调度和管理一个Pod。
        - 自动扩展：当节点加入或离开集群时，DaemonSet会自动添加或删除相应的Pod。如果一个节点被删除或者由于某种原因变得不可用，那么该节点上的DaemonSet Pod也会被清理；反之，如果有新节点加入，DaemonSet将确保在新节点上启动一个Pod实例。
- 2. 精确控制Pod部署位置
        - 节点选择器：通过使用NodeSelector、NodeAffinity或其他节点标签，可以精确地控制DaemonSet中的Pod部署在哪些节点上。例如，可以选择仅在具有特定硬件或功能的节点上运行DaemonSet。
        - 避免冲突：默认情况下，DaemonSet保证在每个节点上只运行一个Pod实例。这可以通过PodDisruptionBudget等机制来进一步强化，并且可以通过PodAntiAffinity规则来避免同一个节点上运行多个相同的DaemonSet Pod。   
- 3. 支持版本升级和回滚
        - 更新策略：DaemonSet支持多种更新策略，包括滚动更新、按需更新等，以确保在维护或升级守护进程时能够平滑过渡。这些更新策略类似于Deployment的滚动更新策略，但更侧重于节点级别的更新而不是基于副本数量。
        - 版本控制：DaemonSet能够管理其Pod的生命周期，包括初始化容器、健康检查以及重启策略等，从而支持版本升级和回滚操作。
- 4. 适用于集群级别的基础服务
        - 基础服务部署：DaemonSet通常用于部署那些提供集群层面功能的服务，如日志收集代理（如Fluentd或Filebeat）、监控代理（如Prometheus Node Exporter或cAdvisor）、网络插件以及其他需要在每个工作节点上都有一个实例运行的基础服务。
        - 系统守护进程：DaemonSet的主要作用是确保集群中的所有（或符合条件的部分）节点上都能按需运行指定的系统守护进程或其他基础组件，以提供集群范围内的基础设施支持。
- 5. 与其他资源对象的区别
        - 与Deployment的区别：DaemonSet与Deployment的主要区别在于，DaemonSet确保每个节点上运行一个Pod，而Deployment则确保集群中运行指定数量的Pod副本，这些Pod副本可以分布在不同的节点上。因此，DaemonSet的yaml文件中不支持定义replicas。
综上所述，DaemonSet在Kubernetes中扮演着确保集群每个节点上运行必要守护进程或服务的重要角色，其特性使得它成为部署和管理集群级别基础服务的理想选择。

## 25. pod的共享资源
    1）PID 命名空间：Pod 中的不同应用程序可以看到其他应用程序的进程 ID；

    2）网络命名空间：Pod 中的多个容器能够访问同一个IP和端口范围；

    3）IPC 命名空间：Pod 中的多个容器能够使用 SystemV IPC 或 POSIX 消息队列进行通信；

    4）UTS 命名空间：Pod 中的多个容器共享一个主机名；

    5）Volumes（共享存储卷）：Pod 中的各个容器可以访问在 Pod 级别定义的 Volumes

## 26. pause容器作用是什么
- 每个pod里运行着一个特殊的被称之为pause的容器，也称根容器，而其他容器则称为业务容器；
- 创建pause容器主要是为了为业务容器提供 Linux命名空间，共享基础：包括 pid、icp、net 等，以及启动 init 进程，并收割僵尸进程；
- 这些业务容器共享pause容器的网络命名空间和volume挂载卷，
- 当pod被创建时，pod首先会创建pause容器，从而把其他业务容器加入pause容器，从而让所有业务容器都在同一个命名空间中，这样可以就可以实现网络共享。
- pod还可以共享存储，在pod级别引入数据卷volume，业务容器都可以挂载这个数据卷从而实现持久化存储。

## 27. 标签和标签选择器是什么，如何使用
- 标签是键值对类型，标签可以附加到任何资源对象上，主要用于管理对象，查询和筛选。

- 标签常被用于标签选择器的匹配度检查，从而完成资源筛选；一个资源可以定义一个或多个标签在其上面。

- 标签选择器，标签要与标签选择器结合在一起，标签选择器允许我们选择标记有特定标签的资源对象子集，如pod，并对这些特定标签的pod进行查询，删除等操作。

- 标签和标签选择器最重要的使用之一在于，在deployment中，在pod模板中定义pod的标签，然后在deployment定义标签选择器，这样就通过标签选择器来选择哪些pod是受其控制的，service也是通过标签选择器来关联哪些pod是服务后端pod

## 28. service是如何与pod关联的？
答案是通过标签选择器，每一个由deployment创建的pod都带有标签，这样，service就可以定义标签选择器来关联哪些pod是作为其后端了，就是这样，service就与pod管联在一起了。

## 29. service的域名解析格式、pod的域名解析格式
- service的DNS域名表示格式为`<servicename>.<namespace>.svc.<clusterdomain>`   
    - servicename是service的名称   
    - namespace是service所处的命名空间   
    - clusterdomain是k8s集群设置的域名后缀，一般默认为 cluster.local   

- pod的DNS域名格式为：`<pod-ip>.<namespace>.pod.<clusterdomain> `，
    - pod-ip需要使用-将ip直接的点替换掉
    - namespace为pod所在的命名空间
    - clusterdomain是k8s集群设置的域名后缀，一般默认为 cluster.local

## 30. service的类型有哪几种
service的类型一般有4中，分别是：

- ClusterIP：表示service仅供集群内部使用，默认值就是ClusterIP类型

- NodePort：表示service可以对外访问应用，会在每个节点上暴露一个端口，这样外部浏览器访问地址为：任意节点的IP：NodePort就能连上service了

- LoadBalancer：表示service对外访问应用，这种类型的service是公有云环境下的service，此模式需要外部云厂商的支持，需要有一个公网IP地址

- ExternalName：这种类型的service会把集群外部的服务引入集群内部，这样集群内直接访问service就可以间接的使用集群外部服务了

一般情况下，service都是ClusterIP类型的，通过ingress接入的外部流量。
## 31. 如何创建一个service代理外部的服务，或者换句话来说，在k8s集群内的应用如何访问外部的服务，如数据库服务，缓存服务等?

答：可以通过创建一个没有标签选择器的service来代理集群外部的服务。

- 1、创建service时不指定selector标签选择器，但需要指定service的port端口、端口的name、端口协议等，这样创建出来的service因为没有指定标签选择器就不会自动创建endpoint；

- 2、手动创建一个与service同名的endpoint，endpoint中定义外部服务的IP和端口，endpoint的名称一定要与service的名称一样，端口协议也要一样，端口的name也要与service的端口的name一样，不然endpoint不能与service进行关联。
完成以上两步，k8s会自动将service和同名的endpoint进行关联，
这样，k8s集群内的应用服务直接访问这个service就可以相当于访问外部的服务了。

## 32. service、endpoint、kube-proxys三种的关系是什么？
- service：

    - 在kubernetes中，service是一种为一组功能相同的pod提供单一不变的接入点的资源。
    - 当service被建立时，service的IP和端口不会改变，这样外部的客户端（也可以是集群内部的客户端）通过service的IP和端口来建立链接，这些链接会被路由到提供该服务的任意一个pod上。
    - 通过这样的方式，客户端不需要知道每个单独提供服务的pod地址，这样pod就可以在集群中随时被创建或销毁。
- endpoint：

    - service维护一个叫endpoint的资源列表，endpoint资源对象保存着service关联的pod的ip和端口。
    - 从表面上看，当pod消失，service会在endpoint列表中剔除pod，当有新的pod加入，service就会将pod ip加入endpoint列表；
    - 但是底层的逻辑是，endpoint的这种自动剔除、添加、更新pod的地址其实底层是由endpoint controller控制的，endpoint controller负责监听service和对应的pod副本的变化，如果监听到service被删除，则删除和该service同名的endpoint对象，如果监听到新的service被创建或者修改，则根据该service信息获取得相关pod列表，然后创建或更新service对应的endpoint对象，如果监听到pod事件，则更新它所对应的service的endpoint对象。
- kube-proxy：

    - kube-proxy运行在node节点上，在Node节点上实现Pod网络代理，维护网络规则和四层负载均衡工作，

    - kube-proxy会监听api-server中从而获取service和endpoint的变化情况，创建并维护路由规则以提供服务IP和负载均衡功能。

## 33. deployment怎么实现扩容和缩容
答：直接修改pod副本数即可，可以通过下面的方式来修改pod副本数：

- 1、直接修改yaml文件的replicas字段数值，然后kubectl apply -f xxx.yaml来实现更新；

- 2、使用kubectl edit deployment xxx 修改replicas来实现在线更新；

- 3、使用kubectl scale --replicas=5 deployment/deployment-nginx命令来扩容缩容。

## 34. deployment的更新升级策略有哪些？
答：deployment的升级策略主要有两种。
- 1、Recreate 重建更新：这种更新策略会杀掉所有正在运行的pod，然后再重新创建的pod；
- 2、rollingUpdate 滚动更新：这种更新策略，deployment会以滚动更新的方式来逐个更新pod，同时通过设置滚动更新的两个参数maxUnavailable、maxSurge来控制更新的过程。

## 35. deployment的滚动更新策略有两个特别主要的参数，解释一下它们是什么意思？
答：deployment的滚动更新策略，rollingUpdate 策略，主要有两个参数，maxUnavailable、maxSurge。

- maxUnavailable：最大不可用数，maxUnavailable用于指定deployment在更新的过程中不可用状态的pod的最大数量，maxUnavailable的值可以是一个整数值，也可以是pod期望副本的百分比，如25%，计算时向下取整。

- maxSurge：最大激增数，maxSurge指定deployment在更新的过程中pod的总数量最大能超过pod副本数多少个，maxSurge的值可以是一个整数值，也可以是pod期望副本的百分比，如25%，计算时向上取整。

## 36. deployment更新的命令有哪些？
答：可以通过三种方式来实现更新deployment。

- 1、直接修改yaml文件的镜像版本，然后`kubectl apply -f xxx.yaml`来实现更新；

- 2、使用`kubectl edit deployment xxx `实现在线更新；

- 3、使用`kubectl set image deployment/nginx busybox=busybox nginx=nginx:1.9.1 `命令来更新。

## 37. 简述一下deployment的更新过程?
deployment是通过控制replicaset来实现，由replicaset真正创建pod副本，每更新一次deployment，都会创建新的replicaset，下面来举例deployment的更新过程：

假设要升级一个nginx-deployment的版本镜像为nginx:1.9，deployment的定义滚动更新参数如下:
```
replicas: 3
deployment.spec.strategy.type: RollingUpdate
maxUnavailable：25%
maxSurge：25%

```
通过计算我们得出，3*25%=0.75，maxUnavailable是向下取整，则maxUnavailable=0，maxSurge是向上取整，则maxSurge=1，所以我们得出在整个deployment升级镜像过程中，不管旧的pod和新的pod是如何创建消亡的，pod总数最大不能超过3+maxSurge=4个，最大pod不可用数3-maxUnavailable=3个。   

现在具体讲一下deployment的更新升级过程：

使用`kubectl set image deployment/nginx nginx=nginx:1.9 --record `命令来更新；

- 1、deployment创建一个新的replaceset，先新增1个新版本pod，此时pod总数为4个，不能再新增了，再新增就超过pod总数4个了；旧=3，新=1，总=4；

- 2、减少一个旧版本的pod，此时pod总数为3个，这时不能再减少了，再减少就不满足最大pod不可用数3个了；旧=2，新=1，总=3；

- 3、再新增一个新版本的pod，此时pod总数为4个，不能再新增了；旧=2，新=2，总=4；

- 4、减少一个旧版本的pod，此时pod总数为3个，这时不能再减少了；旧=1，新=2，总=3；

- 5、再新增一个新版本的pod，此时pod总数为4个，不能再新增了；旧=1，新=3，总=4；

- 6、减少一个旧版本的pod，此时pod总数为3个，更新完成，pod都是新版本了；旧=0，新=3，总=3；

## 38. deployment的回滚使用什么命令
- 在升级deployment时`kubectl set image` 命令加上` --record `参数可以记录具体的升级历史信息，

- 使用`kubectl rollout history deployment/deployment-nginx `命令来查看指定的deployment升级历史记录，

- 如果需要回滚到某个指定的版本，可以使用`kubectl rollout undo deployment/deployment-nginx --to-revision=2`命令来实现。
## 39. pv的访问模式有哪几种
pv的访问模式有3种，如下：

- ReadWriteOnce，简写：RWO 表示，只仅允许单个节点以读写方式挂载；
- ReadWriteMany，简写：RWX 表示，可以被多个节点以读写方式挂载；
- ReadOnlyMany，简写：ROX 表示，可以被许多节点以只读方式挂载；

## 40. 在pv的生命周期中，一般有几种状态
pv一共有4中状态，分别是：
创建pv后，pv的状态有以下4种：
- Available（可用）:表示pv已经创建正常，处于可用状态；
- Bound（已绑定）:表示pv已经被某个pvc绑定，一个pv一旦被某个pvc绑定，那么该pvc就独占该pv，其他pvc不能再与该pv绑定；
- Released（已释放）:表示pvc被删除了，pv状态就会变成已释放；
- Failed（失败）:表示pv的自动回收失败；


## 41. pv存储空间不足怎么扩容?
一般的，我们会使用动态分配存储资源，

在创建`storageclass`时指定参数 `allowVolumeExpansion：true`，表示允许用户通过修改pvc申请的存储空间自动完成pv的扩容，

当增大pvc的存储空间时，不会重新创建一个pv，而是扩容其绑定后的pv。

这样就能完成扩容了。但是`allowVolumeExpansion`这个特性只支持扩容空间不支持减少空间。

## 42. 存储类的资源回收策略:
主要有2中回收策略，delete 删除，默认就是delete策略、retain 保留。
- Retain：保留，该策略允许手动回收资源，当删除PVC时，PV仍然存在，PV被视为已释放，管理员可以手动回收卷。
- Delete：删除，如果Volume插件支持，删除PVC时会同时删除PV，动态卷默认为Delete，目前支持Delete的存储后端包括AWS EBS，GCE PD，Azure Disk，OpenStack Cinder等。

### 注意：使用存储类动态创建的pv默认继承存储类的回收策略，当然当pv创建后你也可以手动修改pv的回收策略。
## 43. 怎么使一个node脱离集群调度，比如要停机维护但是又不能影响业务应用
使用`kubectl drain`命令

## 44. etcd集群节点之间是怎么同步数据的？
通过Raft协议进行节点之间数据同步， 保证节点之间的数据一致性

## 45. k8s集群外流量怎么访问Pod？
可以通过Service的NodePort方式访问，会在所有节点监听同一个端口，比如：30000，访问节点的流量会被重定向到对应的Service上面；

## 46. K8S 资源限制 QoS
答：Quality of Service（Qos）

主要有三种类别：

- 1）BestEffort：什么都不设置（CPU or Memory），佛系申请资源；

- 2）Burstable：Pod 中的容器至少一个设置了CPU 或者 Memory 的请求；

- 3）Guaranteed：Pod 中的所有容器必须设置 CPU 和 Memory，并且 request 和 limit 值相等；

## 47. k8s数据持久化的方式有哪些？

- 1)EmptyDir（空目录）：没有指定要挂载宿主机上的某个目录，直接由Pod内保部映射到宿主机上。类似于docker中的manager volume；
    - 场景有：
        - a.只需要临时将数据保存在磁盘上，比如在合并/排序算法中；
        - b.作为两个容器的共享存储，使得第一个内容管理的容器可以将生成的数据存入其中，同时由同一个webserver容器对外提供这些页面;    
    - emptyDir的特性：同个pod里面的不同容器，共享同一个持久化目录，当pod节点删除时，volume的数据也会被删除。如果仅仅是容器被销毁，pod还在，则不会影响volume中的数据。
    - 总结来说：emptyDir的数据持久化的生命周期和使用的pod一致。一般是作为临时存储使用。

- 2）Hostpath：将宿主机上已存在的目录或文件挂载到容器内部。类似于docker中的bind mount挂载方式；

- 3）PersistentVolume（简称PV）：基于NFS服务的PV，也可以基于GFS的PV。
    - 它的作用是统一数据持久化目录，方便管理，PVC是向PV申请应用所需的容量大小，K8s集群中可能会有多个PV，PVC和PV若要关联，其定义的访问模式必须一致。定义的storageClassName也必须一致，若群集中存在相同的（名字、访问模式都一致）两个PV，那么PVC会选择向它所需容量接近的PV去申请，或者随机申请；

## 48. kubelet 监控 Node 节点资源使用是通过什么组件来实现的？

答：用Metrics Server提供核心指标，包括Node、Pod的CPU和内存的使用。而Metrics Server需要采集node上的cAdvisor提供的数据资源，

当 kubelet 服务启动时，它会自动启动 cAdvisor 服务，然后 cAdvisor 会实时采集所在节点的性能指标及在节点上运行的容器的性能指标。

kubelet 的启动参数 --cadvisor-port 可自定义 cAdvisor 对外提供服务的端口号，默认是 4194

## 49. rc/rs实现原理？
- Replication Controller 可以保证Pod始终处于规定的副本数，

- 而当前推荐的做法是使用Deployment+ReplicaSet，

- ReplicaSet 号称下一代的 Replication Controller，当前唯一区别是RS支持set-based selector，

RC是通过ReplicationManager监控RC和RC内Pod的状态，从而增删Pod，以实现维持特定副本数的功能，RS也是大致相同；

## 50. 简述Kubernetes自动扩容机制?
- Kubernetes使用Horizontal Pod Autoscaler（HPA）的控制器实现基于CPU使用率进行自动Pod扩缩容的功能。
- HPA控制器周期性地监测目标Pod的资源性能指标，并与HPA资源对象中的扩缩容条件进行对比，在满足条件时对Pod副本数量进行调整；

## 51. 简述Kubernetes Service分发后端的策略?
- 1）`RoundRobin`：默认为轮询模式，即轮询将请求转发到后端的各个Pod上；
- 2）`SessionAffinity`：基于客户端IP地址进行会话保持的模式，即第1次将某个客户端发起的请求转发到后端的某个Pod上，之后从相同的客户端发起的请求都将被转发到后端相同的Pod上；

## 52. 简述Kubernetes Headless Service?
在某些应用场景中，若需要人为指定负载均衡器，不使用Service提供的默认负载均衡的功能，或者应用程序希望知道属于同组服务的其他实例。
Kubernetes提供了`Headless Service`来实现这种功能，即不为Service设置ClusterIP（入口IP地址），仅通过Label Selector将后端的Pod列表返回给调用的客户端；

## 53. 简述Kubernetes外部如何访问集群内的服务?
- 映射Pod到物理机：将Pod端口号映射到宿主机，即在Pod中采用hostPort方式，以使客户端应用能够通过物理机访问容器应用；
- 映射Service到物理机：将Service端口号映射到宿主机，即在Service中采用nodePort方式，以使客户端应用能够通过物理机访问容器应用；
- 映射Service到LoadBalancer：通过设置LoadBalancer映射到云服务商提供的LoadBalancer地址。这种用法仅用于在公有云服务提供商的云平台上设置Service的场景；

## 54. 简述Kubernetes ingress?
- K8s的Ingress资源对象，用于将不同URL的访问请求转发到后端不同的Service，以实现HTTP层的业务路由机制。

- K8s使用了Ingress策略和Ingress Controller，两者结合并实现了一个完整的Ingress负载均衡器。

- 使用Ingress进行负载分发时，Ingress Controller基于Ingress规则将客户端请求直接转发到Service对应的后端Endpoint（Pod）上，从而跳过kube-proxy的转发功能，kube-proxy不再起作用，

全过程为：ingress controller + ingress 规则 ----> services；

## 55. 简述Kubernetes各模块如何与API Server通信?
K8s API Server作为集群的核心，负责集群各功能模块之间的通信。

集群内的各个功能模块通过API Server将信息存入etcd，当需要获取和操作这些数据时，则通过API Server提供的REST接口（用GET、LIST或WATCH方法）来实现，从而实现各模块之间的信息交互。

- 1）kubelet进程与API Server的交互：每个Node上的kubelet每隔一个时间周期，就会调用一次API Server的REST接口报告自身状态，API Server在接收到这些信息后，会将节点状态信息更新到etcd中；

- 2）kube-controller-manager进程与API Server的交互：kube-controller-manager中的Node Controller模块通过API Server提供的Watch接口实时监控Node的信息，并做相应处理

- 3）kube-scheduler进程与API Server的交互：Scheduler通过API Server的Watch接口监听到新建Pod副本的信息后，会检索所有符合该Pod要求的Node列表，开始执行Pod调度逻辑，在调度成功后将Pod绑定到目标节点上；