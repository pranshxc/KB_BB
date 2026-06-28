---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-13_demo-brute-forcing-a-macos-users-real-name-from-a-browser-using-mdns.md
original_filename: 2023-07-13_demo-brute-forcing-a-macos-users-real-name-from-a-browser-using-mdns.md
title: 'Demo: Brute-forcing a macOS user’s real name from a browser using mDNS'
category: documents
detected_topics:
- command-injection
- mfa
- rate-limit
- automation-abuse
- supply-chain
tags:
- imported
- documents
- command-injection
- mfa
- rate-limit
- automation-abuse
- supply-chain
language: en
raw_sha256: d8792d8833a58479be422708df57a1a1ec3f6923e853c77ac080be22d4955332
text_sha256: 3b8dfa4966f07758537a8480661c6d732006c2ce930502d1d1bdcd8926503ec3
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Demo: Brute-forcing a macOS user’s real name from a browser using mDNS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-13_demo-brute-forcing-a-macos-users-real-name-from-a-browser-using-mdns.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, rate-limit, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `d8792d8833a58479be422708df57a1a1ec3f6923e853c77ac080be22d4955332`
- Text SHA256: `3b8dfa4966f07758537a8480661c6d732006c2ce930502d1d1bdcd8926503ec3`


## Content

---
title: "Demo: Brute-forcing a macOS user’s real name from a browser using mDNS"
page_title: "Brute-forcing a macOS user’s real name from a browser using mDNS"
url: "https://fingerprint.com/blog/apple-macos-mdns-brute-force/"
final_url: "https://fingerprint.com/blog/apple-macos-mdns-brute-force/"
authors: ["Konstantin Darutkin"]
programs: ["Apple (macOS)"]
bugs: ["Privacy issue", "Bruteforce", "mDNS"]
publication_date: "2023-07-13"
added_date: "2023-08-08"
source: "pentester.land/writeups.json"
original_index: 929
---

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAMCAIAAADtbgqsAAAACXBIWXMAAAsTAAALEwEAmpwYAAACOklEQVR42mWS22vTcBTH819Na5te7GV2D10VN+akFWqldRPXUldfpi97ULciXp4UVFDm9M0HwYGwVSmC+DAYOsZWelnbpGmTNPf0ksbvmqKIh5Pk/H45n/M958ePYBim3W5zHNfpdCRJ6vV6g8FgOBya/xp2+v1+t9vVNE1VVWSKoki0Wi2WZXmexwIlSuVK6bhWrlONRoOmaYqiR28KAoBRGrCiKIAFQSAsWRj+5b98DbqdEZ8jPkl6vT6Xy+33BwKBSQSx2FVZlpED2b+wJQszDePD551ns05z5VwtM3Vpbm5pKe3xnPX5/A4HGYlE0ZoFW21jTMKaFobBPm1tpRaS7zfe3Ms9DIVCMzOzLpfnfxjKiE9gaAojA5zP52128rSdnJg4NT9/OZO5FQ6fh7jT6YpGrwDAzIDRP/JPYDziyABvb+/YHaTH6yfdnpU7dzc33yUSSZvtjN3uQC0AOO0/A0N1DGMNuFAoBINT09NhCC4vZ1OpVDZ7GycHj8evIQ0wZBEAxrwEPiBRT9d1WdXqdBNeLFdeb7x9/uLlt+8/GJavUXSzzeoDQ+v1ZU0XFbUjKWxHHMOqIuuGyX181VyNso9uNtcX9rIXdzMXSqsx/mmGe5JmH6fp3A0qt0itLzbWrtcfJGv3EwR6QCc4Bh23h6WV6qHWKHWpyoA5RiBXj/jiPnf0ky/+kquHQukAAZbtg73m/u4Yxr1B2z3DGJimgcs4eluOnd7QlFQdjp4FWeFFqd0RGI7/DewcMcQmVMeqAAAAAElFTkSuQmCC)

Summarize this article with

