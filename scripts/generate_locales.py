#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = json.loads((ROOT / "data/protocols.json").read_text(encoding="utf-8"))["protocols"]
L = json.loads((ROOT / "data/languages.json").read_text(encoding="utf-8"))["languages"]
NL = chr(10)

# title, intro, browse, catalog, taxonomy, paths, specification, contribution, notice
TEXT = {
"en": ["Awesome Network Protocols","A curated multilingual index of network protocols, standards, tools, and teaching resources.","Browse","Protocol catalog","By layer and purpose","Learning paths","Entry specification","Contribute","English is the canonical editorial source for names, standards, identifiers, and technical meaning."],
"zh-TW": ["網路協定資源大全","經過整理的網路協定、標準、工具與教學資源多語言索引。","瀏覽","協定目錄","依網路層與用途分類","學習路線","條目規範","參與貢獻","此語言由社群維護；名稱、標準與數字以英文規範來源為準。"],
"ja": ["ネットワークプロトコル大全","ネットワークプロトコル、標準、ツール、教材を整理した多言語インデックスです。","閲覧","プロトコル一覧","レイヤー・用途別分類","学習パス","項目仕様","貢献する","この言語版はコミュニティ管理です。名称、規格、数値は英語の正式仕様を基準とします。"],
"ko": ["네트워크 프로토콜 모음","네트워크 프로토콜, 표준, 도구와 교육 자료를 정리한 다국어 색인입니다.","둘러보기","프로토콜 목록","계층 및 용도별 분류","학습 경로","항목 명세","기여하기","이 언어는 커뮤니티가 관리합니다. 이름, 표준과 수치는 영어 공식 사양을 기준으로 합니다."],
"es": ["Protocolos de red increíbles","Índice multilingüe de protocolos, estándares, herramientas y recursos didácticos de redes.","Explorar","Catálogo de protocolos","Por capa y propósito","Rutas de aprendizaje","Especificación de entradas","Contribuir","Versión comunitaria. Los nombres, estándares y números siguen la fuente normativa inglesa."],
"pt-BR": ["Protocolos de rede incríveis","Índice multilíngue de protocolos, padrões, ferramentas e materiais didáticos de redes.","Explorar","Catálogo de protocolos","Por camada e finalidade","Trilhas de aprendizagem","Especificação de entradas","Contribuir","Versão comunitária. Nomes, padrões e números seguem a fonte normativa em inglês."],
"fr": ["Protocoles réseau remarquables","Index multilingue de protocoles, normes, outils et ressources pédagogiques réseau.","Parcourir","Catalogue des protocoles","Par couche et usage","Parcours d’apprentissage","Spécification des fiches","Contribuer","Version communautaire. Les noms, normes et nombres suivent la source normative anglaise."],
"de": ["Ausgezeichnete Netzwerkprotokolle","Mehrsprachiger Index für Netzwerkprotokolle, Standards, Werkzeuge und Lehrmaterialien.","Durchsuchen","Protokollkatalog","Nach Schicht und Zweck","Lernpfade","Eintragsspezifikation","Mitwirken","Community-Version. Namen, Standards und Zahlen folgen der englischen Normquelle."],
"ru": ["Каталог сетевых протоколов","Многоязычный каталог сетевых протоколов, стандартов, инструментов и учебных материалов.","Обзор","Каталог протоколов","По уровням и назначению","Учебные маршруты","Спецификация записи","Участие","Версия сообщества. Названия, стандарты и числа сверяются с английским нормативным источником."],
"ar": ["بروتوكولات الشبكات الرائعة","فهرس متعدد اللغات لبروتوكولات الشبكات والمعايير والأدوات والمواد التعليمية.","تصفح","فهرس البروتوكولات","حسب الطبقة والغرض","مسارات التعلم","مواصفات الإدخال","المساهمة","نسخة مجتمعية. تعتمد الأسماء والمعايير والأرقام على المصدر الإنجليزي المعياري."]
}

LAYERS = ["Physical", "Data Link", "Network", "Transport", "Session", "Presentation", "Application"]
PURPOSES = ["Web & APIs", "DNS & discovery", "Routing", "Network management", "Remote access", "File transfer", "Email", "Identity", "Encryption & VPN", "Real-time media", "Messaging", "IoT & proximity", "Cloud native & containers", "Industrial & automotive"]

