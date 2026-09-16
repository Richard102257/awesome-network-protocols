# Awesome Network Protocols

> A curated, multilingual map of network protocols, standards, tools, and teaching resources.

[English](README.md) · [简体中文](docs/zh-CN/README.md) · [繁體中文](docs/zh-TW/README.md) · [日本語](docs/ja/README.md) · [한국어](docs/ko/README.md) · [Español](docs/es/README.md) · [Português](docs/pt-BR/README.md) · [Français](docs/fr/README.md) · [Deutsch](docs/de/README.md) · [Русский](docs/ru/README.md) · [العربية](docs/ar/README.md)

## What this repository is

This project organizes network protocols by layer, purpose, and industry. Every entry uses the same evidence-based format: purpose, principle, identifiers, standards, security notes, tools, and learning resources.

It aims for useful coverage rather than claiming to contain every protocol ever created.

## Browse

- [Detailed taxonomy: by layer and purpose](docs/en/taxonomy.md)
- [Protocol catalog](docs/en/catalog.md)
- [Learning paths](docs/en/learning-paths.md)
- [Protocol entry specification](docs/en/protocol-entry.md)
- [Contributing](CONTRIBUTING.md)
- [Translation guide](TRANSLATING.md)

## Coverage

| Domain | Examples |
|---|---|
| Web and APIs | HTTP, HTTPS, WebSocket, QUIC |
| Naming and discovery | DNS, DHCP, mDNS, DNS-SD, ARP |
| Transport and addressing | TCP, UDP, SCTP, IPv4, IPv6, ICMP |
| Routing | BGP, OSPF, RIP, IS-IS |
| Local networks | Ethernet, Wi-Fi, VLAN, STP, LLDP |
| Security and identity | TLS, IPsec, SSH, Kerberos, WireGuard |
| Messaging and media | MQTT, CoAP, SIP, RTP, RTCP |
| File and email | FTP, SFTP, SMB, NFS, SMTP, IMAP, POP3 |
| Industrial and device | CAN, Modbus TCP, Zigbee, Bluetooth LE |

## Repository structure

- data/protocols.json — canonical language-neutral protocol index
- docs/en/ — English documentation
- docs/zh-CN/ — Simplified Chinese documentation
- schemas/ — machine-readable data rules
- scripts/validate.py — local and automated validation

## Contributing a protocol

1. Add or update its record in [data/protocols.json](data/protocols.json).
2. Use stable protocol IDs and official standards as primary sources.
3. Add both English and Chinese names and summaries when possible.
4. Run: python3 scripts/validate.py
5. Open a pull request using the supplied template.

## Quality principles

- Prefer RFCs and standards-body documents over secondary summaries.
- Separate protocol facts from implementation advice.
- Mark obsolete, experimental, and proprietary protocols clearly.
- Never describe transport encryption as complete application security.
- Keep translations aligned by stable IDs instead of line numbers.
- Use accessible diagrams with text alternatives.

## License

Documentation and structured data use [CC BY 4.0](LICENSE). Validation code uses the MIT terms included in the same file.
