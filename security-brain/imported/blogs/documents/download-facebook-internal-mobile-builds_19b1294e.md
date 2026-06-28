---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-31_download-facebook-internal-mobile-builds.md
original_filename: 2021-03-31_download-facebook-internal-mobile-builds.md
title: Download Facebook internal mobile builds
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
- mobile-security
- supply-chain
language: en
raw_sha256: 19b1294eea0bff2432f3b04f09cdb5e4fa051cf9dc1a4e7990a7d177c9dfd707
text_sha256: 76cd730b0bf8ff64e3da0559be836fb7d9b8b9ccde927b708206490cf5766e55
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Download Facebook internal mobile builds

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-31_download-facebook-internal-mobile-builds.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `19b1294eea0bff2432f3b04f09cdb5e4fa051cf9dc1a4e7990a7d177c9dfd707`
- Text SHA256: `76cd730b0bf8ff64e3da0559be836fb7d9b8b9ccde927b708206490cf5766e55`


## Content

---
title: "Download Facebook internal mobile builds"
page_title: "Download Facebook internal mobile builds - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/download-facebook-internal-mobile-builds/"
final_url: "https://philippeharewood.com/download-facebook-internal-mobile-builds/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "6,000"
publication_date: "2021-03-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3778
---

Posted on [March 31, 2021](https://philippeharewood.com/download-facebook-internal-mobile-builds/)

# Download Facebook internal mobile builds

Facebook serves mobile apps, modules, firmware and packages via a few utility endpoints. One of these is defined as m.facebook.com/mobile_builds. Via a specific misconfiguration it was possible to use a variation of this URL to download local, profile , in-house and development builds for numerous Facebook, Instagram, Workplace, Portal and Oculus products. The proof of concept sent to Facebook was a simple bash  
  
`for i in {183448000..183448100}  
do  
wget "https://m.facebook.com/mobile_builds/?build_number=$i&no_fw=1" --header='cookie: sb=; datr=; fr=; dpr=2' --content-disposition  
done`

Changing the range of build numbers allowed one to query for past builds since 2019 or request builds as recent as March 2021. IPAs, APKs, internal Windows and experimental Oculus packages were also found in the dump. A few internal apps also held auth tokens for Facebook’s interngraph.intern.facebook.com endpoint.  
  
**Impact** (A verbatim explanation of the bounty by Facebook):

This could have let a malicious user access our internal mobile builds.

**Timeline**

Mar 31, 2021 4:43 pm – Report sent  
Mar 31, 2021 6:04 pm – Confirmation of submission by Facebook  
_“We’ve managed to reproduce your report and will get back to you once we have had a chance to investigate. In the meantime could you please stop further testing on this? As always, we’ll evaluate the full impact of the issue from our side and let you know 🙂_ “  
Mar 31, 2021 6:36 pm – Further investigation of submission by Facebook  
Mar 31, 2021 7:31 pm – Confirmation of patch by Facebook  
Apr 26, 2021 – $6000 Bounty awarded by Facebook
