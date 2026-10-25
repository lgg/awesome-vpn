# Awesome VPN

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

> A curated collection of VPN and proxy clients, servers, management panels, subscription tools, censorship circumvention, DPI bypass, DNS, routing, diagnostics, guides, and communities.

**English-first · vendor-neutral · self-hosting-friendly · updated as the ecosystem changes.** The focus is useful software and technical resources, not free public proxy lists or VPN advertisements.

This list covers **VPNs, application proxies, local DPI circumvention, encrypted DNS, mesh networking, and reverse tunnels**. These solve different problems: a local DPI-bypass tool **does not** inherently hide your public IP; a proxy client **does not** provide a server or subscription by itself. See the **[client directory by platform](CLIENTS.md)**, [Compatibility](COMPATIBILITY.md) and [Troubleshooting](TROUBLESHOOTING.md).

**Legend:** `[OSS]` source available under an open-source license · `[Closed]` proprietary/closed-source client · `[Legacy]` archived or apparently dormant; verify before use · `[Self-hosted]` deploy on infrastructure you control. Activity and supported features can change; always check upstream releases and documentation.

## Contents

- [Client directory and selection guide](CLIENTS.md)
- [2026 research and ecosystem additions](ECOSYSTEM-RESEARCH-2026.md)
- [DPI, router tools and specialist forum research (October 2026)](DPI-RESEARCH-2026.md)
- [Further DPI/client research and security notes (October 2026)](DPI-RESEARCH-ROUND2-2026.md)
- [Proxy and VPN cores](#proxy-and-vpn-cores)
- [Desktop clients](#desktop-clients)
- [Android clients](#android-clients)
- [iOS, iPadOS and Apple clients](#ios-ipados-and-apple-clients)
- [HarmonyOS NEXT clients](#harmonyos-next-clients)
- [VPNs and private mesh networks](#vpns-and-private-mesh-networks)
- [Decentralized and anonymity networks](#decentralized-and-anonymity-networks)
- [Server panels and dashboards](#server-panels-and-dashboards)
- [Monitoring, resilience and node operations](#monitoring-resilience-and-node-operations)
- [Subscriptions, billing and automation](#subscriptions-billing-and-automation)
- [Deployment, forwarding and tunnels](#deployment-forwarding-and-tunnels)
- [DPI bypass and censorship circumvention](#dpi-bypass-and-censorship-circumvention)
- [Telegram connectivity and MTProto proxies](#telegram-connectivity-and-mtproto-proxies)
- [DNS and DNS tunnels](#dns-and-dns-tunnels)
- [Routers, OpenWrt and transparent proxying](#routers-openwrt-and-transparent-proxying)
- [Routing rules and geodata](#routing-rules-and-geodata)
- [Diagnostics and measurements](#diagnostics-and-measurements)
- [Documentation and configuration examples](#documentation-and-configuration-examples)
- [Communities and reference catalogs](#communities-and-reference-catalogs)
- [Research and curated discussions](#research-and-curated-discussions)
- [Maintenance and contributing](#maintenance-and-contributing)

**Looking for an app to install?** Start with **[CLIENTS.md](CLIENTS.md)** for a platform-by-platform index, original GitHub releases and verified App Store listings. Use the sections below for broader project discovery.
## Proxy and VPN cores

- **[Xray-core](https://github.com/XTLS/Xray-core)** [OSS] — Extensible proxy core for VLESS, VMess, Trojan, Shadowsocks, REALITY and more.
- **[sing-box](https://github.com/SagerNet/sing-box)** [OSS] — Universal proxy platform with configurable routing and multiple inbound/outbound protocols.
- **[mihomo (Clash Meta)](https://github.com/MetaCubeX/mihomo/releases)** [OSS] — Rule-based Clash-family proxy core. **Note:** repository metadata may be inconsistent; prefer the verified release history and official documentation before downloading.
- **[V2Ray (v2fly)](https://github.com/v2fly/v2ray-core)** [OSS] — General-purpose core from the V2Ray ecosystem.
- **[Hysteria 2](https://github.com/HyNetworks/hysteria)** [OSS] — QUIC-based censorship-resistant proxy optimized for challenging networks.
- **[TrustTunnel](https://github.com/TrustTunnel/TrustTunnel)** — VPN/tunnel protocol project focused on obfuscation; verify official clients and interoperability rather than assuming Xray/sing-box support.
- **[TUIC protocol](https://github.com/tuic-protocol/tuic)** [OSS] — Specification for a QUIC-based TCP/UDP proxy; **not** an implementation.
- **[TUIC implementation](https://github.com/Itsusinn/tuic)** [OSS] — Client/server implementation of TUIC.
- **[Shadowsocks Rust](https://github.com/shadowsocks/shadowsocks-rust)** [OSS] — Rust implementation of the Shadowsocks proxy.
- **[Trojan](https://github.com/trojan-gfw/trojan)** [OSS] — TLS-based Trojan proxy implementation; check maintenance before deploying.
- **[mieru](https://github.com/enfein/mieru)** [OSS] — SOCKS5/HTTP(S) proxy system for circumventing censorship.
- **[NaïveProxy](https://github.com/klzgrad/naiveproxy)** [OSS] — Chromium-network-stack-based HTTP/2/3 proxy camouflage and tunneling.
- **[Cloak](https://github.com/cbeuw/Cloak)** [OSS] — Pluggable transport for proxy traffic camouflage and probe resistance.
- **[Brook](https://github.com/txthinking/brook)** [OSS] — Programmable cross-platform client/server tunnel and proxy suite; use its own protocol/configuration rather than assuming Xray compatibility.
- **[Shadowsocks v2ray-plugin](https://github.com/shadowsocks/v2ray-plugin)** [OSS] — SIP003 WebSocket/TLS transport plugin for Shadowsocks; requires server-side support.
- **[sing-box-lx](https://github.com/Leadaxe/sing-box-lx)** [Fork] — Client-side sing-box fork behind L×Box, with additional transports such as XHTTP/AmneziaWG; not a substitute for upstream sing-box compatibility documentation.
- **[Outline Server](https://github.com/OutlineFoundation/outline-server)** [OSS] — Self-hosted Shadowsocks server and API for managing Outline access keys.
- **[AmneziaWG Go](https://github.com/amnezia-vpn/amneziawg-go)** [OSS] — Userspace AmneziaWG implementation; protocol family differs from WireGuard-compatible proxy subscriptions.
- **[OpenVPN](https://github.com/OpenVPN/openvpn)** [OSS] — Traditional TLS VPN daemon.
- **[TiredVPN](https://github.com/tiredvpn/tiredvpn)** [OSS] [Experimental] — Separate Go client/server VPN using adaptive transport selection; cross-ISP robustness and protocol security claims are not independently tested here.
- **[Qeli](https://github.com/litvinovtd/qeli)** [Experimental] — Self-hosted TUN VPN with Rust core and Android/Windows/macOS clients; hybrid cryptography and obfuscation are **not independently vetted here**. Pre-1.0 protocol.
- **[Veil](https://github.com/alibakhtiari/Veil)** [Experimental] — MASQUE/WireGuard-oriented tunneling client with desktop and Android applications; confirm release maturity before use.
- **[Mullvad VPN app](https://github.com/mullvad/mullvadvpn-app)** [OSS] — Provider-specific multi-platform VPN application; **not** a generic bring-your-own-Xray client.
- **[SoftEther VPN](https://github.com/SoftEtherVPN/SoftEtherVPN)** [OSS] — Multiprotocol VPN server and client suite.


## Desktop clients

Windows, macOS and Linux availability varies by release; verify the build for your OS and CPU.

- **[sing-box for Desktop](https://github.com/SagerNet/sing-box-for-desktop)** [OSS] — Official experimental desktop GUI (initially Windows); check release readiness.
- **[v2rayN](https://github.com/2dust/v2rayN)** [OSS] — Multi-platform GUI for Xray, sing-box and other proxy cores; profiles and subscriptions.
- **[v2RayTun](https://github.com/LXST-CODE/v2RayTun)** [Closed] — Windows/macOS/Linux builds in a multi-platform Xray client distribution; download tracks differ by OS.
- **[WINGS V DeX](https://github.com/WINGS-N/WINGSV_DeX)** [OSS] — Linux/Windows companion for WINGS V, supporting Xray and VK TURN transports.
- **[SkipIt](https://github.com/getskipit/skipit)** [OSS] — Windows desktop client using Xray-core and sing-box; verify current OS builds and release maturity.
- **[KEQDIS (keqdroid)](https://github.com/Lemonochka/keqdroid)** [OSS] — Flutter-based Windows/Linux/Android proxy client with Xray/mihomo cores, subscriptions and per-app routing; verify exact OS package/core feature support.
- **[Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev)** [OSS] — Desktop GUI based on mihomo.
- **[FlClash](https://github.com/chen08209/FlClash)** [OSS] — Cross-platform Clash Meta client.
- **[Clash Party](https://github.com/mihomo-party-org/clash-party)** [OSS] — Desktop mihomo GUI.
- **[Throne](https://github.com/throneproj/Throne)** [OSS] — Sing-box-powered cross-platform GUI, suitable for former Nekoray users.
- **[GUI.for.SingBox](https://github.com/GUI-for-Cores/GUI.for.SingBox)** [OSS] — Wails/Vue-based desktop GUI.
- **[v2rayA](https://github.com/v2rayA/v2rayA)** [OSS] — Web-based proxy client with transparent proxy capabilities.
- **[Satelite Proxy](https://github.com/zn0wii/satelite-proxy)** [OSS] — Newer desktop client with sing-box/Xray/mihomo integrations; check platform builds.
- **[Zephyr](https://github.com/Juwan-Hwang/Zephyr)** [OSS] — Lightweight Tauri/Rust mihomo desktop client.
- **[Bettbox](https://github.com/appshubcc/Bettbox)** [OSS] — Desktop/Android network toolbox; consult upstream for supported cores.
- **[INCY](https://github.com/INCY-DEV/incy-platforms)** [Closed] — Cross-platform Xray client with official desktop binary releases; **desktop is pre-alpha** and GitHub is a downloads/metadata repository, not full client source.
- **[OneXray](https://github.com/YuanDevTeam/OneXray)** [OSS] — Xray GUI for Windows, macOS, Linux and mobile, with native configuration imports and Remnawave subscriptions.
- **[GenyConnect](https://github.com/genyleap/GenyConnect)** [OSS] — Multi-platform tunnel/routing client; check upstream-supported builds and capabilities.
- **[AnyPortal](https://github.com/AnyPortal/AnyPortal)** — GUI for Xray/sing-box/mihomo on Windows, macOS, Linux and Android; **iOS tunneling is not available** per upstream.
- **[husi](https://github.com/xchacha20-poly1305/husi)** — Sing-box-family Android and desktop client; macOS desktop builds currently target Apple Silicon, check platform requirements.
- **[FlClashX](https://github.com/pluralplay/FlClashX)** [OSS] — FlClash-derived mihomo client adapted for Remnawave subscriptions; confirm fork-specific maintenance.
- **[Clash Nyanpasu](https://github.com/libnyanpasu/clash-nyanpasu)** [OSS] — Desktop mihomo/Clash GUI with profiles and subscription workflow.
- **[Sparkle](https://github.com/xishang0128/sparkle)** [OSS] — Electron-based mihomo GUI, still evolving.
- **[sing-box-windows](https://github.com/xinggaoya/sing-box-windows)** [OSS] — Tauri desktop sing-box GUI for Windows, macOS and Linux.
- **[OneBox](https://github.com/OneOhCloud/OneBox)** [OSS] — Sing-box desktop GUI; upstream distinguishes official macOS support from community-maintained builds.
- **[Pandora-Box](https://github.com/snakem982/Pandora-Box)** [OSS] — Simple mihomo GUI for desktop environments.
- **[Prizrak-Box](https://github.com/legiz-ru/Prizrak-Box)** [OSS] — Pandora-Box-derived desktop mihomo client with additional platforms/builds.
- **[GUI.for.Clash](https://github.com/GUI-for-Cores/GUI.for.Clash)** [OSS] — Wails-based mihomo/Clash desktop GUI.
- **[ClashX.Meta](https://github.com/MetaCubeX/ClashX.Meta)** [OSS] — macOS menu-bar proxy GUI in the Clash Meta ecosystem.
- **[ClashBar](https://github.com/Sitoi/ClashBar)** [OSS] — SwiftUI/AppKit macOS menu-bar mihomo client.
- **[V2rayU](https://github.com/yanue/V2rayU)** — macOS proxy GUI for V2Ray/Xray-related profiles.
- **[V2RayXS](https://github.com/tzmax/V2RayXS)** [OSS] — macOS GUI for Xray-core.
- **[ShadowsocksX-NG](https://github.com/shadowsocks/ShadowsocksX-NG)** [OSS] — Dedicated macOS Shadowsocks client.
- **[Netch](https://github.com/netchx/netch)** [OSS] — Windows system-/application-level proxy client; check version-specific modes.
- **[Invisible Man XRay](https://github.com/InvisibleManVPN/InvisibleMan-XRayClient)** [OSS] — Windows WPF Xray GUI; last significant activity older, verify releases.
- **[Shadowsocks for Windows](https://github.com/shadowsocks/shadowsocks-windows)** [Legacy] — Classic C# client; upstream had no recent updates as of 2026.
- **[Qeli client](https://github.com/litvinovtd/qeli)** [Experimental] — Native desktop application for Qeli protocol; incompatible with ordinary Xray profile subscriptions.
- **[Veil client](https://github.com/alibakhtiari/Veil)** [Experimental] — Desktop GUI for its MASQUE/WireGuard-based tunnel design; early-stage.
- **[Happ Desktop](https://github.com/Happ-proxy/happ-desktop)** [Closed] — Official Windows/macOS/Linux release repository for the Xray-powered Happ utility.
- **[Nekoray](https://github.com/MatsuriDayo/nekoray)** [Legacy] — Archived Qt client; use only for historical reference.

## Android clients

- **[L×Box (LxBox)](https://github.com/Leadaxe/LxBox)** [OSS] — Android sing-box-lx client combining VLESS/REALITY/XHTTP, AmneziaWG, WARP and Tailscale in one VPN interface; feature claims are version-specific.
- **[Rethink DNS + Firewall](https://github.com/celzero/rethink-app)** [OSS] — Android firewall, encrypted DNS, connection tracking and WireGuard upstream routing; not a generic Xray subscription client.
- **[v2rayNG](https://github.com/2dust/v2rayNG)** [OSS] — Widely used Android Xray/V2Ray client.
- **[sing-box for Android (SFA)](https://github.com/SagerNet/sing-box-for-android)** [OSS] — Android GUI for sing-box.
- **[NekoBox for Android](https://github.com/MatsuriDayo/NekoBoxForAndroid)** [OSS] — Advanced sing-box-based Android client; check release recency.
- **[WINGS V](https://github.com/WINGS-N/WINGSV)** [OSS] — Android Xray-oriented client with per-app controls, WireGuard integration and local DPI-bypass features.
- **[NoDPI4Android](https://github.com/GVCoder09/NoDPI4Android)** [OSS] [Beta] — Android local DPI-circumvention app from the NoDPI project, not a remote VPN exit; latest public APK was beta at review.
- **[KEQDIS (keqdroid) for Android](https://github.com/Lemonochka/keqdroid)** [OSS] — Xray/mihomo client with subscriptions and Android APK releases, sharing a codebase with desktop builds.
- **[TiredVPN Android](https://github.com/tiredvpn/tiredvpn-android)** [OSS] [Experimental] — Android client for its own TiredVPN server/protocol; not a generic Xray share-link importer; no independent security audit established.
- **[v2RayTun](https://github.com/LXST-CODE/v2RayTun)** [Closed] — Cross-platform Xray/AmneziaWG client for Android/TV, Apple and desktop; official GitHub lists platform-specific releases but is not full application source.
- **[Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid)** [OSS] — Android rule-based tunneling client.
- **[Exclave](https://github.com/ExclaveNetwork/Exclave)** [OSS] — Android proxy client.
- **[Hiddify](https://github.com/hiddify/hiddify-app)** [OSS] — Cross-platform client with sing-box-related protocols and subscriptions.
- **[Karing](https://github.com/KaringX/karing)** [OSS] — Cross-platform routing/proxy utility.
- **[Amnezia VPN](https://github.com/amnezia-vpn/amnezia-client)** [OSS] — Client supporting self-hosted VPN deployments and AmneziaWG.
- **[Happ Android](https://github.com/Happ-proxy/happ-android)** [Closed] — Official Android release repository (not a full source-code guarantee).
- **[INCY for Android](https://github.com/INCY-DEV/incy-platforms)** [Closed] — Android/Android TV releases for Xray; source code is not published, use official signed APK/store.
- **[OneXray for Android](https://github.com/YuanDevTeam/OneXray)** [OSS] — Cross-platform Xray client with direct subscriptions and local routing.
- **[Clash Mi](https://github.com/KaringX/clashmi)** [OSS] — Mihomo-based multi-platform client with Android and iOS releases.
- **[husi for Android](https://github.com/xchacha20-poly1305/husi)** — Advanced proxy client with sing-box-based tooling; check OS and ABI requirements.
- **[FlClashX](https://github.com/pluralplay/FlClashX)** [OSS] — Community fork of FlClash including Android/TV distribution.
- **[YumeBox](https://github.com/YumeYucca/YumeBox)** [OSS] — Android mihomo GUI; check release/feature maturity.
- **[Shadowsocks Android](https://github.com/shadowsocks/shadowsocks-android)** [OSS] — Official Shadowsocks client focused on the Shadowsocks protocol, not all Xray protocols.
- **[SimpleXray](https://github.com/lhear/SimpleXray)** [OSS] — Smaller Xray-based Android GUI.
- **[AnyPortal for Android](https://github.com/AnyPortal/AnyPortal)** — Multi-engine proxy GUI; mobile build limitations described upstream.
- **[Xray GUI (SaeedDev94)](https://github.com/SaeedDev94/Xray)** [OSS] — Minimal Android Xray client.
- **[v2whitelist](https://github.com/NullCoreDeveloper/v2whitelist)** [OSS] [Experimental] — Android Xray/V2Ray client exploring mobile-network allowlist environments; ISP results and reliability not guaranteed.
- **[Qeli for Android](https://github.com/litvinovtd/qeli)** [Experimental] — Android client for the dedicated Qeli protocol, not an Xray configuration importer.
- **[Outline Client](https://github.com/OutlineFoundation/outline-apps)** [OSS] — Outline client/manager ecosystem.

**Root users:** See [Surfing](https://github.com/GitMetaio/Surfing) and [box4magisk](https://github.com/CHIZI-0618/box4magisk) under router/transparent-proxy tools; these are not ordinary rootless VPN apps.

**Android caveat:** A standard Android installation generally permits only one active `VpnService` tunnel. Running a proxy client and a separate DPI-bypass app simultaneously may require a supported in-app integration or non-VPN proxy mode. Do not assume every listed client can be combined.

## iOS, iPadOS and Apple clients

- **[sing-box for Apple platforms](https://github.com/SagerNet/sing-box-for-apple)** [OSS] — Official source for iOS, macOS and tvOS clients (SFI/SFM/SFT); see [official graphical clients](https://sing-box.sagernet.org/clients/).
- **[Karing](https://github.com/KaringX/karing)** [OSS] — Apple and other platform releases where available.
- **[Hiddify](https://github.com/hiddify/hiddify-app)** [OSS] — Apple-platform client; check regional App Store availability.
- **[Amnezia VPN](https://github.com/amnezia-vpn/amnezia-client)** [OSS] — Apple and other platform client builds.
- **[v2RayTun for Apple](https://github.com/LXST-CODE/v2RayTun)** [Closed] — iOS/macOS Xray client, with region-dependent App Store availability and separate release tracks.
- **[INCY](https://apps.apple.com/us/app/incy/id6756943388)** [Closed] — iPhone/iPad/Apple TV Xray client; developer publishes platform downloads at [INCY GitHub](https://github.com/INCY-DEV/incy-platforms), not full application source.
- **[OneXray](https://github.com/YuanDevTeam/OneXray)** [OSS] — Xray client with iOS/macOS builds and official store releases.
- **[Clash Mi](https://github.com/KaringX/clashmi)** [OSS] — Mihomo-based iOS/macOS proxy utility with official App Store listing.
- **[V2Box](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690)** [Closed] — Apple-platform Xray-related client with DNS tunneling options, custom JSON imports and subscription controls (features vary by version).
- **[Loon](https://apps.apple.com/us/app/loon/id1373567447)** [Closed] — Paid Apple-platform policy routing/proxy utility with scripting.
- **[Surge 5](https://apps.apple.com/us/app/surge-5/id1442620678)** [Closed] — Advanced Apple networking/proxy rules and debugging utility; check in-app licensing.
- **[Quantumult X](https://apps.apple.com/us/app/quantumult-x/id1443988620)** [Closed] — Paid Apple proxy/rule engine with scripting and custom routing.
- **[Egern](https://apps.apple.com/us/app/egern/id1616105820)** [Closed] — Apple proxy and network tools; check protocol requirements and pricing.
- **[Happ](https://happ.info/)** [Closed] — Xray-powered client with App Store distribution and vendor-maintained downloads.
- **[Streisand](https://apps.apple.com/us/app/streisand/id6450534064)** [Closed] — Apple-platform proxy client; app availability varies by region.
- **[Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118)** [Closed] — Paid Apple-platform network/proxy client.
- **[Stash](https://stash.ws/ios)** [Closed] — Paid iOS/iPadOS/tvOS rule-based proxy client with routing, inspection and rewrites.
- **[Spoofy](https://github.com/ringolol/Spoofy)** [OSS] [Experimental] — iOS/macOS local HTTP/SOCKS5 DPI-bypass proxy with optional Outline routing. **Not a system-wide iOS VPN**, not an App Store app; Wi-Fi/app proxy configuration or sideload is required.
- **[SwByeDPI](https://github.com/mIwr/SwByeDPI)** [OSS] — Swift iOS wrapper around the ByeDPI approach.
- **[MuseDPI](https://github.com/zondaxxx/MuseDPI)** [OSS] — Local DPI circumvention project for iOS and Android.

**Note:** App Store listings, GitHub release assets and public source availability are three separate things. Never infer that a client is open source merely because it has a GitHub releases repository.

## HarmonyOS NEXT clients

- **[ClashBox](https://github.com/xiaobaigroup/ClashBox)** [OSS] — Native HarmonyOS NEXT mihomo-based GUI; check signing and HarmonyOS version requirements. It is **not** merely an Android APK.
- **[Hey](https://github.com/popsiclelmlm/Hey)** [OSS] — Native HarmonyOS NEXT network tunneling and protocol-debugging client.
## VPNs and private mesh networks

For private connectivity between your own devices and services; not interchangeable with censorship-bypass proxy transport.

- **[WireGuard tools](https://github.com/WireGuard/wireguard-tools)** [OSS] — WireGuard userspace tools (GitHub mirror).
- **[Tailscale](https://github.com/tailscale/tailscale)** — WireGuard-based mesh connectivity.
- **[Headscale](https://github.com/juanfont/headscale)** [OSS] [Self-hosted] — Self-hosted implementation of the Tailscale control server.
- **[NetBird](https://github.com/netbirdio/netbird)** [OSS] — Identity-oriented secure mesh and access management.
- **[ZeroTier](https://github.com/zerotier/ZeroTierOne)** — Virtual network overlay implementation.
- **[Pangolin](https://github.com/fosrl/pangolin)** — WireGuard-based zero-trust network access and reverse proxy for self-hosted resources; a private-access platform, **not** an Internet anonymity VPN.
- **[Netmaker](https://github.com/gravitl/netmaker)** — WireGuard virtual-network orchestration for distributed nodes; check current community/commercial feature boundaries.
- **[Nebula](https://github.com/slackhq/nebula)** [OSS] — Scalable encrypted overlay networking.
- **[DefGuard](https://github.com/DefGuard/defguard)** [Self-hosted] — WireGuard-based zero-trust access management with MFA/SSO-oriented integrations; check license by component.
- **[strongSwan](https://github.com/strongswan/strongswan)** [OSS] — IPsec/IKEv2 VPN implementation.
- **[sshuttle](https://github.com/sshuttle/sshuttle)** [OSS] — Transparent forwarding over SSH; a pragmatic VPN-like solution, not a traditional VPN protocol.
- **[Gluetun](https://github.com/passteque/gluetun)** [OSS] [Self-hosted] — VPN-client Docker container supporting OpenVPN/WireGuard and provider configurations.
- **[Firezone](https://github.com/firezone/firezone)** — Remote access/network connectivity stack; review hosting and identity requirements.
- **[PiVPN](https://github.com/pivpn/pivpn)** [OSS] — Simple installation scripts for a personal VPN.

## Decentralized and anonymity networks

These are **different architectures**: some route traffic over community nodes, others offer private encrypted overlays without a general Internet exit. Read each trust and payment model before using it.

- **[Mysterium Node](https://github.com/MysteriumNetwork/node)** [OSS] — Node software for the Mysterium distributed VPN ecosystem; economics and exit-node trust differ from conventional self-hosting.
- **[Sentinel dVPN Node](https://github.com/sentinel-official/sentinel-dvpnx)** [OSS] — Node-side software for the Sentinel decentralized VPN network.
- **[Sentinel dVPN CLI](https://github.com/sentinel-official/sentinel-dvpncli)** [OSS] — Command-line client for Sentinel dVPN connections.
- **[Yggdrasil](https://github.com/yggdrasil-network/yggdrasil-go)** [OSS] — Encrypted IPv6 overlay/mesh; not necessarily an Internet VPN exit.
- **[cjdns](https://github.com/cjdelisle/cjdns)** [OSS] — Public-key-addressed encrypted IPv6 mesh routing.
- **[i2pd](https://github.com/PurpleI2P/i2pd)** [OSS] — C++ I2P router for an anonymity-oriented overlay network.
- **[Orbot for Android](https://github.com/guardianproject/orbot-android)** [OSS] — Android Tor connectivity client (GitHub repository; other upstream distribution may exist).

## Server panels and dashboards

- **[3x-ui](https://github.com/MHSanaei/3x-ui)** [OSS] [Self-hosted] — Xray web panel for users, inbounds, subscriptions and server management.
- **[WireGuard Easy (wg-easy)](https://github.com/wg-easy/wg-easy)** [OSS] [Self-hosted] — WireGuard VPN with Docker-friendly web UI and client management.
- **[swgPanel](https://github.com/SanityProtocol/swg-panel)** [OSS] [Self-hosted] — Web panel for WireGuard, AmneziaWG and related turn-proxy setups across nodes.
- **[WINGS V Control Panel](https://github.com/WINGS-N/wingsv-panel)** [OSS] [Self-hosted] — WINGS V configuration and device control over a dedicated management channel.
- **[WINGS 3x-ui fork](https://github.com/WINGS-N/3x-ui)** [OSS] [Self-hosted] — 3x-ui fork integrating VK TURN proxy alongside Xray inbounds.
- **[x-ui](https://github.com/alireza0/x-ui)** [OSS] [Self-hosted] — Xray control panel with multiprotocol and multiuser features.
- **[s-ui](https://github.com/alireza0/s-ui)** [OSS] [Self-hosted] — Web panel for sing-box.
- **[Remnawave](https://github.com/remnawave/panel)** [Self-hosted] — Multi-node proxy management ecosystem; review upstream license and deployment docs.
- **[Marzban](https://github.com/Gozargah/Marzban)** [OSS] [Self-hosted] — Unified Xray panel.
- **[Marzban Node](https://github.com/Gozargah/Marzban-node)** [OSS] — Worker node for Marzban deployments.
- **[Hiddify Manager](https://github.com/hiddify/Hiddify-Manager)** [OSS] [Self-hosted] — Multiuser panel for censorship-resistant proxy services.
- **[sing-box dashboard](https://github.com/SagerNet/sing-box-dashboard)** [OSS] — Official web dashboard for sing-box; check feature maturity.
- **[MetaCubeXD](https://github.com/MetaCubeX/metacubexd)** [OSS] — Mihomo traffic/rules/connection web dashboard (**not** a subscription-selling server panel).
- **[mikan](https://github.com/Miroshka000/mikan)** [OSS] [Experimental] — New proxy/VPN management panel built on Citrus core; verify protocol coverage and code maturity.
- **[z_panel](https://github.com/acidmiku/z_panel)** [Self-hosted] — Multi-server sing-box management and Hysteria2/VLESS+REALITY provisioning; verify security controls before public deployment.
- **[Raha](https://github.com/Raha-Project/Raha)** [Legacy] — Historical entry linked by the Xray UI community; latest observed repository activity was in 2023. Treat as unmaintained unless verified otherwise.

## Subscriptions, billing and automation

- **[Remnawave Bedolaga Telegram Bot](https://github.com/BEDOLAGA-DEV/remnawave-bedolaga-telegram-bot)** [OSS] — Telegram/web subscription sales and administrative tooling for Remnawave.
- **[Bedolaga Cabinet](https://github.com/BEDOLAGA-DEV/bedolaga-cabinet)** [OSS] — Dedicated web cabinet used alongside Bedolaga subscriptions, purchases and gift flows; see upstream integration requirements.
- **[Remnawave Telegram Shop](https://github.com/Jolymmiels/remnawave-telegram-shop)** — Telegram subscription shop integration; evaluate upstream code and payment handling.
- **[Remnashop](https://github.com/snoups/remnashop)** [OSS] — Remnawave-integrated Telegram subscription store; check available payment integrations.
- **[Remnawave Admin](https://github.com/Case211/remnawave-admin)** — Web dashboard plus Telegram admin bot for Remnawave; inspect license and admin permissions.
- **[STEALTHNET Remnawave Bot](https://github.com/STEALTHNET-APP/remnawave-STEALTHNET-Bot)** — Remnawave-oriented storefront, admin panel and Telegram bot; verify license and payment handling.
- **[Remnawave Telegram Mini App](https://github.com/maposia/remnawave-telegram-sub-mini-app)** — Next.js/Telegram Mini App front end for subscription interactions.
- **[Remnawave Subscription Middleware](https://github.com/Mrvibecodic/remnawave-subscription-middleware)** — Subscription reverse proxy/mirror with API middleware, HWID rules and operator controls.
- **[Remnawave Reverse Proxy](https://github.com/eGamesAPI/remnawave-reverse-proxy)** — Reverse-proxy integration for Remnawave deployments; verify configuration and security properties.
- **[3x-ui Sub Router](https://github.com/lgg/3x-ui-sub-router)** — Subscription delivery and Xray routing/orchestration project.
- **[sublink-worker](https://github.com/7Sageer/sublink-worker)** [OSS] — Cloudflare Worker for processing/converting subscriptions.
- **[subconverter](https://github.com/MetaCubeX/subconverter)** [OSS] — Subscription-format conversion utility.
- **[serenity](https://github.com/SagerNet/serenity)** [OSS] — sing-box configuration generator; check maintenance/release status.

Never post real subscription URLs, tokens, panel credentials or VPN private keys in a public issue.

## Monitoring, resilience and node operations

- **[whitebox](https://github.com/quyxishi/whitebox)** [OSS] — Prometheus exporter checking reachability of Xray, WireGuard, AmneziaWG and Shadowsocks-style endpoints.
- **[Xray Checker Statuspage](https://github.com/Mrvibecodic/xray-checker-statuspage)** [OSS] — Status/incident frontend and Telegram management around Xray Checker; monitoring is not a security audit.
- **[Remnawave Watchdog](https://github.com/vrezerni-netizen/remnawave-watchdog)** [OSS] — Panel-server watchdog with backup/recovery checks and Telegram alerts.
- **[Infra Billing](https://github.com/mishkatik/infra-billing)** — Infrastructure cost/balance dashboard for multiple VPS providers; verify API token scopes.
- **[Remnawave Limiter](https://github.com/syvlech/remnawave-limiter)** [OSS] — Monitor simultaneous connections and device/HWID-related limits with Remnawave.
- **[Remnawave Cloudflare Nodes](https://github.com/hteppl/remnawave-cloudflare-nodes)** [OSS] — Sync Cloudflare DNS records with Remnawave node-health decisions; use least-privilege API keys.
- **[Caddy Tblocker](https://github.com/Medium1992/caddy-tblocker)** — Caddy integration for blocking traffic based on reported client addresses behind trusted reverse proxies.
- **[Remnawave Backup & Restore](https://github.com/distillium/remnawave-backup-restore)** [OSS] — Backup/restore script for the Remnawave deployment and database.
- **[Remnawave scripts](https://github.com/DigneZzZ/remnawave-scripts)** [OSS] — Deployment, upgrades, configuration and lifecycle scripts for Remnawave.
- **[MCP Remnawave](https://github.com/TrackLine/mcp-remnawave)** — MCP integration for Remnawave panel administration; restrict access to trusted assistants.
- **[Xray Config UI Editor](https://github.com/bropines/xray-config-ui-editor)** [OSS] — UI to edit Xray JSON configurations through Remnawave's API.
- **[MRS Converter](https://github.com/MakostaDev/mrs-converter)** [OSS] — Converter/viewer for mihomo `.mrs` routing-rule files.

**Operational warning:** These tools may have privileged access to subscriptions, panel databases, SSH credentials or Cloudflare APIs. Review their permission models, backups and update channels before production deployment.


## Deployment, forwarding and tunnels

- **[RemnaSetup](https://github.com/Capybara-z/RemnaSetup)** [OSS] — Automated Remnawave panel/node deployment; read script before execution.
- **[Remnawave Ansible Playbook](https://github.com/iphizic/remna-playbook)** — Infrastructure-as-code installer for Remnawave; verify inventory and privilege requirements.
- **[AmneziaWG Installer](https://github.com/bivlked/amneziawg-installer)** [OSS] — Ubuntu/Debian self-hosted AmneziaWG 3.x provisioning; test current client/server-version compatibility.
- **[Algo VPN](https://github.com/trailofbits/algo)** [OSS] — Ansible-based personal WireGuard/IKEv2 deployment on a cloud VPS; upstream explicitly **does not claim censorship evasion**.
- **[Wireproxy](https://github.com/windtf/wireproxy)** [OSS] — Userspace WireGuard client exposing SOCKS5/HTTP endpoints without a TUN interface or root access; no SOCKS5 UDP support claimed.
- **[Wireproxy AWG](https://github.com/artem-russkikh/wireproxy-awg)** [OSS] — AmneziaWG-compatible Wireproxy fork for bridging client WireGuard-like tunnels to a SOCKS proxy.
- **[WireGuard Obfuscator](https://github.com/ClusterM/wg-obfuscator)** [OSS] — Lightweight UDP wrapper for self-hosted WireGuard connections; **must be deployed at both ends and is not itself a VPN**.
- **[MasterHttpRelayVPN Rust](https://github.com/therealaleph/MasterHttpRelayVPN-RUST)** [Experimental] — Google Apps Script HTTP relay-based tunnel; assess Google service terms, quotas, trust and security before using it.
- **[Xray-install](https://github.com/XTLS/Xray-install)** [OSS] — **Official** Xray installer/update scripts, linked by Xray's own README.
- **[v2ray-agent](https://github.com/mack-a/v2ray-agent)** [OSS] — Multi-protocol installer for Xray, TUIC, Hysteria 2 and sing-box.
- **[233boy/v2ray](https://github.com/233boy/v2ray)** [OSS] — V2Ray install and management scripts.
- **[sing-box-yg](https://github.com/yonggekkk/sing-box-yg)** [OSS] — VPS setup scripts for sing-box and associated transports.
- **[fscarmen/sing-box](https://github.com/fscarmen/sing-box)** [OSS] — Multi-protocol sing-box provisioning scripts.
- **[frp](https://github.com/fatedier/frp)** [OSS] — Reverse proxy / NAT traversal for publishing a service behind NAT.
- **[GOST v3](https://github.com/go-gost/gost)** [OSS] — Multi-protocol proxy chaining, forwarding, reverse tunneling, TUN/TAP and DNS integration.
- **[WINGS V VK TURN proxy](https://github.com/WINGS-N/vk-turn-proxy)** [OSS] — WINGS-maintained TURN proxy fork for its mobile/desktop client ecosystem; review transport limitations and upstream architecture.
- **[wstunnel](https://github.com/erebe/wstunnel)** [OSS] — Tunnel TCP/UDP traffic over WebSocket or HTTP/2.
- **[chisel](https://github.com/jpillora/chisel)** [OSS] — HTTP-carried TCP/UDP tunneling with SSH security.
- **[udp2raw](https://github.com/wangyu-/udp2raw)** [OSS] — Wrap UDP traffic in raw-socket packet forms for restrictive or unreliable paths.
- **[UDPspeeder](https://github.com/wangyu-/UDPspeeder)** [OSS] — Add forward-error correction for lossy UDP links; not an encrypted VPN on its own.
- **[cloudflared](https://github.com/cloudflare/cloudflared)** — Cloudflare Tunnel connector.
- **[edgetunnel](https://github.com/cmliu/edgetunnel)** — Edge-deployed proxy/tunnel tooling; read upstream terms and limitations.

**Reverse tunnel ≠ VPN:** frp and cloudflared expose/reach network services; their presence alone does not encrypt all device traffic or provide an anonymous VPN exit.

## DPI bypass and censorship circumvention

Local circumvention tools here primarily try to defeat packet inspection and filtering. They do **not** automatically replace a remote VPN.

- **[SpoofDPI](https://github.com/xvzc/spoofdpi)** [OSS] — Cross-platform local DPI-evasion proxy for desktop operating systems; upstream explicitly states **no Android or iOS** distribution.
- **[DPIBreak](https://github.com/dilluti0n/dpibreak)** [OSS] — Linux/Windows DPI-circumvention utility; uses system-level techniques, not a remote VPN exit.
- **[GreenTunnel](https://github.com/SadeghHayeri/GreenTunnel)** [OSS] — Local HTTP/HTTPS anti-censorship tool; filtering effectiveness depends on ISP and network.
- **[NoDPI](https://github.com/GVCoder09/NoDPI)** [OSS] — Desktop DPI-bypass utility; upstream documents services it cannot unblock and links a separate Android port.
- **[Zapret2](https://github.com/bol-van/zapret2)** [OSS] — Current-generation DPI desynchronization toolkit with configurable scripts and blockcheck2 strategy testing.
- **[zapret (v1)](https://github.com/bol-van/zapret)** [OSS] [Legacy] — Earlier version; upstream explicitly directs new development to Zapret2.
- **[Zapret Windows bundle](https://github.com/bol-van/zapret-win-bundle)** [OSS] — Upstream Windows binary bundle and blockcheck utilities; verify the included release generation.
- **[Zapret2UI](https://github.com/Asterlike/zapret2UI)** [Experimental] — Independent Windows GUI for Zapret2 with strategy selection; verify bundled binaries and licensing before installing.
- **[Flowseal Zapret preset](https://github.com/Flowseal/zapret-discord-youtube)** — Windows-oriented packaged presets for Discord/YouTube; **third-party**, not the original Zapret upstream.
- **[youtubeUnblock](https://github.com/Waujito/youtubeUnblock)** [OSS] — YouTube-focused SNI/DPI bypass for Linux, OpenWrt and Entware using NFQUEUE or a kernel module; **not** a Windows/mobile client.
- **[Floweryguard](https://github.com/KarlMerkel/Floweryguard)** [OSS] — Windows DPI-bypass utility and tethering/TTL helper; verify strategies for your network.
- **[DesyncDroyd](https://github.com/sigmabosshvh/DesyncDroyd)** — Android client incorporating zapret2 via Shizuku; review permissions and device compatibility.
- **[ByeDPI Manager](https://github.com/romanvht/ByeDPIManager)** [OSS] — Windows GUI for ByeDPI and ProxiFyre-based traffic redirection.
- **[ByeByeDPI](https://github.com/romanvht/ByeByeDPI)** [OSS] — Android local DPI bypass with routed traffic; distinct from the older ByeDPIAndroid project.
- **[Psiphon tunnel core](https://github.com/psiphon-labs/psiphon-tunnel-core)** [OSS] — Core of the Psiphon anti-censorship system.
- **[CensorTracker](https://github.com/censortracker/censortracker)** [OSS] — Chrome/Firefox anti-censorship extension; check current proxy requirements.
- **[CensorTracker Proxy](https://github.com/censortracker/proxy)** [OSS] — Companion client to connect extension traffic to Xray proxy configurations.
- **[ReQrypt](https://github.com/basil00/reqrypt)** [Legacy] — Older censorship circumvention mechanism; preserved as research/historical resource.
- **[Tor pluggable transports](https://support.torproject.org/tor-browser/circumvention/unblocking-tor/)** — Official overview of obfs4, Snowflake, meek and WebTunnel; distinct from generic VPN tunnels.
- **[GoodbyeDPI](https://github.com/ValdikSS/GoodbyeDPI)** [OSS] — Windows DPI-circumvention utility.
- **[ByeDPI](https://github.com/hufrea/byedpi)** [OSS] — Local DPI bypass engine.
- **[ByeDPI Android](https://github.com/dovecoteescapee/ByeDPIAndroid)** [OSS] — Android integration; older upstream, check alternatives.
- **[ByeByeDPI-x-tg](https://github.com/EwenLoy/ByeByeDPI-x-tg)** [OSS] — Android ByeDPI-based utility with additional local-proxy functionality.
- **[SwByeDPI](https://github.com/mIwr/SwByeDPI)** [OSS] — iOS-focused DPI bypass wrapper.
- **[MuseDPI](https://github.com/zondaxxx/MuseDPI)** [OSS] — DPI bypass on iOS and Android.
- **[net4people/bbs](https://github.com/net4people/bbs)** — Research discussions about circumvention techniques (also under Communities).

Strategies such as fragmentation, spoofed packets, TTL tricks and protocol camouflage can stop working or break connectivity when the network changes. Confirm client compatibility and actual results rather than treating a bypass name as a guarantee.

## Telegram connectivity and MTProto proxies

These projects are specific to Telegram transport. **Telegram MTProxy is not a general-purpose VPN exit** and does not automatically route other apps.

- **[Telemt](https://github.com/telemt/telemt)** — Rust/Tokio-based Telegram MTProxy with TLS-looking fronting and configurable server-side transport features; inspect its release/license.
- **[mtg](https://github.com/9seconds/mtg)** [OSS] — Minimal Go Telegram MTProxy server with version-2 configuration and scalable concurrent sessions.
- **[NTC MTProto 2026 discussion](https://ntc.rkn.quest/t/mtproto-%D0%B2-2026-%D0%B3%D0%BE%D0%B4%D1%83/22506)** — Community comparisons of MTProxy, Telemt and mtg under filtering; field reports are not guarantees.
- **[Official MTProxy](https://github.com/TelegramMessenger/MTProxy)** — Reference MTProto proxy server used by Telegram clients.
- **[mtproto.zig](https://github.com/sleep3r/mtproto.zig)** [OSS] — Lightweight Zig MTProto proxy for a personally operated Linux server, with TLS-looking transport and a documented control interface.
- **[tglock](https://github.com/by-sonic/tglock)** [OSS] — Desktop utility for Telegram-specific WebSocket connectivity; not a system-wide VPN.
- **[PWDTT](https://github.com/luminescq/PWDTT)** [Experimental] — Desktop WireGuard-over-VK-TURN project; depends on third-party relay behaviour and a compatible endpoint.
- **[VK TURN proxy for iOS](https://github.com/anton48/vk-turn-proxy-ios)** [Experimental] — iOS-side implementation of a VK TURN relay integration; inspect entitlements, server compatibility and trust boundaries.

**Historical note:** [WDTT Android](https://github.com/amurcanov/proxy-turn-vk-android) says it is discontinued, and its linked successor [csqtt](https://github.com/amurcanov/csqtt) is archived. Neither is presented as an actively maintained recommendation.

## DNS and DNS tunnels

- **[iodine](https://github.com/yarrick/iodine)** [OSS] — DNS tunnel carrying IPv4 packets over DNS; client and server must use compatible versions, and DNS relaying rules may restrict it.
- **[MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN)** [OSS] — DNS tunneling VPN with resilience and resolver-balancing features; distinct from ordinary encrypted DNS.
- **[StormDNS](https://github.com/nullroute1970/StormDNS)** [Experimental] — Client/server TCP-over-DNS tunnel with SOCKS interface; needs a remote endpoint, DNS delegation and encryption-key management, **not** DoH.
- **[Slipstream](https://github.com/EndPositive/slipstream)** — DNS-based covert communication/tunnel implementation; actual throughput depends on resolvers and network policy.
- **[dnstt](https://www.bamsoftware.com/software/dnstt/)** — DNS-based encrypted tunneling system; [GitHub community mirror](https://github.com/Mygod/dnstt) is not authoritative upstream.
- **[AdGuard Home](https://github.com/AdguardTeam/AdGuardHome)** [OSS] — Self-hosted filtering DNS resolver.
- **[AdGuard dnsproxy](https://github.com/AdguardTeam/dnsproxy)** [OSS] — DNS proxy with DoH/DoT/DoQ and DNSCrypt support.
- **[dnscrypt-proxy](https://github.com/DNSCrypt/dnscrypt-proxy)** [OSS] — Local encrypted-DNS forwarder.
- **[NextDNS CLI](https://github.com/nextdns/nextdns)** — DoH forwarder/client for NextDNS services.
- **[Xray DNS configuration](https://xtls.github.io/en/config/dns.html)** — Official DNS settings, routing and DNS server configuration.
- **[sing-box DNS configuration](https://sing-box.sagernet.org/configuration/dns/)** — DNS servers, rules and strategy settings.

**DoH/DoT do not tunnel arbitrary VPN traffic.** DNS tunneling carries other data inside DNS queries/responses; encrypted DNS merely protects DNS resolution. See [DNS/TUN troubleshooting](TROUBLESHOOTING.md#tun-connects-but-dns-fails).

## Routers, OpenWrt and transparent proxying

- **[Nikki](https://github.com/nikkinikki-org/OpenWrt-nikki)** [OSS] — Mihomo-based OpenWrt transparent proxy package.
- **[PassWall](https://github.com/Openwrt-Passwall/openwrt-passwall)** [OSS] — OpenWrt LuCI proxy management and traffic routing.
- **[PassWall2](https://github.com/Openwrt-Passwall/openwrt-passwall2)** [OSS] — Related OpenWrt LuCI proxy package; check support matrix before choosing between versions.
- **[luci-app-xray](https://github.com/yichya/luci-app-xray)** [OSS] — OpenWrt LuCI integration for Xray configuration.
- **[box4magisk](https://github.com/CHIZI-0618/box4magisk)** [OSS] — Root/Magisk module for Android transparent proxy using sing-box, mihomo, Xray and V2Ray.
- **[Surfing](https://github.com/GitMetaio/Surfing)** [OSS] — Root-only Magisk/KernelSU system-wide proxy based on mihomo.
- **[clash-for-linux](https://github.com/wnlen/clash-for-linux)** [OSS] — Terminal-based Linux deployment of Clash/mihomo.
- **[clashctl](https://github.com/nelvko/clashctl)** [OSS] — CLI setup and management for mihomo on headless Linux.
- **[fancyss](https://github.com/hq450/fancyss)** [OSS] — ASUS/Merlin router proxy plugin; hardware and firmware support must be checked.
- **[WayHop](https://github.com/awadak3davra/wayhop)** [OSS] [Experimental] — Browser-based sing-box policy-routing control for Entware/Keenetic and OpenWrt; pre-1.0.
- **[routeflux](https://github.com/Alaxay8/routeflux)** [OSS] — OpenWrt-native Xray subscription manager with node selection, DNS configuration and transparent routing.
- **[Asuswrt-Merlin AmneziaWG](https://github.com/william-aqn/asuswrt-merlin-amneziawg)** [OSS] — ASUS/Merlin AmneziaWG client and server addon with web UI, on supported routers.
- **[OpenClash](https://github.com/vernesong/OpenClash)** [OSS] — Mihomo/Clash-oriented OpenWrt client integration.
- **[HomeProxy](https://github.com/immortalwrt/homeproxy)** [OSS] — sing-box-based ImmortalWrt/OpenWrt proxy management.
- **[zapret2-openwrt](https://github.com/1andrevich/zapret2-openwrt)** [OSS] — OpenWrt packages for the Zapret2 DPI-bypass engine.
- **[nfqws2-keenetic](https://github.com/nfqws/nfqws2-keenetic)** [OSS] — Current-generation nfqws2 packages for Keenetic/Netcraze Entware, with documented use on some other router firmware; succeeds the unmaintained v1 packages.
- **[nfqws-keenetic-web](https://github.com/nfqws/nfqws-keenetic-web)** [OSS] — Separate web UI for installed nfqws/nfqws2 router packages; not a DPI engine itself.
- **[Zapret Web-GUI](https://github.com/avatarDD/zapret-gui)** [OSS] — Entware/OpenWrt dashboard combining nfqws2, several tunnel backends and per-destination fallback routing; review its firewall and upstream trust boundaries.
- **[Zapret Manager](https://github.com/StressOzz/Zapret-Manager)** — OpenWrt tool for managing DPI, DNS and routing integrations; upstream also promotes a paid VPN service (not endorsed here).
- **[NFQWS-MENU](https://github.com/rndnaame/nfqws-menu)** — Community Entware/Keenetic manager for nfqws/nfqws2 packages and contributed strategies; not the original engine or an official installer.
- **[singA](https://github.com/infinjest/singA)** [Experimental] — arm64 OpenWrt sing-box-lx TProxy gateway with XHTTP/AWG2-oriented routes and web GUI, only tested upstream on a specific Netis NX31/OpenWrt build; license not verified.
- **[Podkop](https://github.com/itdoginfo/podkop)** [OSS] [Beta] — OpenWrt sing-box selective routing; needs OpenWrt 24.10+ and modifies DNS/proxy configuration; read its telemetry caveat for the optional alternative installer.
- **[XKeen](https://github.com/jameszeroX/XKeen)** [OSS] — Keenetic/Netcraze selective TCP/UDP proxy-routing manager using Xray or mihomo; distinct from local DPI desynchronization.

- **[ByeDPI OpenWrt](https://github.com/1andrevich/ByeDPI-OpenWrt)** — OpenWrt package builds for the ByeDPI engine.
- **[Re:Sputnik](https://github.com/1andrevich/re-sputnik)** [OSS] — Desktop wizard for deploying and managing a personal VPN router.
- **[XKeen Panel](https://github.com/Dearonski/xkeen-panel)** — Web UI for XKeen/Xray on Keenetic routers.
- **[ShellCrash](https://github.com/juewuy/ShellCrash)** [OSS] — Run sing-box or mihomo from a shell, often on routers.
- **[Tachyon](https://github.com/Dushnilin/tachyon)** [OSS] — OpenWrt sing-box / DPI-bypass / per-device routing management.
- **[v2rayA](https://github.com/v2rayA/v2rayA)** — Web GUI with transparent proxy capabilities for supported hosts (also listed under Desktop clients).

## Routing rules and geodata

- **[Russia mobile Internet allowlist data](https://github.com/hxehex/russia-mobile-internet-whitelist)** — Community-observed domains/IPs accessible during some mobile-network restrictions; data varies by ISP/time and is **not** a guaranteed bypass.
- **[russia-v2ray-rules-dat](https://github.com/runetfreedom/russia-v2ray-rules-dat)** — Auto-updated routing data for Russian domains/networks and blocking-related rules.
- **[ITDOG allow-domains](https://github.com/itdoginfo/allow-domains)** — Curated domain lists relevant to local filtering and split routing; check licensing and update cadence.
- **[v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat)** — Enhanced GeoIP/geosite rule sets.
- **[Loyalsoldier GeoIP](https://github.com/Loyalsoldier/geoip)** — GeoIP data in formats used by Xray, sing-box and mihomo.
- **[sing-geosite](https://github.com/SagerNet/sing-geosite)** — Geosite rules for sing-box.
- **[sing-geoip](https://github.com/SagerNet/sing-geoip)** — GeoIP rules for sing-box.
- **[meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat)** — Mihomo routing data.
- **[domain-list-community](https://github.com/v2fly/domain-list-community)** — Community-maintained domain lists for V2Ray geosite.
- **[v2fly GeoIP](https://github.com/v2fly/geoip)** — GeoIP database generation.
- **[ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)** — Routing rules, scripts and policy assets for multiple proxy clients.
- **[Loyalsoldier Clash rules](https://github.com/Loyalsoldier/clash-rules)** — Rules for older Clash Premium variants; check compatibility with modern mihomo.

Rule formats are **not automatically interchangeable**: `geoip.dat`, `geosite.dat`, `.srs`, `.mrs`, `.mmdb`, YAML rules and subscription formats differ. Use the format supported by the specific core and release.

## Diagnostics and measurements

- **[DPI Detector](https://github.com/Runnin4ik/dpi-detector)** [OSS] — Detect DNS, TCP/TLS, HTTP filtering and suspicious connection truncation; results are network-specific.
- **[blockcheckw](https://github.com/rcd27/blockcheckw)** [OSS] — Parallel Zapret2 blockcheck strategy-search wrapper with real-content follow-up checks; its block-type classification remains a diagnostic heuristic.
- **[DPI Checkers](https://github.com/hyperion-cs/dpi-checkers)** [OSS] — Web/browser-facing and low-level censorship testing tools.
- **[TSPU Probe](https://github.com/stpavel/tspu-probe)** — Android-focused VPN/TLS/VLESS diagnostics; a probe result is not a universal verdict.
- **[RKN Block Checker](https://github.com/MayersScott/rkn-block-checker)** [OSS] — Layer-by-layer DNS, TCP, TLS and HTTP diagnostics for restrictions on authorized networks.
- **[Prosvet](https://github.com/Derposd/prosvet)** [OSS] — Measurement-only utility with DNS, IP/SNI, TLS/QUIC and throttling checks; publishes local reports and optional public measurements, not a VPN.
- **[YT-DPI](https://github.com/Shiperoid/YT-DPI)** [OSS] — Windows PowerShell/Linux/macOS Bash diagnostics for YouTube/Google DNS, TLS, QUIC and path failures; no bypass engine.
- **[TiredVPN transport measurements](https://github.com/tiredvpn/tiredvpn-measurements)** [Data] — Maintainer-run dated ISP/transport handshake data; not an independent or exhaustive proxy effectiveness benchmark.
- **[VPN Traffic Obfuscation Lab](https://github.com/maxlluky/VPN-Traffic-Obfuscation-Lab)** [OSS] — Reproducible Docker lab comparing packet inspection and obfuscation approaches (research).
- **[Ladon](https://github.com/belotserkovtsev/Ladon)** [OSS] — Reactive DNS/TCP/TLS/HTTP censorship classifier for Linux gateways and OPNsense, producing ipset/routing decisions rather than acting as a VPN.
- **[RKNHardering](https://github.com/xtclovver/RKNHardering)** [OSS] — Android diagnostic checks for VPN/proxy detection, including interface signals and IP comparisons; results are **heuristics**, not a guarantee of invisibility.
- **[DPYProxy](https://github.com/UPB-SysSec/DPYProxy)** [OSS] — Research proxy for testing DPI/DNS censorship evasion mechanisms, including automatic DNS circumvention experiments.
- **[SonicDPI](https://github.com/by-sonic/sonicdpi)** — Rust-based cross-platform DPI-bypass experiment; applicability and independent security review unverified.
- **[Geneva](https://github.com/Kkevsterrr/geneva)** [OSS] — Academic censorship-evasion strategy exploration using generated packet-manipulation strategies; research-grade, not a plug-and-play VPN.
- **[xray-knife](https://github.com/lilendian0x00/xray-knife)** [OSS] — CLI diagnostics and utilities for Xray/sing-box connections; use only on authorized endpoints.
- **[xray-checker](https://github.com/kutovoys/xray-checker)** [OSS] — Prometheus exporter for checking Xray proxy availability, latency and operational health.
- **[OONI Probe](https://github.com/ooni/probe)** [OSS] — Internet censorship measurement client.
- **[OONI Probe CLI](https://github.com/ooni/probe-cli)** [OSS] — CLI measurement and testing engine.
- **[OONI Explorer](https://explorer.ooni.org/)** — Public censorship measurement datasets.
- **[M-Lab](https://www.measurementlab.net/)** — Network performance measurement and datasets.
- **[Wireshark](https://www.wireshark.org/)** — Packet capture and protocol inspection.
- **[tcpdump](https://www.tcpdump.org/)** — CLI packet capture.
- **[mtr](https://github.com/traviscross/mtr)** — Traceroute and latency/loss diagnostics.
- **[iperf3](https://github.com/esnet/iperf)** — Throughput testing between controlled endpoints.
- **[curl](https://curl.se/)** — HTTP/TLS and proxy request verification.
- **[DNS leak test](https://www.dnsleaktest.com/)** — Check public-facing DNS resolvers (not a substitute for packet capture).
- **[ipleak.net](https://ipleak.net/)** — IP/DNS/WebRTC exposure checks (third-party service).
- **[NTC top](https://ntc.party/top)** — Forum's topical entry point (access may vary).
- **[NTC updates](https://ntc.rkn.quest/latest)** — Alternate NTC latest discussions index (availability may vary).

Start with the [practical diagnostic checklist](TROUBLESHOOTING.md): distinguish DNS failures from routing, TCP/UDP, MTU, TLS and TUN-specific problems.

## Documentation and configuration examples

- **[RKNHardering detection reference](https://xtclovver.github.io/RKNHardering/help/ru/)** — Explanations of Android VPN detection signals, with evidence-level distinctions.
- **[Zapret2 manual](https://github.com/bol-van/zapret2/blob/master/docs/manual.md)** — Original DPI-engine documentation and diagnostics.
- **[libXray](https://github.com/XTLS/libXray)** [OSS] — Maintained wrapper for embedding Xray into multi-platform apps.
- **[AndroidLibXrayLite](https://github.com/2dust/AndroidLibXrayLite)** [OSS] — Go Mobile/AAR bridge for Android Xray clients.
- **[Xray documentation](https://xtls.github.io/en/)** — Xray configuration, DNS, routing, protocols and transport reference.
- **[Xray examples](https://github.com/XTLS/Xray-examples)** — Upstream example configurations.
- **[Xray docs source](https://github.com/XTLS/Xray-docs-next)** — Documentation source and changes.
- **[V2Ray examples](https://github.com/v2fly/v2ray-examples)** — Configuration templates from the V2Fly ecosystem.
- **[sing-box documentation](https://sing-box.sagernet.org/)** — Core configuration, DNS, route rules and client information.
- **[Hysteria documentation](https://hysteria.network/)** — Hysteria 2 installation and configuration guides.
- **[3x-ui documentation](https://docs.sanaei.dev/)** — 3x-ui installation and configuration.
- **[Remnawave documentation](https://docs.rw/)** — Panel and subscription ecosystem.
- **[WireGuard quick start](https://www.wireguard.com/quickstart/)** — Basic secure tunnel configuration.
- **[frp documentation](https://gofrp.org/en/)** — Reverse tunnel configuration.
- **[GOST documentation](https://gost.run/)** — Chained forwarding, tunneling, transport and DNS reference.
- **[Xray routing rules](https://xtls.github.io/en/config/routing.html)** — Domain/IP routing and balancers.
- **[sing-box route rules](https://sing-box.sagernet.org/configuration/route/rule/)** — Rule schemas, priorities and actions.
- **[TUIC specification](https://github.com/tuic-protocol/tuic/blob/main/SPEC.md)** — Protocol design (not a runnable binary).

## Communities and reference catalogs

- **[wiki.zapret.moe: TSPU inspectors](https://wiki.zapret.moe/DPI/tspu-inspectors-checkers-2026)** — Technical comparison of censorship measurement tools and their evidentiary limits.
- **[wiki.zapret.moe: protocol index](https://wiki.zapret.moe/protocols/)** — Versioned survey of VPN, proxy and transport family differences; recheck upstream before adopting claims.
- **[Atlas RKN: how network filtering is measured](https://rkn.kitten.software/wiki/tspu-detectors/)** — Research map of independent probes, DNS and traffic-filtering evidence.
- **[Awesome Remnawave](https://docs.rw/awesome-remnawave/)** — Official curated ecosystem of management, billing, deployments, monitoring and clients.
- **[Remnawave community source list](https://github.com/remnawave/panel/blob/main/docs/awesome-remnawave.mdx)** — Source of the community curation (includes provenance and contributed projects).
- **[Awesome anti-censorship](https://github.com/danoctavian/awesome-anti-censorship)** — Additional anti-censorship research/software directory; check each upstream.
- **[Awesome resilient communication](https://github.com/gdamdam/awesome-resilient-communication)** — Failure-tolerant connectivity and off-grid communication projects; some are not VPNs.
- **[VPN Protocol Registry](https://github.com/steveprice-dev/vpn-protocol-registry)** — Evidence-oriented index of provider-developed protocols and obfuscation, not a client.
- **[Xray GitHub Discussions](https://github.com/XTLS/Xray-core/discussions)** — Upstream REALITY/XHTTP and client/core regressions.
- **[Remnawave GitHub Discussions](https://github.com/remnawave/panel/discussions)** — Panel deployment, extensions and community solutions.
- **[Project Xray Telegram](https://t.me/projectXray)** — Official community referenced by XTLS/Xray-core.
- **[Project XTLS channel](https://t.me/projectXtls)** — Official development news referenced by XTLS/Xray-core.
- **[Project VLESS (RU)](https://t.me/projectVless)** — Russian-language VLESS technical community linked by XTLS/Xray-core.
- **[Project XHTTP](https://t.me/projectXhttp)** — XHTTP community linked by XTLS/Xray-core.
- **[Xray UI Telegram channel](https://t.me/XrayUI)** — Channel linking 3x-ui, x-ui, s-ui and Raha.
- **[Xray UI group](https://t.me/XrayUIGroup)** — Public group linked from the official channel.
- **[Xray UI topic link](https://t.me/c/2479497161/1)** — User-contributed deep link; Telegram membership may be required.
- **[INCY Telegram](https://t.me/incy_public)** — Project community linked from INCY official releases.
- **[Clash Mi Telegram](https://t.me/ClashMiApp)** — Community linked by KaringX's Clash Mi project.
- **[v2RayTun Telegram](https://t.me/v2raytun)** — Official client release/news community linked from its GitHub README.
- **[Nikki Telegram](https://t.me/nikkinikki_org)** — OpenWrt Nikki community linked from upstream.
- **[Happ Proxy Telegram](https://t.me/happ_proxy)** — Happ-related Telegram community.
- **[v2rayN Telegram group](https://t.me/v2rayN)** — Client community linked from official v2rayN documentation.
- **[v2rayN Telegram channel](https://t.me/github_2dust)** — v2rayN release/development updates.
- **[Hysteria Telegram](https://t.me/hysteria_github)** — Hysteria project community.
- **[GOST Telegram](https://t.me/gogost)** — Proxy and tunnel chaining discussions (linked from upstream's older repository).
- **[net4people: Russia-labelled discussions](https://github.com/net4people/bbs/issues?q=is%3Aissue%20label%3ARussia)** — ISP measurements, mass IP filtering, DNS hijacking and DPI research from the technical community; individual reports are not universal.
- **[Zapret2 developer discussions](https://github.com/bol-van/zapret2/discussions)** — Current nfqws2/winws2 strategy changes, 2026 regressions and troubleshooting.
- **[nfqws2-keenetic community](https://github.com/nfqws/nfqws2-keenetic/discussions)** — Router integration issues, firmware compatibility and Entware packages.
- **[youtubeUnblock developer discussions](https://github.com/Waujito/youtubeUnblock/discussions)** — Linux/OpenWrt userspace and kernel-module troubleshooting.
- **[NoDPI Lab](https://nodpi.forumotion.com/)** — Tool-focused community forum linked by NoDPI upstream.
- **[SpoofDPI community](https://discord.gg/k7qMbqhrcH)** — Developer-linked Discord for SpoofDPI troubleshooting.
- **[Pangolin community](https://discord.gg/HCJR8Xhme4)** — Developer-linked community on zero-trust self-hosted access.
- **[Netmaker community](https://discord.gg/zRb9Vfhk8A)** — Officially linked WireGuard orchestration discussion.
- **[NTC forum](https://ntc.party/)** — Network restrictions and connectivity discussions (regional availability varies).
- **[NTC community software](https://ntc.rkn.quest/c/community-software/27)** — Upstream discussions for Zapret/ByeDPI/GoodbyeDPI and community tools.
- **[NTC circumvention methods](https://ntc.rkn.quest/c/censorship-circumvention-software/11)** — Proxy transports, anti-censorship clients, WebTunnel, XHTTP and related protocols.
- **[NTC top topics](https://ntc.party/top)** — Popular threads index; access may be blocked or transiently unavailable.
- **[NTC latest topics](https://ntc.rkn.quest/latest)** — Latest threads index; rate limiting may apply.
- **[NTC GoodCheck discussion](https://ntc.rkn.quest/t/goodcheck-%D0%B1%D0%BB%D0%BE%D0%BA%D1%87%D0%B5%D0%BA-%D0%B4%D0%BB%D1%8F-gdpi-zapret-byedpi-%D0%B0%D0%BA%D1%82%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F-%D0%B2-%D0%BF%D1%80%D0%BE%D1%84%D0%B8%D0%BB%D0%B5/10880)** — Forum-maintained multi-engine DPI checker; do not treat user-uploaded archives as audited.
- **[GHSA-5wf9-h793-w73c (Xray)](https://github.com/advisories/GHSA-5wf9-h793-w73c)** — Reviewed upstream certificate-pinning security advisory; check actual bundled/core versions and configuration.
- **[GFW Report](https://gfw.report/)** — Technical Internet censorship research and peer-reviewed publications.
- **[FOCI 2026: QUIC SNI censorship in Russia](https://www.petsymposium.org/foci/2026/foci-2026-0010.php)** — Peer-reviewed study of QUIC/SNI filtering and its measurement.
- **[FOCI 2026: Automated DNS circumvention](https://www.petsymposium.org/foci/2026/foci-2026-0001.php)** — Research on resolver/transport fallbacks and DNS filtering.
- **[PETS 2026: CensorLess](https://www.petsymposium.org/popets/2026/popets-2026-0096.php)** — Serverless censorship-circumvention research; research prototype, not a recommended anonymous VPN service.
- **[Tor Project Forum](https://forum.torproject.org/)** — Bridges, pluggable transports and Tor client troubleshooting.
- **[OpenWrt Forum](https://forum.openwrt.org/)** — Router integrations, firewall/routing configurations and third-party packages.
- **[NTC alternate host](https://ntc.rkn.quest/)** — Alternate forum host.
- **[net4people/bbs](https://github.com/net4people/bbs)** — Research-led Internet censorship-circumvention discussions.
- **[OONI](https://ooni.org/)** — Internet censorship measurement research.
- **[Awesome sing-box](https://github.com/oceanapplications/awesome-sing-box)** — Ecosystem-specific curated reference.
- **[Proxy Client Radar](https://clientsradar.com/)** — Independently maintained client activity/ranking tracker; metrics are not security audits.

## Research and curated discussions

- [Research notes: NTC, alternative awesome lists, protocol and dVPN ecosystems](RESEARCH-2026.md) — Source-by-source review, selected discussion threads, what was already in the catalog and what was deliberately excluded.
- [DPI and router research: Zapret2/ByeDPI ecosystem, current project status and specialist communities](DPI-RESEARCH-2026.md) — Source-checked additions and explicit caveats (October 2026).
- [Second DPI/client research pass: diagnostics, routers, transport measurements, current forums and Xray security advisory](DPI-RESEARCH-ROUND2-2026.md) — New source-checked references and explicit inclusion/exclusion criteria.

## Maintenance and contributing

The list favors **maintained original repositories, official distribution pages, and verifiable technical resources**. Links are not endorsements or independent security audits. Activity is a point-in-time observation, not an uptime guarantee.

- [Client directory](CLIENTS.md) — OS/architecture-aware choice guide, current sources and proprietary/legacy labels.
- [Client research notes](CLIENT-RESEARCH-2026.md) — New-project verification, sources and exclusions.
- [Latest ecosystem research](ECOSYSTEM-RESEARCH-2026.md) — Verifications, active/experimental tools, and notable compatibility reports.
- [Further transport & client research](TRANSPORT-RESEARCH-2026.md) — Verified upstream, NTC/net4people reports and explicit limitations.
- [Research notes](RESEARCH-2026.md) — Audited sources, primary discussions and editorial decisions from the October 2026 deep research.
- [Contributing guidelines](CONTRIBUTING.md) — How to propose a project, verify links, and avoid misleading compatibility claims.
- [Client compatibility matrix](COMPATIBILITY.md) — Platform, family of core, source/distribution and caveats. A supported core does **not** imply every transport is supported.
- [Troubleshooting](TROUBLESHOOTING.md) — DNS, TUN, route leaks, connectivity, reverse tunnels and tests.
- [Source and maintenance notes](MAINTENANCE.md) — Snapshot of edge cases and outdated links from the initial review.

**Last curated:** 2026-10-25. New suggestions and corrections are welcome via pull request.
