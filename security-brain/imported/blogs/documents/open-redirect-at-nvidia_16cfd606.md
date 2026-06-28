---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-16_open-redirect-at-nvidia.md
original_filename: 2022-08-16_open-redirect-at-nvidia.md
title: Open Redirect at Nvidia
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- path-traversal
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- path-traversal
language: en
raw_sha256: 16cfd60643e1737f13ff5166e31be1e24bc951edab0861e2d067a726b3f5049f
text_sha256: ae663eae3fb85e6de3af49eaff27c7e892afba2427b64082295afb801757a0fa
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Open Redirect at Nvidia

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-16_open-redirect-at-nvidia.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `16cfd60643e1737f13ff5166e31be1e24bc951edab0861e2d067a726b3f5049f`
- Text SHA256: `ae663eae3fb85e6de3af49eaff27c7e892afba2427b64082295afb801757a0fa`


## Content

---
title: "Open Redirect at Nvidia"
url: "https://xthemo.medium.com/open-redirect-at-nvidia-62343b45f85b"
authors: ["Mohamed Abdelhady"]
programs: ["Nvidia"]
bugs: ["Open redirect"]
publication_date: "2022-08-16"
added_date: "2022-09-26"
source: "pentester.land/writeups.json"
original_index: 2303
scraped_via: "browseros"
---

# Open Redirect at Nvidia

Open Redirect at Nvidia
Mohamed Abdelhady
Follow
1 min read
·
Aug 16, 2022

11

2

Hi everyone , I’m Mohamed Abdelhady.

At first I gonna explain What Open Redirect is ?

So, we already should know what Open redirect is. For someone who doesn’t it is when remote attacker can set arbitrary value as a redirect destination.

https://domain.com/any_endpoint?redirectUrl=https://app.domain.com

Which in the end leads to app.domain.com. But what if someone malforms this URL into the following:

https://domain.com/any_endpoint?redirectUrl=https://evil.com

That will redirect to evil.com .

Get Mohamed Abdelhady’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The Nvidia bug is similar to the previous

https://subdomain.nvidia.com/PATH?vuln-paramter=https://subdomain.nvidia.com/

At first I found a URL parameter redirect to anther nvidia subdomain. So I tried to change the subdomain to xthemo.com and it worked . Then I tried to check if I can escalate it to

https://subdomain.nvidia.com/PATH?vuln-paramter=https://xthemo.com/
1-SSRF

I put my burp collaborator and clicked pull now button if the response was 200 than would be SSRF but unfortunately I found the response was 302 then means the nvidia website just redirect

https://subdomain.nvidia.com/PATH?vuln-paramter=https://burp-collaborator.net
2-XSS

I tried to inject XSS payload like javascript:alert() and it’s bypasses but it didn’t work

https://subdomain.nvidia.com/PATH?vuln-paramter=javascript:alert()
3-LFI

I tried to read internal files like hosts file using ?vuln-URL=C:/WINDOWS/System32/drivers/etc/hosts and LFI word list but unfortunately it didn’t get any content

https://subdomain.nvidia.com/PATH?vuln-paramter=C:/WINDOWS/System32/drivers/etc/hosts