LOCAL_NAMES = {
"en": ["Physical|Data Link|Network|Transport|Session|Presentation|Application", "Web and APIs|DNS and service discovery|Routing|Network management|Remote access|File transfer|Email|Identity and authentication|Encryption and VPN|Real-time audio and video|Message queues|IoT and proximity|Cloud native and containers|Industrial and automotive", "Protocol|Port / identifier|Core role|Official specification"],
"zh-TW": ["實體層|資料連結層|網路層|傳輸層|會議層|表達層|應用層", "Web 與 API|DNS 與服務探索|路由|網路管理|遠端存取|檔案傳輸|電子郵件|身分驗證|加密與 VPN|即時影音|訊息佇列|IoT 與短距離通訊|雲原生與容器網路|工業與汽車協定", "協定|連接埠／識別碼|核心作用|官方規範"],
"ja": ["物理層|データリンク層|ネットワーク層|トランスポート層|セッション層|プレゼンテーション層|アプリケーション層", "Web と API|DNS とサービス検出|ルーティング|ネットワーク管理|リモートアクセス|ファイル転送|メール|認証|暗号化と VPN|リアルタイムメディア|メッセージング|IoT と近距離通信|クラウドとコンテナ|産業・車載", "プロトコル|ポート／識別子|主な役割|公式仕様"],
"ko": ["물리 계층|데이터 링크 계층|네트워크 계층|전송 계층|세션 계층|표현 계층|응용 계층", "웹 및 API|DNS 및 서비스 검색|라우팅|네트워크 관리|원격 접속|파일 전송|이메일|인증|암호화 및 VPN|실시간 미디어|메시징|IoT 및 근거리 통신|클라우드 및 컨테이너|산업 및 자동차", "프로토콜|포트／식별자|핵심 역할|공식 명세"],
"es": ["Capa física|Capa de enlace|Capa de red|Capa de transporte|Capa de sesión|Capa de presentación|Capa de aplicación", "Web y API|DNS y descubrimiento|Enrutamiento|Gestión de red|Acceso remoto|Transferencia de archivos|Correo|Identidad|Cifrado y VPN|Medios en tiempo real|Mensajería|IoT y proximidad|Nube y contenedores|Industrial y automoción", "Protocolo|Puerto／identificador|Función principal|Especificación oficial"],
"pt-BR": ["Camada física|Camada de enlace|Camada de rede|Camada de transporte|Camada de sessão|Camada de apresentação|Camada de aplicação", "Web e APIs|DNS e descoberta|Roteamento|Gerenciamento de rede|Acesso remoto|Transferência de arquivos|E-mail|Identidade|Criptografia e VPN|Mídia em tempo real|Mensageria|IoT e proximidade|Nuvem e contêineres|Industrial e automotivo", "Protocolo|Porta／identificador|Função principal|Especificação oficial"],
"fr": ["Couche physique|Couche liaison|Couche réseau|Couche transport|Couche session|Couche présentation|Couche application", "Web et API|DNS et découverte|Routage|Gestion réseau|Accès distant|Transfert de fichiers|Courriel|Identité|Chiffrement et VPN|Média temps réel|Messagerie|IoT et proximité|Cloud et conteneurs|Industrie et automobile", "Protocole|Port／identifiant|Rôle principal|Spécification officielle"],
"de": ["Bitübertragungsschicht|Sicherungsschicht|Vermittlungsschicht|Transportschicht|Sitzungsschicht|Darstellungsschicht|Anwendungsschicht", "Web und APIs|DNS und Erkennung|Routing|Netzwerkverwaltung|Fernzugriff|Dateiübertragung|E-Mail|Identität|Verschlüsselung und VPN|Echtzeitmedien|Messaging|IoT und Nahbereich|Cloud und Container|Industrie und Fahrzeug", "Protokoll|Port／Kennung|Hauptaufgabe|Offizielle Spezifikation"],
"ru": ["Физический уровень|Канальный уровень|Сетевой уровень|Транспортный уровень|Сеансовый уровень|Уровень представления|Прикладной уровень", "Веб и API|DNS и обнаружение|Маршрутизация|Управление сетью|Удалённый доступ|Передача файлов|Почта|Идентификация|Шифрование и VPN|Медиа реального времени|Сообщения|IoT и ближняя связь|Облако и контейнеры|Промышленность и автомобили", "Протокол|Порт／идентификатор|Основная роль|Официальная спецификация"],
"ar": ["الطبقة الفيزيائية|طبقة ربط البيانات|طبقة الشبكة|طبقة النقل|طبقة الجلسة|طبقة العرض|طبقة التطبيق", "الويب وواجهات API|DNS واكتشاف الخدمات|التوجيه|إدارة الشبكة|الوصول البعيد|نقل الملفات|البريد|الهوية|التشفير وVPN|الوسائط الفورية|المراسلة|إنترنت الأشياء والاتصال القريب|السحابة والحاويات|الصناعة والسيارات", "البروتوكول|المنفذ／المعرّف|الدور الأساسي|المواصفة الرسمية"]
}

