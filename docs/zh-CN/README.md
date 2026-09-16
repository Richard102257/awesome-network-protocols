# Awesome Network Protocols

> 一个经过整理、支持多语言的网络协议、标准、工具与教学资源地图。

[English](../../README.md) · [简体中文](README.md) · [繁體中文](../zh-TW/README.md) · [日本語](../ja/README.md) · [한국어](../ko/README.md) · [Español](../es/README.md) · [Português](../pt-BR/README.md) · [Français](../fr/README.md) · [Deutsch](../de/README.md) · [Русский](../ru/README.md) · [العربية](../ar/README.md)

## 这是什么

本项目按网络层、用途和行业整理网络协议。每个条目采用统一格式：用途、工作原理、端口或标识符、标准、安全说明、分析工具及学习资料。

项目追求可靠且实用的覆盖范围，不宣称收录历史上出现过的全部协议。

## 浏览内容

- [详细分类：按网络层与用途](taxonomy.md)
- [协议目录](catalog.md)
- [学习路线](learning-paths.md)
- [协议条目规范](protocol-entry.md)
- [贡献指南](../../CONTRIBUTING.md)
- [翻译指南](../../TRANSLATING.md)

## 收录范围

| 领域 | 示例 |
|---|---|
| Web 与 API | HTTP、HTTPS、WebSocket、QUIC |
| 命名与发现 | DNS、DHCP、mDNS、DNS-SD、ARP |
| 传输与寻址 | TCP、UDP、SCTP、IPv4、IPv6、ICMP |
| 路由 | BGP、OSPF、RIP、IS-IS |
| 局域网 | Ethernet、Wi-Fi、VLAN、STP、LLDP |
| 安全与身份 | TLS、IPsec、SSH、Kerberos、WireGuard |
| 消息与媒体 | MQTT、CoAP、SIP、RTP、RTCP |
| 文件与邮件 | FTP、SFTP、SMB、NFS、SMTP、IMAP、POP3 |
| 工业与设备 | CAN、Modbus TCP、Zigbee、Bluetooth LE |

## 如何贡献协议

1. 在 [data/protocols.json](../../data/protocols.json) 中新增或修改记录。
2. 使用稳定的协议 ID，并优先引用官方标准。
3. 尽量同时提供英文和中文名称及摘要。
4. 运行：python3 scripts/validate.py
5. 使用仓库模板提交拉取请求。

## 内容原则

- 优先引用 RFC 和标准组织文档。
- 区分协议事实与具体实现建议。
- 明确标注已废弃、实验性和专有协议。
- 不把传输加密描述为完整的应用安全。
- 使用稳定 ID 对齐翻译，避免依赖行号。
- 图表必须提供文本替代说明。

## 许可证

文档和结构化数据采用 [CC BY 4.0](../../LICENSE)，校验脚本等代码采用同一文件内的 MIT 条款。
