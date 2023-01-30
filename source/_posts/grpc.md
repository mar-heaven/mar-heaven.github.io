---
title: grpc
date: 2023-01-26 18:17:48
tags:
    - grpc
    - go
categories: 协议
---

### 引言
随着应用的日益复杂，单一服务已经不能很好地承载日益庞大的用户请求，当唯一一个服务由于各种原因不能正常运行（数据库满载，机房故障）导致系统整体挂掉显然是不能接受的。解决上述问题思路就是风险均摊，比如机房故障我们可以把服务部署在多个地区，然后把服务从大的服务拆分成若干个小的服务，这样当一个服务出现问题的时候也可以保证其他服务正常运行，至少不是所有服务全部炸掉，比如直播的时候弹幕服务不可用，但是用户依然可以正常观看直播，只是不能和主播实时互动而已。
以上粗略描述了微服务的基本思想和要解决的痛点。

### gRPC？
要了解 *grpc* 首先我们要说说 *rpc*，**Remote procedure call**，远程过程调用。
通常我们在本地调用一个方法的时候是用类似这样的方式：
```
func SayHello(name string) {
    return "hello" + name
}

func main() {
    res := SayHello("Ginta")
}
```
那如果我们想调用的函数是远程的一台机器，并且也想使用 *SayHello(argument)* 这种方式直接调用，就需要约定好怎么传参，返回参数是什么，以及怎么去连接。这种约定就是所谓的协议。*rpc* 主要包含通信协议和序列化协议：
通信协议：如http，tcp
序列化协议：如protobuf,json

我们常用的说的 *restful* 就是使用的 *json* 去实现的序列化，这种序列化方式的优势是直观可读，但是压缩率低，传输就会很慢。

protobuf是一款用C++开发的跨语言、跨平台、二进制编码的数据序列化协议，以超高的压缩率著称，极大地提高了传输效率。缺点就是需要专门的库去解析。

gRPC的官网主页只有一句简单的说明：”A high performance, open source universal RPC framework“。一个开源的高性能RPC框架。使用 *HTTP2* 为传输协议，*HTTP1* 中也可以多个请求利用一个连接，但是服务端返回的时候是根据pipeline中发送的顺序返回的，如果有一个阻塞了其他都不能返回，*HTTP2* 很好地解决了这一点。*gRPC* 使用 *protobuf* 来序列化数据。

### protocol buffers

### go的grpc实现
#### proto声明
```
syntax = "proto3";

package grpc;

option go_package = "grpc/pb;proto";


service HelloService {
  rpc SayHello (SayHelloRequest) returns (SayHelloResponse);
}

message SayHelloRequest {
  string Name = 1;
}

message SayHelloResponse {
  string Message = 1;
}
```
#### server
```
package main

import (
	"context"
	"fmt"
	"net"

	"google.golang.org/grpc"
	pb "grpc-study/pb"
)

type Server struct {
	pb.UnimplementedHelloServiceServer
}

func (s *Server) SayHello(ctx context.Context, request *pb.SayHelloRequest) (*pb.SayHelloResponse, error) {
	return &pb.SayHelloResponse{
		Message: fmt.Sprintf("hello %s", request.Name),
	}, nil
}

func main() {
	// open a port
	listen, _ := net.Listen("tcp", ":9090")

	// create a grpc server
	server := grpc.NewServer()

	// register service
	pb.RegisterHelloServiceServer(server, &Server{})

	server.Serve(listen)
}
```
#### client
```
package main

import (
	"context"
	"fmt"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"

	pb "grpc-study/pb"
)

func main() {
	conn, err := grpc.Dial("localhost:9090", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		return
	}
	defer conn.Close()

	// start a client
	client := pb.NewHelloServiceClient(conn)
	response, err := client.SayHello(context.Background(), &pb.SayHelloRequest{Name: "Ginta"})
	if err != nil {
		return
	}
	fmt.Println(response.GetMessage())
}
```

### grpcurl
**grpcurl** 工具可以查询 *grpc* 服务的 *API*, 用来调试 *grpc* 服务很方便
安装：`go install github.com/fullstorydev/grpcurl/cmd/grpcurl@latest`。
要使用 *grpcurl* 我们要在代码里先启动 *reflection* 反射服务
```
package main
import (
	...
	""google.golang.org/grpc/reflection""
)

func main() {
	...
	server := grpc.NewServer()

	// register service
	pb.RegisterHelloServiceServer(server, &Server{})

	// register reflection
	reflection.Register(server)
	....
}
```
然后就可以使用 *grpcurl* 来调试了，先看看服务有哪些接口, `grpcurl  localhost:9000 list`，报了一个异常 **Failed to dial target host "localhost:9000": tls: first record does not look like a TLS handshake**，*grpc* 是用的 *http2* 协议, 虽然不强求但是一般传输也都是要加密的，这里提示我们少了 *TLS* 加密，我们可以先使用明文。`grpcurl -plaintext localhost:9000 list`。
可以看到已经返回了我们服务的列表：
```
grpc.HelloService
grpc.reflection.v1alpha.ServerReflection
```
,第二个是我们开启的反射服务，可以用 *grpcurl -plaintext localhost:9000 list grpc.HelloService* 命令看看 *grpc.HelloService* 服务有哪些方法名，或者用`grpcurl -plaintext localhost:9000 describe grpc.HelloService`会返回更多的信息，包括方法的出入请求。
```
grpc.HelloService is a service:
service HelloService {
  rpc SayHello ( .grpc.SayHelloRequest ) returns ( .grpc.SayHelloResponse );
}
```
我们来请求一下这个 **SayHello** 方法，`grpcurl -plaintext -d '{"Name": "Ginta"}' localhost:9000 grpc.HelloService/SayHello`:
```
{
  "Message": "hello Ginta"
}
```




### 补充
#### grpc通信加密
#### 服务发现