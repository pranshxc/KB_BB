---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-25_rce-via-account-takeover.md
original_filename: 2023-08-25_rce-via-account-takeover.md
title: RCE via Account Takeover
category: documents
detected_topics:
- oauth
- idor
- access-control
- ssrf
- xss
- command-injection
tags:
- imported
- documents
- oauth
- idor
- access-control
- ssrf
- xss
- command-injection
language: en
raw_sha256: d6902d1c59f3a864d7f14090dcc59657d77ddae3410ce2da3626b30deea10594
text_sha256: 652cd96e49bbed860a5065e8c7835e666576834565bcfcbe78d9fed2322d95ec
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# RCE via Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-25_rce-via-account-takeover.md
- Source Type: markdown
- Detected Topics: oauth, idor, access-control, ssrf, xss, command-injection
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `d6902d1c59f3a864d7f14090dcc59657d77ddae3410ce2da3626b30deea10594`
- Text SHA256: `652cd96e49bbed860a5065e8c7835e666576834565bcfcbe78d9fed2322d95ec`


## Content

---
title: "RCE via Account Takeover"
url: "https://medium.com/vault-infosec/rce-via-account-takeover-a6fea7390385"
authors: ["Karthikeyan.V (@karthithehacker)"]
bugs: ["RCE", "Account takeover", "IDOR"]
publication_date: "2023-08-25"
added_date: "2023-09-05"
source: "pentester.land/writeups.json"
original_index: 833
scraped_via: "browseros"
---

# RCE via Account Takeover

RCE via Account Takeover
Karthikeyan
Follow
3 min read
·
Aug 25, 2023

37

1

Press enter or click to view image in full size

In this blog, I am going to share a bug that I came across while performing VAPT for a private project.

Get Karthikeyan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This is a CMS website that I was doing VAPT for. so in CMS, the chance of finding bugs is lower as their version is updated and there are no known CVEs and exploits for that particular version. Initially, I understood the application flow, then tested for bugs like XSS, SSRF, LFI, etc None of them worked out, there are some custom templates used in the website, so I tried SSTI and CSTI for the template injection, but it was also in vain.
Then something caught my eye while navigating to the My Account section, The UserID was passing in the URL, and then I started to tamper with the UserID, and now it’s showing the user details of the tampered UserID. Similarly, the UserID passes in the URL for the Change Password, where it asks for the current password to change the password. I changed the UserID value in the URL to that of another user, and surprisingly, it worked, and was able to change the password without any validation.

Press enter or click to view image in full size

Then I figured out the Admin’s user ID must be one, tried to change its password and it worked. Now I have control over the Admin’s account After that traversed the admin account and found an option to execute PHP code on the website which reminds me of the pentestmonkey php reverse shell.

Press enter or click to view image in full size

Then I used ngrok for port forwarding to receive a connection. I altered the payload, started a Netcat listener on my local machine, and executed the payload in the PHP execute function. As soon as the payload was executed, a reverse shell was spawned in the terminal.

Press enter or click to view image in full size

The reason I was able to take over the account is because of the custom OAuth implemented on the site, where they didn’t configure the authorization properly. The PHP execute extension should not be used on the website; in the event of a breach or successful attack, the attacker might use this functionality to take control of the system. The CMS vendor also advises the user not to use these kinds of extensions.

I hope you find this blog useful, will be back with another interesting blog.
