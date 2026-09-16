# Por camada e finalidade

[← Explorar](README.md)

> Versão comunitária. Nomes, padrões e números seguem a fonte normativa em inglês.

## OSI — Por camada e finalidade

### Camada física

| Protocolo | Porta／identificador | Especificação oficial |
|---|---|---|
| [Ethernet PHY](https://standards.ieee.org/ieee/802.3/10422/) | media/signals | [↗](https://standards.ieee.org/ieee/802.3/10422/) |
| [Wi-Fi PHY](https://standards.ieee.org/ieee/802.11/10548/) | radio/modulation | [↗](https://standards.ieee.org/ieee/802.11/10548/) |

### Camada de enlace

| Protocolo | Porta／identificador | Especificação oficial |
|---|---|---|
| [Ethernet](https://standards.ieee.org/ieee/802.3/10422/) | — | [↗](https://standards.ieee.org/ieee/802.3/10422/) |
| [Wi-Fi](https://standards.ieee.org/ieee/802.11/10548/) | — | [↗](https://standards.ieee.org/ieee/802.11/10548/) |
| [ARP](https://www.rfc-editor.org/rfc/rfc826) | — | [↗](https://www.rfc-editor.org/rfc/rfc826) |

### Camada de rede

| Protocolo | Porta／identificador | Especificação oficial |
|---|---|---|
| [IPv4](https://www.rfc-editor.org/rfc/rfc791) | — | [↗](https://www.rfc-editor.org/rfc/rfc791) |
| [IPv6](https://www.rfc-editor.org/rfc/rfc8200) | — | [↗](https://www.rfc-editor.org/rfc/rfc8200) |
| [ICMP](https://www.rfc-editor.org/rfc/rfc792) | — | [↗](https://www.rfc-editor.org/rfc/rfc792) |
| [OSPF](https://www.rfc-editor.org/rfc/rfc2328) | — | [↗](https://www.rfc-editor.org/rfc/rfc2328) |

### Camada de transporte

| Protocolo | Porta／identificador | Especificação oficial |
|---|---|---|
| [TCP](https://www.rfc-editor.org/rfc/rfc9293) | — | [↗](https://www.rfc-editor.org/rfc/rfc9293) |
| [UDP](https://www.rfc-editor.org/rfc/rfc768) | — | [↗](https://www.rfc-editor.org/rfc/rfc768) |
| [QUIC](https://www.rfc-editor.org/rfc/rfc9000) | — | [↗](https://www.rfc-editor.org/rfc/rfc9000) |

### Camada de sessão

| Protocolo | Porta／identificador | Especificação oficial |
|---|---|---|
| [SIP](https://www.rfc-editor.org/rfc/rfc3261) | 5060/5061 | [↗](https://www.rfc-editor.org/rfc/rfc3261) |
| [WebSocket](https://www.rfc-editor.org/rfc/rfc6455) | 80/443 | [↗](https://www.rfc-editor.org/rfc/rfc6455) |

### Camada de apresentação

| Protocolo | Porta／identificador | Especificação oficial |
|---|---|---|
| [TLS](https://www.rfc-editor.org/rfc/rfc8446) | — | [↗](https://www.rfc-editor.org/rfc/rfc8446) |

### Camada de aplicação

| Protocolo | Porta／identificador | Especificação oficial |
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

## Por camada e finalidade — 14

### Web e APIs

| Protocolo | Porta／identificador | Função principal | Especificação oficial |
|---|---|---|---|
| [HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112) | 80/443 | Web e APIs | [↗](https://www.rfc-editor.org/rfc/rfc9112) |
| [HTTP/2](https://www.rfc-editor.org/rfc/rfc9113) | 443 | Web e APIs | [↗](https://www.rfc-editor.org/rfc/rfc9113) |
| [HTTP/3](https://www.rfc-editor.org/rfc/rfc9114) | UDP 443 | Web e APIs | [↗](https://www.rfc-editor.org/rfc/rfc9114) |
| [WebSocket](https://www.rfc-editor.org/rfc/rfc6455) | 80/443 | Web e APIs | [↗](https://www.rfc-editor.org/rfc/rfc6455) |
| [gRPC](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md) | 443 | Web e APIs | [↗](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md) |

### DNS e descoberta

| Protocolo | Porta／identificador | Função principal | Especificação oficial |
|---|---|---|---|
| [DNS](https://www.rfc-editor.org/rfc/rfc1034) | 53 | DNS e descoberta | [↗](https://www.rfc-editor.org/rfc/rfc1034) |
| [DNSSEC](https://www.rfc-editor.org/rfc/rfc4033) | 53 | DNS e descoberta | [↗](https://www.rfc-editor.org/rfc/rfc4033) |
| [DoH](https://www.rfc-editor.org/rfc/rfc8484) | 443 | DNS e descoberta | [↗](https://www.rfc-editor.org/rfc/rfc8484) |
| [mDNS](https://www.rfc-editor.org/rfc/rfc6762) | UDP 5353 | DNS e descoberta | [↗](https://www.rfc-editor.org/rfc/rfc6762) |
| [DNS-SD](https://www.rfc-editor.org/rfc/rfc6763) | 53/5353 | DNS e descoberta | [↗](https://www.rfc-editor.org/rfc/rfc6763) |

### Roteamento

| Protocolo | Porta／identificador | Função principal | Especificação oficial |
|---|---|---|---|
| [BGP](https://www.rfc-editor.org/rfc/rfc4271) | TCP 179 | Roteamento | [↗](https://www.rfc-editor.org/rfc/rfc4271) |
| [OSPF](https://www.rfc-editor.org/rfc/rfc2328) | IP 89 | Roteamento | [↗](https://www.rfc-editor.org/rfc/rfc2328) |
| [IS-IS](https://www.rfc-editor.org/rfc/rfc1195) | CLNS | Roteamento | [↗](https://www.rfc-editor.org/rfc/rfc1195) |
| [RIP](https://www.rfc-editor.org/rfc/rfc2453) | UDP 520 | Roteamento | [↗](https://www.rfc-editor.org/rfc/rfc2453) |
| [Babel](https://www.rfc-editor.org/rfc/rfc8966) | UDP 6696 | Roteamento | [↗](https://www.rfc-editor.org/rfc/rfc8966) |

### Gerenciamento de rede

| Protocolo | Porta／identificador | Função principal | Especificação oficial |
|---|---|---|---|
| [SNMPv3](https://www.rfc-editor.org/rfc/rfc3411) | UDP 161/162 | Gerenciamento de rede | [↗](https://www.rfc-editor.org/rfc/rfc3411) |
| [NETCONF](https://www.rfc-editor.org/rfc/rfc6241) | TCP 830 | Gerenciamento de rede | [↗](https://www.rfc-editor.org/rfc/rfc6241) |
| [RESTCONF](https://www.rfc-editor.org/rfc/rfc8040) | 443 | Gerenciamento de rede | [↗](https://www.rfc-editor.org/rfc/rfc8040) |
| [Syslog](https://www.rfc-editor.org/rfc/rfc5424) | 514/6514 | Gerenciamento de rede | [↗](https://www.rfc-editor.org/rfc/rfc5424) |
| [NTP](https://www.rfc-editor.org/rfc/rfc5905) | UDP 123 | Gerenciamento de rede | [↗](https://www.rfc-editor.org/rfc/rfc5905) |

### Acesso remoto

| Protocolo | Porta／identificador | Função principal | Especificação oficial |
|---|---|---|---|
| [SSH](https://www.rfc-editor.org/rfc/rfc4251) | TCP 22 | Acesso remoto | [↗](https://www.rfc-editor.org/rfc/rfc4251) |
| [Telnet](https://www.rfc-editor.org/rfc/rfc854) | TCP 23 | Acesso remoto | [↗](https://www.rfc-editor.org/rfc/rfc854) |
| [RDP](https://learn.microsoft.com/openspecs/windows_protocols/ms-rdpbcgr/) | 3389 | Acesso remoto | [↗](https://learn.microsoft.com/openspecs/windows_protocols/ms-rdpbcgr/) |
| [VNC/RFB](https://www.rfc-editor.org/rfc/rfc6143) | TCP 5900 | Acesso remoto | [↗](https://www.rfc-editor.org/rfc/rfc6143) |

### Transferência de arquivos

| Protocolo | Porta／identificador | Função principal | Especificação oficial |
|---|---|---|---|
| [FTP](https://www.rfc-editor.org/rfc/rfc959) | TCP 20/21 | Transferência de arquivos | [↗](https://www.rfc-editor.org/rfc/rfc959) |
| [SFTP](https://datatracker.ietf.org/doc/html/draft-ietf-secsh-filexfer-13) | TCP 22 | Transferência de arquivos | [↗](https://datatracker.ietf.org/doc/html/draft-ietf-secsh-filexfer-13) |
| [TFTP](https://www.rfc-editor.org/rfc/rfc1350) | UDP 69 | Transferência de arquivos | [↗](https://www.rfc-editor.org/rfc/rfc1350) |
| [NFSv4.1](https://www.rfc-editor.org/rfc/rfc8881) | TCP 2049 | Transferência de arquivos | [↗](https://www.rfc-editor.org/rfc/rfc8881) |
| [SMB 3](https://learn.microsoft.com/openspecs/windows_protocols/ms-smb2/) | TCP 445 | Transferência de arquivos | [↗](https://learn.microsoft.com/openspecs/windows_protocols/ms-smb2/) |

### E-mail

| Protocolo | Porta／identificador | Função principal | Especificação oficial |
|---|---|---|---|
| [SMTP](https://www.rfc-editor.org/rfc/rfc5321) | 25/465/587 | E-mail | [↗](https://www.rfc-editor.org/rfc/rfc5321) |
| [IMAP4rev2](https://www.rfc-editor.org/rfc/rfc9051) | 143/993 | E-mail | [↗](https://www.rfc-editor.org/rfc/rfc9051) |
| [POP3](https://www.rfc-editor.org/rfc/rfc1939) | 110/995 | E-mail | [↗](https://www.rfc-editor.org/rfc/rfc1939) |
| [MIME](https://www.rfc-editor.org/rfc/rfc2045) | message format | E-mail | [↗](https://www.rfc-editor.org/rfc/rfc2045) |
| [JMAP](https://www.rfc-editor.org/rfc/rfc8620) | HTTPS | E-mail | [↗](https://www.rfc-editor.org/rfc/rfc8620) |

### Identidade

| Protocolo | Porta／identificador | Função principal | Especificação oficial |
|---|---|---|---|
| [Kerberos V5](https://www.rfc-editor.org/rfc/rfc4120) | 88 | Identidade | [↗](https://www.rfc-editor.org/rfc/rfc4120) |
| [LDAP](https://www.rfc-editor.org/rfc/rfc4511) | 389/636 | Identidade | [↗](https://www.rfc-editor.org/rfc/rfc4511) |
| [RADIUS](https://www.rfc-editor.org/rfc/rfc2865) | 1812/1813 | Identidade | [↗](https://www.rfc-editor.org/rfc/rfc2865) |
| [TACACS+](https://www.rfc-editor.org/rfc/rfc8907) | TCP 49 | Identidade | [↗](https://www.rfc-editor.org/rfc/rfc8907) |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | HTTPS | Identidade | [↗](https://openid.net/specs/openid-connect-core-1_0.html) |

### Criptografia e VPN

| Protocolo | Porta／identificador | Função principal | Especificação oficial |
|---|---|---|---|
| [TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) | varies | Criptografia e VPN | [↗](https://www.rfc-editor.org/rfc/rfc8446) |
| [IPsec/IKEv2](https://www.rfc-editor.org/rfc/rfc4301) | IP 50/51 | Criptografia e VPN | [↗](https://www.rfc-editor.org/rfc/rfc4301) |
| [WireGuard](https://www.wireguard.com/protocol/) | UDP | Criptografia e VPN | [↗](https://www.wireguard.com/protocol/) |
| [OpenVPN](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/) | 1194 common | Criptografia e VPN | [↗](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/) |
| [MACsec](https://standards.ieee.org/ieee/802.1AE/7427/) | Ethernet | Criptografia e VPN | [↗](https://standards.ieee.org/ieee/802.1AE/7427/) |

### Mídia em tempo real

| Protocolo | Porta／identificador | Função principal | Especificação oficial |
|---|---|---|---|
| [SIP](https://www.rfc-editor.org/rfc/rfc3261) | 5060/5061 | Mídia em tempo real | [↗](https://www.rfc-editor.org/rfc/rfc3261) |
| [SDP](https://www.rfc-editor.org/rfc/rfc8866) | payload | Mídia em tempo real | [↗](https://www.rfc-editor.org/rfc/rfc8866) |
| [RTP/RTCP](https://www.rfc-editor.org/rfc/rfc3550) | dynamic | Mídia em tempo real | [↗](https://www.rfc-editor.org/rfc/rfc3550) |
| [SRTP](https://www.rfc-editor.org/rfc/rfc3711) | dynamic | Mídia em tempo real | [↗](https://www.rfc-editor.org/rfc/rfc3711) |
| [WebRTC](https://www.w3.org/TR/webrtc/) | dynamic | Mídia em tempo real | [↗](https://www.w3.org/TR/webrtc/) |

### Mensageria

| Protocolo | Porta／identificador | Função principal | Especificação oficial |
|---|---|---|---|
| [MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) | 1883/8883 | Mensageria | [↗](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) |
| [AMQP 1.0](https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html) | 5672/5671 | Mensageria | [↗](https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html) |
| [STOMP 1.2](https://stomp.github.io/stomp-specification-1.2.html) | 61613 common | Mensageria | [↗](https://stomp.github.io/stomp-specification-1.2.html) |
| [NATS](https://docs.nats.io/reference/reference-protocols/nats-protocol) | 4222 common | Mensageria | [↗](https://docs.nats.io/reference/reference-protocols/nats-protocol) |
| [DDS](https://www.omg.org/spec/DDS/) | varies | Mensageria | [↗](https://www.omg.org/spec/DDS/) |

### IoT e proximidade

| Protocolo | Porta／identificador | Função principal | Especificação oficial |
|---|---|---|---|
| [CoAP](https://www.rfc-editor.org/rfc/rfc7252) | 5683/5684 | IoT e proximidade | [↗](https://www.rfc-editor.org/rfc/rfc7252) |
| [Bluetooth LE](https://www.bluetooth.com/specifications/specs/core-specification/) | 2.4 GHz | IoT e proximidade | [↗](https://www.bluetooth.com/specifications/specs/core-specification/) |
| [Zigbee](https://csa-iot.org/all-solutions/zigbee/) | 802.15.4 | IoT e proximidade | [↗](https://csa-iot.org/all-solutions/zigbee/) |
| [Thread](https://www.threadgroup.org/support#specifications) | IPv6 | IoT e proximidade | [↗](https://www.threadgroup.org/support#specifications) |
| [Matter](https://csa-iot.org/all-solutions/matter/) | IP | IoT e proximidade | [↗](https://csa-iot.org/all-solutions/matter/) |

### Nuvem e contêineres

| Protocolo | Porta／identificador | Função principal | Especificação oficial |
|---|---|---|---|
| [VXLAN](https://www.rfc-editor.org/rfc/rfc7348) | UDP 4789 | Nuvem e contêineres | [↗](https://www.rfc-editor.org/rfc/rfc7348) |
| [Geneve](https://www.rfc-editor.org/rfc/rfc8926) | UDP 6081 | Nuvem e contêineres | [↗](https://www.rfc-editor.org/rfc/rfc8926) |
| [BGP EVPN](https://www.rfc-editor.org/rfc/rfc7432) | BGP | Nuvem e contêineres | [↗](https://www.rfc-editor.org/rfc/rfc7432) |
| [CNI](https://www.cni.dev/docs/spec/) | local API | Nuvem e contêineres | [↗](https://www.cni.dev/docs/spec/) |
| [OpenFlow](https://opennetworking.org/sdn-resources/openflow-switch-specification/) | TCP 6653 | Nuvem e contêineres | [↗](https://opennetworking.org/sdn-resources/openflow-switch-specification/) |

### Industrial e automotivo

| Protocolo | Porta／identificador | Função principal | Especificação oficial |
|---|---|---|---|
| [Modbus TCP](https://www.modbus.org/specs.php) | TCP 502 | Industrial e automotivo | [↗](https://www.modbus.org/specs.php) |
| [OPC UA](https://reference.opcfoundation.org/Core/Part1/) | 4840 common | Industrial e automotivo | [↗](https://reference.opcfoundation.org/Core/Part1/) |
| [PROFINET](https://www.profibus.com/technology/profinet) | Ethernet | Industrial e automotivo | [↗](https://www.profibus.com/technology/profinet) |
| [EtherCAT](https://www.ethercat.org/en/technology.html) | Ethernet | Industrial e automotivo | [↗](https://www.ethercat.org/en/technology.html) |
| [CAN](https://www.iso.org/standard/63648.html) | message ID | Industrial e automotivo | [↗](https://www.iso.org/standard/63648.html) |

> Versão comunitária. Nomes, padrões e números seguem a fonte normativa em inglês.

[English details](../en/taxonomy.md) · [中文详表](../zh-CN/taxonomy.md)
