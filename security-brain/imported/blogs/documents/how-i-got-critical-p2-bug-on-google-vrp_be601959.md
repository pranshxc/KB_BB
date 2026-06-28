---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-04_how-i-got-critical-p2-bug-on-google-vrp.md
original_filename: 2024-08-04_how-i-got-critical-p2-bug-on-google-vrp.md
title: How I Got Critical P2 Bug on Google VRP
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: be601959af1661f178c0b0f4439fdea124d57235699357cc5be860e1319fd56d
text_sha256: 106992792cc40f3d64d81db26e6111fb7cfe8a9d193a416cc168bdeae31efde0
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: false
---

# How I Got Critical P2 Bug on Google VRP

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-04_how-i-got-critical-p2-bug-on-google-vrp.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: False
- Raw SHA256: `be601959af1661f178c0b0f4439fdea124d57235699357cc5be860e1319fd56d`
- Text SHA256: `106992792cc40f3d64d81db26e6111fb7cfe8a9d193a416cc168bdeae31efde0`


## Content

---
title: "How I Got Critical P2 Bug on Google VRP"
url: "https://medium.com/@rhashibur75/how-i-got-critical-p2-bug-on-google-vrp-165017145af8"
authors: ["Kazi Hashibur Rahman"]
programs: ["Google"]
bugs: ["Missing authentication", "Information disclosure"]
publication_date: "2024-08-04"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 107
scraped_via: "browseros"
---

# How I Got Critical P2 Bug on Google VRP

How I Got Critical P2 Bug on Google
Kazi Hashibur Rahman
Follow
2 min read
·
Aug 4, 2024

435

6

Hello Bug Hunters, Let’s start my second writeups on Bug Hunting.

I am just thinking about, what if i got valid bug on Google? Then I’m going for it & surprisedly I got it. (Just Kidding)

See My Report. (Google VRP) ->

Summary: Exposed “Google Cloud RADIS G4 Superset Dashboard” without authentication, potentially revealing sensitive data.

The vulnerability is known to third parties!

Program: Google VRP

URL: http://107.167.xxx.xxx:8080/superset/welcome/

Vulnerability type: Critical Sensitive data exposure

Details

I recently discovered a potentially exposed Google Cloud RADIS G4 Superset Dashboard that may present a security risk. The dashboard appears to be publicly accessible without proper authentication or security measures.

Details:

Type of Issue: Exposed Google Cloud RADIS G4 Superset Dashboard
Description: The dashboard is accessible without authentication, which could allow unauthorized users to view and interact with potentially sensitive data.

Steps to Reproduce:

-> I using this google dork “inurl:8x8x:xxxxxxxxx” (Dork isHidden for all)
-> After few deep analyses then i found the google cloud “G4 Superset Dashboard” direct accessible without authentication.
IP: The Dashboard IP address “107.167.xxx.xxx”

More Info:

PORT STATE SERVICE

22/tcp open ssh

80/tcp open http

443/tcp open https

8080/tcp open http-proxy

URL: The Dashboard direct “http://107.167.xxx.xxx:8x8x/superset/welcome/"

Get Kazi Hashibur Rahman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Please let me know if you need further details or assistance in addressing this issue. I am available to provide more information if necessary.

Regards, Kazi Hashibur Rahman

Attack scenario:
Who can exploit the vulnerability: Any unauthorized user with internet access who discovers the exposed Google Cloud RADIS G4 Superset Dashboard can exploit this vulnerability.
What they gain when doing so: They gain access to potentially sensitive data displayed on the dashboard, which may include confidential business information, operational metrics, and other critical data that should not be publicly accessible. This unauthorized access can lead to data breaches, information leakage, and other security risks.

PoC (Proof of Concept):

Press enter or click to view image in full size

===============================================================

Thanks for reading.

Tips: Recon is most powerful & helpful. This bug found by that through.

Tips More: Use Google dork i just use google dork for targeting google :_)

Respect+ our Team Members who actually help us for this bug they also part of this HoF.
->
Founder & CEO — t.me/oghbnz
Co-Founder & Manager — t.me/BNJ_9AM
Senior Admin — t.me/organic_root

HoF:

Press enter or click to view image in full size

Join Telegram Community — https://t.me/tch_community
Subscribe on YouTube — https://www.youtube.com/@RootMate?sub_confirmation=1
If you have any qus ? — rhashibur75@gmail.com

📝 : Kazi Hashibur Rahman
