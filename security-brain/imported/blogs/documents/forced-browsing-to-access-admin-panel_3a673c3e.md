---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-13_forced-browsing-to-access-admin-panel.md
original_filename: 2021-07-13_forced-browsing-to-access-admin-panel.md
title: Forced Browsing to Access Admin Panel
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 3a673c3e3740f41d56feb415fbba9b1e1c4ef78ed04edf4709b739de8d39ca12
text_sha256: b85de1ae8f0435c44b2032a1a0008d5277d81379954610fb0d630814083acf26
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Forced Browsing to Access Admin Panel

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-13_forced-browsing-to-access-admin-panel.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `3a673c3e3740f41d56feb415fbba9b1e1c4ef78ed04edf4709b739de8d39ca12`
- Text SHA256: `b85de1ae8f0435c44b2032a1a0008d5277d81379954610fb0d630814083acf26`


## Content

---
title: "Forced Browsing to Access Admin Panel"
url: "https://vijetareigns.medium.com/forced-browsing-to-access-admin-panel-214a7defa2a5"
authors: ["the_unluck_guy (@7he_unlucky_guy)"]
bugs: ["Forced browsing"]
publication_date: "2021-07-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3509
scraped_via: "browseros"
---

# Forced Browsing to Access Admin Panel

the_unlucky_guy
 highlighted

Forced Browsing to Access Admin Panel
the_unlucky_guy
Follow
2 min read
·
Jul 13, 2021

534

4

Hello hackers, it’s been a while and I haven’t write anything about my finding. So, I decided to share one of my interesting findings. I am not allowed to share the organization name so I will be using redacted.com as the main domain.

*.redacted.com is in scope. As usual, I started with subdomain enumeration, for subdomain enumeration I mostly use a combination of subfinder +findomain+amass. After enumerating all subdomains of redacted.com, I saw an interesting subdomain admin.redacted.com. So I think why not try pwning admin panel. I fired my burp suite and started exploring admin.redacted.com. When I open admin.redacted.com then the website redirected me to the login page admin.redacted.com/login. I tried for some common username/password combinations to log in but none worked. Side by side I fetched all Javascript files using the GetJS tool and started looking for juicy information in JS files. I got some common path in JS files like /admin/dashboard , /admin/user , /backend , /admin/user/backend. When I try to browse these paths then the website again redirected me to the login page. I was like.

Then I started looking into all requests of admin.redacted.com in burp. I saw an interested endpoint /backend/admin/user/user-menu.json in which the cookie header having PHPSESSID and some extra server-side cookies.

Press enter or click to view image in full size

So, I thought why not try to explore the endpoints /admin/dashboard, /admin/user, /backend, /admin/user/backend using those cookies, and yayy I can see all details of the admin panel which is exposing server-side sensitive information. I was only allowed to browse endpoint by forced browsing to the path with cookies, when I manually try to browse by clicking on the website then again I was redirected to the login page. So, I can see details only by forced browsing the path with cookies I have.

Get the_unlucky_guy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Timeline:

October 21, 2020 — Reported

October 26, 2020 — Triaged and Bounty awarded

December 10, 2020 — Fixed.

Thanks for reading, hope you learned something new. Do clap and share if you like. I will write more of my findings soon so, stay tuned for my next write-up.

Twitter: 7he_unlucky_guy