[](https://chat.openai.com/?q=Summarize+this+article+and+explain+how+Fingerprint+helps+prevent+and+detect+online+fraud+for+me+specifically%3A+https%3A%2F%2Ffingerprint.com%2Fblog%2Fapple-macos-mdns-brute-force)[](https://claude.ai/new?q=Summarize+this+article+and+explain+how+Fingerprint+helps+prevent+and+detect+online+fraud+for+me+specifically%3A+https%3A%2F%2Ffingerprint.com%2Fblog%2Fapple-macos-mdns-brute-force)[](https://x.com/i/grok?text=Summarize+this+article+and+explain+how+Fingerprint+helps+prevent+and+detect+online+fraud+for+me+specifically%3A+https%3A%2F%2Ffingerprint.com%2Fblog%2Fapple-macos-mdns-brute-force)[](https://www.perplexity.ai/search/new?q=Summarize+this+article+and+explain+how+Fingerprint+helps+prevent+and+detect+online+fraud+for+me+specifically%3A+https%3A%2F%2Ffingerprint.com%2Fblog%2Fapple-macos-mdns-brute-force)[](https://www.google.com/search?udm=50&aep=11&q=Summarize+this+article+and+explain+how+Fingerprint+helps+prevent+and+detect+online+fraud+for+me+specifically%3A+https%3A%2F%2Ffingerprint.com%2Fblog%2Fapple-macos-mdns-brute-force)

 _This article is the second in a series that explores potential privacy vulnerabilities in Apple devices. In the[first article](https://fingerprint.com/blog/apple-id-region-leak/), we discussed detecting a system Apple ID region. This article presents a technique for revealing a user's first name without permissions using the mDNS protocol._  
  
**DISCLAIMER:** [Fingerprint](https://fingerprint.com/) as a company does not use this technique in our products, and we do not provide cross-site tracking services. We focus on detecting and preventing fraud and supporting modern privacy trends for removing third-party tracking entirely. There should be open discussions about such techniques to help internet browser providers fix them quickly.

## Introduction

In this article, we explain how the real name of a macOS user can be leaked through a browser without permissions.

The name brute-forcing technique uses a pre-made list of the 50 most popular gender-specific names from a specific country origin. Our experiments showed that this is enough to detect a macOS user’s name correctly in 65% of the cases on average.

## Multicast DNS protocol and Apple Bonjour 

The exploit implementation relies on the [multicast DNS](https://en.wikipedia.org/wiki/Multicast_DNS) (mDNS) protocol. In simple terms, the mDNS protocol is designed to register, discover, or broadcast device names over a local network.

For instance, when a specific device, such as a printer, wants to be discovered on a local network, it sends a registration UDP packet to the reserved internal IP address `224.0.0.251`, which contains a hostname like `HP_LaserJet_Printer.local`. The `.local` domain TLD indicates that the hostname should be resolved using the mDNS protocol.

Such packets are automatically broadcast by a router to other devices in a local network, so they can cache the hostname. Alternatively, devices can send query packets to the same reserved IP address and try to discover a specifically named device, which may not exist in the network.

Some examples of mDNS hostnames are:

  1. `johns-mac-mini.local`
  2. `david-ZenBook-UX431DA-UM431DA.local`
  3. `james-iphone.local`
  4. `canon-mf644c.local`
  5. `bedroom-appletv.local`
  6. `dlinkrouter.local`

The multicast DNS protocol is widely used on Apple devices as part of the [Apple Bonjour](https://developer.apple.com/bonjour/) feature.

By default, Apple devices expose the first name of a user in their local hostnames, which we are going to use for the name brute-forcing technique. You can view or change your macOS local hostname in the **Sharing** section of **System Settings.**

![apple sharing settings window](/static/d0153f469b4c85a8e7065b97da438a2d/f7616/1.png)

## Resolving mDNS hostnames from a browser

Unfortunately, the multicast DNS protocol is based on UDP packets. Browser JavaScript environments do not support arbitrary UDP sockets, so it is not possible to use the mDNS protocol directly in a browser.

However, we can resolve hostnames from browsers by using a timing workaround. Let’s make two regular `fetch` GET requests to existing `device-1.local` and non-existing `device-2.local` mDNS addresses:

![2](/static/46873a8e879d563f66a7a06b7893d0e8/f7616/2.png)

The browser will try to resolve the hostname provided in a URL address. If the address is resolved, it will send a TCP packet to the 80 port, which in our case will most likely be closed. On the screenshot above you can see two different error messages:

  * `ERR_CONNECTION_REFUSED` for the existing `device-1.local`
  * `ERR_NAME_NOT_RESOLVED` for non-existing `device-2.local`

Both errors will be mapped into the same `Failed to fetch` JavaScript error, so we can’t rely on the error type, but we can perform a timing attack. Local networks are fast, so the valid mDNS hostname registered in the network will be resolved in a reasonable time frame, which is significantly faster than the default connection timeout. In the example above, the difference is four milliseconds for a valid address versus five seconds for an invalid one.

This approach is consistent enough for the proof of concept solution and works similarly in all major browsers. In practice, you can use any network JavaScript API, such as `iframe`, `Image` or `WebRTC`, to perform timing attacks for DNS resolving.

## MacOS username brute-forcing

As illustrated earlier, the default macOS local hostname contains the user's first name and device name. Moreover, the hostname depends on a system language locale:

  * English: `<name>s-macbook-pro.local`
  * French: `macbook-air-de-<name>.local`
  * Russian: `mac-mini-<name>.local`

For example, we can take the top 1,000 names, the top 10 locales, and five common macOS device names. In this scenario, it would be necessary to test 50,000 distinct hostnames, which might take over an hour. A more efficient strategy would be to limit the search scope to a single locale, a single device, and the 50 most common names within that specific locale. While this affects accuracy, it makes the attack more feasible in practical terms and significantly faster in general.

The locale selection can be based on a browser time zone, language, or IP address location. Safari browser, for example, reveals the system locale with the `navigator.language` property, which is typically consistent with the targeted hostname locale. Also, there are other workarounds to discover the user's country of origin, such as the [Apple ID region detection](https://fingerprint.com/blog/apple-id-region-leak/) method discussed previously.

The device options can be narrowed down by using the screen resolution. For instance, the `1728x1117` resolution is most likely a 16-inch Macbook Pro. An extended screen can be detected by using the `screen.isExtended` property, which will fallback the device options to three to five of the most commonly used Apple macOS devices.

## Conclusion

Considering the inherent weaknesses and numerous limitations, this attack isn't practical. It can be effortlessly detected in the network tab of browser developer tools unless there is deliberate intent from a website owner to de-anonymize its visitors.

This series of articles merely explores the boundaries of internet privacy and relies on unconventional privacy breaching techniques. As another example, by combining this method with [detection of installed applications](https://fingerprint.com/blog/external-protocol-flooding/), there’s a potential to develop a harmful website capable of displaying your real name and job title, based on the list of professional applications used, all without requiring any permissions.

Even though this article mentions Apple devices running macOS, the mDNS discovery technique can be utilized in variety of ways. For instance, it could be used to perform a local network scan to detect devices such as printers, smart TVs, smart speakers, and other home IoT devices.

This method is also applicable to iPhones and iPads, given that [sync over Wi-Fi](https://support.apple.com/guide/mac-help/wi-fi-syncing-mchlada1d602/mac) or Safari remote debug features are activated.

### All article tags

  * [Apple](/blog/tag/apple/)
  * [Engineering](/blog/tag/engineering/)

Share this post
