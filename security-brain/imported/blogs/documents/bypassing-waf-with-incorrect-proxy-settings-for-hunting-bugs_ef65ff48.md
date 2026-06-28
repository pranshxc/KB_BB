---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-25_bypassing-waf-with-incorrect-proxy-settings-for-hunting-bugs_2.md
original_filename: 2021-01-25_bypassing-waf-with-incorrect-proxy-settings-for-hunting-bugs_2.md
title: Bypassing WAF with incorrect proxy settings for Hunting Bugs.
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: ef65ff48faf3c1f757309f34555b8c854a28d81e4ae0489a5e9e2cb1584cfe59
text_sha256: 78b1e0e19f666b47a02aaf1e2ff12437d9364b32c1273e6d2e12d9532690f3a5
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing WAF with incorrect proxy settings for Hunting Bugs.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-25_bypassing-waf-with-incorrect-proxy-settings-for-hunting-bugs_2.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `ef65ff48faf3c1f757309f34555b8c854a28d81e4ae0489a5e9e2cb1584cfe59`
- Text SHA256: `78b1e0e19f666b47a02aaf1e2ff12437d9364b32c1273e6d2e12d9532690f3a5`


## Content

---
title: "Bypassing WAF with incorrect proxy settings for Hunting Bugs."
url: "https://shaurya-sharma.medium.com/bypassing-waf-with-incorrect-proxy-settings-for-hunting-bugs-3449b7716f59"
authors: ["Shaurya Sharma (@ShauryaSharma05)"]
bugs: ["URL validation bypass"]
publication_date: "2021-01-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3971
scraped_via: "browseros"
---

# Bypassing WAF with incorrect proxy settings for Hunting Bugs.

Bypassing WAF with incorrect proxy settings for Hunting Bugs.
Shaurya Sharma
Follow
2 min read
·
Feb 25, 2021

93

Press enter or click to view image in full size

Let’s Suppose the target system has the address-:

"Https: // targetdomain"

By accident, I noticed that some CSS and JavaScript resources were available on the subdomain responsible for authenticating on the site.

The odd thing was that while browsing the end node (something like) I received an HTTP 404 response from the server, which made me suspect the presence of WAF (Web Application Firewall).

"Https: //auth.targetdomain/vulnerable_endpoint? Param = malicious_RCE_payload"

Looking at one of the applications on the host:

(for example, https: // targetdomain/appname/appname ), I got authentication at the address “ https: //auth.targetdomain “ .

So I noticed another strange thing during authentication. At some point, a redirect to an address like : “https: // targetdomain /? Cfru = aHR0cHM6Ly90YXJnZXRkb21haW4vYXBwbmFtZQ = =”

Get Shaurya Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The string “aHR0cHM6Ly90YXJnZXRkb21haW4vYXBwbmFtZQ == “ is explicitly base64 encoded. After decoding, this payload it turned out to be nothing more than the “https: // targetdomain / appname” address , which I tried to access before starting authentication.

The turning point occurred at the moment when I made the following assumption: if the resource viewed directly, our HTTP request immediately goes to the WAF, where there is a rule that recognizes suspicious behavior (the malicious payload pointed to by “param”), sends an HTTP 404 error in response, and actually blocks the attack.

https: //auth.targetdomain/vulnerable_endpoint? param = malicious_RCE_payload

But what if we encode the url

https: //auth.targetdomain/vulnerable_endpoint? param = malicious_RCE_payload

in base64 and the resulting string:

“AHR0cHM6Ly9hdXRoLnRhcmdldGRvbWFpbi92dWxuZXJhYmxlX2VuZHBvaW50P3BhcmFtPW1hbGljaW91c19SQ0VfcGF5bG9hZA ==“

And pass it through the parameter “cfru”:

https // targetdomain /? cfru = aHR0cHM6Ly9hdXRoLnRhcmdldGRvbWFpbi92dWxuZXJhYmxlX2VuZHBvaW50P3BhcmFtPW1hbGljaW91c19SQ0VfhcZGF5=bG9

In this case:

The request goes through the WAF and is not recognized as suspicious.
Then the request goes to Bluecoat, where the cfru parameter is decoded and a GET request is sent to the internal host.
As a result, a vulnerability is initiated.
Bingo! Happy Hacking…….
