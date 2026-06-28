---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-08_write-up-google-vrp-na-ssrf-bypass-with-quadzero-in-google-cloud-monitoring.md
original_filename: 2021-03-08_write-up-google-vrp-na-ssrf-bypass-with-quadzero-in-google-cloud-monitoring.md
title: 'Write Up – Google VRP N/A: SSRF Bypass With Quadzero In Google Cloud Monitoring'
category: documents
detected_topics:
- ssrf
- command-injection
tags:
- imported
- documents
- ssrf
- command-injection
language: en
raw_sha256: e6795c96fce683852532dddf1c4849b72b1dc02094177e67503d80ffe98dafd8
text_sha256: 869bae1e71cad78c16b949fa807f14bd686e58899067d49d49209c3782ec9cf4
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Write Up – Google VRP N/A: SSRF Bypass With Quadzero In Google Cloud Monitoring

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-08_write-up-google-vrp-na-ssrf-bypass-with-quadzero-in-google-cloud-monitoring.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `e6795c96fce683852532dddf1c4849b72b1dc02094177e67503d80ffe98dafd8`
- Text SHA256: `869bae1e71cad78c16b949fa807f14bd686e58899067d49d49209c3782ec9cf4`


## Content

---
title: "Write Up – Google VRP N/A: SSRF Bypass With Quadzero In Google Cloud Monitoring"
page_title: "GOOGLE VRP N/A – SSRF BYPASS WITH QUADZERO IN GOOGLE CLOUD MONITORING – @omespino"
url: "https://omespino.com/write-up-google-vrp-n-a-ssrf-bypass-with-quadzero-in-google-cloud-monitoring/"
final_url: "https://omespino.com/write-up-google-vrp-n-a-ssrf-bypass-with-quadzero-in-google-cloud-monitoring/"
authors: ["Omar Espino (@omespino)"]
programs: ["Google"]
bugs: ["SSRF"]
publication_date: "2021-03-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3830
---

WEBN/A[March 2021](/write-up-google-vrp-n-a-ssrf-bypass-with-quadzero-in-google-cloud-monitoring/)

# GOOGLE VRP N/A – SSRF BYPASS WITH QUADZERO IN GOOGLE CLOUD MONITORING

**Introduction**

Hi everyone It’s been a while since my last post, but I’m back, I want to tell you a very short story about one of my last bugs, and how I managed to bypass some Google Cloud Monitoring protections to achieve an SSRF

****

Background:

This is just a **lame** “bypass” or workaround for the fix that Google implemented for [David Nechuta’s](https://twitter.com/david_nechuta) 31k USD SSRF (write up reference [31k$ SSRF in Google Cloud Monitoring led to metadata exposure](https://nechudav.blogspot.com/2020/11/31k-ssrf-in-google-cloud-monitoring.html))

**Extracted from Google VRP’s report:** (the actual Google VRP report)  
  
Summary SSRF (“Skipping Unsafe Address” bypass) in https://console.cloud.google.com/monitoring/uptime

Steps to reproduce:  
  
1.- Go to <https://console.cloud.google.com/monitoring/uptime>  
2.- click on “CREATE UPTIME CHECK”
  
  
  1 Title
  anything
  
  2 Target
  - TCP
  - URL
  - Hostname: 0.0.0.0
  (it seems that there is some regex that blocks any IP starting with
  127.*, 169.*, 10.*, 172.*, 192.* or some common local IPs, but not quad zero)
  - Port: 22
  
  3 Response validation
  - Response timeout: 1s
  - Content matching: is enabled
  - Response Content: “SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.10”
  (without the quotes)
  
  4 Alert and Notification
  - Do not create an alert
  
  5 Click on “TEST” button

3.- Exploitation

If you set the host **0.0.0.0** and Response Content match to **“SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.10”** you are going to get the following message **Responded with “SUCCESS” in 0 ms.** and you can start playing the responses. Something worth mentioning is that if the request takes 0 ms seconds was because we hit **localhost** ; if you change **“SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.10”** for anything else or add any extra char the response will be **Responded with “ERROR” in 0 ms. Content does not contain “any string”.**

[![](/assets/images/2021/01/ssrf_cloud_mon2.webp)](/assets/images/2021/01/ssrf_cloud_mon2.webp)

Attack scenario:  
  
The attacker can perform server-side requests directly to the **localhost** , for example in this case to get a local service banner as SSH  
  
Each time that you send a **“Response Content *”** string check in the **“Response Validation”** option, you will get just 2 different JSON responses, if the response contains **“contentMismatch”: true** , the string does not match, but it contains **“checkPassed”: true** , that means that the local server response match that string, per example the string **“SSH”** match, so at this point, you can get the banner it with some **permutations** , per example if you start checking **“SSH[1..9-_aZ]”** etc. and **“SSH-“** matches, then you can start looking for **“SSH-[1..9-_aZ]”** and if **“SSH-2”** match you can then start looking for **“SSH-2[1..9-_aZ]”** and so on, and this can be easily automated with burp suite or any language program  

****Report Timeline****

**Jan 5, 2021: Sent the report to Google VRP  
Jan 6, 2021: Got a message from google that the bug was triaged (P3)  
Jan 15, 2021: ![](/assets/images/2021/01/download-1.webp) **Nice catch!** Bug Accepted (P3 → P2)  
Jan 21, 2020: Got a message from Google that the issue does not meet the bar for a financial reward  
Jan 21, 2020: I had a little chat with GoogleVRP’s team ([Eduardo @sirdarckcat](https://twitter.com/sirdarckcat) and he did a double check on this, thank you very much!), but not reward anyway.**

[![](/assets/images/2021/03/Screen_Shot_2021-01-28_at_12.38.59_PM.webp)](/assets/images/2021/03/Screen_Shot_2021-01-28_at_12.38.59_PM.webp)

**March, 2020: Fixed by Google**  
**  
**************

Well that’s it, share your thoughts, what do you think about how they handle that security issue? If you have any doubt, comments or suggestions just drop me a line here or on Twitter [@omespino](https://twitter.com/omespino), read you later.

[](/write-up-google-vrp-n-a-arbitrary-local-file-read-macos-via-a-tag-and-null-byte-in-google-earth-pro-desktop-app/)

[](/write-up-google-vrp-n-a-sandboxed-rce-as-root-on-apigee-api-proxies/)