# name, official URL, port/identifier, short language-neutral teaching cue
GROUPS = [
[("HTTP/1.1","https://www.rfc-editor.org/rfc/rfc9112","80/443","request-response"),("HTTP/2","https://www.rfc-editor.org/rfc/rfc9113","443","binary multiplexing"),("HTTP/3","https://www.rfc-editor.org/rfc/rfc9114","UDP 443","HTTP over QUIC"),("WebSocket","https://www.rfc-editor.org/rfc/rfc6455","80/443","full-duplex session"),("gRPC","https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md","443","remote procedure calls")],
[("DNS","https://www.rfc-editor.org/rfc/rfc1034","53","hierarchical naming"),("DNSSEC","https://www.rfc-editor.org/rfc/rfc4033","53","signed DNS data"),("DoH","https://www.rfc-editor.org/rfc/rfc8484","443","encrypted DNS"),("mDNS","https://www.rfc-editor.org/rfc/rfc6762","UDP 5353","local multicast naming"),("DNS-SD","https://www.rfc-editor.org/rfc/rfc6763","53/5353","service discovery")],
[("BGP","https://www.rfc-editor.org/rfc/rfc4271","TCP 179","policy path vector"),("OSPF","https://www.rfc-editor.org/rfc/rfc2328","IP 89","link-state routing"),("IS-IS","https://www.rfc-editor.org/rfc/rfc1195","CLNS","link-state routing"),("RIP","https://www.rfc-editor.org/rfc/rfc2453","UDP 520","distance vector"),("Babel","https://www.rfc-editor.org/rfc/rfc8966","UDP 6696","loop-avoiding distance vector")],
[("SNMPv3","https://www.rfc-editor.org/rfc/rfc3411","UDP 161/162","managed objects"),("NETCONF","https://www.rfc-editor.org/rfc/rfc6241","TCP 830","configuration transactions"),("RESTCONF","https://www.rfc-editor.org/rfc/rfc8040","443","YANG over HTTP"),("Syslog","https://www.rfc-editor.org/rfc/rfc5424","514/6514","event messages"),("NTP","https://www.rfc-editor.org/rfc/rfc5905","UDP 123","clock synchronization")],
[("SSH","https://www.rfc-editor.org/rfc/rfc4251","TCP 22","encrypted terminal"),("Telnet","https://www.rfc-editor.org/rfc/rfc854","TCP 23","plaintext terminal"),("RDP","https://learn.microsoft.com/openspecs/windows_protocols/ms-rdpbcgr/","3389","remote desktop"),("VNC/RFB","https://www.rfc-editor.org/rfc/rfc6143","TCP 5900","remote framebuffer")],
[("FTP","https://www.rfc-editor.org/rfc/rfc959","TCP 20/21","separate control and data"),("SFTP","https://datatracker.ietf.org/doc/html/draft-ietf-secsh-filexfer-13","TCP 22","files over SSH"),("TFTP","https://www.rfc-editor.org/rfc/rfc1350","UDP 69","block transfer"),("NFSv4.1","https://www.rfc-editor.org/rfc/rfc8881","TCP 2049","remote filesystem"),("SMB 3","https://learn.microsoft.com/openspecs/windows_protocols/ms-smb2/","TCP 445","stateful file sharing")],
[("SMTP","https://www.rfc-editor.org/rfc/rfc5321","25/465/587","mail relay"),("IMAP4rev2","https://www.rfc-editor.org/rfc/rfc9051","143/993","mailbox sync"),("POP3","https://www.rfc-editor.org/rfc/rfc1939","110/995","mail download"),("MIME","https://www.rfc-editor.org/rfc/rfc2045","message format","media encoding"),("JMAP","https://www.rfc-editor.org/rfc/rfc8620","HTTPS","JSON mail sync")],
[("Kerberos V5","https://www.rfc-editor.org/rfc/rfc4120","88","ticket authentication"),("LDAP","https://www.rfc-editor.org/rfc/rfc4511","389/636","directory access"),("RADIUS","https://www.rfc-editor.org/rfc/rfc2865","1812/1813","AAA"),("TACACS+","https://www.rfc-editor.org/rfc/rfc8907","TCP 49","device administration"),("OpenID Connect","https://openid.net/specs/openid-connect-core-1_0.html","HTTPS","identity claims")],
[("TLS 1.3","https://www.rfc-editor.org/rfc/rfc8446","varies","secure sessions"),("IPsec/IKEv2","https://www.rfc-editor.org/rfc/rfc4301","IP 50/51","IP security"),("WireGuard","https://www.wireguard.com/protocol/","UDP","key-based tunnel"),("OpenVPN","https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/","1194 common","TLS VPN"),("MACsec","https://standards.ieee.org/ieee/802.1AE/7427/","Ethernet","link encryption")],
[("SIP","https://www.rfc-editor.org/rfc/rfc3261","5060/5061","session signaling"),("SDP","https://www.rfc-editor.org/rfc/rfc8866","payload","media description"),("RTP/RTCP","https://www.rfc-editor.org/rfc/rfc3550","dynamic","media and feedback"),("SRTP","https://www.rfc-editor.org/rfc/rfc3711","dynamic","secure media"),("WebRTC","https://www.w3.org/TR/webrtc/","dynamic","browser real-time media")],
[("MQTT 5.0","https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html","1883/8883","topic broker"),("AMQP 1.0","https://docs.oasis-open.org/amqp/core/v1.0/amqp-core-overview-v1.0.html","5672/5671","message links"),("STOMP 1.2","https://stomp.github.io/stomp-specification-1.2.html","61613 common","text messaging"),("NATS","https://docs.nats.io/reference/reference-protocols/nats-protocol","4222 common","subject messaging"),("DDS","https://www.omg.org/spec/DDS/","varies","real-time pub-sub")],
[("CoAP","https://www.rfc-editor.org/rfc/rfc7252","5683/5684","constrained REST"),("Bluetooth LE","https://www.bluetooth.com/specifications/specs/core-specification/","2.4 GHz","GATT proximity"),("Zigbee","https://csa-iot.org/all-solutions/zigbee/","802.15.4","low-power mesh"),("Thread","https://www.threadgroup.org/support#specifications","IPv6","low-power IP mesh"),("Matter","https://csa-iot.org/all-solutions/matter/","IP","smart-home application")],
[("VXLAN","https://www.rfc-editor.org/rfc/rfc7348","UDP 4789","L2 overlay"),("Geneve","https://www.rfc-editor.org/rfc/rfc8926","UDP 6081","extensible overlay"),("BGP EVPN","https://www.rfc-editor.org/rfc/rfc7432","BGP","overlay reachability"),("CNI","https://www.cni.dev/docs/spec/","local API","container networking"),("OpenFlow","https://opennetworking.org/sdn-resources/openflow-switch-specification/","TCP 6653","SDN flow control")],
[("Modbus TCP","https://www.modbus.org/specs.php","TCP 502","register access"),("OPC UA","https://reference.opcfoundation.org/Core/Part1/","4840 common","industrial information model"),("PROFINET","https://www.profibus.com/technology/profinet","Ethernet","real-time control"),("EtherCAT","https://www.ethercat.org/en/technology.html","Ethernet","on-the-fly processing"),("CAN","https://www.iso.org/standard/63648.html","message ID","bus arbitration")]
]

