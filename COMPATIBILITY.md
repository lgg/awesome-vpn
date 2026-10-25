# Compatibility and platform matrix

[← Back to README](README.md) · [Platform-first client directory](CLIENTS.md)

This document is a **high-level discovery index**, not an automated interoperability test. A client that bundles Xray or sing-box may support only a **subset** of the core's current protocols, transports and options. Subscription import support is **not** equivalent to raw JSON configuration support.

**Legend:** `Xray` / `sing-box` / `mihomo` / `V2Ray` = core family reported by the project. `Various` = multi-engine or VPN stack. `Unverified` = consult upstream. `Partial-source` = project publishes releases/issues but public source availability is not established. A dash does not assert lack of support.

## User-facing clients

| Client | Platforms | Engine / technology | Distribution / code | Important caveats |
| --- | --- | --- | --- | --- |
| [Qeli](https://github.com/litvinovtd/qeli) | Windows, macOS, Android (upstream claims) | **Qeli custom VPN protocol** | AGPL-3.0 core, MPL-2.0 client dirs | **Beta/pre-1.0, security not independently established**; does not import standard Xray subscriptions |
| [KEQDIS](https://github.com/Lemonochka/keqdroid) | Windows x64, Linux, Android | Xray and mihomo (separate cores) | GPL-3.0; official GitHub APK/ZIP/Linux packages | Do not infer stock sing-box support, iOS builds, or every modern XHTTP option |
| [TiredVPN](https://github.com/tiredvpn/tiredvpn) | Linux client/server, Android companion | Dedicated adaptive-tunnel implementation | AGPL-3.0 source and binaries | **Experimental security properties**, dedicated client; not a generic VLESS/Xray import client |
| [NoDPI4Android](https://github.com/GVCoder09/NoDPI4Android) | Android | Local DPI workaround | GPL-3.0; upstream APK beta | Not a remote exit; generally conflicts with a separate Android VPNService; upstream warns that filtering methods vary |

| [Veil](https://github.com/alibakhtiari/Veil) | Desktop, Android | MASQUE/WireGuard tunnel design | AGPL-3.0 | Experimental; check signed binaries and release readiness |
| [v2whitelist](https://github.com/NullCoreDeveloper/v2whitelist) | Android | Xray/V2Ray | GPL-3.0 | Experimental network-filtering scenarios; no guarantee of accessibility |
| [WINGS V DeX](https://github.com/WINGS-N/WINGSV_DeX) | Windows, Linux | Xray, VK TURN | Open source | Project-specific VK TURN integration; check desktop builds and permissions |
| [SkipIt](https://github.com/getskipit/skipit) | Windows (upstream repository description) | Xray, sing-box | Open source | Verify supported builds and current transport implementation |
| [INCY](https://github.com/INCY-DEV/incy-platforms) | Android/TV, iOS/tvOS, Windows/macOS/Linux | Xray | **Closed client** / official binary releases | Desktop **pre-alpha**; GitHub hosts releases/metadata and does not contain complete app source |
| [OneXray](https://github.com/YuanDevTeam/OneXray) | Android, iOS, Windows, macOS, Linux | Xray | GPL-3.0 | Imports share links, JSON, and provider subscriptions; verify each OS's packaged build |
| [Clash Mi](https://github.com/KaringX/clashmi) | Android, iOS, Windows, macOS, Linux | mihomo | GPL-3.0 | Mihomo YAML config, not native arbitrary Xray JSON |
| [FlClashX](https://github.com/pluralplay/FlClashX) | Android/TV, Windows, macOS, Linux (per upstream) | mihomo | GPL-3.0 | Community fork; Remnawave-specific HWID/metadata features |
| [husi](https://github.com/xchacha20-poly1305/husi) | Android, Windows, Linux, macOS Apple Silicon | sing-box family | Source available | No asserted macOS Intel desktop or Windows ARM64 package |
| [V2Box](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690) | iOS, iPadOS, supported Macs | Xray, multiple tunnel types | Closed, App Store | Store notes mention MasterDNS/DNSTT; protocol features need per-version tests |
| [AnyPortal](https://github.com/AnyPortal/AnyPortal) | Windows, macOS, Linux, Android | Xray, sing-box, mihomo, V2Ray | Source repository | **No working iOS TUN** per upstream; distinct OS feature sets |
| [GenyConnect](https://github.com/genyleap/GenyConnect) | Cross-platform (see releases) | Secure tunnel/routing client | GPL-3.0 | Exact operating modes/permissions require verification per OS |
| [Hey](https://github.com/popsiclelmlm/Hey) | HarmonyOS NEXT | Tunnel and protocol-debugging client | GPL-3.0 | Native HarmonyOS, not interchangeable with Android VPN apps |
| [v2rayN](https://github.com/2dust/v2rayN) | Windows, Linux, macOS | Xray, sing-box and others | Open source | Profile types vary between cores/releases |
| [L×Box](https://github.com/Leadaxe/LxBox) | Android | sing-box-lx fork (XHTTP, AmneziaWG, MASQUE etc.) | GPL-3.0 | Maintainer-reported features; use matching fork build; one Android VpnService |
| [Rethink DNS + Firewall](https://github.com/celzero/rethink-app) | Android | DNS/firewall/WireGuard proxifier | Apache-2.0 | No implicit compatibility with arbitrary Xray/Clash subscription URLs |
| [Spoofy](https://github.com/ringolol/Spoofy) | iOS, macOS | Local DPI HTTP/SOCKS proxy | MIT | iOS Wi-Fi/app proxy or sideload; does **not** tunnel all cellular traffic |
| [v2rayNG](https://github.com/2dust/v2rayNG) | Android | Xray, V2Fly | Open source | Android VPN slot; TUN behavior differs from desktop |
| [WINGS V](https://github.com/WINGS-N/WINGSV) | Android | Xray, WireGuard/AmneziaWG, VK TURN | Open source | Some hotspot/transport features need root and specific deployment |
| [v2RayTun](https://github.com/LXST-CODE/v2RayTun) | Android/TV, iOS, macOS, Windows, Linux | Xray, AmneziaWG integration | **Closed** / release-oriented GitHub | Separate OS release tracks; Android/Windows TUN DNS behavior must be checked per release |
| [SFA](https://github.com/SagerNet/sing-box-for-android) | Android | sing-box | Open source | No promise of feature parity with CLI |
| [ByeByeDPI](https://github.com/romanvht/ByeByeDPI) | Android | Local DPI desync through ByeDPI | Open source | Not a remote VPN exit; competes for Android VPN slot |
| [DesyncDroyd](https://github.com/sigmabosshvh/DesyncDroyd) | Android | zapret2 / nfqws2 | Source repository | Shizuku/permissions and device-specific capabilities require checking |
| [NekoBox for Android](https://github.com/MatsuriDayo/NekoBoxForAndroid) | Android | sing-box family | Open source | Confirm recent release, not just Git pushes |
| [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid) | Android | mihomo / Clash Meta | Open source | Clash subscriptions/configs differ from Xray |
| [Exclave](https://github.com/ExclaveNetwork/Exclave) | Android | Proxy client | Open source | See upstream for exact core and supported formats |
| [Hiddify](https://github.com/hiddify/hiddify-app) | Windows, macOS, Linux, Android, iOS | sing-box family / multiple protocols | Open source | Mobile store builds and GitHub releases may differ |
| [Karing](https://github.com/KaringX/karing) | Android, iOS, desktop | sing-box-related routing | Open source | Verify current platforms and transport support |
| [Amnezia VPN](https://github.com/amnezia-vpn/amnezia-client) | Desktop, Android, iOS | WireGuard / AmneziaWG / additional integrations | Open source | Primarily a self-hosted VPN suite, not generic Xray GUI |
| [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev) | Windows, macOS, Linux | mihomo | Open source | Clash/Mihomo configuration family |
| [FlClash](https://github.com/chen08209/FlClash) | Multi-platform | mihomo | Open source | Check builds per operating system |
| [Clash Party](https://github.com/mihomo-party-org/clash-party) | Desktop | mihomo | Open source | GUI features may lag core features |
| [Throne](https://github.com/throneproj/Throne) | Windows, macOS, Linux | sing-box | Open source | Migration from Nekoray is not always 1:1 |
| [GUI.for.SingBox](https://github.com/GUI-for-Cores/GUI.for.SingBox) | Desktop | sing-box | Open source | Native build availability varies |
| [v2rayA](https://github.com/v2rayA/v2rayA) | Linux, Windows, macOS | Xray/V2Ray | Open source | Transparent proxy requires OS/network permissions |
| [Satelite Proxy](https://github.com/zn0wii/satelite-proxy) | Desktop | Xray, sing-box, mihomo | Open source | Relatively new; validate specific imported subscriptions |
| [Zephyr](https://github.com/Juwan-Hwang/Zephyr) | Desktop | mihomo | Open source | Relatively new |
| [Bettbox](https://github.com/appshubcc/Bettbox) | Desktop, Android/TV (per upstream) | Network proxy toolbox | Open source | Exact core/protocol matrix unverified |
| [Happ](https://happ.info/) | Windows, macOS, Linux, Android, iOS, TV (per vendor) | Xray | Proprietary | Public GitHub repositories distribute binaries, not necessarily full source |
| [Streisand](https://apps.apple.com/us/app/streisand/id6450534064) | iOS, iPadOS and other Apple platforms per store | Proxy client | Proprietary | Availability varies by storefront |
| [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118) | Apple platforms per store | Multi-protocol proxy | Proprietary/paid | Exact protocol support depends on version |
| [SwByeDPI](https://github.com/mIwr/SwByeDPI) | iOS | Local ByeDPI wrapper | Open source | Not a remote VPN service |
| [MuseDPI](https://github.com/zondaxxx/MuseDPI) | iOS, Android | Local DPI bypass | Open source | Not an anonymous VPN exit |

## Server management

| Project | Backend focus | Primary purpose | Note |
| --- | --- | --- | --- |
| [WINGS V Panel](https://github.com/WINGS-N/wingsv-panel) | WINGS V ecosystem | Client profile and management control | Not an ordinary generic Xray panel |
| [WINGS 3x-ui fork](https://github.com/WINGS-N/3x-ui) | Xray plus VK TURN integration | Forked server panel | Upstream-specific changes; do not assume upstream 3x-ui compatibility |
| [swgPanel](https://github.com/SanityProtocol/swg-panel) | WireGuard / AmneziaWG | Web panel for VPN users and nodes | Not an Xray/VLESS panel |
| [WireGuard Easy](https://github.com/wg-easy/wg-easy) | WireGuard | Web client management | Does not administer arbitrary Xray/sing-box profiles |
| [3x-ui](https://github.com/MHSanaei/3x-ui) | Xray | Single-/multi-server panel, clients and subscriptions | Feature set evolves quickly |
| [x-ui](https://github.com/alireza0/x-ui) | Xray | Inbounds and user management | Different project from 3x-ui |
| [s-ui](https://github.com/alireza0/s-ui) | sing-box | Web management panel | Sing-box configuration family |
| [Remnawave](https://github.com/remnawave/panel) | Xray | Subscription, user and node management | Verify license and deployment requirements |
| [Marzban](https://github.com/Gozargah/Marzban) | Xray | Multiuser/subscription management | Companion node deployment is separate |
| [Hiddify Manager](https://github.com/hiddify/Hiddify-Manager) | Multi-protocol | Anti-censorship panel | Consult version-specific documentation |
| [MetaCubeXD](https://github.com/MetaCubeX/metacubexd) | mihomo | Client/core monitoring dashboard | **Not** equivalent to a VPN service billing panel |
| [Nikki](https://github.com/nikkinikki-org/OpenWrt-nikki) | mihomo | OpenWrt client transparent proxy plugin | Requires firmware/kernel/firewall4 support; not a general desktop client |

## Router and subscription integrations

| Project | Platform / backend | Use case | Important caveats |
| --- | --- | --- | --- |
| [WayHop](https://github.com/awadak3davra/wayhop) | OpenWrt/Entware; sing-box | Browser-based configuration, failover and traffic charts | **Pre-1.0**; may overlap existing firewall/routing policies |
| [routeflux](https://github.com/Alaxay8/routeflux) | OpenWrt; Xray | Subscribe/select nodes and transparent proxy routing | Firmware, firewall and DNS configuration must be verified |
| [Asuswrt-Merlin AmneziaWG](https://github.com/william-aqn/asuswrt-merlin-amneziawg) | ASUS Merlin/Entware; AmneziaWG | Router client and server, selective routes | Firmware/architecture-specific |
| [Remnawave Subscription Middleware](https://github.com/Mrvibecodic/remnawave-subscription-middleware) | Remnawave subscriptions | Mirroring, profile modification and access rules | Sensitive subscription data, reverse-proxy trust and authentication |
| [MCP Remnawave](https://github.com/TrackLine/mcp-remnawave) | Remnawave API | Administrative automation and integrations | Never expose an unrestricted control/API token to untrusted agents |

## Tunneling and camouflage compatibility

| Tool | Endpoints and scope | What it does not do |
| --- | --- | --- |
| [wireproxy](https://github.com/windtf/wireproxy) | WireGuard client to local SOCKS5/HTTP | No general system-wide TUN; SOCKS5 UDP not implemented as described upstream |
| [wireproxy-awg](https://github.com/artem-russkikh/wireproxy-awg) | AmneziaWG-compatible userspace WireGuard-to-SOCKS | Not a generic Xray protocol converter |
| [wg-obfuscator](https://github.com/ClusterM/wg-obfuscator) | UDP wrapping on both client and self-hosted server | Not a VPN client/server; requires deployment at both ends |
| [MTProxy](https://github.com/TelegramMessenger/MTProxy), [Telemt](https://github.com/telemt/telemt), [mtg](https://github.com/9seconds/mtg) | Telegram-only transport | Cannot replace a whole-device VPN |
| [iodine](https://github.com/yarrick/iodine) | Client/server DNS tunnel carrying IPv4 | Not encrypted DNS alone; both endpoints need compatible protocol versions |

## Protocol and transport vocabulary

| Term | Type | Do not confuse with |
| --- | --- | --- |
| VLESS, VMess, Trojan, Shadowsocks | Proxy protocols | TLS/REALITY and network transport |
| REALITY | Security/handshake layer in supported Xray-style stacks | Complete VPN protocol |
| TCP, gRPC, WebSocket, XHTTP | Transport mechanisms | Core/protocol labels |
| Hysteria 2, TUIC | QUIC-family proxy protocols | Plain UDP forwarding |
| WireGuard / AmneziaWG | VPN protocol family | SOCKS/HTTP proxy |
| DNS over HTTPS (DoH) | Encrypted DNS resolution | DNS-based VPN tunneling |
| DNS tunneling | Carrying a payload over DNS messages | DoH, DoT or DNSCrypt alone |
| Decentralized VPN (dVPN) | VPN routing through distributed network/nodes | Private mesh network with no public exit |
| Private encrypted mesh / overlay | Connecting devices in a cryptographic virtual network | Public web exit node or anonymity guarantee |
| TUN | Virtual network interface / traffic interception | Anonymous VPN provider |
| DPI-bypass / desync | Local filtering-circumvention technique | Encrypted remote exit |
| Subscription URL | Profile delivery and update mechanism | Transport protocol |

## How to verify an actual combination

1. Record **client name + exact version**, operating system, core version and configuration format.
2. Confirm upstream supports the **protocol**, **security/handshake layer** and **transport** independently.
3. Test subscription import and raw configuration separately; do not assume identical behavior.
4. Test TCP and UDP, DNS, IPv4/IPv6, reconnects and split tunneling on the same network.
5. Inspect actual egress IP/DNS and client logs. Avoid publishing credentials, node hostnames or subscription tokens.
6. Update this matrix only with upstream documentation, a cited release note or reproducible tests.

**Snapshot:** 2026-10-25; extended with [NTC and dVPN research](RESEARCH-2026.md), [client release research](CLIENT-RESEARCH-2026.md), and [ecosystem/operations research](ECOSYSTEM-RESEARCH-2026.md). No claim is made that every combination above was manually tested.
