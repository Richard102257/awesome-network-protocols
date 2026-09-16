# 网络协议分类详表

[English](../en/taxonomy.md) · [简体中文](taxonomy.md)

本页提供两个互补视角：**按网络层**回答“协议主要位于通信栈哪里”，**按用途**回答“协议解决什么问题”。同一协议可以属于多个用途。

> OSI 七层是教学模型，并非所有现实协议的精确实现边界。BGP 会话运行于 TCP，但作用于网络路由；TLS 通常位于应用与传输之间。下表按主要职责归类。

## 按网络层

### Physical／物理层

把比特转换成电、光或无线信号，规定介质、调制、编码、速率和链路距离。

| 标准 | 原理与教学重点 | 官方规范 |
|---|---|---|
| Ethernet PHY | 通过双绞线或光纤承载符号，不同 PHY 定义速率与距离 | [IEEE 802.3](https://standards.ieee.org/ieee/802.3/10422/) |
| Wi-Fi PHY | 使用无线信道、调制与编码方案传输帧 | [IEEE 802.11](https://standards.ieee.org/ieee/802.11/10548/) |
| Bluetooth Radio | 在 2.4 GHz 频段通过跳频连接近距离设备 | [Bluetooth Core](https://www.bluetooth.com/specifications/specs/core-specification/) |
| IEEE 802.15.4 | 面向低速、低功耗个人区域网络 | [IEEE 802.15.4](https://standards.ieee.org/ieee/802.15.4/7029/) |

### Data Link／数据链路层

在本地链路传输帧，处理 MAC 地址、介质访问、差错检测、交换和逻辑分段。

| 协议 | 原理与标识符 | 官方规范 |
|---|---|---|
| Ethernet | 用源/目的 MAC、EtherType 和 FCS 封装载荷；交换机学习源地址 | [IEEE 802.3](https://standards.ieee.org/ieee/802.3/10422/) |
| Wi-Fi | 终端关联接入点并在共享无线介质竞争发送帧 | [IEEE 802.11](https://standards.ieee.org/ieee/802.11/10548/) |
| ARP | 广播询问 IPv4 对应的 MAC；EtherType 0x0806 | [RFC 826](https://www.rfc-editor.org/rfc/rfc826) |
| VLAN | 插入 VLAN ID 划分广播域；EtherType 0x8100 | [IEEE 802.1Q](https://standards.ieee.org/ieee/802.1Q/10323/) |
| STP / RSTP | 选举根桥并阻塞冗余路径，形成无环拓扑 | [IEEE 802.1D](https://standards.ieee.org/ieee/802.1D/2605/) |
| LLDP | 相邻设备发布身份、端口和能力；EtherType 0x88CC | [IEEE 802.1AB](https://standards.ieee.org/ieee/802.1AB/10327/) |
| PPP | 在点到点链路协商参数、认证并承载网络层数据 | [RFC 1661](https://www.rfc-editor.org/rfc/rfc1661) |
| MPLS | 加入短标签，使核心设备沿标签交换路径转发 | [RFC 3031](https://www.rfc-editor.org/rfc/rfc3031) |

### Network／网络层

负责跨网络寻址、下一跳选择、分组转发、错误报告和组播控制。

| 协议 | 原理与标识符 | 官方规范 |
|---|---|---|
| IPv4 | 按最长前缀匹配转发 32 位地址分组 | [RFC 791](https://www.rfc-editor.org/rfc/rfc791) |
| IPv6 | 使用 128 位地址、扩展头及邻居发现 | [RFC 8200](https://www.rfc-editor.org/rfc/rfc8200) |
| ICMP / ICMPv6 | 报告不可达、超时等状态；IP 协议号 1 / 58 | [RFC 792](https://www.rfc-editor.org/rfc/rfc792) · [RFC 4443](https://www.rfc-editor.org/rfc/rfc4443) |
| IGMP | 管理 IPv4 组播成员关系；IP 协议号 2 | [RFC 3376](https://www.rfc-editor.org/rfc/rfc3376) |
| IPsec | 用 AH/ESP 认证或加密 IP 分组；协议号 50 / 51 | [RFC 4301](https://www.rfc-editor.org/rfc/rfc4301) |
| OSPF | 泛洪链路状态并计算最短路径；协议号 89 | [RFC 2328](https://www.rfc-editor.org/rfc/rfc2328) |
| IS-IS | 交换链路状态 PDU，建立拓扑数据库并计算域内路由 | [RFC 1195](https://www.rfc-editor.org/rfc/rfc1195) |

### Transport／传输层

在应用进程之间提供复用、可靠性、顺序控制、拥塞控制或低开销数据报。

| 协议 | 核心原理 | 官方规范 |
|---|---|---|
| TCP | 序列号、确认、重传、滑动窗口和拥塞控制构成可靠字节流 | [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293) |
| UDP | 只增加端口、长度和校验和，不建立连接或保证送达 | [RFC 768](https://www.rfc-editor.org/rfc/rfc768) |
| QUIC | 在 UDP 上集成 TLS 1.3、可靠多流和拥塞控制 | [RFC 9000](https://www.rfc-editor.org/rfc/rfc9000) |
| SCTP | 保留消息边界，支持多流与多宿主 | [RFC 9260](https://www.rfc-editor.org/rfc/rfc9260) |
| DCCP | 为实时数据报提供拥塞控制但不保证可靠交付 | [RFC 4340](https://www.rfc-editor.org/rfc/rfc4340) |

### Session／会话层

管理对话建立、恢复、同步点与长期状态；互联网栈常把这些职责放进应用协议。

| 协议 | 核心原理 | 官方规范 |
|---|---|---|
| NetBIOS Session | 建立有状态局域网会话并传输消息 | [RFC 1002](https://www.rfc-editor.org/rfc/rfc1002) |
| RPC | 将远程调用编码为请求响应，用调用 ID 匹配结果 | [RFC 5531](https://www.rfc-editor.org/rfc/rfc5531) |
| SIP | 建立、修改和结束音视频会话，媒体通常交给 RTP | [RFC 3261](https://www.rfc-editor.org/rfc/rfc3261) |
| WebSocket | 由 HTTP Upgrade 建立持续全双工消息会话 | [RFC 6455](https://www.rfc-editor.org/rfc/rfc6455) |

### Presentation／表示层

处理序列化、字符编码、压缩和加密，使双方对字节含义达成一致。

| 协议或格式 | 核心原理 | 官方规范 |
|---|---|---|
| TLS | 认证通信方、协商密钥，以认证加密保护应用字节 | [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) |
| ASN.1 / BER / DER | 用抽象类型描述数据，再按编码规则转换为字节 | [ITU-T X.690](https://www.itu.int/rec/T-REC-X.690/en) |
| XDR | 定义与机器架构无关的二进制数据表示 | [RFC 4506](https://www.rfc-editor.org/rfc/rfc4506) |
| MIME | 描述媒体类型、字符集和多部分消息结构 | [RFC 2045](https://www.rfc-editor.org/rfc/rfc2045) |

### Application／应用层

定义应用直接理解的操作、资源、状态码与业务消息。

| 协议组 | 代表协议 | 教学重点 |
|---|---|---|
| Web | [HTTP](https://www.rfc-editor.org/rfc/rfc9110)、[HTTP/2](https://www.rfc-editor.org/rfc/rfc9113)、[HTTP/3](https://www.rfc-editor.org/rfc/rfc9114) | 方法、资源、状态码、缓存、多路复用 |
| 命名与配置 | [DNS](https://www.rfc-editor.org/rfc/rfc1034)、[DHCP](https://www.rfc-editor.org/rfc/rfc2131)、[mDNS](https://www.rfc-editor.org/rfc/rfc6762) | 分层解析、租约、本地发现 |
| 邮件 | [SMTP](https://www.rfc-editor.org/rfc/rfc5321)、[IMAP](https://www.rfc-editor.org/rfc/rfc9051)、[POP3](https://www.rfc-editor.org/rfc/rfc1939) | 存储转发、同步与下载模型 |
| 文件与远程 | [FTP](https://www.rfc-editor.org/rfc/rfc959)、[SSH](https://www.rfc-editor.org/rfc/rfc4251)、[NFS](https://www.rfc-editor.org/rfc/rfc8881) | 数据通道、认证和远程文件操作 |
| 管理 | [SNMP](https://www.rfc-editor.org/rfc/rfc3411)、[NTP](https://www.rfc-editor.org/rfc/rfc5905)、[NETCONF](https://www.rfc-editor.org/rfc/rfc6241) | 对象查询、时间同步和配置事务 |

## 按用途

以下 14 个用途分类提供协议、核心作用、常用端口及官方来源。

### Web 与 API

- [HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112) — 文本请求响应、持久连接和缓存语义；80/443。
- [HTTP/2](https://www.rfc-editor.org/rfc/rfc9113) — 二进制分帧、头部压缩、单连接多路复用；443。
- [HTTP/3](https://www.rfc-editor.org/rfc/rfc9114) — 在 QUIC 流上承载 HTTP，降低传输层阻塞；UDP 443。
- [WebSocket](https://www.rfc-editor.org/rfc/rfc6455) — HTTP Upgrade 后建立长期双向消息通道；80/443。
- [gRPC](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md) — 基于 HTTP/2 与 Protocol Buffers 的远程过程调用。

### DNS 与服务发现

- [DNS](https://www.rfc-editor.org/rfc/rfc1034) — 分层、分布式地查询域名和资源记录；53。
- [DNSSEC](https://www.rfc-editor.org/rfc/rfc4033) — 用签名建立 DNS 数据来源认证与完整性链。
- [DoT](https://www.rfc-editor.org/rfc/rfc7858)、[DoH](https://www.rfc-editor.org/rfc/rfc8484)、[DoQ](https://www.rfc-editor.org/rfc/rfc9250) — 分别通过 TLS、HTTPS、QUIC 加密 DNS；853/443/853。
- [mDNS](https://www.rfc-editor.org/rfc/rfc6762) — 在本地链路组播解析 .local 名称；UDP 5353。
- [DNS-SD](https://www.rfc-editor.org/rfc/rfc6763) — 使用 PTR、SRV、TXT 枚举服务实例及能力。
- [SSDP](https://openconnectivity.org/developer/specifications/upnp-resources/upnp/) — UPnP 设备通过组播搜索和广播服务；UDP 1900。

### 路由

- [BGP](https://www.rfc-editor.org/rfc/rfc4271) — 自治系统间路径向量与策略选路；TCP 179。
- [OSPF](https://www.rfc-editor.org/rfc/rfc2328) — 域内链路状态和最短路径树；IP 89。
- [IS-IS](https://www.rfc-editor.org/rfc/rfc1195) — 分层链路状态域内路由。
- [RIP](https://www.rfc-editor.org/rfc/rfc2453) — 周期交换距离向量，最大 15 跳；UDP 520。
- [Babel](https://www.rfc-editor.org/rfc/rfc8966) — 为动态网络结合距离向量和可行性条件；UDP 6696。

### 网络管理

- [SNMPv3](https://www.rfc-editor.org/rfc/rfc3411) — 查询管理对象、接收通知并支持认证与隐私；UDP 161/162。
- [NETCONF](https://www.rfc-editor.org/rfc/rfc6241) — 以事务方式操作设备配置数据库；TCP 830。
- [RESTCONF](https://www.rfc-editor.org/rfc/rfc8040) — 用 HTTP 方法访问 YANG 数据；443。
- [Syslog](https://www.rfc-editor.org/rfc/rfc5424) — 传输结构化系统事件；UDP 514 / TLS 6514。
- [NTP](https://www.rfc-editor.org/rfc/rfc5905) — 用四个时间戳估算时延与时钟偏移；UDP 123。

### 远程访问

- [SSH](https://www.rfc-editor.org/rfc/rfc4251) — 加密终端、命令、端口转发和子系统；TCP 22。
- [Telnet](https://www.rfc-editor.org/rfc/rfc854) — 明文虚拟终端；TCP 23，仅适合受控实验或遗留环境。
- [RDP](https://learn.microsoft.com/openspecs/windows_protocols/ms-rdpbcgr/) — 图形桌面、输入与虚拟通道；TCP/UDP 3389。
- [VNC / RFB](https://www.rfc-editor.org/rfc/rfc6143) — 远程帧缓冲更新和输入事件；常用 TCP 5900。

### 文件传输

- [FTP](https://www.rfc-editor.org/rfc/rfc959) — 控制与数据连接分离；TCP 21/20。
- [SFTP](https://datatracker.ietf.org/doc/html/draft-ietf-secsh-filexfer-13) — SSH 内的文件操作子系统；TCP 22。
- [TFTP](https://www.rfc-editor.org/rfc/rfc1350) — 逐块确认的简化 UDP 文件传输；UDP 69。
- [NFSv4.1](https://www.rfc-editor.org/rfc/rfc8881) — 将远程目录挂载到本地命名空间；TCP 2049。
- [SMB 3](https://learn.microsoft.com/openspecs/windows_protocols/ms-smb2/) — 有状态文件共享、锁、签名及可选加密；TCP 445。
- [WebDAV](https://www.rfc-editor.org/rfc/rfc4918) — 扩展 HTTP 以管理远程集合与资源。

### 邮件

- [SMTP](https://www.rfc-editor.org/rfc/rfc5321) — 邮件提交和服务器间存储转发；25/465/587。
- [IMAP4rev2](https://www.rfc-editor.org/rfc/rfc9051) — 以服务器邮箱为准同步邮件状态；143/993。
- [POP3](https://www.rfc-editor.org/rfc/rfc1939) — 列出并下载邮箱消息；110/995。
- [MIME](https://www.rfc-editor.org/rfc/rfc2045) — 定义邮件内容类型、编码和多部分结构。
- [JMAP](https://www.rfc-editor.org/rfc/rfc8620) — 通过 JSON API 同步邮件及相关数据；通常使用 HTTPS。

### 身份认证

- [Kerberos V5](https://www.rfc-editor.org/rfc/rfc4120) — 通过票据授予票据和服务票据实现单点登录；88。
- [LDAP](https://www.rfc-editor.org/rfc/rfc4511) — 查询和修改目录树；389/636。
- [RADIUS](https://www.rfc-editor.org/rfc/rfc2865) — 集中认证、授权和计费；UDP 1812/1813。
- [TACACS+](https://www.rfc-editor.org/rfc/rfc8907) — 网络设备管理登录的认证、授权和审计；TCP 49。
- [OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749) — 委托授权框架，本身不是用户认证协议。
- [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) — 在 OAuth 2.0 上增加可验证用户身份声明。

### 加密与 VPN

- [TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) — 认证端点并保护应用连接。
- [IPsec](https://www.rfc-editor.org/rfc/rfc4301) / [IKEv2](https://www.rfc-editor.org/rfc/rfc7296) — 在 IP 层建立安全关联和隧道。
- [WireGuard](https://www.wireguard.com/protocol/) — 以公钥标识对等方的精简 UDP 隧道。
- [OpenVPN](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/) — 使用 TLS 控制通道协商可配置 VPN。
- [MACsec](https://standards.ieee.org/ieee/802.1AE/7427/) — 对局域网以太网帧逐跳加密和认证。
- [Noise](https://noiseprotocol.org/noise.html) — 用握手模式组合密钥交换、身份和加密状态。

### 实时音视频

- [SIP](https://www.rfc-editor.org/rfc/rfc3261) — 发起、协商、修改和终止媒体会话。
- [SDP](https://www.rfc-editor.org/rfc/rfc8866) — 描述媒体类型、编码、地址和端口。
- [RTP / RTCP](https://www.rfc-editor.org/rfc/rfc3550) — 传输媒体样本并反馈丢包、抖动和时钟信息。
- [SRTP](https://www.rfc-editor.org/rfc/rfc3711) — 为 RTP/RTCP 提供加密、完整性和重放保护。
- [WebRTC](https://www.w3.org/TR/webrtc/) — 浏览器实时通信协议组合，使用 ICE、DTLS、SRTP 等。
- [RTSP](https://www.rfc-editor.org/rfc/rfc7826) — 控制流媒体播放、暂停和定位；常用 TCP 554。

### 消息队列

- [MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) — 代理转发主题消息，支持 QoS 0/1/2。
- [AMQP 1.0](https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html) — 标准化消息、链路、结算和流量控制。
- [STOMP 1.2](https://stomp.github.io/stomp-specification-1.2.html) — 简单文本帧消息协议。
- [NATS](https://docs.nats.io/reference/reference-protocols/nats-protocol) — 轻量主题发布订阅与请求响应。
- [DDS](https://www.omg.org/spec/DDS/) — 面向实时系统的数据中心发布订阅。

### IoT 与短距离通信

- [CoAP](https://www.rfc-editor.org/rfc/rfc7252) — 适合受限设备的 REST 风格 UDP 协议；5683/5684。
- [Bluetooth LE](https://www.bluetooth.com/specifications/specs/core-specification/) — 通过广播、连接和 GATT 服务交换低功耗数据。
- [Zigbee](https://csa-iot.org/all-solutions/zigbee/) — 基于 802.15.4 的低功耗网状网络与应用模型。
- [Thread](https://www.threadgroup.org/support#specifications) — 基于 IPv6/6LoWPAN 的低功耗网状网络。
- [Matter](https://csa-iot.org/all-solutions/matter/) — 基于 IP 的跨厂商智能家居应用协议。
- [LoRaWAN](https://lora-alliance.org/resource_hub/lorawan-specification-v1-0-4/) — 面向远距离、低速终端的星状广域网络。
- [Z-Wave](https://z-wavealliance.org/z-wave-specification/) — 面向智能家居的低功耗网状协议。

### 云原生与容器网络

- [VXLAN](https://www.rfc-editor.org/rfc/rfc7348) — 通过 UDP 封装二层帧构建覆盖网络；UDP 4789。
- [Geneve](https://www.rfc-editor.org/rfc/rfc8926) — 带可扩展元数据的虚拟化封装；UDP 6081。
- [BGP EVPN](https://www.rfc-editor.org/rfc/rfc7432) — 使用 BGP 分发二层/三层覆盖网络可达性。
- [CNI](https://www.cni.dev/docs/spec/) — 容器运行时调用网络插件的接口规范。
- [CRI](https://kubernetes.io/docs/concepts/architecture/cri/) — Kubernetes 与容器运行时的 gRPC 接口。
- [OpenFlow](https://opennetworking.org/sdn-resources/openflow-switch-specification/) — SDN 控制器编程交换机流表的南向协议。

### 工业与汽车协议

- [Modbus TCP](https://www.modbus.org/specs.php) — 使用功能码读写线圈与寄存器；TCP 502。
- [OPC UA](https://reference.opcfoundation.org/Core/Part1/) — 提供信息模型、安全通道和工业服务集合。
- [PROFINET](https://www.profibus.com/technology/profinet) — 工业以太网实时控制和设备工程。
- [EtherCAT](https://www.ethercat.org/en/technology.html) — 帧经过设备时即时读写数据，以获得低延迟控制。
- [DNP3](https://www.dnp.org/About/Overview-of-DNP3-Protocol) — 电力和公用设施遥测控制；TCP/UDP 20000。
- [CAN](https://www.iso.org/standard/63648.html) — 按消息 ID 仲裁的共享汽车控制总线。
- [CAN FD](https://www.iso.org/standard/76561.html) — 提高 CAN 载荷容量和数据阶段速率。
- [Automotive Ethernet](https://www.opensig.org/) — 面向车载网络的单对以太网及配置规范。

## 正式条目的完善标准

每个协议最终应包含：消息时序、关键报文字段、端口或 EtherType、依赖协议、安全保证与缺失保证、Wireshark 过滤器、最小抓包示例、开源实现、实验环境以及版本或废弃状态。详细格式见[协议条目规范](protocol-entry.md)。

