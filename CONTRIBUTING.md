# Contributing

[← Back to README](README.md)

Thanks for helping keep Awesome VPN accurate, diverse and useful.

## Scope

Accepted: maintained VPN and proxy implementations, client GUIs, self-hosted management panels, subscription tools, DNS and tunneling infrastructure, DPI circumvention, diagnostics, privacy/security measurements, routing datasets, configuration examples, technical documentation, and specialist forums.

Not accepted: affiliate VPN rankings, referral campaigns, leaked subscriptions/credentials, unverified free node collections, suspicious binaries without an official upstream, crypto or gambling promotions, unrelated generic apps, and copies of other awesome lists without added verification.

## Inclusion checklist

- [ ] Link resolves to the **official upstream project, verified distribution, or original documentation**.
- [ ] Explain what the tool actually does in **one factual sentence**; do not use marketing claims.
- [ ] Pick the right category (a DPI bypass engine is not an anonymous VPN; a dashboard is not a server core).
- [ ] Check upstream activity and latest release; mark abandoned/archived projects `[Legacy]`.
- [ ] Specify `[Closed]` where source is not available; GitHub-hosted binary releases alone are **not** open source.
- [ ] If you claim a protocol, transport, feature or supported OS, link to upstream documentation or a release note.
- [ ] Do not expose credentials, links containing tokens, user/device identifiers, panel URLs tied to private subscriptions, or sensitive logs.
- [ ] Avoid duplicates and broken/redirecting old GitHub repository paths.
- [ ] When changing client compatibility claims, update [COMPATIBILITY.md](COMPATIBILITY.md) with the corresponding caveats.
- [ ] When adding a **VPN/proxy client**, update [CLIENTS.md](CLIENTS.md), identify its official release/store channel and distinguish a binary-only repository from open application source.
- [ ] For a **panel, monitoring tool, billing bot or router add-on**, describe required API privileges and trust boundaries; do not imply a security review or broad protocol compatibility based on a README alone.
- [ ] For **DPI, MTProxy, DNS tunneling and WireGuard obfuscation**, say which application traffic is actually routed, whether both endpoints must be modified and whether the tool supplies an anonymous public exit. Cite current upstream/ISP evidence for censorship claims.
- [ ] For new clients, document primary-source evidence, release/distribution channel, license and caveats in [README.md](README.md), [CLIENTS.md](CLIENTS.md) and [COMPATIBILITY.md](COMPATIBILITY.md) as applicable. Do not create another dated research-log file.
- [ ] For recurring diagnostics, add a short, **safe and reproducible** note to [TROUBLESHOOTING.md](TROUBLESHOOTING.md).


## Keeping the repository lean

**README.md is the canonical curated project directory and home of important research/forum references.** Keep supplementary files only when they serve a specific enduring reader workflow:

- [CLIENTS.md](CLIENTS.md): platform-first app directory and official download channels.
- [COMPATIBILITY.md](COMPATIBILITY.md): protocol/core/platform support and explicit caveats.
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md): actionable, reproducible diagnostics.
- [CONTRIBUTING.md](CONTRIBUTING.md): review rules and maintenance process.

**Do not add `RESEARCH-YYYY.md`, `DPI-RESEARCH-*.md`, progress reports or duplicate meta-documents** for each research pass. Integrate verified, useful project entries into the relevant section of README, platform-specific client facts into CLIENTS/COMPATIBILITY, and practical diagnostics into TROUBLESHOOTING. Summarize notable exclusion decisions only when they help avoid misleading recommendations; routine research history already exists in PRs and git history.

## Maintenance routine

- **Monthly:** scan upstream archived/repository-move status, release maturity, distribution changes, external links and maintainer announcements; correct broken or redirected references.
- **After notable core/client changes:** recheck real transport/platform support in [COMPATIBILITY.md](COMPATIBILITY.md), especially XHTTP, REALITY, iOS Network Extensions, Android VpnService, TUN and DNS detours.
- **When adding router/VPS tooling:** review root access and network configuration changes (dnsmasq, nftables, iptables, sing-box), least-privilege API tokens, backup/restore and rollback plans.
- **When a forum host changes:** check the forum's authentic upstream domain, do not silently replace with unverifiable mirrors.
- **When reviewing a candidate:** distinguish repository activity from a signed release, tested bypass, independent security review or protocol interoperation. Reject ambiguous licensing claims, phishing/malware repacks and leaked/proxy-scraping node dumps.
- **Before merging:** run local catalog validation or check successful GitHub Actions, review README duplicate entries/relative links, and ensure every added resource has a factual explanation.

## Suggested entry style

```markdown
- **[Project](https://github.com/OWNER/REPO)** [OSS] — Brief, specific explanation of its actual functionality.
```

Use the exact upstream name/capitalization. Links should point to source or project homepage rather than an arbitrary third-party mirror. Mark a project `[Self-hosted]` when an operator can deploy it and `[Legacy]` when archived or apparently unmaintained.

## Compatibility changes

Document the precise version and feature tested. In particular, do not mark all Xray, sing-box or mihomo transports as supported just because the client embeds one of those cores. A feature requires evidence from an upstream release, documentation or reproducible test.

## Local checks

Run:

```sh
python scripts/validate_catalog.py
```

The script validates Markdown structure, local links, duplicate identical section entries and the basic format of GitHub links. It intentionally does not perform high-volume live HTTP checks; GitHub rate limits, Telegram membership links and geo-blocked forums can cause misleading failures.

## PRs

Small, focused PRs with reliable links are welcome. For a larger contribution, group changes by topic and mention how links and compatibility details were verified. Do not submit auto-generated link dumps without review.