def save(code, name, parts):
    folder = ROOT / "docs" / code
    folder.mkdir(parents=True, exist_ok=True)
    (folder / name).write_text(NL.join(parts).rstrip() + NL, encoding="utf-8")

switch = " · ".join(
    "[{}]({})".format(x["nativeName"], "../../README.md" if x["code"] == "en" else "../{}/README.md".format(x["code"]))
    for x in L
)

for lang in L:
    code = lang["code"]
    if code == "zh-CN":
        continue
    title, intro, browse, catalog, taxonomy, paths, spec, contribute, notice = TEXT[code]
    save(code, "README.md", ["# " + title, "", "> " + intro, "", switch, "", "## " + browse, "", "[{}](catalog.md) · [{}](taxonomy.md) · [{}](learning-paths.md) · [{}](protocol-entry.md)".format(catalog, taxonomy, paths, spec), "", "> " + notice, "", "## " + contribute, "", "[CONTRIBUTING.md](../../CONTRIBUTING.md) · [TRANSLATING.md](../../TRANSLATING.md)"])
    rows = ["- [{}]({}) — {} · {} · {}".format(p["name"], p["url"], p["layer"], p["category"], ", ".join(p["standard"])) for p in P]
    save(code, "catalog.md", ["# " + catalog, "", "[← " + browse + "](README.md)", "", "> " + notice, ""] + rows)
    layer_names, purpose_names, headers = LOCAL_NAMES[code]
    layer_names, purpose_names, headers = layer_names.split("|"), purpose_names.split("|"), headers.split("|")
    taxonomy_parts = ["# " + taxonomy, "", "[← " + browse + "](README.md)", "", "> " + notice, "", "## OSI — " + taxonomy, ""]
    layer_keys = ["physical", "data-link", "network", "transport", "session", "presentation", "application"]
    layer_fallback = {"physical": [("Ethernet PHY", "https://standards.ieee.org/ieee/802.3/10422/", "media/signals"), ("Wi-Fi PHY", "https://standards.ieee.org/ieee/802.11/10548/", "radio/modulation")], "session": [("SIP", "https://www.rfc-editor.org/rfc/rfc3261", "5060/5061"), ("WebSocket", "https://www.rfc-editor.org/rfc/rfc6455", "80/443")]}
    for layer_key, layer_name in zip(layer_keys, layer_names):
        taxonomy_parts += ["### " + layer_name, "", "| {} | {} | {} |".format(headers[0], headers[1], headers[3]), "|---|---|---|"]
        selected = [(p["name"], p["url"], "/".join(p["ports"]) or "—") for p in P if p["layer"] == layer_key]
        selected += layer_fallback.get(layer_key, [])
        taxonomy_parts += ["| [{}]({}) | {} | [↗]({}) |".format(name, url, port, url) for name, url, port in selected] or ["| — | — | — |"]
        taxonomy_parts += [""]
    taxonomy_parts += ["## " + taxonomy + " — 14", ""]
    for purpose_name, protocols_in_group in zip(purpose_names, GROUPS):
        taxonomy_parts += ["### " + purpose_name, "", "| {} | {} | {} | {} |".format(headers[0], headers[1], headers[2], headers[3]), "|---|---|---|---|"]
        taxonomy_parts += ["| [{}]({}) | {} | {} | [↗]({}) |".format(name, url, port, cue if code == "en" else purpose_name, url) for name, url, port, cue in protocols_in_group]
        taxonomy_parts += [""]
    taxonomy_parts += ["> " + notice, "", "[English details](../en/taxonomy.md) · [中文详表](../zh-CN/taxonomy.md)"]
    save(code, "taxonomy.md", taxonomy_parts)
    save(code, "learning-paths.md", ["# " + paths, "", "[← " + browse + "](README.md)", "", "Ethernet / Wi-Fi → ARP / DHCP → IPv4 / IPv6 → TCP / UDP → DNS → TLS → HTTP", "", "> " + notice])
    save(code, "protocol-entry.md", ["# " + spec, "", "[← " + browse + "](README.md)", "", "1. Identity and stable ID", "2. Purpose", "3. Core principle", "4. Layer and dependencies", "5. Message flow", "6. Packet fields and ports", "7. Security guarantees and limitations", "8. Packet capture and analyzer filter", "9. Implementations", "10. Official standards", "", "> " + notice])

print("Generated 5 documents for {} community languages".format(len(TEXT)))
