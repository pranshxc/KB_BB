---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-25_bugbounty-api-keys-leakage-source-code-disclosure-in-indias-largest-e-commerce-h.md
original_filename: 2018-02-25_bugbounty-api-keys-leakage-source-code-disclosure-in-indias-largest-e-commerce-h.md
title: '#BugBounty — API keys leakage, Source code disclosure in India’s largest e-commerce
  health care company.'
category: documents
detected_topics:
- path-traversal
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- path-traversal
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 1d4891a2e41345da4b93d380bb6639a1746e838308700902f3ea9695d3ca3253
text_sha256: ae4dc4d602dbe7a349fdef307189e482922563731cddbfb04cf52acaabbaa384
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — API keys leakage, Source code disclosure in India’s largest e-commerce health care company.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-25_bugbounty-api-keys-leakage-source-code-disclosure-in-indias-largest-e-commerce-h.md
- Source Type: markdown
- Detected Topics: path-traversal, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `1d4891a2e41345da4b93d380bb6639a1746e838308700902f3ea9695d3ca3253`
- Text SHA256: `ae4dc4d602dbe7a349fdef307189e482922563731cddbfb04cf52acaabbaa384`


## Content

---
title: "#BugBounty — API keys leakage, Source code disclosure in India’s largest e-commerce health care company."
page_title: "#BugBounty — API keys leakage, Source code disclosure in India’s largest e-commerce health care company. | by Avinash Jain (@logicbomb) | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/bugbounty-api-keys-leakage-source-code-disclosure-in-indias-largest-e-commerce-health-care-c75967392c7e"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["Path traversal"]
publication_date: "2018-02-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5963
scraped_via: "browseros"
---

# #BugBounty — API keys leakage, Source code disclosure in India’s largest e-commerce health care company.

#BugBounty — API keys leakage, Source code disclosure in India’s largest e-commerce health care company.
Avinash Jain (@logicbomb)
Follow
3 min read
·
Feb 25, 2018

893

3

Hi Guys,

Back with a long pending vulnerability that I found during my bug bounty hunt, though a late blog but I found it worth sharing. I have found this vulnerability in India’s largest online health platform website.

By this vulnerability, I was able to read source code of the application , sensitive files like webconfig where I got APIs key of mail server, sms, payment gateway etc and further I was also able to use these mail server key to send mail from their enterprise mail server and were even able to send sms using the sms keys to thier customers. Let’s see how I was able to do so —

The technique that was used to find this vulnerability was Path Traversal Attack.

Vulnerable URL

I found this vulnerability in the URL and the parameter as shown in the screenshot above.

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The response of the above URL HTTP request was as below-

Vulnerable Request response

If you look at the screenshot above, you will see the HTTP header “Server” . By this I analysed that Microsoft-IIS web server is in use. So I tried to open WIN.INI file of windows by path traversal attack.

Path traversal atatck

And I got the following response-

HTTP Response

This is the content of WIN.INI file. So by this I was confirmed that Local File Inclusion vulnerability exist. So I tried escalating this vulnerability and went on to read some source code of the application —

Login page source code request

As I knew it was an IIS server so I was clear about how application directory looks like and I tried reading source code of login page and as expected I got the below response —

Login page source code

Similarly , I was able to download the complete source code of the application of any page. Now comes the critical aspect of this, the web.config file is below –

Web Config file inclusion

and when I saw the response of the above request, I had a huge smile on my face :D

Press enter or click to view image in full size

All the sensitive APIs key were exposed!- Mail server API key, IIS server admin credentials , SMS API keys, Payment Gateway Keys and this was something really critical. I was able to use these keys to send mails, send SMS to user, payment manipulation and several more.

Report details-

19-June-2016 — Bug reported to the concerned company.

11-July-2016 — Bug was marked fixed.

11-July-2016 — Re-tested and confirmed the fix.

1-Aug-2016 — Awarded by company.

Thanks for reading!

~Logicbomb (https://twitter.com/logicbomb_1)
