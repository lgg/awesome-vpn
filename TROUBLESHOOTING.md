# Troubleshooting VPN, proxy, DNS and TUN setups

[← Back to README](README.md) · [Compatibility](COMPATIBILITY.md)

This is a reproducible **diagnostic checklist**, not a universal bypass recipe. Record your OS, client/core versions, whether TUN or system-proxy mode is active, and the exact failed operation. Use hosts you operate or are authorized to test.

## First classify the failure

| Symptom | First checks |
| --- | --- |
| IP connectivity works, hostnames fail | DNS server reachability, resolver selection, route/detour, IPv6 |
| Local browser works but other apps fail | System proxy vs TUN, per-app routing, unsupported UDP |
| Proxy works but TUN does not | TUN permissions, stack, DNS interception, default route, firewall |
| Works without VPN but not through proxy | Domain rules, DNS, protocol, handshake, target filtering |
| Connecting works on one ISP only | UDP/QUIC reachability, MTU, DPI filtering, TLS/transport compatibility |
| Tunnel connects but public IP is unchanged | Routing rule selected DIRECT; check individual request path |
| Works from LAN but not via VPS | Reverse tunnel registration, listener, TLS/SNI, firewall, upstream address |
| Only some domains fail | Domain-vs-IP routing, IPv6, SNI, split DNS, rule-set precedence |

## Basic tests

**Windows PowerShell**

```powershell
Resolve-DnsName example.com
Test-NetConnection example.com -Port 443
curl.exe -I https://example.com
Get-NetRoute -AddressFamily IPv4 | Sort-Object RouteMetric | Select-Object -First 20
Get-DnsClientServerAddress
```

**Linux**

```bash
getent ahosts example.com
dig example.com A
dig example.com AAAA
ip route get 1.1.1.1
ss -tulpen
curl -Iv --connect-timeout 10 https://example.com
```

Commands above gather local evidence. They are not proof that a route, proxy or DNS server is safe or private. Before packet capture, check that you have authorization and remove private information from any shared logs.

## TUN connects but DNS fails

A recurring failure mode in some desktop clients: packets to an IP address work inside the TUN, but domain lookups time out.

1. Compare **system-proxy mode** and **TUN mode** against the same domain.
2. Check whether TUN DNS queries go to the intended resolver or loop into the TUN.
3. Confirm the DNS upstream is reachable **through the intended outbound**, not accidentally via a blocked direct route.
4. If the client supports DNS `detour`, explicitly choose the documented proxy outbound; otherwise verify client-specific DNS settings.
5. Compare DoH with direct UDP/53 using the same resolver, and note failures separately.
6. Recheck IPv4/IPv6 rules and DNS cache; failing IPv6 paths can masquerade as DNS failures.

**Real-world example:** on Windows v2RayTun with Xray plus gVisor-based TUN, an earlier problem was fixed by routing DoH DNS upstream `https://1.1.1.1/dns-query` through the Xray proxy rather than sending resolver traffic directly. This is an example of a **client-specific configuration workaround**, not a universal recommendation; DNS detour behavior may differ across releases.

