---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-01-24_bugbounty-linkedln-how-i-was-able-to-bypass-open-redirection-protection.md
original_filename: 2018-01-24_bugbounty-linkedln-how-i-was-able-to-bypass-open-redirection-protection.md
title: '#BugBounty @ Linkedln-How I was able to bypass Open Redirection Protection'
category: documents
detected_topics:
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 2475e746050dcabafbf56cc049ebcdf7e39b9ef976e9c95c7b9bf3f32560d7e7
text_sha256: dba092980791ee278d0691ffa4bb7325fa42acada1660446d3eac7db577652e9
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty @ Linkedln-How I was able to bypass Open Redirection Protection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-01-24_bugbounty-linkedln-how-i-was-able-to-bypass-open-redirection-protection.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `2475e746050dcabafbf56cc049ebcdf7e39b9ef976e9c95c7b9bf3f32560d7e7`
- Text SHA256: `dba092980791ee278d0691ffa4bb7325fa42acada1660446d3eac7db577652e9`


## Content

---
title: "#BugBounty @ Linkedln-How I was able to bypass Open Redirection Protection"
url: "https://medium.com/bugbountywriteup/bugbounty-linkedln-how-i-was-able-to-bypass-open-redirection-protection-2e143eb36941"
authors: ["Avinash Jain (@logicbomb_1)"]
programs: ["LinkedIn"]
bugs: ["Open redirect"]
publication_date: "2018-01-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6000
scraped_via: "browseros"
---

# #BugBounty @ Linkedln-How I was able to bypass Open Redirection Protection

1

1

·

Top highlight

#BugBounty @ Linkedln-How I was able to bypass Open Redirection Protection
Avinash Jain (@logicbomb)
Follow
3 min read
·
Jan 25, 2018

693

6

Hi Guys,

Here I’ll be talking about a nice vulnerability that I found couple of months ago in Linkedln. Before jumping into the vulnerability, let me quickly brief you about Open Redirection-

Open redirection vulnerabilities arise when an application incorporates user-controllable data into the target of a redirection in an unsafe way. An attacker can construct a URL within the application that causes a redirection to an arbitrary external domain. An example of a vulnerable website link could look something like this: http://xyz.com/login.html?vulparam =https://xyz.com/next

In this example, “vulparam” parameter indicates where to send user upon successful login. If website doesn’t validate the “vulparam” parameter value to make sure that target web page is legitimate and intended, attacker could manipulate that parameter to send a victim to a fake page crafted by attacker: https://xyzcom/login.html?vulparam=http://evil.com

But bypassing Linkedln open redirection was not that easy. The vulnerable URL was —

https://www.linkedin.com/lite/external-redirect?url=http://evilzone.org&urlHash=YKI5

Linkedln has indeed some good protection against open redirection since I was not able to bypass using some common techniques like

url=../evilzone.org , url= ///evilzone.org , url= ///www.linkedln.com@www.evilzone.org/%2f%2e%2e

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now simply changing the “url” value to any malicious site won’t work here. As you can see there is an extra parameter “urlHash” which looks like some hash value for the URL to which the user getting redirected so if “urlHash” value is the actual valid hash value for the “url” then only successful redirection will take place. One thing was clear till now basic techniques were not going to do anything good and then I went back to the raw request to find some help —

Open Redirection Raw Request

The request includes the “referer” field, which indicates the last page the user was on (the one where they clicked the link) and here something striked my mind- “How about changing the referer header value and see whether the validation working there?” . So I quickly jumped into it and changed the header value to some other domains and [face palm] still no luck. :/ .

Let’s give one more try , I searched for LinkedIn android app referer and found the following link- https://github.com/snowplow/referer-parser/issues/131 and there came across LinkedIn android referer value as “ android-app://com.linkedin.android” . I used the referer value in the “referer” header field and the rest is as below :D —

Press enter or click to view image in full size

Successful redirection and yeah finally I managed to bypass the Open redirection protection of LinkedIn :)

Report details-

11-Nov-2017 — Bug reported to the concerned company.

07-Dec-2017 — Bug was marked fixed.

21-Dec-2017 — Re-tested and confirmed the fix.

Thanks for reading!

~Logicbomb (https://twitter.com/logicbomb_1)
