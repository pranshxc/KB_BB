---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-04_stealing-side-channel-attack-tokens-in-facebook-account-switcher.md
original_filename: 2019-01-04_stealing-side-channel-attack-tokens-in-facebook-account-switcher.md
title: Stealing Side-Channel Attack Tokens in Facebook Account Switcher
category: documents
detected_topics:
- command-injection
- mfa
- otp
tags:
- imported
- documents
- command-injection
- mfa
- otp
language: en
raw_sha256: e390e94cd2988ff9272915e3971f099d9c3334a2043cc7d5de11435e1395b3b7
text_sha256: dbb40b1fdd935723fe0149dc70c027b3ff73103d42ed434a28eb35d7bb24212c
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing Side-Channel Attack Tokens in Facebook Account Switcher

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-04_stealing-side-channel-attack-tokens-in-facebook-account-switcher.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, otp
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `e390e94cd2988ff9272915e3971f099d9c3334a2043cc7d5de11435e1395b3b7`
- Text SHA256: `dbb40b1fdd935723fe0149dc70c027b3ff73103d42ed434a28eb35d7bb24212c`


## Content

---
title: "Stealing Side-Channel Attack Tokens in Facebook Account Switcher"
url: "https://medium.com/@maxpasqua/stealing-side-channel-attack-tokens-in-facebook-account-switcher-90c5944e3b58"
authors: ["Max Pasqua"]
programs: ["Meta / Facebook"]
bugs: ["Token leak"]
bounty: "1,000"
publication_date: "2019-01-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5490
scraped_via: "browseros"
---

# Stealing Side-Channel Attack Tokens in Facebook Account Switcher

Stealing Side-Channel Attack Tokens in Facebook Account Switcher
Max Pasqua
Follow
2 min read
·
Jan 5, 2019

213

2

After receiving an email from facebook that somebody requested to join my group I decided to open the link in a different account to see the results. I was brought to the “account switcher” page that looks like this.

Upon hitting continue it would normally log you out and prompt you to log in on the new account. But in the url for the account switcher there was a next paramater controlling where to go after hitting continue. On top of being able to control where the request goes, it also appends a fb_dtsg_ag token (the token used to prevent side-channel attacks on facebook).

The next task was to somehow find a a way to steal the tokens once the user hits continue. My main goal was to get the token to redirect to apps.facebook.com where I could harvest the token using an embedded iframe to pull the data from the url. The only problem was the next paramater didn’t support subdomains so it could only redirect to https://www.facebook.com/. Luckily enough facebook has an endpoint https://www.facebook.com/n/? where you can put any facebook domain after the ? and it will redirect. After a little bit of url encoding the final URL looked like this

https://www.facebook.com/notif_account_switching/&next=https%3A%2F%2Fwww.facebook.com%2Fn%2F%3Fhttps%253A%252F%252Fapps.facebook.com%252FAPPTOSTEALTOKENS%252523

Get Max Pasqua’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I clicked continue, and then checked my websites log file to see this

Press enter or click to view image in full size

Success!

Timeline

Submitted- December 7th, 2018

Triaged- December 10th, 2018

Team Asks for Verification on fix- January 3rd, 2019

Bounty Awarded($1000)- January 4th, 2019
