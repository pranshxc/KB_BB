---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-16_disclosing-wifi-password-via-content-provider-injection-in-xiaomi.md
original_filename: 2020-08-16_disclosing-wifi-password-via-content-provider-injection-in-xiaomi.md
title: Disclosing wifi password via content provider injection in Xiaomi
category: documents
detected_topics:
- command-injection
- mobile-security
tags:
- imported
- documents
- command-injection
- mobile-security
language: en
raw_sha256: 2fa01c5f10062fc46339f493d44748ecb10974a6ec27f029e79be86663731ae6
text_sha256: aa727faf2bd3c38576d1156a9e3c954a959e5071ad12a04321748ce82afcf36d
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Disclosing wifi password via content provider injection in Xiaomi

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-16_disclosing-wifi-password-via-content-provider-injection-in-xiaomi.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `2fa01c5f10062fc46339f493d44748ecb10974a6ec27f029e79be86663731ae6`
- Text SHA256: `aa727faf2bd3c38576d1156a9e3c954a959e5071ad12a04321748ce82afcf36d`


## Content

---
title: "Disclosing wifi password via content provider injection in Xiaomi"
page_title: "Disclosing wifi password via content provider injection in Xiaomi – Vishwaraj Bhattrai"
url: "https://vishwarajbhattrai.wordpress.com/2020/08/16/disclosing-wifi-password-via-content-provider-injection-in-xiaomi/"
final_url: "https://vishwarajbhattrai.wordpress.com/2020/08/16/disclosing-wifi-password-via-content-provider-injection-in-xiaomi/"
authors: ["Vishwaraj Bhattrai (@vishwaraj101)"]
programs: ["Xiaomi"]
bugs: ["Content provider injection", "Vulnerable Android content provider", "Android"]
publication_date: "2020-08-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4318
---

### Summary:

The saved Wi-Fi passwords in Android are stored in the `data\misc\wifi` directory which can only be accessed if you have root access. So in general you cannot list or access the /data directory until and unless you have root access or the files are world readable writable .

### Device used:

(Xiaomi Redmi note 7 pro 9)
  
  
  ➜ appreview adb shell getprop | grep -E "ro.miui.region|ro.build.fingerprint"
  [ro.build.fingerprint]: [xiaomi/violet/violet:9/PKQ1.181203.001/V10.3.13.0.PFHINXM:user/release-keys]
  [ro.miui.region]: [IN]
  

### Poc steps:

Connect the device and run the below drozer command it will dump the wifi passwords along with other details in cleartext

`run app.provider.query content://wifi/wifi`

### Fix:

Don’t export the content provider containing user information.  
Protect it via custom permissions.

Or store it in encrypted format.

## Impact

Any app within the system can query and fetch wifi credentials which is not permitted by default by the system because to access the stored password the device need to be rooted but here it is easily available using which malicious app can login into victims router and can also alter the dns settings which will disclose user browsing activites to the attacker

### Disclosure Timeline

Reported on Jul 18th 2019  
Triaged on Jul 18th 2019  
Fix reviewed and ticket closure on Sep 11th 2019  

### Share this:

  * [ Share on X (Opens in new window) X ](https://vishwarajbhattrai.wordpress.com/2020/08/16/disclosing-wifi-password-via-content-provider-injection-in-xiaomi/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://vishwarajbhattrai.wordpress.com/2020/08/16/disclosing-wifi-password-via-content-provider-injection-in-xiaomi/?share=facebook)
  * 

Like Loading…

Published by

vishwaraj bhattrai

Security enthusiast
