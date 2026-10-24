# Source and maintenance notes

[← Back to README](README.md)

**Initial research snapshot:** 2026-10-25. Project activity timestamps are approximate observations and can change. The existence of a repository is **not** evidence of security, code quality or protocol interoperability.

## Notable upstream caveats

| Project / link | Observation | How this catalog handles it |
| --- | --- | --- |
| [Raha](https://github.com/Raha-Project/Raha) | Repository was reachable but latest observed push was 2023-12-16. | Included with **[Legacy]**, not presented as a maintained panel. |
| [Nekoray](https://github.com/MatsuriDayo/nekoray) | GitHub marks the upstream archived. | Listed as **[Legacy]** and directs readers toward newer GUIs. |
| [PalkaDPI (old link)](https://github.com/zondaxxx/PalkaDPI) | Provided/previously discussed repository path did not resolve during this audit. | Not added to active recommendations until a verified upstream is found. |
| [Hysteria (old path)](https://github.com/apernet/hysteria) | Historical path was no longer resolved by GitHub's repository API at audit time. | Uses current [HyNetworks/hysteria](https://github.com/HyNetworks/hysteria) project instead. |
| [TUIC upstream spec](https://github.com/tuic-protocol/tuic) | This repository is a specification, not a runnable implementation. | Catalog distinguishes it from the [Itsusinn implementation](https://github.com/Itsusinn/tuic). |
| [mihomo repository](https://github.com/MetaCubeX/mihomo) | API repository description at audit time referenced an unrelated game/Python project while release history documented the proxy core. | Links to releases and cautions users to verify provenance before installing. |
| [Happ binaries](https://github.com/Happ-proxy/happ-android) | GitHub repositories host release assets; this is not automatically evidence of full open-source client code. | Listed as **[Closed]**, with official vendor distribution. |
| [v2RayTun](https://github.com/LXST-CODE/v2RayTun) | Public issues/releases/roadmap; complete source-code availability cannot be assumed. | No unverified `[OSS]` badge. |
| [NTC](https://ntc.party/) | Forum and mirror availability may depend on network and region. | Both primary and alternate addresses, with availability caveat. |
| [Xray UI private-topic link](https://t.me/c/2479497161/1) | Telegram `/c/` links can require group membership. | Retained as user-provided resource, without promising anonymous access. |

## Initial inclusion criteria

1. The tool is substantively related to VPNs, proxies, anti-censorship, routing or network diagnostics.
2. Prefer official GitHub projects, original documentation and developer-controlled distribution.
3. Explicitly separate clients, servers, panels, DNS and local DPI bypass.
4. Place cross-platform tools in their primary category and optionally mention them elsewhere for discoverability.
5. Label legacy and proprietary resources; avoid equating a recent push with a vetted release.
6. Do not link to leaked paid subscriptions, private endpoints or dubious unaudited node aggregators.

## Maintenance routine

- Monthly: scan changed upstream default branches, releases, archival flags and moved URLs.
- Each new entry: verify source authenticity, link destination and category.
- After major client/core releases: revisit [COMPATIBILITY.md](COMPATIBILITY.md) and split-TUN/DNS issues.
- After a forum domain moves: check both accessibility and authenticity before changing URLs.
- Prefer short descriptions in README and detailed comparisons in dedicated files so the front page stays navigable.

## Discovery references

Cross-checked with [awesome-sing-box](https://github.com/oceanapplications/awesome-sing-box), [Proxy Client Radar](https://clientsradar.com/), source GitHub repositories and the user-supplied VPN/DPI/Xray/TG links. These references are discovery aids, not independent source-code security audits.
