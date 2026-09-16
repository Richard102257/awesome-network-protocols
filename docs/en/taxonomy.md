# By layer and purpose

[← Browse](README.md)

> English is the canonical editorial source for names, standards, identifiers, and technical meaning.

## OSI — By layer and purpose

### Physical

| Protocol | Port / identifier | Official specification |
|---|---|---|
| [Ethernet PHY](https://standards.ieee.org/ieee/802.3/10422/) | media/signals | [↗](https://standards.ieee.org/ieee/802.3/10422/) |
| [Wi-Fi PHY](https://standards.ieee.org/ieee/802.11/10548/) | radio/modulation | [↗](https://standards.ieee.org/ieee/802.11/10548/) |

### Data Link

| Protocol | Port / identifier | Official specification |
|---|---|---|
| [Ethernet](https://standards.ieee.org/ieee/802.3/10422/) | — | [↗](https://standards.ieee.org/ieee/802.3/10422/) |
| [Wi-Fi](https://standards.ieee.org/ieee/802.11/10548/) | — | [↗](https://standards.ieee.org/ieee/802.11/10548/) |
| [ARP](https://www.rfc-editor.org/rfc/rfc826) | — | [↗](https://www.rfc-editor.org/rfc/rfc826) |

### Network

| Protocol | Port / identifier | Official specification |
|---|---|---|
| [IPv4](https://www.rfc-editor.org/rfc/rfc791) | — | [↗](https://www.rfc-editor.org/rfc/rfc791) |
| [IPv6](https://www.rfc-editor.org/rfc/rfc8200) | — | [↗](https://www.rfc-editor.org/rfc/rfc8200) |
| [ICMP](https://www.rfc-editor.org/rfc/rfc792) | — | [↗](https://www.rfc-editor.org/rfc/rfc792) |
| [OSPF](https://www.rfc-editor.org/rfc/rfc2328) | — | [↗](https://www.rfc-editor.org/rfc/rfc2328) |

### Transport

| Protocol | Port / identifier | Official specification |
|---|---|---|
| [TCP](https://www.rfc-editor.org/rfc/rfc9293) | — | [↗](https://www.rfc-editor.org/rfc/rfc9293) |
| [UDP](https://www.rfc-editor.org/rfc/rfc768) | — | [↗](https://www.rfc-editor.org/rfc/rfc768) |
| [QUIC](https://www.rfc-editor.org/rfc/rfc9000) | — | [↗](https://www.rfc-editor.org/rfc/rfc9000) |

### Session

| Protocol | Port / identifier | Official specification |
|---|---|---|
| [SIP](https://www.rfc-editor.org/rfc/rfc3261) | 5060/5061 | [↗](https://www.rfc-editor.org/rfc/rfc3261) |
| [WebSocket](https://www.rfc-editor.org/rfc/rfc6455) | 80/443 | [↗](https://www.rfc-editor.org/rfc/rfc6455) |

### Presentation

| Protocol | Port / identifier | Official specification |
|---|---|---|
| [TLS](https://www.rfc-editor.org/rfc/rfc8446) | — | [↗](https://www.rfc-editor.org/rfc/rfc8446) |

### Application

| Protocol | Port / identifier | Official specification |
|---|---|---|
| [HTTP](https://www.rfc-editor.org/rfc/rfc9110) | 80 | [↗](https://www.rfc-editor.org/rfc/rfc9110) |
| [DNS](https://www.rfc-editor.org/rfc/rfc1034) | 53 | [↗](https://www.rfc-editor.org/rfc/rfc1034) |
| [DHCP](https://www.rfc-editor.org/rfc/rfc2131) | 67/68 | [↗](https://www.rfc-editor.org/rfc/rfc2131) |
| [BGP](https://www.rfc-editor.org/rfc/rfc4271) | 179 | [↗](https://www.rfc-editor.org/rfc/rfc4271) |
| [SSH](https://www.rfc-editor.org/rfc/rfc4251) | 22 | [↗](https://www.rfc-editor.org/rfc/rfc4251) |
| [SMTP](https://www.rfc-editor.org/rfc/rfc5321) | 25/465/587 | [↗](https://www.rfc-editor.org/rfc/rfc5321) |
| [MQTT](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) | 1883/8883 | [↗](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) |
| [RTP](https://www.rfc-editor.org/rfc/rfc3550) | — | [↗](https://www.rfc-editor.org/rfc/rfc3550) |
| [Modbus TCP](https://www.modbus.org/specs.php) | 502 | [↗](https://www.modbus.org/specs.php) |

## By layer and purpose — 14

### Web and APIs

| Protocol | Port / identifier | Core role | Official specification |
|---|---|---|---|
| [HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112) | 80/443 | request-response | [↗](https://www.rfc-editor.org/rfc/rfc9112) |
| [HTTP/2](https://www.rfc-editor.org/rfc/rfc9113) | 443 | binary multiplexing | [↗](https://www.rfc-editor.org/rfc/rfc9113) |
| [HTTP/3](https://www.rfc-editor.org/rfc/rfc9114) | UDP 443 | HTTP over QUIC | [↗](https://www.rfc-editor.org/rfc/rfc9114) |
| [WebSocket](https://www.rfc-editor.org/rfc/rfc6455) | 80/443 | full-duplex session | [↗](https://www.rfc-editor.org/rfc/rfc6455) |
| [gRPC](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md) | 443 | remote procedure calls | [↗](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md) |

### DNS and service discovery

| Protocol | Port / identifier | Core role | Official specification |
|---|---|---|---|
| [DNS](https://www.rfc-editor.org/rfc/rfc1034) | 53 | hierarchical naming | [↗](https://www.rfc-editor.org/rfc/rfc1034) |
| [DNSSEC](https://www.rfc-editor.org/rfc/rfc4033) | 53 | signed DNS data | [↗](https://www.rfc-editor.org/rfc/rfc4033) |
| [DoH](https://www.rfc-editor.org/rfc/rfc8484) | 443 | encrypted DNS | [↗](https://www.rfc-editor.org/rfc/rfc8484) |
| [mDNS](https://www.rfc-editor.org/rfc/rfc6762) | UDP 5353 | local multicast naming | [↗](https://www.rfc-editor.org/rfc/rfc6762) |
| [DNS-SD](https://www.rfc-editor.org/rfc/rfc6763) | 53/5353 | service discovery | [↗](https://www.rfc-editor.org/rfc/rfc6763) |

### Routing

| Protocol | Port / identifier | Core role | Official specification |
|---|---|---|---|
| [BGP](https://www.rfc-editor.org/rfc/rfc4271) | TCP 179 | policy path vector | [↗](https://www.rfc-editor.org/rfc/rfc4271) |
| [OSPF](https://www.rfc-editor.org/rfc/rfc2328) | IP 89 | link-state routing | [↗](https://www.rfc-editor.org/rfc/rfc2328) |
| [IS-IS](https://www.rfc-editor.org/rfc/rfc1195) | CLNS | link-state routing | [↗](https://www.rfc-editor.org/rfc/rfc1195) |
| [RIP](https://www.rfc-editor.org/rfc/rfc2453) | UDP 520 | distance vector | [↗](https://www.rfc-editor.org/rfc/rfc2453) |
| [Babel](https://www.rfc-editor.org/rfc/rfc8966) | UDP 6696 | loop-avoiding distance vector | [↗](https://www.rfc-editor.org/rfc/rfc8966) |

### Network management

| Protocol | Port / identifier | Core role | Official specification |
|---|---|---|---|
| [SNMPv3](https://www.rfc-editor.org/rfc/rfc3411) | UDP 161/162 | managed objects | [↗](https://www.rfc-editor.org/rfc/rfc3411) |
| [NETCONF](https://www.rfc-editor.org/rfc/rfc6241) | TCP 830 | configuration transactions | [↗](https://www.rfc-editor.org/rfc/rfc6241) |
| [RESTCONF](https://www.rfc-editor.org/rfc/rfc8040) | 443 | YANG over HTTP | [↗](https://www.rfc-editor.org/rfc/rfc8040) |
| [Syslog](https://www.rfc-editor.org/rfc/rfc5424) | 514/6514 | event messages | [↗](https://www.rfc-editor.org/rfc/rfc5424) |
| [NTP](https://www.rfc-editor.org/rfc/rfc5905) | UDP 123 | clock synchronization | [↗](https://www.rfc-editor.org/rfc/rfc5905) |

### Remote access

| Protocol | Port / identifier | Core role | Official specification |
|---|---|---|---|
| [SSH](https://www.rfc-editor.org/rfc/rfc4251) | TCP 22 | encrypted terminal | [↗](https://www.rfc-editor.org/rfc/rfc4251) |
| [Telnet](https://www.rfc-editor.org/rfc/rfc854) | TCP 23 | plaintext terminal | [↗](https://www.rfc-editor.org/rfc/rfc854) |
| [RDP](https://learn.microsoft.com/openspecs/windows_protocols/ms-rdpbcgr/) | 3389 | remote desktop | [↗](https://learn.microsoft.com/openspecs/windows_protocols/ms-rdpbcgr/) |
| [VNC/RFB](https://www.rfc-editor.org/rfc/rfc6143) | TCP 5900 | remote framebuffer | [↗](https://www.rfc-editor.org/rfc/rfc6143) |

### File transfer

| Protocol | Port / identifier | Core role | Official specification |
|---|---|---|---|
| [FTP](https://www.rfc-editor.org/rfc/rfc959) | TCP 20/21 | separate control and data | [↗](https://www.rfc-editor.org/rfc/rfc959) |
| [SFTP](https://datatracker.ietf.org/doc/html/draft-ietf-secsh-filexfer-13) | TCP 22 | files over SSH | [↗](https://datatracker.ietf.org/doc/html/draft-ietf-secsh-filexfer-13) |
| [TFTP](https://www.rfc-editor.org/rfc/rfc1350) | UDP 69 | block transfer | [↗](https://www.rfc-editor.org/rfc/rfc1350) |
| [NFSv4.1](https://www.rfc-editor.org/rfc/rfc8881) | TCP 2049 | remote filesystem | [↗](https://www.rfc-editor.org/rfc/rfc8881) |
| [SMB 3](https://learn.microsoft.com/openspecs/windows_protocols/ms-smb2/) | TCP 445 | stateful file sharing | [↗](https://learn.microsoft.com/openspecs/windows_protocols/ms-smb2/) |

### Email

| Protocol | Port / identifier | Core role | Official specification |
|---|---|---|---|
| [SMTP](https://www.rfc-editor.org/rfc/rfc5321) | 25/465/587 | mail relay | [↗](https://www.rfc-editor.org/rfc/rfc5321) |
| [IMAP4rev2](https://www.rfc-editor.org/rfc/rfc9051) | 143/993 | mailbox sync | [↗](https://www.rfc-editor.org/rfc/rfc9051) |
| [POP3](https://www.rfc-editor.org/rfc/rfc1939) | 110/995 | mail download | [↗](https://www.rfc-editor.org/rfc/rfc1939) |
| [MIME](https://www.rfc-editor.org/rfc/rfc2045) | message format | media encoding | [↗](https://www.rfc-editor.org/rfc/rfc2045) |
| [JMAP](https://www.rfc-editor.org/rfc/rfc8620) | HTTPS | JSON mail sync | [↗](https://www.rfc-editor.org/rfc/rfc8620) |

### Identity and authentication

| Protocol | Port / identifier | Core role | Official specification |
|---|---|---|---|
| [Kerberos V5](https://www.rfc-editor.org/rfc/rfc4120) | 88 | ticket authentication | [↗](https://www.rfc-editor.org/rfc/rfc4120) |
| [LDAP](https://www.rfc-editor.org/rfc/rfc4511) | 389/636 | directory access | [↗](https://www.rfc-editor.org/rfc/rfc4511) |
| [RADIUS](https://www.rfc-editor.org/rfc/rfc2865) | 1812/1813 | AAA | [↗](https://www.rfc-editor.org/rfc/rfc2865) |
| [TACACS+](https://www.rfc-editor.org/rfc/rfc8907) | TCP 49 | device administration | [↗](https://www.rfc-editor.org/rfc/rfc8907) |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | HTTPS | identity claims | [↗](https://openid.net/specs/openid-connect-core-1_0.html) |

### Encryption and VPN

| Protocol | Port / identifier | Core role | Official specification |
|---|---|---|---|
| [TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) | varies | secure sessions | [↗](https://www.rfc-editor.org/rfc/rfc8446) |
| [IPsec/IKEv2](https://www.rfc-editor.org/rfc/rfc4301) | IP 50/51 | IP security | [↗](https://www.rfc-editor.org/rfc/rfc4301) |
| [WireGuard](https://www.wireguard.com/protocol/) | UDP | key-based tunnel | [↗](https://www.wireguard.com/protocol/) |
| [OpenVPN](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/) | 1194 common | TLS VPN | [↗](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/) |
| [MACsec](https://standards.ieee.org/ieee/802.1AE/7427/) | Ethernet | link encryption | [↗](https://standards.ieee.org/ieee/802.1AE/7427/) |

### Real-time audio and video

| Protocol | Port / identifier | Core role | Official specification |
|---|---|---|---|
| [SIP](https://www.rfc-editor.org/rfc/rfc3261) | 5060/5061 | session signaling | [↗](https://www.rfc-editor.org/rfc/rfc3261) |
| [SDP](https://www.rfc-editor.org/rfc/rfc8866) | payload | media description | [↗](https://www.rfc-editor.org/rfc/rfc8866) |
| [RTP/RTCP](https://www.rfc-editor.org/rfc/rfc3550) | dynamic | media and feedback | [↗](https://www.rfc-editor.org/rfc/rfc3550) |
| [SRTP](https://www.rfc-editor.org/rfc/rfc3711) | dynamic | secure media | [↗](https://www.rfc-editor.org/rfc/rfc3711) |
| [WebRTC](https://www.w3.org/TR/webrtc/) | dynamic | browser real-time media | [↗](https://www.w3.org/TR/webrtc/) |

### Message queues

| Protocol | Port / identifier | Core role | Official specification |
|---|---|---|---|
| [MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) | 1883/8883 | topic broker | [↗](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) |
| [AMQP 1.0](https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html) | 5672/5671 | message links | [↗](https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html) |
| [STOMP 1.2](https://stomp.github.io/stomp-specification-1.2.html) | 61613 common | text messaging | [↗](https://stomp.github.io/stomp-specification-1.2.html) |
| [NATS](https://docs.nats.io/reference/reference-protocols/nats-protocol) | 4222 common | subject messaging | [↗](https://docs.nats.io/reference/reference-protocols/nats-protocol) |
| [DDS](https://www.omg.org/spec/DDS/) | varies | real-time pub-sub | [↗](https://www.omg.org/spec/DDS/) |

### IoT and proximity

| Protocol | Port / identifier | Core role | Official specification |
|---|---|---|---|
| [CoAP](https://www.rfc-editor.org/rfc/rfc7252) | 5683/5684 | constrained REST | [↗](https://www.rfc-editor.org/rfc/rfc7252) |
| [Bluetooth LE](https://www.bluetooth.com/specifications/specs/core-specification/) | 2.4 GHz | GATT proximity | [↗](https://www.bluetooth.com/specifications/specs/core-specification/) |
| [Zigbee](https://csa-iot.org/all-solutions/zigbee/) | 802.15.4 | low-power mesh | [↗](https://csa-iot.org/all-solutions/zigbee/) |
| [Thread](https://www.threadgroup.org/support#specifications) | IPv6 | low-power IP mesh | [↗](https://www.threadgroup.org/support#specifications) |
| [Matter](https://csa-iot.org/all-solutions/matter/) | IP | smart-home application | [↗](https://csa-iot.org/all-solutions/matter/) |

### Cloud native and containers

| Protocol | Port / identifier | Core role | Official specification |
|---|---|---|---|
| [VXLAN](https://www.rfc-editor.org/rfc/rfc7348) | UDP 4789 | L2 overlay | [↗](https://www.rfc-editor.org/rfc/rfc7348) |
| [Geneve](https://www.rfc-editor.org/rfc/rfc8926) | UDP 6081 | extensible overlay | [↗](https://www.rfc-editor.org/rfc/rfc8926) |
| [BGP EVPN](https://www.rfc-editor.org/rfc/rfc7432) | BGP | overlay reachability | [↗](https://www.rfc-editor.org/rfc/rfc7432) |
| [CNI](https://www.cni.dev/docs/spec/) | local API | container networking | [↗](https://www.cni.dev/docs/spec/) |
| [OpenFlow](https://opennetworking.org/sdn-resources/openflow-switch-specification/) | TCP 6653 | SDN flow control | [↗](https://opennetworking.org/sdn-resources/openflow-switch-specification/) |

### Industrial and automotive

| Protocol | Port / identifier | Core role | Official specification |
|---|---|---|---|
| [Modbus TCP](https://www.modbus.org/specs.php) | TCP 502 | register access | [↗](https://www.modbus.org/specs.php) |
| [OPC UA](https://reference.opcfoundation.org/Core/Part1/) | 4840 common | industrial information model | [↗](https://reference.opcfoundation.org/Core/Part1/) |
| [PROFINET](https://www.profibus.com/technology/profinet) | Ethernet | real-time control | [↗](https://www.profibus.com/technology/profinet) |
| [EtherCAT](https://www.ethercat.org/en/technology.html) | Ethernet | on-the-fly processing | [↗](https://www.ethercat.org/en/technology.html) |
| [CAN](https://www.iso.org/standard/63648.html) | message ID | bus arbitration | [↗](https://www.iso.org/standard/63648.html) |

> English is the canonical editorial source for names, standards, identifiers, and technical meaning.

[English details](../en/taxonomy.md) · [中文详表](../zh-CN/taxonomy.md)
