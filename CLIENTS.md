# VPN & Proxy Client Directory (October 2026)

[← Awesome VPN](README.md) · [Compatibility notes](COMPATIBILITY.md) · [Troubleshooting](TROUBLESHOOTING.md) · [Source audit](CLIENT-RESEARCH-2026.md)

> Platform-first catalog of proxy/VPN client applications and router integrations. Entries are cross-indexed here for discoverability, not ranked by speed or promised bypass reliability. **Last curated 2026-10-25.**

**Read this before choosing:** These tools do not automatically provide a VPN server or subscription. An Xray client may not fully implement every protocol/transport exposed by Xray-core; **REALITY, XHTTP, TLS, DNS, IPv6, TUN and subscriptions** require independent per-version verification. `[Closed]` means the application source is not published, even if its underlying networking core is open source. Source code in a repository alone is **not** evidence of a security audit.

**Quick navigation:** [Desktop](#windows-macos--linux-desktop) · [Android](#android-and-android-tv) · [Apple](#ios-ipados-macos-apple-tv) · [Routers/root](#routers-headless-linux-and-rooted-android) · [Install, updates, safety](#downloads-updates-and-trust)

## Windows, macOS & Linux (desktop)

| Client | Engine / family | Official project or distribution | Status / limitations |
| --- | --- | --- | --- |
| **Qeli desktop (beta)** | Dedicated Qeli protocol | [Upstream](https://github.com/litvinovtd/qeli) | **Experimental/pre-1.0**, Windows/macOS; full VPN, not an Xray GUI; see threat model |
| **Veil desktop (experimental)** | MASQUE/WireGuard | [Upstream](https://github.com/alibakhtiari/Veil) | Early stage desktop GUI; check release signing and tested platforms |
| **v2rayN** |
| **v2rayN** | Xray, sing-box, V2Fly | [Upstream](https://github.com/2dust/v2rayN) | OSS; multi-platform, signed releases; features vary with selected core |
| **v2RayTun** | Xray, AmneziaWG | [Upstream](https://github.com/LXST-CODE/v2RayTun) | Closed client; public releases/roadmap, separate platform tracks |
| **INCY** | Xray | [Upstream](https://github.com/INCY-DEV/incy-platforms) | Closed client; Windows/macOS/Linux desktop builds **pre-alpha** as of Oct 2026 |
| **OneXray** | Xray | [Upstream](https://github.com/YuanDevTeam/OneXray) | GPL-3.0; direct JSON, profiles and provider subscriptions; native installers vary |
| **GenyConnect** | Multi-protocol networking | [Upstream](https://github.com/genyleap/GenyConnect) | GPL-3.0; client and routing features depend on platform builds |
| **AnyPortal** | Xray, sing-box, mihomo, V2Ray | [Upstream](https://github.com/AnyPortal/AnyPortal) | Windows/macOS/Linux/Android source; upstream **iOS TUN currently blocked** |
| **Clash Verge Rev** | mihomo | [Upstream](https://github.com/clash-verge-rev/clash-verge-rev) | OSS; mature desktop policy routing and profiles |
| **FlClash** | mihomo | [Upstream](https://github.com/chen08209/FlClash) | OSS; desktop, Android and Android TV |
| **FlClashX** | mihomo | [Upstream](https://github.com/pluralplay/FlClashX) | GPL-3.0; community fork with Remnawave-oriented features |
| **Clash Party** | mihomo | [Upstream](https://github.com/mihomo-party-org/clash-party) | OSS; desktop GUI |
| **Throne** | sing-box | [Upstream](https://github.com/throneproj/Throne) | GPL-3.0; successor in Nekoray lineage |
| **husi** | sing-box family | [Upstream](https://github.com/xchacha20-poly1305/husi) | Source available; Windows/Linux/macOS Apple Silicon desktop builds; confirm binaries |
| **GUI.for.SingBox** | sing-box | [Upstream](https://github.com/GUI-for-Cores/GUI.for.SingBox) | GPL-3.0; cross-platform GUI |
| **sing-box-windows** | sing-box | [Upstream](https://github.com/xinggaoya/sing-box-windows) | MIT; Tauri desktop UI |
| **OneBox** | sing-box | [Upstream](https://github.com/OneOhCloud/OneBox) | Apache-2.0; macOS upstream support, other systems community/experimental |
| **Satelite Proxy** | Xray, sing-box, mihomo | [Upstream](https://github.com/zn0wii/satelite-proxy) | Newer desktop client; verify individual core versions |
| **Netch** | Mixed proxies | [Upstream](https://github.com/netchx/netch) | GPL-3.0; Windows-specific; version-dependent mode support |
| **Clash Nyanpasu** | mihomo | [Upstream](https://github.com/libnyanpasu/clash-nyanpasu) | GPL-3.0; desktop |
| **Sparkle** | mihomo | [Upstream](https://github.com/xishang0128/sparkle) | GPL-3.0; work in progress |
| **ClashX.Meta** | Clash Meta | [Upstream](https://github.com/MetaCubeX/ClashX.Meta) | AGPL-3.0; macOS menu bar |
| **ClashBar** | mihomo | [Upstream](https://github.com/Sitoi/ClashBar) | GPL-3.0; native macOS menu bar |
| **V2rayU** | V2Ray/Xray family | [Upstream](https://github.com/yanue/V2rayU) | macOS; subscriptions/share links |
| **V2RayXS** | Xray | [Upstream](https://github.com/tzmax/V2RayXS) | GPL-3.0; macOS |
| **Happ Desktop** | Xray | [Upstream](https://github.com/Happ-proxy/happ-desktop) | Closed; release repository only |
| **ShadowsocksX-NG** | Shadowsocks | [Upstream](https://github.com/shadowsocks/ShadowsocksX-NG) | GPL-3.0; macOS |
| **Invisible Man XRay** | Xray | [Upstream](https://github.com/InvisibleManVPN/InvisibleMan-XRayClient) | MIT; Windows/WPF, slower release cycle |
| **Shadowsocks Windows** | Shadowsocks | [Upstream](https://github.com/shadowsocks/shadowsocks-windows) | Legacy Windows C# app; historical reference |

## Android and Android TV

| Client | Engine / family | Official project or distribution | Status / limitations |
| --- | --- | --- | --- |
| **v2whitelist** | Xray/V2Ray | [Upstream](https://github.com/NullCoreDeveloper/v2whitelist) | GPL-3.0; Android client for experimental mobile-network allowlist scenarios; no guaranteed ISP support |
| **Qeli Android (beta)** | Dedicated Qeli protocol | [Upstream](https://github.com/litvinovtd/qeli) | Experimental; incompatible with VLESS/Reality subscription import |
| **v2rayNG** |
| **v2rayNG** | Xray, V2Fly | [Upstream](https://github.com/2dust/v2rayNG) | GPL-3.0; Android client; official GitHub releases |
| **v2RayTun** | Xray, AmneziaWG | [Upstream](https://github.com/LXST-CODE/v2RayTun) | Closed; Android/Android TV packages; GitHub and Google Play |
| **INCY** | Xray | [Upstream](https://github.com/INCY-DEV/incy-platforms) | Closed; Google Play and signed APK; Android release tags separate |
| **OneXray** | Xray | [Upstream](https://github.com/YuanDevTeam/OneXray) | GPL-3.0; Android 10+ per upstream |
| **sing-box for Android (SFA)** | sing-box | [Upstream](https://github.com/SagerNet/sing-box-for-android) | Official Android GUI; client/core version may differ |
| **NekoBox for Android** | sing-box family | [Upstream](https://github.com/MatsuriDayo/NekoBoxForAndroid) | Upstream slower-moving; check actual latest release |
| **WINGS V** | Xray, WireGuard, AmneziaWG, VK TURN | [Upstream](https://github.com/WINGS-N/WINGSV) | GPL-3.0; many additional features are root-dependent |
| **Clash Meta for Android** | mihomo | [Upstream](https://github.com/MetaCubeX/ClashMetaForAndroid) | OSS; Clash config family |
| **Clash Mi** | mihomo | [Upstream](https://github.com/KaringX/clashmi) | GPL-3.0; Flutter, Android & iOS among other systems |
| **FlClash** | mihomo | [Upstream](https://github.com/chen08209/FlClash) | OSS; Android/TV distribution |
| **FlClashX** | mihomo | [Upstream](https://github.com/pluralplay/FlClashX) | GPL-3.0; Remnawave-related fork, Android/TV |
| **husi** | sing-box family | [Upstream](https://github.com/xchacha20-poly1305/husi) | Source available; advanced Android client |
| **Karing** | sing-box family | [Upstream](https://github.com/KaringX/karing) | OSS; Android/iOS and other platforms |
| **Hiddify** | sing-box family | [Upstream](https://github.com/hiddify/hiddify-app) | Source available; multi-platform subscriptions |
| **Exclave** | libexclavecore | [Upstream](https://github.com/ExclaveNetwork/Exclave) | Android client, custom core; verify desired protocols |
| **YumeBox** | mihomo | [Upstream](https://github.com/YumeYucca/YumeBox) | AGPL-3.0; niche Android GUI, upstream docs limited |
| **Shadowsocks Android** | shadowsocks-rust | [Upstream](https://github.com/shadowsocks/shadowsocks-android) | OSS; Shadowsocks-specific rather than generic Xray |
| **SimpleXray** | Xray | [Upstream](https://github.com/lhear/SimpleXray) | MPL-2.0; minimal Android GUI |
| **AnyPortal** | Xray, sing-box, mihomo, V2Ray | [Upstream](https://github.com/AnyPortal/AnyPortal) | Android variant uses its own core integration; verify TUN permissions |
| **Xray (SaeedDev94)** | Xray | [Upstream](https://github.com/SaeedDev94/Xray) | MIT; lightweight Android GUI |
| **Outline** | Outline | [Upstream](https://github.com/OutlineFoundation/outline-apps) | OSS; compatible with Outline server, not arbitrary Xray |
| **Amnezia VPN** | AmneziaWG, WireGuard, Xray integrations | [Upstream](https://github.com/amnezia-vpn/amnezia-client) | OSS; self-hosted VPN client/server ecosystem |

## iOS, iPadOS, macOS, Apple TV

| Client | Engine / family | Official project or distribution | Status / limitations |
| --- | --- | --- | --- |
| **sing-box for Apple** | sing-box | [Upstream](https://github.com/SagerNet/sing-box-for-apple) | Official Apple client source; iOS/macOS/tvOS |
| **INCY** | Xray | [Upstream](https://apps.apple.com/us/app/incy/id6756943388) | Closed; official App Store; Mac and Apple TV availability can be device/store-specific |
| **v2RayTun** | Xray, AmneziaWG | [Upstream](https://github.com/LXST-CODE/v2RayTun) | Closed; separate iOS/macOS tracks; storefront-region restrictions |
| **OneXray** | Xray | [Upstream](https://apps.apple.com/us/app/onexray/id6745748773) | Open-source client; [source](https://github.com/YuanDevTeam/OneXray) |
| **Clash Mi** | mihomo | [Upstream](https://apps.apple.com/us/app/clash-mi/id6744321968) | Open-source client; [source](https://github.com/KaringX/clashmi) |
| **Karing** | sing-box | [Upstream](https://github.com/KaringX/karing) | OSS; official repo and App Store versions differ |
| **Hiddify** | sing-box | [Upstream](https://github.com/hiddify/hiddify-app) | Source available; iOS store builds/releases may differ |
| **V2Box** | Xray-family + multiple tunnels | [Upstream](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690) | Closed; store listing includes MasterDNS and DNSTT; not all modes are a remote VPN |
| **Shadowrocket** | Multi-protocol proxy | [Upstream](https://apps.apple.com/us/app/shadowrocket/id932747118) | Paid/closed; proprietary core and format |
| **Streisand** | Xray | [Upstream](https://apps.apple.com/us/app/streisand/id6450534064) | Closed; storefront availability varies |
| **Happ** | Xray | [Upstream](https://happ.info/) | Closed; official download site |
| **Stash** | Rules/proxy engine | [Upstream](https://stash.ws/ios) | Paid/closed; policy rules, scripting |
| **Loon** | Multi-protocol utility | [Upstream](https://apps.apple.com/us/app/loon/id1373567447) | Paid/closed; routing and scripting |
| **Quantumult X** | Multi-protocol utility | [Upstream](https://apps.apple.com/us/app/quantumult-x/id1443988620) | Paid/closed; custom rules and scripting |
| **Surge 5** | Network rule engine | [Upstream](https://apps.apple.com/us/app/surge-5/id1442620678) | Closed; advanced routing/debugging, review purchase options |
| **Egern** | Proxy utility | [Upstream](https://apps.apple.com/us/app/egern/id1616105820) | Closed; check current subscription/protocol support |
| **SwByeDPI** | Local DPI bypass | [Upstream](https://github.com/mIwr/SwByeDPI) | Not a remote VPN exit |
| **MuseDPI** | Local DPI bypass | [Upstream](https://github.com/zondaxxx/MuseDPI) | Not a remote VPN exit |

## Routers, headless Linux and rooted Android

| Client | Engine / family | Official project or distribution | Status / limitations |
| --- | --- | --- | --- |
| **WayHop** | sing-box policy routing | [Upstream](https://github.com/awadak3davra/wayhop) | MIT; OpenWrt/Entware/Keenetic; pre-1.0, not a desktop VPN client |
| **routeflux** | Xray | [Upstream](https://github.com/Alaxay8/routeflux) | MIT; OpenWrt native, profile selection, DNS and transparent proxy |
| **Asuswrt-Merlin AmneziaWG** | AmneziaWG | [Upstream](https://github.com/william-aqn/asuswrt-merlin-amneziawg) | MIT; firmware- and hardware-dependent ASUS router addon |
| **OpenClash** |
| **OpenClash** | mihomo/Clash | [Upstream](https://github.com/vernesong/OpenClash) | OSS; OpenWrt integration |
| **Nikki** | mihomo | [Upstream](https://github.com/nikkinikki-org/OpenWrt-nikki) | GPL-3.0; OpenWrt 24.10+, kernel 5.13+, firewall4 per upstream |
| **PassWall** | Xray, sing-box + multiple options | [Upstream](https://github.com/Openwrt-Passwall/openwrt-passwall) | GPL-3.0; LuCI OpenWrt |
| **PassWall2** | Proxy cores configurable | [Upstream](https://github.com/Openwrt-Passwall/openwrt-passwall2) | GPL-3.0; different deployment path from PassWall |
| **HomeProxy** | sing-box | [Upstream](https://github.com/immortalwrt/homeproxy) | ImmortalWrt ARM64/AMD64 context per upstream |
| **ShellCrash** | sing-box, mihomo | [Upstream](https://github.com/juewuy/ShellCrash) | Router/headless shell tool |
| **fancyss** | V2Ray/Xray | [Upstream](https://github.com/hq450/fancyss) | ASUS/Merlin firmware-specific |
| **luci-app-xray** | Xray | [Upstream](https://github.com/yichya/luci-app-xray) | MPL-2.0; OpenWrt LuCI integration |
| **clash-for-linux** | mihomo | [Upstream](https://github.com/wnlen/clash-for-linux) | MIT; command-line Linux |
| **clashctl** | mihomo | [Upstream](https://github.com/nelvko/clashctl) | MIT; headless Linux setup |
| **Surfing** | mihomo | [Upstream](https://github.com/GitMetaio/Surfing) | GPL-3.0; root-only Magisk/KernelSU module |
| **box4magisk** | Xray, V2Ray, sing-box, mihomo | [Upstream](https://github.com/CHIZI-0618/box4magisk) | GPL-3.0; root-only Android transparent proxy |
| **ClashBox** | mihomo | [Upstream](https://github.com/xiaobaigroup/ClashBox) | Native HarmonyOS NEXT ArkTS client; not Android APK |
| **Hey** | Network tunnel / protocol debug | [Upstream](https://github.com/popsiclelmlm/Hey) | GPL-3.0; native HarmonyOS NEXT, separate from Android APKs |

## Downloads, updates and trust

1. **Prefer original upstream**: the linked project GitHub repository, linked official GitHub Releases, developer website, or the developer's verified App Store/Google Play page. Beware of mirror sites using the same product name.
2. **Different clients need different configuration formats.** Xray JSON is not Mihomo YAML; v2ray subscription URI lists are not interchangeable with arbitrary sing-box rule-set JSON. See [COMPATIBILITY.md](COMPATIBILITY.md).
3. **Version numbers belong to distribution tracks.** A client may have independent Android, desktop, macOS and iOS releases. Never compare them as if they were one version timeline.
4. **Closed-source disclosure matters.** INCY, v2RayTun and Happ use public repositories for documentation, downloads, roadmap and issue tracking, but that is not proof of complete client source. App Store availability can differ by Apple ID country.
5. **Android Obtainium** can watch GitHub releases, but verify release-tag and APK filters: for example, [INCY publishes a platform-specific Obtainium configuration](https://github.com/INCY-DEV/incy-platforms/blob/main/README.md#android-updates-with-obtainium). Never install the wrong platform build just because it shares the repository.
6. **Check package signatures** if published by upstream; compare update channel, file hash/size and expected app ID before installing. Do not trust unverified repacks.
7. **Do not assume a proxy equals a privacy VPN.** Local DPI workarounds, SSH tunneling, a remote VPN exit and a private mesh have different security properties.
8. **Never paste private subscription URLs or keys** into public issues, untrusted validation sites, or community screenshots.

## What we intentionally do not assert

- No universal, manually tested checklist of VLESS/REALITY/XHTTP/TUIC/Hysteria2 compatibility across every release.
- No universal Android per-app bypass, VPN hotspot forwarding, DNS leak protection or kill-switch guarantees.
- No claim that store ratings, GitHub stars or a new commit imply security.
- No claim that App Store appearance on macOS/visionOS means a dedicated fully native build.
- No claim that this catalog has installed or reverse-engineered all clients.

Consult the original GitHub issue tracker or release notes for device-specific reports. To report a broken link or newly launched client, see [CONTRIBUTING.md](CONTRIBUTING.md).
