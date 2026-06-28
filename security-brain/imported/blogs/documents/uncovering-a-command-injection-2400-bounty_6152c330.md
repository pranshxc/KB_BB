---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-14_uncovering-a-command-injection-2400-bounty.md
original_filename: 2023-10-14_uncovering-a-command-injection-2400-bounty.md
title: Uncovering a Command Injection, $2400 Bounty
category: documents
detected_topics:
- command-injection
- sqli
- file-upload
- api-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- sqli
- file-upload
- api-security
- mobile-security
- supply-chain
language: en
raw_sha256: 6152c330d33af59315962d52e9827326a9b1246534296e067bd6644bd6eca272
text_sha256: 6e7876df19fe176dce04f8fc768d7dcbfbeb8685896a050d5ac6586122d2a851
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Uncovering a Command Injection, $2400 Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-14_uncovering-a-command-injection-2400-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, sqli, file-upload, api-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `6152c330d33af59315962d52e9827326a9b1246534296e067bd6644bd6eca272`
- Text SHA256: `6e7876df19fe176dce04f8fc768d7dcbfbeb8685896a050d5ac6586122d2a851`


## Content

---
title: "Uncovering a Command Injection, $2400 Bounty"
page_title: "Uncovering a Command Injection, $2400 Bounty — Voorivex Team"
url: "https://blog.voorivex.team/uncovering-a-command-injection-2400-bounty"
final_url: "https://blog.voorivex.team/uncovering-a-command-injection-2400-bounty"
authors: ["0xrz (@omidxrz)"]
bugs: ["OS command injection", "RCE", "File upload", "Weak credentials"]
bounty: "2,400"
publication_date: "2023-10-14"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 715
---

[All posts](/)

Web · Cmd Injection · 14 Oct 2023 · $2,400 bounty

# Uncovering a Command Injection, $2400 Bounty

Hello, in this write-up I will explain how I found four P1 and two P2 bugs and showed multiple attack scenarios — starting from ASN-driven asset discovery and ending at a command injection in a forgotten admin upload endpoint. 

![](assets/avatars/omid-rezaei.png)

Written by [Omid Rezaei](/authors/omid-rezaei)

## Recon

On wide-scope programs the first move is mapping the company's ASNs and CIDRs, which gives you the IPs to enumerate, fingerprint, and find origin servers behind a CDN. [bgpview.io](https://bgpview.io) lists the company's ASNs by name; from there, this pipeline turns an ASN into live services: 
  
  
  whois -h whois.radb.net -- '-i origin AS123' | grep -Eo "([0-9.]+){4}/[0-9]+" | uniq | mapcidr -silent | httpx

`whois` dumps owner info, `grep` extracts CIDRs, [mapcidr](https://github.com/projectdiscovery/mapcidr) expands them to IPs, and `httpx` probes for live services. A faster but less complete alternative is the Shodan ASN query: 
  
  
  asn:AS123

_Note — Shodan ASN search requires a paid account._ Shodan turned up ~200 IPs; one looked like an admin panel — that's where I started. 

## Vulnerability Discovery

![Admin login page on the discovered IP](assets/images/uncovering-a-command-injection-2400-bounty/01-admin-login.png)

Wappalyzer flagged PHP. SQLi on the login form went nowhere, so I switched to directory fuzzing with [ffuf](https://github.com/ffuf/ffuf) and got a 401 on `/Config/`. In the browser, `admin:admin` simply worked. 

![Post-login admin panel after entering admin:admin](assets/images/uncovering-a-command-injection-2400-bounty/02-admin-default.png)

Default creds on a panel like that suggested the rest of the surface was sloppy too. Among the side directories (`js`, `css`, `images`, `data`) a `.rar` file in `images` caught my eye: 

![A rogue .rar file inside the images directory](assets/images/uncovering-a-command-injection-2400-bounty/03-images-folder-rar.png)

Inside was a Chinese-language `.doc` with admin instructions for swapping the site logo:

![Chinese instructions document — page 1](assets/images/uncovering-a-command-injection-2400-bounty/04-doc-page1.png)

![Chinese instructions document — page 2 referencing changelogo.php](assets/images/uncovering-a-command-injection-2400-bounty/05-doc-page2.png)

Hitting `changelogo.php` in the browser silently 30x'd to `index.php`. In Burp the actual response told a different story: 

![changelogo.php response — file-upload form revealed](assets/images/uncovering-a-command-injection-2400-bounty/06-changelogo-source.png)

A file-upload form. I tested with a GIF first, which worked:

![GIF upload accepted](assets/images/uncovering-a-command-injection-2400-bounty/07-upload-test.png)

![Uploaded GIF visible in /images](assets/images/uncovering-a-command-injection-2400-bounty/08-uploaded-image.png)

![Additional supporting screenshot](assets/images/uncovering-a-command-injection-2400-bounty/09-medium-image.png)

A web shell upload didn't make it through — only `.png` and `.gif` were accepted. Last resort: try injection in the `filename` field itself. SQLi/SSTI/eval payloads bounced; a shell-injection payload landed: 
  
  
  filename="test || sleep 30 ||.gif"

![Command injection via filename — sleep delay observed](assets/images/uncovering-a-command-injection-2400-bounty/10-rce-success.png)

Sweeping the same admin-panel fingerprint across the IP range I'd built earlier surfaced a second instance with the identical bug. 

## Report

I reported all of them at once. Within hours, every report was triaged.

![HackerOne triage notifications for the reports](assets/images/uncovering-a-command-injection-2400-bounty/11-triaged.png)

Thanks for reading. Twitter: [@omidxrz](https://twitter.com/0xrzzz).
