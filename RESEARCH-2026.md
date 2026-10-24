# Research notes: VPN ecosystem, NTC and source lists (October 2026)

[← Back to README](README.md) · [Compatibility](COMPATIBILITY.md) · [Troubleshooting](TROUBLESHOOTING.md)

**Research snapshot:** 2026-10-25. This file records what was actually found and why projects were included or omitted. It is not a live availability feed or a promise that a tool works on every ISP. GitHub existence/activity, release reliability and independent security audits are distinct questions.

## 1. NTC (No Thought is a Crime) — primary technical forum

- [Latest topics](https://ntc.rkn.quest/latest) — discover current network filtering reports and fresh client releases.
- [Popular topics](https://ntc.party/top) — popularity-based discovery; check freshness separately.
- [Community software](https://ntc.rkn.quest/c/community-software/27) — dedicated discussions for Zapret, ByeDPI, GoodbyeDPI, dnstt and community utilities.
- [Circumvention methods & software](https://ntc.rkn.quest/c/censorship-circumvention-software/11) — proxy transports, network protocols, clients and methods.
- [Research and publications](https://ntc.rkn.quest/c/censorship-research-and-publications/19) — forum category link subject to upstream path changes.

**Access caveat:** During this pass, direct fetches to `ntc.party/top` returned 502 and `ntc.rkn.quest/latest` intermittently returned 429; indexed topic/category pages were used. **Do not interpret this as a comprehensive review of every latest/top post.** Forum comments are user claims until reproduced or corroborated upstream.

### Discussion threads worth following

| Thread | Why it matters | Source |
| --- | --- | --- |
| Zapret2 discussion | Development, Lua-based strategies, `nfqws2` and `blockcheck2` edge cases | [NTC](https://ntc.rkn.quest/t/zapret2-обсуждение/21161) |
| Zapret changes / blockcheck2 | Original author's announcements, auto-testing workflow and deprecation of v1 | [NTC](https://ntc.rkn.quest/t/zapret-whats-new/61) |
| B-Checker for ByeDPI | Windows strategy-search wrapper; checks DNS, IP-specific filtering and response cutoffs | [NTC](https://ntc.rkn.quest/t/b-checker-авто-подбор-и-сохранение-стратегий-byedpibyebyedpi-батник-для-windows/14291) |
| Zapret Checker | Strategy-search scripts for Windows; verify exact release source rather than unreviewed community archives | [NTC](https://ntc.rkn.quest/t/zapret-checker-авто-подбор-и-сохранение-стратегий-windows/23814) |
| Android DesyncDroyd | Zapret2 + Android/Shizuku implementation and reported limitations | [NTC](https://ntc.rkn.quest/t/desyncdroyd-zapret2-на-android-без-root-с-автоподбором-стратегий/25826) |
| SKIPI (SkipIt) | Community discussion of Xray/VLESS/Reality/Hysteria clients; verify actual platform list in upstream | [NTC](https://ntc.rkn.quest/t/skipi-современный-open-source-клиент-для-xray-vless-reality-hysteria-2-на-android-и-desktop/25690) |
| L×Box | sing-box/AmneziaWG-related client discussion; insufficient verified upstream to recommend yet | [NTC](https://ntc.rkn.quest/t/l%C3%97box/25262) |
| MasterDnsVPN experiences | DNS tunnel field reports; not proof of general ISP compatibility | [NTC](https://ntc.rkn.quest/c/community-software/27) |
| XHTTP | Useful discussion of practical transport compatibility, behavior and troubleshooting | [NTC category](https://ntc.rkn.quest/c/censorship-circumvention-software/11) |
| VPN vs DPI desync | Clear distinction between filtering-specific desynchronization and tunneling through remote servers | [NTC](https://ntc.rkn.quest/t/vpn-vs-dpi-desync-в-рф/26265) |
| VPN/Android detection checks | Background and user reports linked to RKNHardering | [NTC](https://ntc.rkn.quest/t/android-приложение-для-проверки-устойчивости-обхода-по-методичке-минцифры/23888) |

**Best engineering insight:** Separate **DNS resolution**, **IP filtering**, **TLS/QUIC filtering**, **response-size cutoff**, **VPN transport blocking** and **application-level routing**. A single strategy/test can report success while the actual browser fails; collect real per-protocol outcomes, packet captures where authorized, and versioned configuration before claiming a fix. These practices are also reflected in [Troubleshooting](TROUBLESHOOTING.md).

## 2. Requested GitHub repositories — reviewed

| Source | Status in this list | Further useful discovery |
| --- | --- | --- |
| [WINGS V](https://github.com/WINGS-N/WINGSV) | Already listed; kept as an Android client | [WINGS V DeX](https://github.com/WINGS-N/WINGSV_DeX), [control panel](https://github.com/WINGS-N/wingsv-panel), [VK TURN proxy](https://github.com/WINGS-N/vk-turn-proxy), [3x-ui fork](https://github.com/WINGS-N/3x-ui), and separate [swgPanel](https://github.com/SanityProtocol/swg-panel). |
| [Bedolaga Remnawave Bot](https://github.com/BEDOLAGA-DEV/remnawave-bedolaga-telegram-bot) | Already listed; remains under subscriptions/billing | [Bedolaga Cabinet](https://github.com/BEDOLAGA-DEV/bedolaga-cabinet) is a companion web project. |
| [MasterDnsVPN](https://github.com/masterking32/MasterDnsVPN) | Already listed in DNS tunnels | Compare architecture and network needs with [Slipstream](https://github.com/EndPositive/slipstream) and other DNS transport work. |
| [MuseDPI](https://github.com/zondaxxx/MuseDPI) | Already listed; iOS/Android local DPI bypass | Keep separate from remote proxy/VPN clients. |
| [RKNHardering](https://github.com/xtclovver/RKNHardering) | Moved to diagnostics for a clearer classification | [Detection reference](https://xtclovver.github.io/RKNHardering/help/ru/), [Telegram](https://t.me/RKNHardering), and [Matrix](https://matrix.to/#/%23RKN_Hardering:matrix.kangel.tech). This is a *detection/test application*, not a VPN. |

## 3. Other awesome lists — screened, not blindly copied

### [awesome-foss/awesome-sysadmin — VPN section](https://github.com/awesome-foss/awesome-sysadmin#vpn)

A curated, broader sysadmin catalog with proven general-purpose options. New relevant entries include [DefGuard](https://github.com/DefGuard/defguard), [Gluetun](https://github.com/passteque/gluetun), [sshuttle](https://github.com/sshuttle/sshuttle) and [strongSwan](https://github.com/strongswan/strongswan). Firezone, Headscale, Nebula, OpenVPN and SoftEther were already in Awesome VPN.

The list also includes [ocserv](https://gitlab.com/openconnect/ocserv), a Cisco AnyConnect-compatible server. It is intentionally linked here rather than presented as verified GitHub software, because its primary source is GitLab.

### [carmen41511/awesome-decentralized-vpn](https://github.com/carmen41511/awesome-decentralized-vpn)

Last observed GitHub push of this **source list** was 2023, so verify all projects independently. Useful leads included [Mysterium Node](https://github.com/MysteriumNetwork/node), [Sentinel dVPN](https://github.com/sentinel-official/sentinel-dvpnx), [Orbot](https://github.com/guardianproject/orbot-android) and [cjdns](https://github.com/cjdelisle/cjdns). Additional verified ecosystem entries: [Yggdrasil](https://github.com/yggdrasil-network/yggdrasil-go), [i2pd](https://github.com/PurpleI2P/i2pd), [Sentinel CLI](https://github.com/sentinel-official/sentinel-dvpncli).

**Excluded from core VPN list:** generic WebRTC/BitTorrent libraries, ordinary file sharing and blockchain infrastructure without a direct VPN/tunneling use case. The old [sentinel-official/sentinel](https://github.com/sentinel-official/sentinel) project was observed **archived** and is superseded for our scope by active dVPN node/CLI projects.

### [awesome-vpn/awesome-vpn](https://github.com/awesome-vpn/awesome-vpn)

Primarily aggregates **public, periodically refreshed proxy configurations** (YAML, sing-box JSON and base64) and client quick-start instructions. Familiar clients such as v2rayN, v2rayNG, Clash Verge Rev and NekoBox are already listed. **Do not mirror, ingest, recommend or automatically test the public exit nodes**: unknown operators may intercept traffic or disappear; the repo explicitly cautions against sensitive use. Listing this source as a research reference is not endorsement of its proxy endpoints.

## 4. Upstream source verification examples

- [Zapret2](https://github.com/bol-van/zapret2) is the author's **current-generation engine**; [zapret v1](https://github.com/bol-van/zapret) explicitly states EOL/no new features. Prefer [official documentation](https://github.com/bol-van/zapret2/blob/master/docs/manual.md), not third-party repacks.
- [Zapret2 OpenWrt builds](https://github.com/1andrevich/zapret2-openwrt) and [ByeDPI for OpenWrt](https://github.com/1andrevich/ByeDPI-OpenWrt) solve router-specific packaging problems.
- [RKNHardering](https://github.com/xtclovver/RKNHardering) describes detection signals; hiding one check does not prove a VPN is undetectable.
- [WINGS V](https://github.com/WINGS-N/WINGSV) exposes multiple subsystems (Xray, WireGuard, AmneziaWG, VK TURN); treat VK-based connection disguise as an experimental approach that depends on service/network behavior.
- [GFW Report](https://gfw.report/) is a useful **research source** with contemporary analysis of regional filtering, QUIC behavior and the censorship arms race, not a VPN client.
- [net4people/bbs](https://github.com/net4people/bbs), [Tor Project Forum](https://forum.torproject.org/) and [OpenWrt Forum](https://forum.openwrt.org/) are useful specialist communities with different focus areas.

## 5. Maintenance follow-up checklist

- [ ] Verify official latest release and signing provenance of new/experimental desktop and Android clients.
- [ ] Check whether a panel manages an **Xray core**, **sing-box core**, **WireGuard device**, or just a GUI/dashboards; do not conflate them.
- [ ] Validate remote VPN vs local desync vs DNS tunnel vs mesh network categories after adding new tools.
- [ ] Check for NTC forum domain changes and topic redirects; maintain a fallback to category URLs.
- [ ] Monitor upstream archival and repository moves (especially older awesome lists).
- [ ] Never publish private subscription URIs, Telegram invite tokens, panel credentials or raw client captures.

All entries were selected manually by topical relevance. **There has been no comprehensive installation, security audit or network-by-network functionality testing.**
