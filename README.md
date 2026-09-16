# Awesome Network Protocols · 网络协议大全

按网络层和实际用途整理的多语言网络协议学习索引。选择下面的分类即可进入详表，查看协议作用、端口或标识符及官方规范。

## 按网络层

| 网络层 | 主要内容 | 代表协议 |
|---|---|---|
| [Physical／物理层](docs/zh-CN/taxonomy.md#physical物理层) | 比特在物理介质上的传输方式 | Ethernet PHY、Wi-Fi PHY、DSL |
| [Data Link／数据链路层](docs/zh-CN/taxonomy.md#data-link数据链路层) | 局域网成帧、介质访问和链路寻址 | Ethernet、Wi-Fi、VLAN、ARP |
| [Network／网络层](docs/zh-CN/taxonomy.md#network网络层) | 跨网络寻址、转发和路由 | IPv4、IPv6、ICMP、OSPF、BGP |
| [Transport／传输层](docs/zh-CN/taxonomy.md#transport传输层) | 端到端传输、可靠性和拥塞控制 | TCP、UDP、SCTP、QUIC |
| [Session／会话层](docs/zh-CN/taxonomy.md#session会话层) | 建立、维持和恢复通信会话 | NetBIOS Session Service、SIP |
| [Presentation／表示层](docs/zh-CN/taxonomy.md#presentation表示层) | 数据编码、压缩与加密表示 | TLS、ASN.1、XDR |
| [Application／应用层](docs/zh-CN/taxonomy.md#application应用层) | 面向用户和应用的网络服务 | HTTP、DNS、SSH、SMTP、MQTT |

## 按用途

| 分类 | 代表协议与技术 |
|---|---|
| [Web 与 API](docs/zh-CN/taxonomy.md#web-与-api) | HTTP、HTTPS、WebSocket、QUIC |
| [DNS 与服务发现](docs/zh-CN/taxonomy.md#dns-与服务发现) | DNS、mDNS、DNS-SD、DHCP |
| [路由](docs/zh-CN/taxonomy.md#路由) | BGP、OSPF、RIP、IS-IS |
| [网络管理](docs/zh-CN/taxonomy.md#网络管理) | SNMP、NETCONF、RESTCONF、Syslog |
| [远程访问](docs/zh-CN/taxonomy.md#远程访问) | SSH、Telnet、RDP、VNC |
| [文件传输](docs/zh-CN/taxonomy.md#文件传输) | FTP、SFTP、SMB、NFS |
| [邮件](docs/zh-CN/taxonomy.md#邮件) | SMTP、IMAP、POP3 |
| [身份认证](docs/zh-CN/taxonomy.md#身份认证) | Kerberos、RADIUS、LDAP、OAuth 2.0 |
| [加密与 VPN](docs/zh-CN/taxonomy.md#加密与-vpn) | TLS、IPsec、WireGuard、OpenVPN |
| [实时音视频](docs/zh-CN/taxonomy.md#实时音视频) | RTP、RTCP、SIP、WebRTC |
| [消息队列](docs/zh-CN/taxonomy.md#消息队列) | MQTT、AMQP、STOMP、NATS |
| [IoT 与短距离通信](docs/zh-CN/taxonomy.md#iot-与短距离通信) | CoAP、MQTT、Zigbee、Bluetooth LE |
| [云原生与容器网络](docs/zh-CN/taxonomy.md#云原生与容器网络) | gRPC、HTTP/2、VXLAN、CNI |
| [工业与汽车协议](docs/zh-CN/taxonomy.md#工业与汽车协议) | Modbus TCP、OPC UA、CAN、Automotive Ethernet |

## 学习路线

- [从零开始学习网络协议](docs/zh-CN/learning-paths.md)：从分层模型、抓包和寻址开始，逐步理解 TCP/IP、DNS、HTTP 与安全协议。
- [完整协议目录](docs/zh-CN/catalog.md)：按统一格式浏览当前收录的协议。
- [协议条目规范](docs/zh-CN/protocol-entry.md)：了解每个协议条目应包含的原理、标识符、安全信息和学习资源。

## 其他语言

[English](docs/en/README.md) · [简体中文](docs/zh-CN/README.md) · [繁體中文](docs/zh-TW/README.md) · [日本語](docs/ja/README.md) · [한국어](docs/ko/README.md) · [Español](docs/es/README.md) · [Português](docs/pt-BR/README.md) · [Français](docs/fr/README.md) · [Deutsch](docs/de/README.md) · [Русский](docs/ru/README.md) · [العربية](docs/ar/README.md)

## 参与完善

欢迎补充协议、官方标准和教学资源。提交前请阅读[贡献指南](CONTRIBUTING.md)与[翻译指南](TRANSLATING.md)，并运行：

```bash
python3 scripts/validate.py
```

文档和结构化数据使用 [CC BY 4.0](LICENSE)，校验代码使用同一文件中附带的 MIT 条款。
