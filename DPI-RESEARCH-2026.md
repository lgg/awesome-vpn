# DPI circumvention, router integrations and technical forums — 2026-10-25

[← Catalog](README.md) · [Existing research](ECOSYSTEM-RESEARCH-2026.md) · [Troubleshooting](TROUBLESHOOTING.md)

A source-reviewed follow-up focused on **Zapret2, ByeDPI/ByeByeDPI, DPI diagnostics, OpenWrt/Keenetic and research communities**. Projects were checked against upstream repository metadata and their own README where possible on October 25, 2026. **Not** an installation test, binary-signature verification, security audit or claim of ISP-wide success. GitHub push dates are not release dates.

## Verified baseline already in the catalog

- [Zapret2](https://github.com/bol-van/zapret2) is the actively developed successor. [Zapret v1](https://github.com/bol-van/zapret) explicitly says EOL/no new features.
- [ByeDPI](https://github.com/hufrea/byedpi), [ByeByeDPI](https://github.com/romanvht/ByeByeDPI), [ByeDPIAndroid](https://github.com/dovecoteescapee/ByeDPIAndroid), [GoodbyeDPI](https://github.com/ValdikSS/GoodbyeDPI), [SpoofDPI](https://github.com/xvzc/spoofdpi), the [Flowseal Zapret preset](https://github.com/Flowseal/zapret-discord-youtube) and [zapret2-openwrt](https://github.com/1andrevich/zapret2-openwrt) were already listed.
- A local anti-DPI program is **not automatically an encrypted VPN or remote exit**. It may fail against IP-blocking, DNS interception or provider-specific filtering. Android typically allows one active VPNService at a time.

## New curated software references

| Project | Category | Upstream-verified scope | Notes |
| --- | --- | --- | --- |
| [youtubeUnblock](https://github.com/Waujito/youtubeUnblock) | Local anti-DPI | Linux/OpenWrt/Entware YouTube-focused SNI circumvention; NFQUEUE userspace and optional kernel-module approach | **Linux only** per upstream; do not advertise a native Windows or phone application |
| [NoDPI](https://github.com/GVCoder09/NoDPI) | Local anti-DPI | Desktop DPI-bypass tool, independent fork with a [separate Android project](https://github.com/GVCoder09/NoDPI4Android) | Upstream acknowledges destinations/methods that do not work; not universal |
| [Zapret2UI](https://github.com/Asterlike/zapret2UI) | Windows GUI | Independent Windows wrapper for Zapret2 `winws2`, strategy workflow and Telegram bridge | Small project; GitHub licensing metadata did not identify a recognized SPDX license at review; no security audit claimed |
| [nfqws2-keenetic](https://github.com/nfqws/nfqws2-keenetic) | Router anti-DPI | nfqws2 packaging for Keenetic/Netcraze with Entware; documents OpenWrt/Padavan use | Supersedes older [nfqws-keenetic](https://github.com/nfqws/nfqws-keenetic), whose README states it no longer receives updates |
| [nfqws-keenetic-web](https://github.com/nfqws/nfqws-keenetic-web) | Router UI | Separate web-interface packages for nfqws and nfqws2 | Requires matching installed backend and router packages; do not mistake UI for engine |
| [Zapret Web-GUI](https://github.com/avatarDD/zapret-gui) | Router multipath | Entware/OpenWrt web dashboard combining nfqws2 with tunnel/routing backends | Different data paths have different trust models; external relays do not mean universal availability |
| [Zapret Manager](https://github.com/StressOzz/Zapret-Manager) | Router management | OpenWrt management interface integrating multiple DPI/routing backends | Upstream also promotes a commercial service; this listing is for the **tool**, not an endorsement of that service; check script privileges |
| [Podkop](https://github.com/itdoginfo/podkop) | OpenWrt routing | Sing-box-based selected-domain/traffic tunneling; explicitly beta | Upstream: OpenWrt 24.10+, at least 25 MB free, touches dnsmasq/sing-box; an optional alternative installer explicitly sends device/installation telemetry |
| [XKeen](https://github.com/jameszeroX/XKeen) | Keenetic routing | Xray/mihomo-based transparent selective TCP/UDP routing | Not itself a DPI desynchronization engine; confirm router/Entware/firewall requirements |
| [blockcheckw](https://github.com/rcd27/blockcheckw) | Diagnostics | Parallel Rust wrapper around Zapret2 blockcheck2, with follow-up real-content checks | Tool-specific classifications are heuristic and must be compared with real application traffic |
| [StormDNS](https://github.com/nullroute1970/StormDNS) | DNS transport | Client/server TCP tunnel embedded in DNS requests and replies, based on MasterDnsVPN | Different from DoH; requires both client and a remote server, delegated DNS setup and protection of encryption keys; security unreviewed here |

The repository also has [Tachyon](https://github.com/Dushnilin/tachyon), [Re:Sputnik](https://github.com/1andrevich/re-sputnik), [ByeDPI OpenWrt](https://github.com/1andrevich/ByeDPI-OpenWrt), [DPIBreak](https://github.com/dilluti0n/dpibreak), [MuseDPI](https://github.com/zondaxxx/MuseDPI), [SwByeDPI](https://github.com/mIwr/SwByeDPI), and other alternatives; these were **not duplicated**.

## Interesting, but not promoted as established installs

- [FlClashM](https://github.com/makriq-org/FlClashM): a developing Android mihomo/FlClashX fork that **claims** integrated ByeDPI, NaiveProxy, olcRTC and StormDNS nodes. These are fork-specific extensions, not stock mihomo guarantees. App/API/security maturity and real ISP success need independent testing.
- [olcRTC](https://github.com/openlibrecommunity/olcrtc): WebRTC transport research; **archived on 2026-10-05**, and upstream points to future rework in [snolc](https://github.com/owenewans/snolc). Do not recommend the old project as maintained.
- [OSTP](https://github.com/ospab/ostp): recently proposed encrypted transport; [net4people proposal](https://github.com/net4people/bbs/issues/673) asks for expert protocol review. Treated as experimental; no independent audit verified.
- [nfqws-keenetic](https://github.com/nfqws/nfqws-keenetic): historical v1 packaging, superseded by nfqws2-keenetic. [remittor/zapret-openwrt](https://github.com/remittor/zapret-openwrt) remains a separate **zapret v1** packaging line (default branch `zap1`), not a substitute for the Zapret2 catalog entry.
- [PowerTunnel](https://github.com/krlvm/PowerTunnel) and [DPITunnel](https://github.com/nomoresat/DPITunnel-cli) are useful historical designs; observed source pushes were in 2023. Prefer current tools for new installs unless a specific legacy scenario demands them.

## High-signal communities and original discussions

### DPI engines, strategy testing and routers

- [Zapret2 upstream Discussions](https://github.com/bol-van/zapret2/discussions) — current `winws2`/`nfqws2` strategy migrations, Lua desync, and 2026 troubleshooting.
- [Zapret2 NTC discussion](https://ntc.rkn.quest/t/zapret2-%D0%BE%D0%B1%D1%81%D1%83%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5/21161) — author/community updates, provider-dependent workarounds (reports are not verified guarantees).
- [ByeDPI upstream Discussions](https://github.com/hufrea/byedpi/discussions) — engine-specific reports and regressions.
- [nfqws community](https://t.me/nfqws) and [nfqws2-keenetic discussions](https://github.com/nfqws/nfqws2-keenetic/discussions) — router/Entware and firmware-specific questions.
- [youtubeUnblock Discussions](https://github.com/Waujito/youtubeUnblock/discussions) — kernel/userspace integration on Linux/OpenWrt.
- [Podkop documentation](https://podkop.net/) and [Podkop issues](https://github.com/itdoginfo/podkop/issues) — transparent proxy routing, DNS and firmware constraints.
- [NTC community software](https://ntc.rkn.quest/c/community-software/27), [NTC circumvention category](https://ntc.rkn.quest/c/censorship-circumvention-software/11) and [latest posts](https://ntc.rkn.quest/latest) — regional field reports; access and indexing vary.
- [NoDPI Lab forum](https://nodpi.forumotion.com/) — tool-specific community linked from the official NoDPI README.

### Recent network measurement/research worth following

- [net4people #677 (2026-10-21)](https://github.com/net4people/bbs/issues/677) — analysis of an entropy-related function in QDPI; research context, not proof of its real-world deployment on a given ISP.
- [net4people #671 (2026-09-30)](https://github.com/net4people/bbs/issues/671) — observed large IP-blocking events in Russia; data is limited to tested networks/providers.
- [net4people #663 (2026-09-02)](https://github.com/net4people/bbs/issues/663) — a user's hypothesis about degraded traffic in TUN mode; **not evidence of general DPI-based TUN detection**.
- [net4people/bbs](https://github.com/net4people/bbs/issues) — original technical discussions and independent network measurements.
- [OONI Explorer](https://explorer.ooni.org/) and [GFW Report](https://gfw.report/) — measurement datasets and research; compare observation dates, country and network.

## Engineering reading notes

1. Keep local DPI desynchronization, a remote encrypted VPN exit, DNS tunneling and policy routing in **separate** categories; each can require a different trust, endpoint and testing model.
2. For every claimed bypass, record ISP/ASN, access network, destination, DNS path, protocol, client/core version, time and application-level result. Neither GitHub activity nor a single successful probe proves universal efficacy.
3. On routers, back up the network and DNS configuration before installing multiple policy-routing managers; avoid blindly executing remote shell scripts as root. Some projects change dnsmasq, nftables or sing-box state.
4. GUI wrappers may package executables from another upstream. Verify release origin, any bundled binaries, code-signing/hashes where provided, licensing and elevated permissions.
5. Prefer upstream release notes and independently reproducible measurements over forum popularity, fork stars or unverified claims about mobile network allowlists.
