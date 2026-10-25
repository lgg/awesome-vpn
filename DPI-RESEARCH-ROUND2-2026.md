# DPI, client and measurement research — second pass, October 25, 2026

[← README](README.md) · [Previous DPI research](DPI-RESEARCH-2026.md) · [Client directory](CLIENTS.md) · [Compatibility](COMPATIBILITY.md) · [Troubleshooting](TROUBLESHOOTING.md)

**Method.** Compared the latest `master` catalog with primary GitHub repositories, repository metadata, upstream READMEs, published release assets and specialist discussion threads on 2026-10-25. This is a **discovery/source review**, not a code-security audit, software-installation test, independent performance evaluation or proof of any ISP-specific bypass. A published release may be outdated or behave differently by provider, client, IP, access type, and time.

## New catalog additions and verification notes

| Project | What upstream actually supplies | Verified channel / limits |
| --- | --- | --- |
| [Prosvet](https://github.com/Derposd/prosvet) | Go-based censorship **measurement only**; differentiates DNS/IP/SNI/TLS/QUIC failures, throttling, and service-level symptoms; local reports and optional submission | [Releases](https://github.com/Derposd/prosvet/releases): 0.1.1 published October 12; MIT; Windows/Linux/macOS/OpenWrt binaries. **No traffic tunneling**. Author-reported test classifications and public map require independent corroboration |
| [YT-DPI](https://github.com/Shiperoid/YT-DPI) | PowerShell/Bash diagnostics for YouTube/Google transport path including DNS, HTTP, TLS and QUIC | [Releases](https://github.com/Shiperoid/YT-DPI/releases): 3.0.2 on October 19; MIT. Windows 10/11 (PowerShell 5.1/7), Bash edition for Linux/macOS/Entware. **Does not itself bypass censorship**; README versions may lag release tags |
| [NFQWS-MENU](https://github.com/rndnaame/nfqws-menu) | Interactive Entware package/menu management and **community-contributed** nfqws/nfqws2 strategies for Keenetic/Netcraze | Sources and scripts on `main`, no latest GitHub release found. Not the original engine by bol-van or the packaging organization `nfqws`; shell installer requires privileged access, inspect before executing |
| [singA](https://github.com/infinjest/singA) | OpenWrt arm64 transparent sing-box-lx gateway with TProxy, XHTTP/AWG2-oriented profile support, DNS and policy routing | [Releases](https://github.com/infinjest/singA/releases) contain a sing-box-lx arm64 build. Maintainer tested **Netis NX31/arm64 on OpenWrt 25.12.4**; other routers **unverified**. Shell installer rewrites network rules; back up first. GitHub API did not report an SPDX license: **source-available, license unverified** |
| [KEQDIS (keqdroid)](https://github.com/Lemonochka/keqdroid) | GPL-3.0 Flutter app with Xray/mihomo, subscriptions, split tunneling; Windows, Linux, Android | [v0.29.0 release](https://github.com/Lemonochka/keqdroid/releases/tag/v0.29.0) on Oct 23 contained Windows x64 ZIP, Android APKs and Linux binaries. Neither an Apple/iOS client nor universal XHTTP feature parity is implied |
| [NoDPI4Android](https://github.com/GVCoder09/NoDPI4Android) | Android port/GUI of the NoDPI local DPI approach, separate from [desktop project](https://github.com/GVCoder09/NoDPI) | GPL-3.0; latest GitHub release observed **v2.0-beta (May 30)**. Does not guarantee all services or offer a general remote VPN exit; mind Android single-VPNService behavior |
| [TiredVPN](https://github.com/tiredvpn/tiredvpn) | Separate Go client/server VPN implementation, with adaptive transport-selection claims | [v1.11.8 release](https://github.com/tiredvpn/tiredvpn/releases/tag/v1.11.8) on Oct 20; AGPL-3.0 text in LICENSE; [Android source/client](https://github.com/tiredvpn/tiredvpn-android). **Experimental**: no third-party protocol/security audit or independently reproduced 20+ bypass claims established here |
| [tiredvpn-measurements](https://github.com/tiredvpn/tiredvpn-measurements) | Maintainer-controlled longitudinal connectivity reports comparing multiple transports, ISPs and destinations | CC-BY-4.0 data, push Oct 3; project describes Rostelecom and MegaFon measurement positions. **Not an independent benchmark** of its companion VPN; notes explicitly say its current failure reports do not distinguish resets, drops and timeouts |

Additional notable source candidates not promoted into the primary README without more evidence: [snax1k/new-zapret2-gui](https://github.com/snax1k/new-zapret2-gui) describes a *zapret2* UI but its own README says bundled `winws` is **zapret v72.13 (v1)**; the title is therefore potentially misleading, and it modifies Windows with admin permissions. [stillemptyNOW/aether-zapret](https://github.com/stillemptyNOW/aether-zapret) was a new Flowseal wrapper with little project history. [hussaroff/tunnel](https://github.com/hussaroff/tunnel) is explicitly proprietary and includes account/server distribution; self-reported whitelist success is not verified. [pabragin/xiaomi-be5000-openwrt](https://github.com/pabragin/xiaomi-be5000-openwrt) produces device-specific Xiaomi BE5000 firmware, **not** a general OpenWrt anti-DPI distribution. [blindtechnique/az-awg2](https://github.com/blindtechnique/az-awg2) is experimental AWG2 on top of an AntiZapret stack: no general performance/security assertion from README alone.

## High-signal research and specialist forums

### NTC: practical DPI and strategy debugging

The [NTC Community software category](https://ntc.rkn.quest/c/community-software/27) on October 23 listed recently active Zapret, ByeDPI and router discussions, but individual threads sometimes returned HTTP 429. Refer to the categorized entries rather than assuming a comprehensive scrape.

- [Zapret2 discussion](https://ntc.rkn.quest/t/zapret2-%D0%BE%D0%B1%D1%81%D1%83%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5/21161) — current `nfqws2`/Lua migration, user/provider failures.
- [B-Checker](https://ntc.rkn.quest/t/b-checker-%D0%B0%D0%B2%D1%82%D0%BE-%D0%BF%D0%BE%D0%B4%D0%B1%D0%BE%D1%80-%D0%B8-%D1%81%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%B5%D0%B3%D0%B8%D0%B9-byedpibyebyedpi-%D0%B1%D0%B0%D1%82%D0%BD%D0%B8%D0%BA-%D0%B4%D0%BB%D1%8F-windows/14291) — community Windows strategy selection for ByeDPI/ByeByeDPI; read download origin carefully.
- [zapret-Checker](https://ntc.rkn.quest/t/zapret-checker-%D0%B0%D0%B2%D1%82%D0%BE-%D0%BF%D0%BE%D0%B4%D0%B1%D0%BE%D1%80-%D0%B8-%D1%81%D0%BE%D1%85%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%B5%D0%B3%D0%B8%D0%B9-windows/23814) — Windows strategy-search discussions.
- [GoodCheck](https://ntc.rkn.quest/t/goodcheck-%D0%B1%D0%BB%D0%BE%D0%BA%D1%87%D0%B5%D0%BA-%D0%B4%D0%BB%D1%8F-gdpi-zapret-byedpi-%D0%B0%D0%BA%D1%82%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F-%D0%B2-%D0%BF%D1%80%D0%BE%D1%84%D0%B8%D0%BB%D0%B5/10880) — multi-engine checker; forum-distributed executable/scripts, **not audited here**.
- [Re:HomeProxy](https://ntc.rkn.quest/t/rehomeproxy-%D0%BE%D0%B1%D0%BE%D0%BB%D0%BE%D1%87%D0%BA%D0%B0-%D0%BA%D0%BB%D0%B8%D0%B5%D0%BD%D1%82-sing-box-%D0%BD%D0%B0-openwrt-%D1%81-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B5%D0%B9-byedpi-%D0%B8-zapret2/25263) — router integration discussion, not proof of a stable release.

### Independent research and upstream debugging

- [Zapret2 Discussions](https://github.com/bol-van/zapret2/discussions) — read the [16 KB stallbreak discussion](https://github.com/bol-van/zapret2/discussions/327) from October 15 as a **reproducible experiment**, not a universal workaround.
- [net4people #671](https://github.com/net4people/bbs/issues/671) — reports of mass IP bans and changes on particular hosting networks (Sept/Oct 2026); provider/ASN scope matters.
- [net4people #657](https://github.com/net4people/bbs/issues/657) — reports of UDP/53 DNS interception vs TCP/53 behavior on several access networks; re-test before generalizing.
- [net4people #663](https://github.com/net4people/bbs/issues/663) — report of TUN-mode related connection degradation; is **not confirmed evidence that the network recognizes TUN itself**.
- [net4people #650](https://github.com/net4people/bbs/issues/650) — ongoing LTE allowlist testing and failed/uncertain methods; a useful source for *limitations*, not guaranteed recipes.
- [FOCI 2026 QUIC SNI filtering study](https://www.petsymposium.org/foci/2026/foci-2026-0010.php) — peer-reviewed method and temporal evidence; distinguish researchers' measured dates from present-day ISP conditions.
- [OONI Explorer](https://explorer.ooni.org/) — compare network-specific measurements with the reported access provider, country and test date.

## Security finding relevant to Xray administrators

[GHSA-5wf9-h793-w73c](https://github.com/advisories/GHSA-5wf9-h793-w73c) is an **official reviewed Xray-core vulnerability advisory**, published July 10 and updated October 2, 2026. It concerns certificate pinning via `pinnedPeerCertSha256` in some configurations, particularly a missing TLS `serverName`, which can permit MITM/incorrect certificate acceptance. The advisory gives the patched Go module version **`1.260327.1-0.20260710210335-64fada32b5b9`**; Xray's [v26.7.11 release](https://github.com/XTLS/Xray-core/releases/tag/v26.7.11) is linked in the advisory. Check the exact embedded Xray-core version in **both standalone clients and panels**. Do not assume every VLESS/REALITY connection is vulnerable, or that using a particular GUI implies the patch is deployed.

Also review the upstream [Zapret2 Windows-wrapper security discussion](https://github.com/bol-van/zapret2/discussions/159): members disagree over particular historical GUI behaviors, so **do not label an entire tool malicious without independent verification**. The practical implication is to inspect elevated installers, `hosts` permissions, Defender/firewall changes, downloaded helper executables and persistence; prefer original author releases.

## Editorial and testing policy

1. Record the exact upstream repository, release date, license, hardware and actual supported features.
2. Keep measurement utilities separate from anti-DPI packet modifiers and remote VPNs; a browser handshake test ≠ tunneled UDP, audio/video and DNS.
3. Explicitly identify community repacks, unaudited custom protocol implementations, possible telemetry and unverified claims about nationwide mobile allowlists.
4. Compare fixed/mobile, ISP/ASN, DNS resolver path, IPv4/IPv6, TCP/QUIC, TLS fingerprints and reported failure type before attributing failure to DPI.
5. For WinDivert/root/Entware installers, inspect scripts and review privileged actions; GitHub stars, release assets and discussions aren't a malware or security audit.
