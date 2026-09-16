# По уровням и назначению

[← Обзор](README.md)

> Версия сообщества. Названия, стандарты и числа сверяются с английским нормативным источником.

## OSI — По уровням и назначению

### Физический уровень

| Протокол | Порт／идентификатор | Официальная спецификация |
|---|---|---|
| [Ethernet PHY](https://standards.ieee.org/ieee/802.3/10422/) | media/signals | [↗](https://standards.ieee.org/ieee/802.3/10422/) |
| [Wi-Fi PHY](https://standards.ieee.org/ieee/802.11/10548/) | radio/modulation | [↗](https://standards.ieee.org/ieee/802.11/10548/) |

### Канальный уровень

| Протокол | Порт／идентификатор | Официальная спецификация |
|---|---|---|
| [Ethernet](https://standards.ieee.org/ieee/802.3/10422/) | — | [↗](https://standards.ieee.org/ieee/802.3/10422/) |
| [Wi-Fi](https://standards.ieee.org/ieee/802.11/10548/) | — | [↗](https://standards.ieee.org/ieee/802.11/10548/) |
| [ARP](https://www.rfc-editor.org/rfc/rfc826) | — | [↗](https://www.rfc-editor.org/rfc/rfc826) |

### Сетевой уровень

| Протокол | Порт／идентификатор | Официальная спецификация |
|---|---|---|
| [IPv4](https://www.rfc-editor.org/rfc/rfc791) | — | [↗](https://www.rfc-editor.org/rfc/rfc791) |
| [IPv6](https://www.rfc-editor.org/rfc/rfc8200) | — | [↗](https://www.rfc-editor.org/rfc/rfc8200) |
| [ICMP](https://www.rfc-editor.org/rfc/rfc792) | — | [↗](https://www.rfc-editor.org/rfc/rfc792) |
| [OSPF](https://www.rfc-editor.org/rfc/rfc2328) | — | [↗](https://www.rfc-editor.org/rfc/rfc2328) |

### Транспортный уровень

| Протокол | Порт／идентификатор | Официальная спецификация |
|---|---|---|
| [TCP](https://www.rfc-editor.org/rfc/rfc9293) | — | [↗](https://www.rfc-editor.org/rfc/rfc9293) |
| [UDP](https://www.rfc-editor.org/rfc/rfc768) | — | [↗](https://www.rfc-editor.org/rfc/rfc768) |
| [QUIC](https://www.rfc-editor.org/rfc/rfc9000) | — | [↗](https://www.rfc-editor.org/rfc/rfc9000) |

### Сеансовый уровень

| Протокол | Порт／идентификатор | Официальная спецификация |
|---|---|---|
| [SIP](https://www.rfc-editor.org/rfc/rfc3261) | 5060/5061 | [↗](https://www.rfc-editor.org/rfc/rfc3261) |
| [WebSocket](https://www.rfc-editor.org/rfc/rfc6455) | 80/443 | [↗](https://www.rfc-editor.org/rfc/rfc6455) |

### Уровень представления

| Протокол | Порт／идентификатор | Официальная спецификация |
|---|---|---|
| [TLS](https://www.rfc-editor.org/rfc/rfc8446) | — | [↗](https://www.rfc-editor.org/rfc/rfc8446) |

### Прикладной уровень

| Протокол | Порт／идентификатор | Официальная спецификация |
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

## По уровням и назначению — 14

### Веб и API

| Протокол | Порт／идентификатор | Основная роль | Официальная спецификация |
|---|---|---|---|
| [HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112) | 80/443 | Веб и API | [↗](https://www.rfc-editor.org/rfc/rfc9112) |
| [HTTP/2](https://www.rfc-editor.org/rfc/rfc9113) | 443 | Веб и API | [↗](https://www.rfc-editor.org/rfc/rfc9113) |
| [HTTP/3](https://www.rfc-editor.org/rfc/rfc9114) | UDP 443 | Веб и API | [↗](https://www.rfc-editor.org/rfc/rfc9114) |
| [WebSocket](https://www.rfc-editor.org/rfc/rfc6455) | 80/443 | Веб и API | [↗](https://www.rfc-editor.org/rfc/rfc6455) |
| [gRPC](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md) | 443 | Веб и API | [↗](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md) |

### DNS и обнаружение

| Протокол | Порт／идентификатор | Основная роль | Официальная спецификация |
|---|---|---|---|
| [DNS](https://www.rfc-editor.org/rfc/rfc1034) | 53 | DNS и обнаружение | [↗](https://www.rfc-editor.org/rfc/rfc1034) |
| [DNSSEC](https://www.rfc-editor.org/rfc/rfc4033) | 53 | DNS и обнаружение | [↗](https://www.rfc-editor.org/rfc/rfc4033) |
| [DoH](https://www.rfc-editor.org/rfc/rfc8484) | 443 | DNS и обнаружение | [↗](https://www.rfc-editor.org/rfc/rfc8484) |
| [mDNS](https://www.rfc-editor.org/rfc/rfc6762) | UDP 5353 | DNS и обнаружение | [↗](https://www.rfc-editor.org/rfc/rfc6762) |
| [DNS-SD](https://www.rfc-editor.org/rfc/rfc6763) | 53/5353 | DNS и обнаружение | [↗](https://www.rfc-editor.org/rfc/rfc6763) |

### Маршрутизация

| Протокол | Порт／идентификатор | Основная роль | Официальная спецификация |
|---|---|---|---|
| [BGP](https://www.rfc-editor.org/rfc/rfc4271) | TCP 179 | Маршрутизация | [↗](https://www.rfc-editor.org/rfc/rfc4271) |
| [OSPF](https://www.rfc-editor.org/rfc/rfc2328) | IP 89 | Маршрутизация | [↗](https://www.rfc-editor.org/rfc/rfc2328) |
| [IS-IS](https://www.rfc-editor.org/rfc/rfc1195) | CLNS | Маршрутизация | [↗](https://www.rfc-editor.org/rfc/rfc1195) |
| [RIP](https://www.rfc-editor.org/rfc/rfc2453) | UDP 520 | Маршрутизация | [↗](https://www.rfc-editor.org/rfc/rfc2453) |
| [Babel](https://www.rfc-editor.org/rfc/rfc8966) | UDP 6696 | Маршрутизация | [↗](https://www.rfc-editor.org/rfc/rfc8966) |

### Управление сетью

| Протокол | Порт／идентификатор | Основная роль | Официальная спецификация |
|---|---|---|---|
| [SNMPv3](https://www.rfc-editor.org/rfc/rfc3411) | UDP 161/162 | Управление сетью | [↗](https://www.rfc-editor.org/rfc/rfc3411) |
| [NETCONF](https://www.rfc-editor.org/rfc/rfc6241) | TCP 830 | Управление сетью | [↗](https://www.rfc-editor.org/rfc/rfc6241) |
| [RESTCONF](https://www.rfc-editor.org/rfc/rfc8040) | 443 | Управление сетью | [↗](https://www.rfc-editor.org/rfc/rfc8040) |
| [Syslog](https://www.rfc-editor.org/rfc/rfc5424) | 514/6514 | Управление сетью | [↗](https://www.rfc-editor.org/rfc/rfc5424) |
| [NTP](https://www.rfc-editor.org/rfc/rfc5905) | UDP 123 | Управление сетью | [↗](https://www.rfc-editor.org/rfc/rfc5905) |

### Удалённый доступ

| Протокол | Порт／идентификатор | Основная роль | Официальная спецификация |
|---|---|---|---|
| [SSH](https://www.rfc-editor.org/rfc/rfc4251) | TCP 22 | Удалённый доступ | [↗](https://www.rfc-editor.org/rfc/rfc4251) |
| [Telnet](https://www.rfc-editor.org/rfc/rfc854) | TCP 23 | Удалённый доступ | [↗](https://www.rfc-editor.org/rfc/rfc854) |
| [RDP](https://learn.microsoft.com/openspecs/windows_protocols/ms-rdpbcgr/) | 3389 | Удалённый доступ | [↗](https://learn.microsoft.com/openspecs/windows_protocols/ms-rdpbcgr/) |
| [VNC/RFB](https://www.rfc-editor.org/rfc/rfc6143) | TCP 5900 | Удалённый доступ | [↗](https://www.rfc-editor.org/rfc/rfc6143) |

### Передача файлов

| Протокол | Порт／идентификатор | Основная роль | Официальная спецификация |
|---|---|---|---|
| [FTP](https://www.rfc-editor.org/rfc/rfc959) | TCP 20/21 | Передача файлов | [↗](https://www.rfc-editor.org/rfc/rfc959) |
| [SFTP](https://datatracker.ietf.org/doc/html/draft-ietf-secsh-filexfer-13) | TCP 22 | Передача файлов | [↗](https://datatracker.ietf.org/doc/html/draft-ietf-secsh-filexfer-13) |
| [TFTP](https://www.rfc-editor.org/rfc/rfc1350) | UDP 69 | Передача файлов | [↗](https://www.rfc-editor.org/rfc/rfc1350) |
| [NFSv4.1](https://www.rfc-editor.org/rfc/rfc8881) | TCP 2049 | Передача файлов | [↗](https://www.rfc-editor.org/rfc/rfc8881) |
| [SMB 3](https://learn.microsoft.com/openspecs/windows_protocols/ms-smb2/) | TCP 445 | Передача файлов | [↗](https://learn.microsoft.com/openspecs/windows_protocols/ms-smb2/) |

### Почта

| Протокол | Порт／идентификатор | Основная роль | Официальная спецификация |
|---|---|---|---|
| [SMTP](https://www.rfc-editor.org/rfc/rfc5321) | 25/465/587 | Почта | [↗](https://www.rfc-editor.org/rfc/rfc5321) |
| [IMAP4rev2](https://www.rfc-editor.org/rfc/rfc9051) | 143/993 | Почта | [↗](https://www.rfc-editor.org/rfc/rfc9051) |
| [POP3](https://www.rfc-editor.org/rfc/rfc1939) | 110/995 | Почта | [↗](https://www.rfc-editor.org/rfc/rfc1939) |
| [MIME](https://www.rfc-editor.org/rfc/rfc2045) | message format | Почта | [↗](https://www.rfc-editor.org/rfc/rfc2045) |
| [JMAP](https://www.rfc-editor.org/rfc/rfc8620) | HTTPS | Почта | [↗](https://www.rfc-editor.org/rfc/rfc8620) |

### Идентификация

| Протокол | Порт／идентификатор | Основная роль | Официальная спецификация |
|---|---|---|---|
| [Kerberos V5](https://www.rfc-editor.org/rfc/rfc4120) | 88 | Идентификация | [↗](https://www.rfc-editor.org/rfc/rfc4120) |
| [LDAP](https://www.rfc-editor.org/rfc/rfc4511) | 389/636 | Идентификация | [↗](https://www.rfc-editor.org/rfc/rfc4511) |
| [RADIUS](https://www.rfc-editor.org/rfc/rfc2865) | 1812/1813 | Идентификация | [↗](https://www.rfc-editor.org/rfc/rfc2865) |
| [TACACS+](https://www.rfc-editor.org/rfc/rfc8907) | TCP 49 | Идентификация | [↗](https://www.rfc-editor.org/rfc/rfc8907) |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | HTTPS | Идентификация | [↗](https://openid.net/specs/openid-connect-core-1_0.html) |

### Шифрование и VPN

| Протокол | Порт／идентификатор | Основная роль | Официальная спецификация |
|---|---|---|---|
| [TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) | varies | Шифрование и VPN | [↗](https://www.rfc-editor.org/rfc/rfc8446) |
| [IPsec/IKEv2](https://www.rfc-editor.org/rfc/rfc4301) | IP 50/51 | Шифрование и VPN | [↗](https://www.rfc-editor.org/rfc/rfc4301) |
| [WireGuard](https://www.wireguard.com/protocol/) | UDP | Шифрование и VPN | [↗](https://www.wireguard.com/protocol/) |
| [OpenVPN](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/) | 1194 common | Шифрование и VPN | [↗](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/) |
| [MACsec](https://standards.ieee.org/ieee/802.1AE/7427/) | Ethernet | Шифрование и VPN | [↗](https://standards.ieee.org/ieee/802.1AE/7427/) |

### Медиа реального времени

| Протокол | Порт／идентификатор | Основная роль | Официальная спецификация |
|---|---|---|---|
| [SIP](https://www.rfc-editor.org/rfc/rfc3261) | 5060/5061 | Медиа реального времени | [↗](https://www.rfc-editor.org/rfc/rfc3261) |
| [SDP](https://www.rfc-editor.org/rfc/rfc8866) | payload | Медиа реального времени | [↗](https://www.rfc-editor.org/rfc/rfc8866) |
| [RTP/RTCP](https://www.rfc-editor.org/rfc/rfc3550) | dynamic | Медиа реального времени | [↗](https://www.rfc-editor.org/rfc/rfc3550) |
| [SRTP](https://www.rfc-editor.org/rfc/rfc3711) | dynamic | Медиа реального времени | [↗](https://www.rfc-editor.org/rfc/rfc3711) |
| [WebRTC](https://www.w3.org/TR/webrtc/) | dynamic | Медиа реального времени | [↗](https://www.w3.org/TR/webrtc/) |

### Сообщения

| Протокол | Порт／идентификатор | Основная роль | Официальная спецификация |
|---|---|---|---|
| [MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) | 1883/8883 | Сообщения | [↗](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) |
| [AMQP 1.0](https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html) | 5672/5671 | Сообщения | [↗](https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html) |
| [STOMP 1.2](https://stomp.github.io/stomp-specification-1.2.html) | 61613 common | Сообщения | [↗](https://stomp.github.io/stomp-specification-1.2.html) |
| [NATS](https://docs.nats.io/reference/reference-protocols/nats-protocol) | 4222 common | Сообщения | [↗](https://docs.nats.io/reference/reference-protocols/nats-protocol) |
| [DDS](https://www.omg.org/spec/DDS/) | varies | Сообщения | [↗](https://www.omg.org/spec/DDS/) |

### IoT и ближняя связь

| Протокол | Порт／идентификатор | Основная роль | Официальная спецификация |
|---|---|---|---|
| [CoAP](https://www.rfc-editor.org/rfc/rfc7252) | 5683/5684 | IoT и ближняя связь | [↗](https://www.rfc-editor.org/rfc/rfc7252) |
| [Bluetooth LE](https://www.bluetooth.com/specifications/specs/core-specification/) | 2.4 GHz | IoT и ближняя связь | [↗](https://www.bluetooth.com/specifications/specs/core-specification/) |
| [Zigbee](https://csa-iot.org/all-solutions/zigbee/) | 802.15.4 | IoT и ближняя связь | [↗](https://csa-iot.org/all-solutions/zigbee/) |
| [Thread](https://www.threadgroup.org/support#specifications) | IPv6 | IoT и ближняя связь | [↗](https://www.threadgroup.org/support#specifications) |
| [Matter](https://csa-iot.org/all-solutions/matter/) | IP | IoT и ближняя связь | [↗](https://csa-iot.org/all-solutions/matter/) |

### Облако и контейнеры

| Протокол | Порт／идентификатор | Основная роль | Официальная спецификация |
|---|---|---|---|
| [VXLAN](https://www.rfc-editor.org/rfc/rfc7348) | UDP 4789 | Облако и контейнеры | [↗](https://www.rfc-editor.org/rfc/rfc7348) |
| [Geneve](https://www.rfc-editor.org/rfc/rfc8926) | UDP 6081 | Облако и контейнеры | [↗](https://www.rfc-editor.org/rfc/rfc8926) |
| [BGP EVPN](https://www.rfc-editor.org/rfc/rfc7432) | BGP | Облако и контейнеры | [↗](https://www.rfc-editor.org/rfc/rfc7432) |
| [CNI](https://www.cni.dev/docs/spec/) | local API | Облако и контейнеры | [↗](https://www.cni.dev/docs/spec/) |
| [OpenFlow](https://opennetworking.org/sdn-resources/openflow-switch-specification/) | TCP 6653 | Облако и контейнеры | [↗](https://opennetworking.org/sdn-resources/openflow-switch-specification/) |

### Промышленность и автомобили

| Протокол | Порт／идентификатор | Основная роль | Официальная спецификация |
|---|---|---|---|
| [Modbus TCP](https://www.modbus.org/specs.php) | TCP 502 | Промышленность и автомобили | [↗](https://www.modbus.org/specs.php) |
| [OPC UA](https://reference.opcfoundation.org/Core/Part1/) | 4840 common | Промышленность и автомобили | [↗](https://reference.opcfoundation.org/Core/Part1/) |
| [PROFINET](https://www.profibus.com/technology/profinet) | Ethernet | Промышленность и автомобили | [↗](https://www.profibus.com/technology/profinet) |
| [EtherCAT](https://www.ethercat.org/en/technology.html) | Ethernet | Промышленность и автомобили | [↗](https://www.ethercat.org/en/technology.html) |
| [CAN](https://www.iso.org/standard/63648.html) | message ID | Промышленность и автомобили | [↗](https://www.iso.org/standard/63648.html) |

> Версия сообщества. Названия, стандарты и числа сверяются с английским нормативным источником.

[English details](../en/taxonomy.md) · [中文详表](../zh-CN/taxonomy.md)
