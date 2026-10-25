# Client ecosystem research — 2026-10-25

[← README](README.md) · [Client directory](CLIENTS.md) · [Compatibility](COMPATIBILITY.md) · [Earlier network research](RESEARCH-2026.md)

## Purpose and source hierarchy

This is a dated research snapshot of **VPN/proxy client applications**, not just protocols. Discovery is based on [Proxy Client Radar](https://clientsradar.com/) (public 2026-10-25 snapshots), official GitHub repositories and their READMEs, [GitHub Xray projects](https://github.com/topics/xray), [GitHub sing-box projects](https://github.com/topics/sing-box), and official vendor/store listings. Prefer **official source/download** over a mirror or aggregator claim. **Repository present, actively pushed, audited, signed and working are different properties**.

Cross-checked client examples via GitHub repository metadata (October 25): `YuanDevTeam/OneXray`, `INCY-DEV/incy-platforms`, `xchacha20-poly1305/husi`, `pluralplay/FlClashX`, `KaringX/clashmi`, `YumeYucca/YumeBox`, `Sitoi/ClashBar`, `OneOhCloud/OneBox`, `nikkinikki-org/OpenWrt-nikki`, `MetaCubeX/ClashX.Meta`, `libnyanpasu/clash-nyanpasu`, `CHIZI-0618/box4magisk`, `Openwrt-Passwall/openwrt-passwall2`, and others listed in [CLIENTS.md](CLIENTS.md).

## Requests from this round

| Project | Result | Actual upstream notes |
| --- | --- | --- |
| **v2rayNG** | Already present; indexed again in CLIENTS.md | [2dust/v2rayNG](https://github.com/2dust/v2rayNG) is **Android**, not the desktop app. |
| **v2rayN** | Already present; indexed in CLIENTS.md | [2dust/v2rayN](https://github.com/2dust/v2rayN) is **Windows, macOS and Linux** (Xray/sing-box). |
| **v2RayTun** | Already present; description expanded to desktop and Apple | [LXST-CODE/v2RayTun](https://github.com/LXST-CODE/v2RayTun) is a release/roadmap repository. Its README explicitly lists Android, Android TV, iOS, macOS, Windows, Linux and AmneziaWG; separate platform releases; not verifiable as full open-source application. |
| **INCY** | New, in README + CLIENTS.md | [INCY-DEV/incy-platforms](https://github.com/INCY-DEV/incy-platforms) distributes clients for Android/TV, iOS/Apple TV and desktop. Desktop is explicitly **pre-alpha**; application is closed-source even though Xray-core is open source. Developer maintains [docs](https://docs.incy.cc/), [official site](https://incy.cc/), and [Android Obtainium guide](https://github.com/INCY-DEV/incy-platforms#android-updates-with-obtainium). |
| **OneXray** | New | [YuanDevTeam/OneXray](https://github.com/YuanDevTeam/OneXray) is GPL-3.0 with a multi-platform application/source code, and publishes [Remnawave-specific import help](https://onexray.com/docs/servers/remnawave/). |
| **Clash Mi** | New | [KaringX/clashmi](https://github.com/KaringX/clashmi) is a mihomo client with iOS, Android and desktop releases. Source repo also contains promotional links: our catalog links **only to the official source and store**, not the promotions. |

## Newly identified client families

- **mihomo desktop and mobile:** [FlClashX](https://github.com/pluralplay/FlClashX) (Remnawave-targeted fork), [Clash Nyanpasu](https://github.com/libnyanpasu/clash-nyanpasu), [Sparkle](https://github.com/xishang0128/sparkle), [ClashX.Meta](https://github.com/MetaCubeX/ClashX.Meta), [ClashBar](https://github.com/Sitoi/ClashBar), [YumeBox](https://github.com/YumeYucca/YumeBox), [GUI.for.Clash](https://github.com/GUI-for-Cores/GUI.for.Clash), [Pandora-Box](https://github.com/snakem982/Pandora-Box) and [Prizrak-Box](https://github.com/legiz-ru/Prizrak-Box).
- **sing-box desktops:** [husi](https://github.com/xchacha20-poly1305/husi), [sing-box-windows](https://github.com/xinggaoya/sing-box-windows) and [OneBox](https://github.com/OneOhCloud/OneBox). Husi does **not** currently advertise Intel macOS desktop support; OneBox separates macOS upstream support from community/experimental Windows/Linux support.
- **OpenWrt, Linux and root Android:** [Nikki](https://github.com/nikkinikki-org/OpenWrt-nikki), [PassWall](https://github.com/Openwrt-Passwall/openwrt-passwall), [PassWall2](https://github.com/Openwrt-Passwall/openwrt-passwall2), [luci-app-xray](https://github.com/yichya/luci-app-xray), [Surfing](https://github.com/GitMetaio/Surfing), [box4magisk](https://github.com/CHIZI-0618/box4magisk), [clashctl](https://github.com/nelvko/clashctl), [clash-for-linux](https://github.com/wnlen/clash-for-linux).
- **HarmonyOS NEXT:** [ClashBox](https://github.com/xiaobaigroup/ClashBox), built with ArkTS. Native HarmonyOS NEXT is **not** the same as Android APK compatibility.
- **Older but relevant:** [ShadowsocksX-NG](https://github.com/shadowsocks/ShadowsocksX-NG), [V2RayXS](https://github.com/tzmax/V2RayXS), [V2rayU](https://github.com/yanue/V2rayU), [Netch](https://github.com/netchx/netch). [Shadowsocks Windows](https://github.com/shadowsocks/shadowsocks-windows) explicitly labeled **Legacy** because of age.

## Apple clients and proprietary software

Unlike source projects, App Store applications may disappear per country. The following are directly linked to verified Apple App Store listing pages, not third-party app mirrors:

- [INCY](https://apps.apple.com/us/app/incy/id6756943388) — closed-source Xray client; official developer [INCY](https://incy.cc/).
- [OneXray](https://apps.apple.com/us/app/onexray/id6745748773) — public [GPL-3.0 source](https://github.com/YuanDevTeam/OneXray).
- [Clash Mi](https://apps.apple.com/us/app/clash-mi/id6744321968) — public [GPL-3.0 source](https://github.com/KaringX/clashmi).
- [V2Box](https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690) — closed-source; store updates in 2026 describe **MasterDNS, DNSTT**, custom Xray routing/configs; this is not proof of tested compatibility with every server implementation.
- [Loon](https://apps.apple.com/us/app/loon/id1373567447), [Surge 5](https://apps.apple.com/us/app/surge-5/id1442620678), [Quantumult X](https://apps.apple.com/us/app/quantumult-x/id1443988620), [Egern](https://apps.apple.com/us/app/egern/id1616105820) — closed-source policy-routing/network utilities with different price/licensing and protocol combinations.
- Existing [Shadowrocket](https://apps.apple.com/us/app/shadowrocket/id932747118), [Streisand](https://apps.apple.com/us/app/streisand/id6450534064) and [Stash](https://stash.ws/ios) remain available as distinct options.

Do **not** infer features from the name alone; for example, Hysteria2 in an App Store description does not mean a particular obfuscation/transport option is supported.

## Interesting items screened but not prioritized

| Source | Why not presented as a current top recommendation |
| --- | --- |
| [mapleafgo/singcast](https://github.com/mapleafgo/singcast) | GitHub metadata implies sing-box, but the currently retrieved README still describes an older Flutter/Clash client and strikes out iOS; source of truth is inconsistent. Omitted from curated recommendations pending clarification. |
| [MatsuriDayo/nekoray](https://github.com/MatsuriDayo/nekoray) | Archived; already correctly labeled Legacy in README. |
| [MatsuriDayo/NekoBoxForAndroid](https://github.com/MatsuriDayo/NekoBoxForAndroid) | Popular but last observed repository push in Feb 2026; retained with maintenance caveat, not falsely described as frequently updated. |
| [SagerNet/SagerNet](https://github.com/SagerNet/SagerNet) | Archived Android project; modern sing-box for Android is a better default. |
| [spencerwooo/mihoro](https://github.com/spencerwooo/mihoro) | Niche Linux CLI, slow update cadence; consider adding with a maintenance caveat if expanding terminal-focused tools. |
| [666OS/ClashMac](https://github.com/666OS/ClashMac) | Closed-source macOS distribution; already many alternatives, not needed as a first-priority list entry. |
| [shadowsocks/shadowsocks-ios](https://github.com/shadowsocks/shadowsocks-ios) | Upstream reports it was removed; not a viable current iOS recommendation. |
| [xiaobaigroup/ClashBox](https://github.com/xiaobaigroup/ClashBox) | Included for native HarmonyOS NEXT, with signing/platform caveats. |
| [YumeYucca/YumeBox](https://github.com/YumeYucca/YumeBox) | Repository exists with AGPL-3.0, but default `README.md` was not retrievable in this pass; treat feature coverage as unverified beyond client family. |

## Cross-check with Xray-core's official GUI index

The upstream [XTLS/Xray-core README](https://github.com/XTLS/Xray-core#gui-clients) explicitly lists desktop, Android, Apple, OpenWrt, ASUS and HarmonyOS client projects. This is a **discovery list**, not a compatibility or security certification.

New relevant, independently verified entries:
- [AnyPortal](https://github.com/AnyPortal/AnyPortal): Windows/macOS/Linux/Android multiple-core GUI. **Important:** its own README explicitly states that iOS support is blocked by Apple Network Extension signing/entitlement work; do not list it as a functioning iOS VPN.
- [GenyConnect](https://github.com/genyleap/GenyConnect): GPL-3.0, cross-platform secure tunnel/routing application.
- [Hey](https://github.com/popsiclelmlm/Hey): native HarmonyOS NEXT tunnel and protocol-debugging app.
- [xray-knife](https://github.com/lilendian0x00/xray-knife): tooling for Xray/sing-box connection inspection and diagnostics.
- [xray-checker](https://github.com/kutovoys/xray-checker): Xray proxy health checks and Prometheus export.
- [Xray-install](https://github.com/XTLS/Xray-install): upstream's own Xray installer and upgrade tooling.
- [libXray](https://github.com/XTLS/libXray) and [AndroidLibXrayLite](https://github.com/2dust/AndroidLibXrayLite): wrappers/toolchain for clients, **not end-user VPN applications**.

The upstream list still points to [Furious](https://github.com/LorenEteval/Furious), but that GitHub repository returned **404** when checked on October 25, 2026. It was **not** added.

Officially linked Telegram communities: [Project Xray](https://t.me/projectXray), [Project XTLS channel](https://t.me/projectXtls), [Project VLESS](https://t.me/projectVless), [Project XHTTP](https://t.me/projectXhttp), plus existing [v2rayN](https://t.me/v2rayN) and [INCY](https://t.me/incy_public).

## Maintainer checklist

- Update the [platform directory](CLIENTS.md) whenever a client is added to the [main catalog](README.md).
- Don't add the same URL twice inside one README topical section; cross-listing across OS sections can be intentional.
- Keep primary GitHub sources and **platform-specific official stores** distinguishable.
- Mark app **source/distribution model** (open application code vs binary releases/closed source) separately from the underlying proxy core's license.
- Respect local/OS limitations (root, Android `VpnService`, Apple `Network Extension`, ARM64 vs x64, HarmonyOS native apps, Linux glibc).
- Run `python scripts/validate_catalog.py` before approving PRs and check external links independently where access allows.

*Snapshot date: October 25, 2026. This was an upstream metadata/documentation audit, not a security penetration test or hands-on installation of every app.*


## October 25 follow-up: verified current release channels

- **[KEQDIS](https://github.com/Lemonochka/keqdroid)** is GPL-3.0, with [v0.29.0](https://github.com/Lemonochka/keqdroid/releases/tag/v0.29.0) published 2026-10-23 containing Android APK, Windows x64 ZIP and Linux packages. Upstream describes Xray/mihomo and split tunneling, **not** an iOS release or automatically every core-specific transport. Cross-indexed in [CLIENTS.md](CLIENTS.md) and [COMPATIBILITY.md](COMPATIBILITY.md).
- **[TiredVPN Android](https://github.com/tiredvpn/tiredvpn-android)** is a separate AGPL-3.0 client for [TiredVPN](https://github.com/tiredvpn/tiredvpn), not a generic VLESS importer; [v1.11.3 APK](https://github.com/tiredvpn/tiredvpn-android/releases/tag/v1.11.3) published 2026-10-20. **Experimental**, no independent security/compatibility test was established. [TiredVPN measurement data](https://github.com/tiredvpn/tiredvpn-measurements) is from its own maintainer, not an independent benchmark.
- **[NoDPI4Android](https://github.com/GVCoder09/NoDPI4Android)** is a local DPI bypass tool rather than remote tunnel; GPL-3.0, [v2.0-beta APK](https://github.com/GVCoder09/NoDPI4Android/releases/tag/v2.0-beta) was the latest observed release. The Android VPNService limitation applies when trying to run another VPN client at the same time.
- **[singA](https://github.com/infinjest/singA)** is an experimental arm64 OpenWrt gateway rather than a general-purpose Android or desktop client. Only Netis NX31/OpenWrt 25.12.4 is explicitly reported tested; no SPDX license appeared in repository metadata, so it is not labeled OSS.
- **[NFQWS-MENU](https://github.com/rndnaame/nfqws-menu)** is a *router management script* for community nfqws strategies, and therefore does not imply a full general-purpose VPN exit or official bol-van endorsement.

Consult [the detailed second-pass research and security review](DPI-RESEARCH-ROUND2-2026.md) for exact evidence, testing scope and exclusions. Client build availability, source-code licensing, and transport compatibility remain separate checks.
