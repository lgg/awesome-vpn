# Transport, MTProto and censorship research — 2026-10-25

[← Main catalog](README.md) · [Client directory](CLIENTS.md) · [Compatibility](COMPATIBILITY.md) · [Troubleshooting](TROUBLESHOOTING.md) · [Previous research](ECOSYSTEM-RESEARCH-2026.md)

This is a dated, **source-checked editorial record**. Project availability, GitHub commit date and an author's feature claims are *not* security audits or interoperability tests. The list favors original source and documentation rather than random APK mirrors, free proxy lists and anonymous Telegram downloads.

## What was missing and is now included

| Area | Project | What the official source establishes | Limitations |
| --- | --- | --- | --- |
| Android multi-protocol | [L×Box](https://github.com/Leadaxe/LxBox) | GPL-3.0 client using [sing-box-lx](https://github.com/Leadaxe/sing-box-lx), covering XHTTP, VLESS/REALITY, AmneziaWG, MASQUE/WARP and more | Fork-specific implementation; do not assume stock sing-box parity; check current build |
| Android firewall | [Rethink DNS + Firewall](https://github.com/celzero/rethink-app) | Apache-2.0 Android DNS/firewall/WireGuard proxifier | Not an Xray/v2rayN clone or generic VLESS URI importer |
| Desktop DPI | [SpoofDPI](https://github.com/xvzc/spoofdpi) | Apache-2.0 local DPI tool; project's README explicitly excludes iOS and Android | No remote VPN exit or official phone app |
| Desktop DPI | [DPIBreak](https://github.com/dilluti0n/dpibreak), [GreenTunnel](https://github.com/SadeghHayeri/GreenTunnel) | System/local DPI manipulation utilities | Network-specific effectiveness, distinct from remote proxy/VPN |
| Apple DPI | [Spoofy](https://github.com/ringolol/Spoofy) | MIT local HTTP/SOCKS5 proxy; supports TLS fragmentation and optional Outline | **Not system-wide iOS VPN**; sideload or application/Wi-Fi proxy; no cellular-wide coverage |
| Routing diagnostics | [Ladon](https://github.com/belotserkovtsev/Ladon) | MIT gateway/OPNsense reactive probes across DNS/TCP/TLS/HTTP; ipset/routing outputs | Classifier, not a standalone VPN and not definitive proof of censorship |
| WireGuard proxy | [wireproxy](https://github.com/windtf/wireproxy), [wireproxy-awg](https://github.com/artem-russkikh/wireproxy-awg) | Userspace WireGuard and AWG connection exposed as HTTP/SOCKS proxy | Not general TUN; main wireproxy README lists SOCKS UDP as unimplemented |
| WireGuard camouflage | [wg-obfuscator](https://github.com/ClusterM/wg-obfuscator) | GPL-3.0 UDP obfuscator independent of the WireGuard binary | **Requires matched components at both ends**; does not itself provide a VPN |
| Private access / mesh | [Pangolin](https://github.com/fosrl/pangolin), [Netmaker](https://github.com/gravitl/netmaker) | WireGuard-based remote access / virtual-network orchestration | Different product/license tiers; not anonymity or guaranteed censorship bypass |
| Self-hosted VPN | [Algo VPN](https://github.com/trailofbits/algo) | AGPL-3.0 Ansible installer for personal WireGuard/IKEv2 | Upstream explicitly **disclaims censorship evasion/anonymity guarantees** |
| DNS tunnel | [iodine](https://github.com/yarrick/iodine) | ISC implementation carrying IPv4 inside DNS requests/responses | Requires control of authoritative domain/server; client/server version compatibility; not DoH |
| HTTP relay | [MasterHttpRelayVPN Rust](https://github.com/therealaleph/MasterHttpRelayVPN-RUST) | MIT Google Apps Script relay-based prototype | Reliance on external infrastructure, quota, terms of service and trust; marked experimental |
| Telegram | [Official MTProxy](https://github.com/TelegramMessenger/MTProxy), [Telemt](https://github.com/telemt/telemt), [mtg](https://github.com/9seconds/mtg), [mtproto.zig](https://github.com/sleep3r/mtproto.zig) | Different MTProto server implementations (C, Rust, Go and Zig) | **Telegram-specific**, not a system VPN; proxy latency, fronting and middle-ends vary |
| Telegram desktop | [tglock](https://github.com/by-sonic/tglock) | MIT Rust/egui Telegram-specific connectivity utility | Only Telegram traffic; inspect transport and security claims |
| TURN experiments | [PWDTT](https://github.com/luminescq/PWDTT), [VK TURN proxy for iOS](https://github.com/anton48/vk-turn-proxy-ios) | Client implementations using TURN/relay transports | Experimental, external relay dependency, support can cease |
| Other protocol/transport | [Brook](https://github.com/txthinking/brook), [Shadowsocks v2ray-plugin](https://github.com/shadowsocks/v2ray-plugin) | Independently implemented proxy platform, and SIP003 transport plugin for Shadowsocks | Distinct configuration and server-side compatibility requirements |

## Specialist communities and active 2026 technical reports

### NTC: software authors, regional DPI and real-world troubleshooting

- [Community software](https://ntc.rkn.quest/c/community-software/27) — October 2026 activity around Zapret2, ByeDPI, automatic strategy selection and filtering measurements.
- [Circumvention methods & software](https://ntc.rkn.quest/c/censorship-circumvention-software/11) — TLS/XHTTP, VPN protocols, DNS tunneling, Tor bridges and mobile routing.
- [MTProto in 2026](https://ntc.rkn.quest/t/mtproto-%D0%B2-2026-%D0%B3%D0%BE%D0%B4%D1%83/22506) — user comparisons of mtg and Telemt, with a wide range of ISP-specific outcomes.
- [Reactive Ladon Anti-DPI](https://ntc.rkn.quest/t/ladon-%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9-%D0%BE%D0%B1%D1%85%D0%BE%D0%B4-dpi-%D0%B1%D0%BB%D0%BE%D0%BA%D0%B8%D1%80%D0%BE%D0%B2%D0%BE%D0%BA/24686) — author introduction, how DNS/TLS probing maps to routing decisions.
- [iOS ByeDPI alternatives, including Spoofy](https://ntc.rkn.quest/t/%D0%B0%D0%BD%D0%B0%D0%BB%D0%BE%D0%B3-byedpi-%D0%B4%D0%BB%D1%8F-ios-%E2%80%94-rumble/19150) — ecosystem discovery only; verify iOS Network Extension and cellular routing claims in the project's own documentation.
- [Slipstream/dnstt relevance discussion](https://ntc.rkn.quest/c/censorship-circumvention-software/11) — ongoing community field reports, not proof of universal transport availability.

**Reading rule:** distinguish the report date, access ISP, test host, packet size, DNS path and actual transport. A successful browser test does not prove general traffic tunneling.

### net4people: research issue threads

The [net4people/bbs issue forum](https://github.com/net4people/bbs/issues) is especially valuable for technical evidence, measurement methodology and counterexamples.

- [#671 — recent mass IP bans in Russia](https://github.com/net4people/bbs/issues/671) (opened 2026-09-30).
- [#663 — possible TUN detection at DPI level?](https://github.com/net4people/bbs/issues/663) (opened 2026-09-02). **A question and hypothesis, not an established detection mechanism.**
- [#662 — Cloudflare reachability from one Moscow AS follows IP prefix, not hostname](https://github.com/net4people/bbs/issues/662) (opened 2026-09-02). A **single AS-specific observation**.
- [#657 — DNS hijacking in Russia](https://github.com/net4people/bbs/issues/657) (opened 2026-08-26).
- [#658 — Fountain codes in censorship circumvention rendezvous (FOCI 2026)](https://github.com/net4people/bbs/issues/658) (opened 2026-08-27).
- [Russia-labelled net4people threads](https://github.com/net4people/bbs/issues?q=is%3Aissue%20label%3ARussia) — active filtering/research context.

### Direct developer communities

- [SpoofDPI Discord](https://discord.gg/k7qMbqhrcH) — linked from upstream README.
- [Pangolin Discord](https://discord.gg/HCJR8Xhme4) — linked from upstream README; focuses on zero-trust access.
- [Netmaker Discord](https://discord.gg/zRb9Vfhk8A) — linked from upstream README; focused on WireGuard mesh management.
- [NTC](https://ntc.rkn.quest/), [Tor Forum](https://forum.torproject.org/) and [OpenWrt Forum](https://forum.openwrt.org/) remain useful for different network-layer questions.

## Exclusions and status checks

- **WDTT Android** ([amurcanov/proxy-turn-vk-android](https://github.com/amurcanov/proxy-turn-vk-android)) explicitly declares the project discontinued in its README. Its linked [csqtt](https://github.com/amurcanov/csqtt) was marked **archived** by the GitHub API on 2026-10-25. Kept as historic context only, not a current install recommendation.
- **A little-known new project is not inherently safer or better** than established Xray/WireGuard: no independent code audit is implied by stars, MIT/GPL license, claimed obfuscation or a recent push.
- **Bypass tool ≠ VPN.** SpoofDPI, GreenTunnel, Spoofy, Ladon and wg-obfuscator serve different operational layers. Server-side MTProxy cannot be reused as a general HTTP VPN.
- **VPN ≠ anonymity.** Pangolin/Netmaker/Algo are chiefly private connectivity tools. VPN egress, logging, access policy and traffic analysis each require an independent assessment.
- **No public exit-node dumps** or self-described "free unlimited VPN" providers are mirrored into this directory.
- **Protocol compatibility is empirical.** Check exact client, server, core/fork, firmware and transport versions and avoid copying test results across operators/ASNs without evidence.

All new entries were checked against their upstream GitHub repository metadata and, for key projects, their original README in October 2026. This was *not* a hands-on installation on every supported OS or an external-link crawl of every web forum page.
