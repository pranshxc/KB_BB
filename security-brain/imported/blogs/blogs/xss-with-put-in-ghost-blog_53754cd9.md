---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-19_xss-with-put-in-ghost-blog.md
original_filename: 2018-10-19_xss-with-put-in-ghost-blog.md
title: XSS with PUT in Ghost Blog
category: blogs
detected_topics:
- xss
- command-injection
- otp
- cors
- api-security
tags:
- imported
- blogs
- xss
- command-injection
- otp
- cors
- api-security
language: en
raw_sha256: 53754cd9b5ff434cc05b61582e15fb50468d1808bbb0c5d9a4983399179ac036
text_sha256: 6306107e897c6a90bff1aab9c8746e3ab2e83e1821794dfbbd39a440fc30a8d5
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# XSS with PUT in Ghost Blog

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-19_xss-with-put-in-ghost-blog.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, cors, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `53754cd9b5ff434cc05b61582e15fb50468d1808bbb0c5d9a4983399179ac036`
- Text SHA256: `6306107e897c6a90bff1aab9c8746e3ab2e83e1821794dfbbd39a440fc30a8d5`


## Content

---
title: "XSS with PUT in Ghost Blog"
url: "https://www.itsecguy.com/xss-with-put-in-ghost-blog/"
final_url: "https://www.itsecguy.com/xss-with-put-in-ghost-blog/"
authors: ["Derek (@StackCrash)"]
programs: ["Ghost"]
bugs: ["XSS"]
publication_date: "2018-10-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5638
---

19 October 2018 / [XSS](/tag/xss/)

# XSS with PUT in Ghost Blog

# Intoduction

For my blog I have tried several content management systems and a while ago I decided to use Ghost for its simplicity and ease of use. Recently, I found XSS in the Ghost platform from at least version 1.24.9 and still in the latest version on [GitHub](https://github.com/TryGhost/Ghost). Most likely the XSS exists in much earlier versions as well.

_Note: this XSS does require administrator or owner roles and due to CORS/Same-Origin restrictions the likelyhood of exploitation outside of lab conditions is low._

# XSS in the API

While auditing Ghost I discovered that there is an API call that is vulnerable to XSS. The particular API call is `/ghost/api/v0.1/settings/`. The API call can be triggered from several of the settings tabs when an administrator or owner saves the settings. The API call sends a PUT request with JSON parameters. There are four parameters in the JSON that are vulnerable to XSS: logo, cover_image, ghost_head and ghost_foot. All four of the parameters will cause a XSS payload to be executed on every page of the website served by Ghost. The payload itself is very simple and only involves closing a script block before providing a new script block containing the XSS payload.  
![logo_xss_request](/content/images/2018/10/logo_xss_request.png)  
The full settings JSON does not need to be sent with the request in order to exploit the XSS. Only sending the desired parameter and payload is sufficient.  
![xss_payload](/content/images/2018/10/xss_payload.png)

Note: the ghost_head and ghost_foot parameters are the same ones where in the administrator interface a user can place custom scripts. So they are meant to contain scripts so the XSS ends up being intended functionality for those two parameters.

## Rediscovery

After finding the XSS I decided to do some more digging in Ghost past and found out I rediscovered an old XSS. VoidSec had previously discovered [XSS](https://voidsec.com/ghost-blogging-platform/) in the same API call. It should be noted Ghost claimed in version [0.5.9](https://github.com/TryGhost/Ghost/releases/tag/0.5.9) to have remediated this vulnerability and the original payload from VoidSec's report didn't work in the version I tested.

# Limitations

Due to the API call being an authenticated PUT request and limitations of CORS exploiting the vulnerability an attacker would have to have to be able to access the session token for an administrator or owner. It is possible to bypass the CORS restrictions by sending the request through a proxy such as [CORS Anywhere](https://github.com/Rob--W/cors-anywhere) But modern browsers won't send the session token with the request since it doesn't comply with the same origin policy. Bypassing the same origin policy is the harder part. There are ways to by pass the same origin policy but thats for another blog post.

# Disclosure

I initially disclosed to [[email protected]](/cdn-cgi/l/email-protection#5724323422253e232e17303f38242379382530) and until I sent a third email about the impending public disclosure I never received a response. After the thrid email they responded referencing their now updated [SECURITY.md](https://github.com/TryGhost/Ghost/commit/ebe0177b4f6fcc6c7debb741c95c985a69d0449b).

I did verify the XSS still exist as of version 2.2.0.

## Timeline

21 July 2018 - Initial reported to Ghost via email  
30 July 2018 - Follow-up email sent to Ghost  
4 October 2018 - Notified Ghost of upcoming public disclosure  
5 October 2018 - Response from Ghost referencing updated SECURITY.md  
19 October 2018 - Public disclosure after 90 days since initial report

#### [StackCrash](/author/stackcrash/)

Read [more posts](/author/stackcrash/) by this author.

[Read More](/author/stackcrash/)
