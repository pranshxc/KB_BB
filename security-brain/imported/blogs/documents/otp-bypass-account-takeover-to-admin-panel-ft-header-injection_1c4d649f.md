---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-28_otp-bypass-account-takeover-to-admin-panel-ft-header-injection.md
original_filename: 2021-01-28_otp-bypass-account-takeover-to-admin-panel-ft-header-injection.md
title: OTP Bypass Account Takeover to Admin Panel — Ft. Header Injection
category: documents
detected_topics:
- rate-limit
- access-control
- api-security
- command-injection
- otp
- supply-chain
tags:
- imported
- documents
- rate-limit
- access-control
- api-security
- command-injection
- otp
- supply-chain
language: en
raw_sha256: 1c4d649f5faffd69fc41e93625be2b74ea8a6b551671fddd0e50e8cc53e6bad4
text_sha256: f1d106da48ecee36dca3f8d34d6680488cd0c59063d954b75871f799a5c42e28
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# OTP Bypass Account Takeover to Admin Panel — Ft. Header Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-28_otp-bypass-account-takeover-to-admin-panel-ft-header-injection.md
- Source Type: markdown
- Detected Topics: rate-limit, access-control, api-security, command-injection, otp, supply-chain
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `1c4d649f5faffd69fc41e93625be2b74ea8a6b551671fddd0e50e8cc53e6bad4`
- Text SHA256: `f1d106da48ecee36dca3f8d34d6680488cd0c59063d954b75871f799a5c42e28`


## Content

---
title: "OTP Bypass Account Takeover to Admin Panel — Ft. Header Injection"
url: "https://logicbomb.medium.com/otp-bypass-account-takeover-to-admin-panel-ft-header-injection-16f2982a0136"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["OTP bypass", "Account takeover"]
publication_date: "2021-01-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3958
scraped_via: "browseros"
---

# OTP Bypass Account Takeover to Admin Panel — Ft. Header Injection

OTP Bypass Account Takeover to Admin Panel — Ft. Header Injection
Avinash Jain (@logicbomb)
Follow
4 min read
·
Jan 27, 2021

704

2

Press enter or click to view image in full size
Image Credit — keycdn.com

It
looks like this year has great promises at least the starting is good. Already 3 bug bounty in the pipeline(just showing off:P) and learned a nice methodology which laid down the opportunity for me to write and share this writeup with everyone. The best thing about being a part time bug bounty hunter is the learnings that it gives.

Besides working as a security engineer, if you are also a part time bug bounty hunter then always try to implement the learning you get from it, the defense mechanisms in your full time job wherever possible & also give back to the security community through blogs and writeups.

This writeup is also about something that I learned recently so let’s jump into the technicalities.

The target was an online education platform where there was OTP authentication implemented. When there is an OTP based login, the first thing that comes to everyone’s mind — “How to bypass it?”. Firstly I tried to brute force it and found that there was IP-based rate limiting implemented. That means varying client IP or the IP presented to the upstream server would be able to bypass rate limiting for OTP brute force.

If the client is behind a proxy, the proxy forwards the IP address of the client to the server in a specific header, X-Forwarded-For. In some cases, a client can use this header to spoof his IP address.

I tried the same here and inserted X-Forwarded-For header, gave it to the intruder to brute force OTP for a given phone number with varying IP address, and set Cluster bomb as a brute force attack type.

Press enter or click to view image in full size

and as expected, I was able to brute force the OTP to get the successful OTP login. Now it’s time to perform horizontal privilege escalation. It was evident that there is header injection present, so apart from bypassing IP access control or rate limiting, there could be other possibilities also that can be exploited here. Remembering what I did in my earlier organization where we restricted our WordPress administrator interfaces to only internal IPs based on the client’s IP address. Here how it works —

So if an allowed internal IP address is put in the header value, proxy will end up forwarding the value of X-Forwareded-For header even if the connection actually originated from a non-whitelisted IP address and allow the attacker to access the restricted page or API endpoint.

If the “X-Forward-For: 127.0.0.1” header is set, the responding server assumes that it is being accessed by an internal IP and allows the user to access restricted content. But for this, you need to be lucky to find such restricted pages. Normally admin pages/panel admin/sensitive endpoint is restricted.

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Tried accessing WordPress administrator interfaces on their blog page (wp-admin) and it was 200 OK!

Press enter or click to view image in full size

Now it was a matter of time to directory brute force and find if there is any more endpoint that is being IP based restricted. Found some useful resources to find such endpoints and gave them to Intruder to do the rest.
https://github.com/ziadab/AdminBomber/blob/master/AdminBomber.py https://github.com/s0md3v/Breacher/blob/master/paths.txt

Press enter or click to view image in full size

Luckily out of all those, there was one admin page of their CMS catalog which gave 200 OK (/cms/_admin/logon.php) and along with 200 OK, it was well succeded horizontal privilege escalation (though I haven’t gone one level up to try to login into the portal).

Possible Fix

Allow specifying a list of IPs (or CIDR’s) of trusted proxies and load balancers. If the request didn’t come from one of them, discard the X-Forwarded-For. Here is what Nginx does: Go through the list (starting from the last entry) and check each entry to see if it’s the list of trusted proxies. When one is encountered that’s not on the list, discard everything before it.

This is all about this interesting learning where to bypass IP based rate limiting host header injection was used (X-Forwarded-For) which was further used to access restricted endpoints.

Report details-

8-Jan-2021 — Bug reported to the concerned company.

11-Jan-2021 — Bug was marked fixed.

11-Jan-2021 — Re-tested and confirmed the fix.

20-Jan-2021 — Rewarded.

Thanks for reading!

~Logicbomb ( https://twitter.com/logicbomb_1 )
