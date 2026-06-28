---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-28_blind-ssrf-in-skype-microsoft.md
original_filename: 2022-10-28_blind-ssrf-in-skype-microsoft.md
title: Blind SSRF in Skype (Microsoft)
category: documents
detected_topics:
- cloud-security
- ssrf
- command-injection
- api-security
tags:
- imported
- documents
- cloud-security
- ssrf
- command-injection
- api-security
language: en
raw_sha256: d61a9b97c0a1397d59d5dba028045a067ecbc1901dd12a1d60b5478c7d5066e3
text_sha256: c7be09548f63eff8146f46aace6bdc58fd58b3737b86f97044fa0ec4b4342ee6
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Blind SSRF in Skype (Microsoft)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-28_blind-ssrf-in-skype-microsoft.md
- Source Type: markdown
- Detected Topics: cloud-security, ssrf, command-injection, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `d61a9b97c0a1397d59d5dba028045a067ecbc1901dd12a1d60b5478c7d5066e3`
- Text SHA256: `c7be09548f63eff8146f46aace6bdc58fd58b3737b86f97044fa0ec4b4342ee6`


## Content

---
title: "Blind SSRF in Skype (Microsoft)"
url: "https://jayateerthag.medium.com/blind-ssrf-in-skype-microsoft-6639f4961052"
authors: ["Jayateertha Guruprasad (@JayateerthaG)"]
programs: ["Microsoft"]
bugs: ["Blind SSRF"]
publication_date: "2022-10-28"
added_date: "2022-10-28"
source: "pentester.land/writeups.json"
original_index: 1975
scraped_via: "browseros"
---

# Blind SSRF in Skype (Microsoft)

Blind SSRF in Skype (Microsoft)
Jayateertha Guruprasad
Follow
2 min read
·
Oct 28, 2022

239

1

Server Side Request Forgery is a vulnerability that allows attacker to make server request to attacker controlled network location/path.

While analyzing requests in Burp for Skype for Web, found a endpoint at *.*.skype.com/path?url=https://example.com , As the url param appeared interesting tried to change the url with my ngrok instance & got a hit !

Confirmed that it’s Skype which hit the url by looking at the ngrok inspect web console by verifying received User-Agent header(Skype)and IP address in who.is.

Although I was able to make the server hit arbitrary webpage, I couldn’t get full response. I could only get status code, content-type, content-length(size) of response and text content from few selected HTML tags. That’s, it’s not full SSRF as expected, but is a blind/partial SSRF.

Tried to access below paths —

localhost/internal ip address -> Failed
Tried to bypass localhost/internal ip address using url redirect/url shortner methods -> Failed
External ip address/webpage -> Success
Common Azure/AWS/DigitalOcean Meta data IP addresses -> Failed
Not so commonly used, Azure related IP address (168.63.129.16) -> Success -> This IP can be used to determine VM’s health by using http://168.63.129.16/metadata/v1/maintenance endpoint, which should return OK (200 Status Code) if VM is functioning. (Refer this for more information)

Tried changing url param value to http://168.63.129.16/metadata/v1/maintenance , got 200 Ok response, with size of response as 2 bytes which confirms that response text probably contains OK in response.

Get Jayateertha Guruprasad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Made a nice report mentioning all the details and sat back waiting for Microsoft to reproduce and fix the report.

Fortunately this was in scope for bounty under the M365 Bounty Program and got a nice $$$$ bounty !

Press enter or click to view image in full size
Party Hard!

Report Timeline:

Reported — Sep 23, 2022
Additional Details Updated — Oct 3, 2022
Bounty Rewarded — Oct 8, 2022
Fixed — Oct 12, 2022
Liked my article ? Follow me on twitter (@jayateerthaG) and medium for more content about bugbounty, Infosec, cybersecurity and hacking.
From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
