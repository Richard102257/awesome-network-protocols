# حسب الطبقة والغرض

[← تصفح](README.md)

> نسخة مجتمعية. تعتمد الأسماء والمعايير والأرقام على المصدر الإنجليزي المعياري.

## OSI — حسب الطبقة والغرض

### الطبقة الفيزيائية

| البروتوكول | المنفذ／المعرّف | المواصفة الرسمية |
|---|---|---|
| [Ethernet PHY](https://standards.ieee.org/ieee/802.3/10422/) | media/signals | [↗](https://standards.ieee.org/ieee/802.3/10422/) |
| [Wi-Fi PHY](https://standards.ieee.org/ieee/802.11/10548/) | radio/modulation | [↗](https://standards.ieee.org/ieee/802.11/10548/) |

### طبقة ربط البيانات

| البروتوكول | المنفذ／المعرّف | المواصفة الرسمية |
|---|---|---|
| [Ethernet](https://standards.ieee.org/ieee/802.3/10422/) | — | [↗](https://standards.ieee.org/ieee/802.3/10422/) |
| [Wi-Fi](https://standards.ieee.org/ieee/802.11/10548/) | — | [↗](https://standards.ieee.org/ieee/802.11/10548/) |
| [ARP](https://www.rfc-editor.org/rfc/rfc826) | — | [↗](https://www.rfc-editor.org/rfc/rfc826) |

### طبقة الشبكة

| البروتوكول | المنفذ／المعرّف | المواصفة الرسمية |
|---|---|---|
| [IPv4](https://www.rfc-editor.org/rfc/rfc791) | — | [↗](https://www.rfc-editor.org/rfc/rfc791) |
| [IPv6](https://www.rfc-editor.org/rfc/rfc8200) | — | [↗](https://www.rfc-editor.org/rfc/rfc8200) |
| [ICMP](https://www.rfc-editor.org/rfc/rfc792) | — | [↗](https://www.rfc-editor.org/rfc/rfc792) |
| [OSPF](https://www.rfc-editor.org/rfc/rfc2328) | — | [↗](https://www.rfc-editor.org/rfc/rfc2328) |

### طبقة النقل

| البروتوكول | المنفذ／المعرّف | المواصفة الرسمية |
|---|---|---|
| [TCP](https://www.rfc-editor.org/rfc/rfc9293) | — | [↗](https://www.rfc-editor.org/rfc/rfc9293) |
| [UDP](https://www.rfc-editor.org/rfc/rfc768) | — | [↗](https://www.rfc-editor.org/rfc/rfc768) |
| [QUIC](https://www.rfc-editor.org/rfc/rfc9000) | — | [↗](https://www.rfc-editor.org/rfc/rfc9000) |

### طبقة الجلسة

| البروتوكول | المنفذ／المعرّف | المواصفة الرسمية |
|---|---|---|
| [SIP](https://www.rfc-editor.org/rfc/rfc3261) | 5060/5061 | [↗](https://www.rfc-editor.org/rfc/rfc3261) |
| [WebSocket](https://www.rfc-editor.org/rfc/rfc6455) | 80/443 | [↗](https://www.rfc-editor.org/rfc/rfc6455) |

### طبقة العرض

| البروتوكول | المنفذ／المعرّف | المواصفة الرسمية |
|---|---|---|
| [TLS](https://www.rfc-editor.org/rfc/rfc8446) | — | [↗](https://www.rfc-editor.org/rfc/rfc8446) |

### طبقة التطبيق

| البروتوكول | المنفذ／المعرّف | المواصفة الرسمية |
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

## حسب الطبقة والغرض — 14

### الويب وواجهات API

| البروتوكول | المنفذ／المعرّف | الدور الأساسي | المواصفة الرسمية |
|---|---|---|---|
| [HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112) | 80/443 | الويب وواجهات API | [↗](https://www.rfc-editor.org/rfc/rfc9112) |
| [HTTP/2](https://www.rfc-editor.org/rfc/rfc9113) | 443 | الويب وواجهات API | [↗](https://www.rfc-editor.org/rfc/rfc9113) |
| [HTTP/3](https://www.rfc-editor.org/rfc/rfc9114) | UDP 443 | الويب وواجهات API | [↗](https://www.rfc-editor.org/rfc/rfc9114) |
| [WebSocket](https://www.rfc-editor.org/rfc/rfc6455) | 80/443 | الويب وواجهات API | [↗](https://www.rfc-editor.org/rfc/rfc6455) |
| [gRPC](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md) | 443 | الويب وواجهات API | [↗](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md) |

### DNS واكتشاف الخدمات

| البروتوكول | المنفذ／المعرّف | الدور الأساسي | المواصفة الرسمية |
|---|---|---|---|
| [DNS](https://www.rfc-editor.org/rfc/rfc1034) | 53 | DNS واكتشاف الخدمات | [↗](https://www.rfc-editor.org/rfc/rfc1034) |
| [DNSSEC](https://www.rfc-editor.org/rfc/rfc4033) | 53 | DNS واكتشاف الخدمات | [↗](https://www.rfc-editor.org/rfc/rfc4033) |
| [DoH](https://www.rfc-editor.org/rfc/rfc8484) | 443 | DNS واكتشاف الخدمات | [↗](https://www.rfc-editor.org/rfc/rfc8484) |
| [mDNS](https://www.rfc-editor.org/rfc/rfc6762) | UDP 5353 | DNS واكتشاف الخدمات | [↗](https://www.rfc-editor.org/rfc/rfc6762) |
| [DNS-SD](https://www.rfc-editor.org/rfc/rfc6763) | 53/5353 | DNS واكتشاف الخدمات | [↗](https://www.rfc-editor.org/rfc/rfc6763) |

### التوجيه

| البروتوكول | المنفذ／المعرّف | الدور الأساسي | المواصفة الرسمية |
|---|---|---|---|
| [BGP](https://www.rfc-editor.org/rfc/rfc4271) | TCP 179 | التوجيه | [↗](https://www.rfc-editor.org/rfc/rfc4271) |
| [OSPF](https://www.rfc-editor.org/rfc/rfc2328) | IP 89 | التوجيه | [↗](https://www.rfc-editor.org/rfc/rfc2328) |
| [IS-IS](https://www.rfc-editor.org/rfc/rfc1195) | CLNS | التوجيه | [↗](https://www.rfc-editor.org/rfc/rfc1195) |
| [RIP](https://www.rfc-editor.org/rfc/rfc2453) | UDP 520 | التوجيه | [↗](https://www.rfc-editor.org/rfc/rfc2453) |
| [Babel](https://www.rfc-editor.org/rfc/rfc8966) | UDP 6696 | التوجيه | [↗](https://www.rfc-editor.org/rfc/rfc8966) |

### إدارة الشبكة

| البروتوكول | المنفذ／المعرّف | الدور الأساسي | المواصفة الرسمية |
|---|---|---|---|
| [SNMPv3](https://www.rfc-editor.org/rfc/rfc3411) | UDP 161/162 | إدارة الشبكة | [↗](https://www.rfc-editor.org/rfc/rfc3411) |
| [NETCONF](https://www.rfc-editor.org/rfc/rfc6241) | TCP 830 | إدارة الشبكة | [↗](https://www.rfc-editor.org/rfc/rfc6241) |
| [RESTCONF](https://www.rfc-editor.org/rfc/rfc8040) | 443 | إدارة الشبكة | [↗](https://www.rfc-editor.org/rfc/rfc8040) |
| [Syslog](https://www.rfc-editor.org/rfc/rfc5424) | 514/6514 | إدارة الشبكة | [↗](https://www.rfc-editor.org/rfc/rfc5424) |
| [NTP](https://www.rfc-editor.org/rfc/rfc5905) | UDP 123 | إدارة الشبكة | [↗](https://www.rfc-editor.org/rfc/rfc5905) |

### الوصول البعيد

| البروتوكول | المنفذ／المعرّف | الدور الأساسي | المواصفة الرسمية |
|---|---|---|---|
| [SSH](https://www.rfc-editor.org/rfc/rfc4251) | TCP 22 | الوصول البعيد | [↗](https://www.rfc-editor.org/rfc/rfc4251) |
| [Telnet](https://www.rfc-editor.org/rfc/rfc854) | TCP 23 | الوصول البعيد | [↗](https://www.rfc-editor.org/rfc/rfc854) |
| [RDP](https://learn.microsoft.com/openspecs/windows_protocols/ms-rdpbcgr/) | 3389 | الوصول البعيد | [↗](https://learn.microsoft.com/openspecs/windows_protocols/ms-rdpbcgr/) |
| [VNC/RFB](https://www.rfc-editor.org/rfc/rfc6143) | TCP 5900 | الوصول البعيد | [↗](https://www.rfc-editor.org/rfc/rfc6143) |

### نقل الملفات

| البروتوكول | المنفذ／المعرّف | الدور الأساسي | المواصفة الرسمية |
|---|---|---|---|
| [FTP](https://www.rfc-editor.org/rfc/rfc959) | TCP 20/21 | نقل الملفات | [↗](https://www.rfc-editor.org/rfc/rfc959) |
| [SFTP](https://datatracker.ietf.org/doc/html/draft-ietf-secsh-filexfer-13) | TCP 22 | نقل الملفات | [↗](https://datatracker.ietf.org/doc/html/draft-ietf-secsh-filexfer-13) |
| [TFTP](https://www.rfc-editor.org/rfc/rfc1350) | UDP 69 | نقل الملفات | [↗](https://www.rfc-editor.org/rfc/rfc1350) |
| [NFSv4.1](https://www.rfc-editor.org/rfc/rfc8881) | TCP 2049 | نقل الملفات | [↗](https://www.rfc-editor.org/rfc/rfc8881) |
| [SMB 3](https://learn.microsoft.com/openspecs/windows_protocols/ms-smb2/) | TCP 445 | نقل الملفات | [↗](https://learn.microsoft.com/openspecs/windows_protocols/ms-smb2/) |

### البريد

| البروتوكول | المنفذ／المعرّف | الدور الأساسي | المواصفة الرسمية |
|---|---|---|---|
| [SMTP](https://www.rfc-editor.org/rfc/rfc5321) | 25/465/587 | البريد | [↗](https://www.rfc-editor.org/rfc/rfc5321) |
| [IMAP4rev2](https://www.rfc-editor.org/rfc/rfc9051) | 143/993 | البريد | [↗](https://www.rfc-editor.org/rfc/rfc9051) |
| [POP3](https://www.rfc-editor.org/rfc/rfc1939) | 110/995 | البريد | [↗](https://www.rfc-editor.org/rfc/rfc1939) |
| [MIME](https://www.rfc-editor.org/rfc/rfc2045) | message format | البريد | [↗](https://www.rfc-editor.org/rfc/rfc2045) |
| [JMAP](https://www.rfc-editor.org/rfc/rfc8620) | HTTPS | البريد | [↗](https://www.rfc-editor.org/rfc/rfc8620) |

### الهوية

| البروتوكول | المنفذ／المعرّف | الدور الأساسي | المواصفة الرسمية |
|---|---|---|---|
| [Kerberos V5](https://www.rfc-editor.org/rfc/rfc4120) | 88 | الهوية | [↗](https://www.rfc-editor.org/rfc/rfc4120) |
| [LDAP](https://www.rfc-editor.org/rfc/rfc4511) | 389/636 | الهوية | [↗](https://www.rfc-editor.org/rfc/rfc4511) |
| [RADIUS](https://www.rfc-editor.org/rfc/rfc2865) | 1812/1813 | الهوية | [↗](https://www.rfc-editor.org/rfc/rfc2865) |
| [TACACS+](https://www.rfc-editor.org/rfc/rfc8907) | TCP 49 | الهوية | [↗](https://www.rfc-editor.org/rfc/rfc8907) |
| [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) | HTTPS | الهوية | [↗](https://openid.net/specs/openid-connect-core-1_0.html) |

### التشفير وVPN

| البروتوكول | المنفذ／المعرّف | الدور الأساسي | المواصفة الرسمية |
|---|---|---|---|
| [TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) | varies | التشفير وVPN | [↗](https://www.rfc-editor.org/rfc/rfc8446) |
| [IPsec/IKEv2](https://www.rfc-editor.org/rfc/rfc4301) | IP 50/51 | التشفير وVPN | [↗](https://www.rfc-editor.org/rfc/rfc4301) |
| [WireGuard](https://www.wireguard.com/protocol/) | UDP | التشفير وVPN | [↗](https://www.wireguard.com/protocol/) |
| [OpenVPN](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/) | 1194 common | التشفير وVPN | [↗](https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/) |
| [MACsec](https://standards.ieee.org/ieee/802.1AE/7427/) | Ethernet | التشفير وVPN | [↗](https://standards.ieee.org/ieee/802.1AE/7427/) |

### الوسائط الفورية

| البروتوكول | المنفذ／المعرّف | الدور الأساسي | المواصفة الرسمية |
|---|---|---|---|
| [SIP](https://www.rfc-editor.org/rfc/rfc3261) | 5060/5061 | الوسائط الفورية | [↗](https://www.rfc-editor.org/rfc/rfc3261) |
| [SDP](https://www.rfc-editor.org/rfc/rfc8866) | payload | الوسائط الفورية | [↗](https://www.rfc-editor.org/rfc/rfc8866) |
| [RTP/RTCP](https://www.rfc-editor.org/rfc/rfc3550) | dynamic | الوسائط الفورية | [↗](https://www.rfc-editor.org/rfc/rfc3550) |
| [SRTP](https://www.rfc-editor.org/rfc/rfc3711) | dynamic | الوسائط الفورية | [↗](https://www.rfc-editor.org/rfc/rfc3711) |
| [WebRTC](https://www.w3.org/TR/webrtc/) | dynamic | الوسائط الفورية | [↗](https://www.w3.org/TR/webrtc/) |

### المراسلة

| البروتوكول | المنفذ／المعرّف | الدور الأساسي | المواصفة الرسمية |
|---|---|---|---|
| [MQTT 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) | 1883/8883 | المراسلة | [↗](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html) |
| [AMQP 1.0](https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html) | 5672/5671 | المراسلة | [↗](https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html) |
| [STOMP 1.2](https://stomp.github.io/stomp-specification-1.2.html) | 61613 common | المراسلة | [↗](https://stomp.github.io/stomp-specification-1.2.html) |
| [NATS](https://docs.nats.io/reference/reference-protocols/nats-protocol) | 4222 common | المراسلة | [↗](https://docs.nats.io/reference/reference-protocols/nats-protocol) |
| [DDS](https://www.omg.org/spec/DDS/) | varies | المراسلة | [↗](https://www.omg.org/spec/DDS/) |

### إنترنت الأشياء والاتصال القريب

| البروتوكول | المنفذ／المعرّف | الدور الأساسي | المواصفة الرسمية |
|---|---|---|---|
| [CoAP](https://www.rfc-editor.org/rfc/rfc7252) | 5683/5684 | إنترنت الأشياء والاتصال القريب | [↗](https://www.rfc-editor.org/rfc/rfc7252) |
| [Bluetooth LE](https://www.bluetooth.com/specifications/specs/core-specification/) | 2.4 GHz | إنترنت الأشياء والاتصال القريب | [↗](https://www.bluetooth.com/specifications/specs/core-specification/) |
| [Zigbee](https://csa-iot.org/all-solutions/zigbee/) | 802.15.4 | إنترنت الأشياء والاتصال القريب | [↗](https://csa-iot.org/all-solutions/zigbee/) |
| [Thread](https://www.threadgroup.org/support#specifications) | IPv6 | إنترنت الأشياء والاتصال القريب | [↗](https://www.threadgroup.org/support#specifications) |
| [Matter](https://csa-iot.org/all-solutions/matter/) | IP | إنترنت الأشياء والاتصال القريب | [↗](https://csa-iot.org/all-solutions/matter/) |

### السحابة والحاويات

| البروتوكول | المنفذ／المعرّف | الدور الأساسي | المواصفة الرسمية |
|---|---|---|---|
| [VXLAN](https://www.rfc-editor.org/rfc/rfc7348) | UDP 4789 | السحابة والحاويات | [↗](https://www.rfc-editor.org/rfc/rfc7348) |
| [Geneve](https://www.rfc-editor.org/rfc/rfc8926) | UDP 6081 | السحابة والحاويات | [↗](https://www.rfc-editor.org/rfc/rfc8926) |
| [BGP EVPN](https://www.rfc-editor.org/rfc/rfc7432) | BGP | السحابة والحاويات | [↗](https://www.rfc-editor.org/rfc/rfc7432) |
| [CNI](https://www.cni.dev/docs/spec/) | local API | السحابة والحاويات | [↗](https://www.cni.dev/docs/spec/) |
| [OpenFlow](https://opennetworking.org/sdn-resources/openflow-switch-specification/) | TCP 6653 | السحابة والحاويات | [↗](https://opennetworking.org/sdn-resources/openflow-switch-specification/) |

### الصناعة والسيارات

| البروتوكول | المنفذ／المعرّف | الدور الأساسي | المواصفة الرسمية |
|---|---|---|---|
| [Modbus TCP](https://www.modbus.org/specs.php) | TCP 502 | الصناعة والسيارات | [↗](https://www.modbus.org/specs.php) |
| [OPC UA](https://reference.opcfoundation.org/Core/Part1/) | 4840 common | الصناعة والسيارات | [↗](https://reference.opcfoundation.org/Core/Part1/) |
| [PROFINET](https://www.profibus.com/technology/profinet) | Ethernet | الصناعة والسيارات | [↗](https://www.profibus.com/technology/profinet) |
| [EtherCAT](https://www.ethercat.org/en/technology.html) | Ethernet | الصناعة والسيارات | [↗](https://www.ethercat.org/en/technology.html) |
| [CAN](https://www.iso.org/standard/63648.html) | message ID | الصناعة والسيارات | [↗](https://www.iso.org/standard/63648.html) |

> نسخة مجتمعية. تعتمد الأسماء والمعايير والأرقام على المصدر الإنجليزي المعياري.

[English details](../en/taxonomy.md) · [中文详表](../zh-CN/taxonomy.md)
