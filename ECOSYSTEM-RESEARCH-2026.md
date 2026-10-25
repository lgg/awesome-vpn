# VPN ecosystem research — October 25, 2026

[← README](README.md) · [Client directory](CLIENTS.md) · [Compatibility](COMPATIBILITY.md) · [Previous research](RESEARCH-2026.md)

This dated research log tracks **primary upstream repositories**, factual inclusion/exclusion reasons and technical discussions. GitHub push activity proves only that code changed; **it does not establish a release, working bypass, code security or independent audit**. Forums contain unverified user reports. No proxy subscriptions, private endpoints or leaked credentials are curated here.

## The biggest source: Awesome Remnawave

[Official community catalog](https://docs.rw/awesome-remnawave/) · [Versioned source in the Remnawave docs repository](https://github.com/remnawave/panel/blob/main/docs/awesome-remnawave.mdx).

The official catalog covers six areas: **monitoring/analytics, commerce, deployment, backups, miscellaneous extensions and client apps**. Unlike many scattered GitHub topics, it gives precise upstream project names. We cross-checked repository metadata individually and selected:

| Family | Newly included projects | Why |
| --- | --- | --- |
| Monitoring | [whitebox](https://github.com/quyxishi/whitebox), [Xray Checker Statuspage](https://github.com/Mrvibecodic/xray-checker-statuspage), [Remnawave Watchdog](https://github.com/vrezerni-netizen/remnawave-watchdog) | Actual proxy-path monitoring, incidents, watchdogs and backups |
| Node ops | [Cloudflare Nodes](https://github.com/hteppl/remnawave-cloudflare-nodes), [Remnawave Limiter](https://github.com/syvlech/remnawave-limiter), [Caddy Tblocker](https://github.com/Medium1992/caddy-tblocker) | DNS failover, device-limit monitoring and reverse-proxy controls |
| Infrastructure | [Infra Billing](https://github.com/mishkatik/infra-billing), [Remnawave scripts](https://github.com/DigneZzZ/remnawave-scripts), [Backup & Restore](https://github.com/distillium/remnawave-backup-restore) | VPS costs, config maintenance, database recovery |
| Setup | [RemnaSetup](https://github.com/Capybara-z/RemnaSetup), [Ansible Playbook](https://github.com/iphizic/remna-playbook) | Automated deployments; review shell scripts/privilege scopes |
| Commerce | [Remnashop](https://github.com/snoups/remnashop), [Remnawave Admin](https://github.com/Case211/remnawave-admin), [STEALTHNET Bot](https://github.com/STEALTHNET-APP/remnawave-STEALTHNET-Bot), [Telegram Mini App](https://github.com/maposia/remnawave-telegram-sub-mini-app) | Distinct integrations and management UIs, not merely reposts of Bedolaga |
| Subscription/control | [Subscription Middleware](https://github.com/Mrvibecodic/remnawave-subscription-middleware), [MCP Remnawave](https://github.com/TrackLine/mcp-remnawave), [Xray Config UI Editor](https://github.com/bropines/xray-config-ui-editor), [MRS Converter](https://github.com/MakostaDev/mrs-converter) | Subscription mirrors, operator management, API configuration and rule-set tooling |

**Previous coverage retained:** [Remnawave Panel](https://github.com/remnawave/panel), [Bedolaga](https://github.com/BEDOLAGA-DEV/remnawave-bedolaga-telegram-bot), [Bedolaga Cabinet](https://github.com/BEDOLAGA-DEV/bedolaga-cabinet), [Remnawave Telegram Shop](https://github.com/Jolymmiels/remnawave-telegram-shop), [Reverse Proxy](https://github.com/eGamesAPI/remnawave-reverse-proxy), [xray-checker](https://github.com/kutovoys/xray-checker).

**Excluded or deprioritized:** [coolcoala/clash-verge-rev-lite](https://github.com/coolcoala/clash-verge-rev-lite) did not resolve in the GitHub API during this pass. Older [erfjab/Backuper](https://github.com/erfjab/Backuper) was not favored over newer Remnawave-specific backups. [Flowvy](https://github.com/flowvy/desktop) is discoverable but was under discussion for removal in [upstream Remnawave PR #529](https://github.com/remnawave/panel/pull/529), so inclusion was postponed. We do not recommend installing any dependency with privileged panel/API access without local code review.

## Router, VPN protocol and client discoveries

- [WayHop](https://github.com/awadak3davra/wayhop): browser-based policy routing on OpenWrt and Entware/Keenetic with sing-box, node failover and graphs. **Pre-1.0** per maintainer. Check interactions with router's existing rules, and avoid enabling unauthenticated Web UI access.
- [routeflux](https://github.com/Alaxay8/routeflux): OpenWrt-native Xray subscription and transparent proxy management. Review nftables/firewall and firmware requirements.
- [Asuswrt-Merlin AmneziaWG](https://github.com/william-aqn/asuswrt-merlin-amneziawg): specific ASUS firmware integration for AmneziaWG client/server and web UI. Compatibility requires the correct Merlin/Entware firmware and architecture.
- [AmneziaWG Installer](https://github.com/bivlked/amneziawg-installer): self-hosted server provisioning. Automated installers need source review before privileged execution.
- [Qeli](https://github.com/litvinovtd/qeli): new dedicated VPN protocol and TUN clients with hybrid X25519/ML-KEM-768 handshake. The author's own documentation calls it **pre-1.0/beta**, with native binaries included in source control. **No independent audit was established**; do not assume security comparable to well-vetted WireGuard.
- [Veil](https://github.com/alibakhtiari/Veil): early-stage MASQUE/WireGuard desktop/Android tunneling design. Explicitly **experimental** rather than stable recommendation.
- [v2whitelist](https://github.com/NullCoreDeveloper/v2whitelist): experimental Android/Xray tool for difficult mobile access scenarios; network availability depends heavily on ISP.
- [mikan](https://github.com/Miroshka000/mikan): relatively new panel using a self-described Citrus proxy core rather than simply a copy of Xray; verify supported protocol types in the release.
- [Mullvad app](https://github.com/mullvad/mullvadvpn-app): open-source provider-dependent VPN client, included because its code/obfuscation evolution is useful to study, **not** as a generic profile import client.

## Diagnostics, filtering and technical discussions

- [RKN Block Checker](https://github.com/MayersScott/rkn-block-checker): inspect DNS, TCP, TLS and HTTP independently; useful for narrowing down whether failures are name resolution, handshake or web-layer filtering.
- [VPN Traffic Obfuscation Lab](https://github.com/maxlluky/VPN-Traffic-Obfuscation-Lab): reproducible research testbed with packet analysis tools and controlled obfuscation scenarios.
- [SonicDPI](https://github.com/by-sonic/sonicdpi): Rust-based DPI-bypass project. Its broad upstream effectiveness claims were **not independently verified**. Listed as experimentation, not a substitute for VPN anonymity.
- [Russia mobile Internet whitelist data](https://github.com/hxehex/russia-mobile-internet-whitelist): community-measured network allowlist observations. **Not a universal working bypass or guaranteed persistent route.**
- [VPN Protocol Registry](https://github.com/steveprice-dev/vpn-protocol-registry): evidence-oriented reference; categories include protocol, transport, code availability and security claims. Cross-check with primary upstream.
- [Awesome resilient communication](https://github.com/gdamdam/awesome-resilient-communication): useful for shutdown and intermittent connectivity, but **off-grid chat/mesh is not synonymous with Internet VPN access**.
- [Awesome anti-censorship](https://github.com/danoctavian/awesome-anti-censorship): additional open-source research reference.

### Why a client can show connected but no traffic

Recent discussions show two distinct **reports**, not confirmed universal defects:

1. [Xray-core discussion #7144 (2026-10-13)](https://github.com/XTLS/Xray-core/discussions/7144) describes a VLESS/REALITY regression with a particular uTLS `qq` fingerprint across tested Xray versions and ISP paths. **Do not generalize** that all fingerprints or servers are broken.
2. [v2rayN discussion #9567 (2026-06)](https://github.com/2dust/v2rayN/discussions/9567) reports a VLESS/REALITY profile that works with sing-box but not the Xray core on one client/network combination. The discussion does **not** prove all Xray clients fail in Russia.

When diagnosing, record **exact versions of server core and client core**, protocol and handshake security (REALITY/TLS), uTLS fingerprint, DNS path, network/provider, direct-vs-multihop differences and reproduction outcome. See [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## Specialist technical discussion sources

- [Xray-core GitHub Discussions](https://github.com/XTLS/Xray-core/discussions) — protocol changes and regressions from developers and users.
- [Remnawave GitHub Discussions](https://github.com/remnawave/panel/discussions) and [official Awesome Remnawave catalog](https://docs.rw/awesome-remnawave/) — self-hosting, node management and integrations.
- [NTC latest](https://ntc.rkn.quest/latest) and [top](https://ntc.party/top) — ISP-specific filtering reports; availability and indexing may vary.
- [net4people/bbs](https://github.com/net4people/bbs) — specialist circumvention research, protocol measurement and academic discussions.
- [Tor Project Forum](https://forum.torproject.org/) — bridges and pluggable transports; Tor has different properties than regular Xray/VPN.
- [OpenWrt Forum](https://forum.openwrt.org/) — policy routing, nftables, firmware updates and kernel support.
- [Remnawave source curation](https://github.com/remnawave/panel/blob/main/docs/awesome-remnawave.mdx) — curated integration directory tracked in version control.

## Editorial exclusions and ongoing checks

- Exclude public free proxy node dumps, affiliate VPN service rankings and unknown operators: they are **not trustworthy infrastructure documentation**.
- A repository with no license is **not automatically OSS**, even when its source is visible.
- An unreviewed new encryption protocol must be labeled experimental; prefer documented threat model, reproducible builds and independent audit evidence.
- Remnawave plugins can expose credentials or take billing/admin actions. Use least-privilege tokens; check backup and restore before upgrading.
- Android TUN and router transparent proxy are not feature-equivalent. Do not copy client engine/transport support assertions between them without tests.
- Refresh this log when any included project's maintainer, repository, distribution or license changes.

**Last reviewed:** 2026-10-25. No comprehensive external-link live probe, installed APK/build compatibility test or source-code security audit was performed.