Relevant upstream references: [Xray DNS](https://xtls.github.io/en/config/dns.html), [sing-box DNS](https://sing-box.sagernet.org/configuration/dns/), [v2RayTun issues](https://github.com/LXST-CODE/v2RayTun/issues).

## Local DPI bypass versus remote VPN

- A local desynchronization utility changes how traffic appears to a filter. It does **not** inherently provide a remote egress IP.
- A remote VPN/proxy may change egress IP but not reliably bypass every filter.
- On Android, many apps compete for one `VpnService` slot. Try an integration supported **inside one client**, or documented proxy-only modes; do not stack two unrelated VPN services and expect both to work.
- Record whether failures involve **TLS, QUIC/UDP, DNS or routing** before changing unrelated settings.

References: [zapret](https://github.com/bol-van/zapret), [ByeDPI](https://github.com/hufrea/byedpi), [OONI Probe](https://github.com/ooni/probe).

## VLESS + REALITY: a client reports connected, but no usable traffic

**Separate handshake and application delivery.** A client's green connection indicator can mean the upstream accepted a connection while TCP application requests, DNS or routed streams still fail.

Recent upstream reports (not a universal fault statement):

- [Xray-core discussion #7144](https://github.com/XTLS/Xray-core/discussions/7144), opened 2026-10-13: one reporter described a specific `qq` uTLS fingerprint/regression across Xray versions and networks. A core downgrade was used in that report, **not recommended here as a blanket fix** because it can forgo security updates.
- [v2rayN discussion #9567](https://github.com/2dust/v2rayN/discussions/9567): one setup transported traffic with a sing-box core while failing with Xray on the same VLESS + REALITY profile. This does not establish that either core universally works better.

For an authorized diagnostic comparison:

1. Log the exact **server and client core versions**, client build, platform and REALITY/transport settings (omit secret keys).
2. Compare a direct server path with any multihop chain. Do not change DNS, route, core version and fingerprint all at once.
3. Test DNS separately from TLS handshake and an actual HTTPS request. See [TUN DNS](#tun-connects-but-dns-fails).
4. If the client permits **core selection**, compare current supported Xray and sing-box versions using the same imported profile, and record differences.
5. Check upstream issues/releases for known compatibility changes. Do not blindly disable certificate checks, leak private keys or pin vulnerable old versions.

## Domain and application routing

For a split tunnel using country/domain/IP rules:

1. Determine if the rules are evaluated using **hostname**, resolved destination IP, or both.
2. Check priority of DIRECT, BLOCK and proxy matches, including fallback/default rule.
3. Confirm downloaded `geosite`/`geoip` rule files match the running core.
4. Test a known domestic domain, known foreign domain and bare destination IP.
5. Inspect the client's **effective generated configuration** rather than relying on the GUI label.
6. Check whether DNS requests are routed through a different policy from application traffic.

References: [Xray routing](https://xtls.github.io/en/config/routing.html), [sing-box route rules](https://sing-box.sagernet.org/configuration/route/rule/), [Russia routing data](https://github.com/runetfreedom/russia-v2ray-rules-dat).

## NAT / reverse tunnel via VPS

For a self-hosted service on a computer behind NAT (for example, local web administration through a domain pointing to a VPS):

```text
Remote client -> HTTPS domain/VPS -> authenticated tunnel -> private home service
```

- A reverse tunnel such as [frp](https://github.com/fatedier/frp) can avoid exposing the home machine directly to the Internet.
- The tunnel client must be able to reconnect after sleep, IP changes and local network/VPN route changes.
- Confirm the **control connection** to your VPS is excluded from any route rule that would recursively direct it through itself.
- Bind sensitive local services to a private address; put TLS, authentication, rate limiting and firewall rules in front of anything exposed.
- Never forward a 3x-ui or Remnawave administrative panel anonymously without authentication.
- Test DNS resolution and TCP connectivity both to VPS and to the local service independently.

## Before filing an issue

Provide a redacted, reproducible report:

```text
OS / version:
App / version:
Core / version:
Mode: System proxy | TUN | Router | Server
Network: Home Wi-Fi | Mobile | VPS | Other
Protocol / transport (no secrets):
Expected behavior:
Actual behavior:
IP-only test:
DNS test:
TCP/UDP test:
Logs (redacted):
Reproduction steps:
```

**Never include:** private keys, subscription identifiers, auth headers, real user credentials, full config URLs, personal device IDs, or identifiable packet captures.

## Fresh 2026 measurements and TLS security

For a failing VPN/DPI configuration, separate the *observed failure* from its hypothesized root cause. [Prosvet](https://github.com/Derposd/prosvet) and [YT-DPI](https://github.com/Shiperoid/YT-DPI) perform local service/path measurements; [tiredvpn-measurements](https://github.com/tiredvpn/tiredvpn-measurements) publishes maintainer-controlled, dated transport checks. None alone proves that your provider performs particular DPI classification or that a strategy works for every application. Record ISP/ASN, date, client/core version, SNI/TLS handshake details, DNS path, target IP, access type (mobile/wired), and both direct/proxied/TUN results. Avoid sharing packet captures with private credentials or connection identifiers.

**Xray-core security reminder.** Reviewed [advisory GHSA-5wf9-h793-w73c](https://github.com/advisories/GHSA-5wf9-h793-w73c) describes a certificate-pinning configuration that could skip proper hostname verification, potentially enabling MITM. It was published July 10 and updated October 2, 2026; inspect the advisory's affected/fixed module versions and your **actual bundled Xray core**, not merely the GUI/panel version. Specifically inspect configurations that use `pinnedPeerCertSha256`, especially without an explicit `serverName`. This does **not** imply that every VLESS/REALITY connection is affected. Keep certificate/host verification enabled and update affected clients or embedded cores.
