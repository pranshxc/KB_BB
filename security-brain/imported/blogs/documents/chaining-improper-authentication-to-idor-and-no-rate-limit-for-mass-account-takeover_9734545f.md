---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-12_chaining-improper-authentication-to-idor-and-no-rate-limit-for-mass-account-take.md
original_filename: 2021-11-12_chaining-improper-authentication-to-idor-and-no-rate-limit-for-mass-account-take.md
title: chaining improper authentication to idor and no rate limit for mass account
  takeover
category: documents
detected_topics:
- rate-limit
- idor
- ssrf
- xss
- sqli
- command-injection
tags:
- imported
- documents
- rate-limit
- idor
- ssrf
- xss
- sqli
- command-injection
language: en
raw_sha256: 9734545fe6b7ed9abeba9825d1dfbe5a3c40dc1a602fccb27b5644091ed16d14
text_sha256: e11b0109605f602965946101f6f74634c202c0640982a42a52b55cd6f2359017
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# chaining improper authentication to idor and no rate limit for mass account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-12_chaining-improper-authentication-to-idor-and-no-rate-limit-for-mass-account-take.md
- Source Type: markdown
- Detected Topics: rate-limit, idor, ssrf, xss, sqli, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `9734545fe6b7ed9abeba9825d1dfbe5a3c40dc1a602fccb27b5644091ed16d14`
- Text SHA256: `e11b0109605f602965946101f6f74634c202c0640982a42a52b55cd6f2359017`


## Content

---
title: "chaining improper authentication to idor and no rate limit for mass account takeover"
url: "https://tox7cv3nom.github.io/2021/11/12/chaining-of-csrf-token-misconfiguration-and-no-rate-limit-leads-to-mass-account-takeover.html"
final_url: "https://tox7cv3nom.github.io/2021/11/12/chaining-of-csrf-token-misconfiguration-and-no-rate-limit-leads-to-mass-account-takeover.html"
authors: ["mohit (@mohit29295572)"]
bugs: ["Account takeover", "Lack of rate limiting", "CSRF", "IDOR"]
publication_date: "2021-11-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3177
---

Hello folks, hope you all are doing well Today i will share a vulnerablity i discovered in a bug bounty program which leads to takeover of mass accounts login ito the website so let’s start

![animated](https://media.giphy.com/media/QJvwBSGaoc4eI/giphy.gif)

# Recon Phase

I was pentesting on the domain then i found that there is x-rate- limit option there was no point in reporting no rate limit then i dig more spend few hours in fuzzing, parameter bruteforcing if you wanna more about parameter bruteforcing you can read my twitter [post](https://twitter.com/mohit29295572/status/1457031388130000896) then i came to know the endpoint “/api/v1/users/id” I don’t know what to do next when i send that request it shows that 401 unauthorized I started digging deeper more and more then i found out the real mechanism I saw there in headers there was a csrf token which is use to prevent idor I removed the parameter and send the request this time web server comes with the response of 200 with some json response I was happy because i knew there was the weak authentication token If you wanna know more about this vulnerablity you can read from here [here](https://github.com/tox7cv3nom/tox7cv3nom.github.io/edit/master/_posts/2021-05-30-abuse-auth-token-to-get-account-takeover-via-chained-csrf.md)

I start fuzzing on the id enpoint but i got nothing then i saw http history in burpsuite there i saw a request of mine in wich some digits are appearing after the endpoint id that was my forgot password request I create the another account and extract the id of 2nd account then in old reuest i replace the digits of old account from my new account digits but i got 401 i am still stuck at that point I was like :

![animated](https://media.giphy.com/media/l1KVaj5UcbHwrBMqI/giphy.gif)

Then i saw i didn’t remove the csrf token -_- my silly mistake Xd after removing that parameter i get response of 200 means it’s idor confirmed

# Chaining the bugs

I was thinking what to do report or find more bugs for chaining then suddenly a idea stuck in my mind i remember i found a bug called no rate limit earlier I suddenly fire up myburpsuite again capture the request of “https://redacted.com/api/v1/users/id/$$’ and create a the payload since there was only 3 digits i tried 3k-5k range numbers and went to do some work after i came back there i see multiple 200 responses and that responses contains session token, user id, password in plain text, etc. and that was only 2k requests in which i takeover accounts of victims.

If you like my content you can buy me a cofee as a support XD

Tip:-

Always spend time on recon don’t try to find out xml, rce type high vulnerablities at first instance try to find technical bugs and one more thing by putting blindly xss,sqli,ssrf and ssti payloads doesnt make you hacker but recon and patience does <3

Sorry for my grammer mistakes if any have in article and keep hacking :p
