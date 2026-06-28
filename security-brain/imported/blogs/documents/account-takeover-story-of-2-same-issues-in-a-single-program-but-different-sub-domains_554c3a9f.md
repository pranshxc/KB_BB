---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-10_account-takeover-story-of-2-same-issues-in-a-single-program-but-different-sub-do.md
original_filename: 2021-10-10_account-takeover-story-of-2-same-issues-in-a-single-program-but-different-sub-do.md
title: Account Takeover — Story of 2 same issues in a single program but different
  sub-domains.
category: documents
detected_topics:
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 554c3a9f491108c487f5e4a0bd1d5d32d6a563438565542c248bf91d56447cf5
text_sha256: 57dc1d67aead5c2ee01ab4cbecfb0d9be1cc301b720474b84e574a6d258de561
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover — Story of 2 same issues in a single program but different sub-domains.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-10_account-takeover-story-of-2-same-issues-in-a-single-program-but-different-sub-do.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `554c3a9f491108c487f5e4a0bd1d5d32d6a563438565542c248bf91d56447cf5`
- Text SHA256: `57dc1d67aead5c2ee01ab4cbecfb0d9be1cc301b720474b84e574a6d258de561`


## Content

---
title: "Account Takeover — Story of 2 same issues in a single program but different sub-domains."
url: "https://hunter-55.medium.com/account-takeover-story-of-2-same-issues-in-a-single-program-but-different-sub-domains-in-10-minutes-840b2701db91"
authors: ["Himanshu Pdy (@himanshu_pdy)"]
bugs: ["Account takeover"]
publication_date: "2021-10-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3252
scraped_via: "browseros"
---

# Account Takeover — Story of 2 same issues in a single program but different sub-domains.

Account Takeover — Story of 2 same issues in a single program but different sub-domains.
himanshu pdy
Follow
3 min read
·
Oct 10, 2021

65

Hello Security folks, Here is interesting finding which I want to share.I only write when I find something unique or something interesting. Otherwise there are so many bug-hunters who find excellent security issues and write about them. There are tons of write-ups related to every security issue. My Twitter and Linkedin.

Here’s My Story :-
Past Finding :-

About 1 years ago, at this exact same time I found straightforward security issue related to account takeover.The scope was very limited. Only 3 subdomains.

Security Issue ( Took only 5 minutes ):-

During sign up process on app.target.com , the system was not checking whether the email is owned by user or not.
Also the application was not verifying whether the email id is already in server or not.
So I was able to sign up with any email id and takeover any user account.

I though let’s take it to something more severe, so I tested support@target.com and viola I was able to takeover it and able to view all projects.

So I reported it to them through HackerOne and they patched It by implementing verification whether the email is already registered in server or not.They rewarded me with 3 digit bounty — i expected 4 digit … LOL.

They fixed it by verifying whether the email is already registered or not, but didn’t implemented whether the user is owner of the email or not.
That means no verification on sign up process.

3. I asked them to put a verification at sign up process but they said that will be not a problem for our company.

Get himanshu pdy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I said ok, and moved to next target on HackerOne.

After 1 Year, [September — 2021] story continues.

Remember I said no verification on sign up process was still there.

So recently , I started poking around their android application. I was going through their application source code (Apk file ) and found some normal website.

I first ignored them , I don’t know why.

So the main story, the website was “app.trgt.net” , which was similar to app.target.com. They used “trgt” as the sort form of target.

* This is a mirror page of the same website and the patch is implemented here also ( whether email is already registered or not in the database ).

* But they didn’t verify whether the email is owned by user or not. ( No Verification on signup process )

I tried to sign up with support@target.com and guess what I got the access to several ongoing project files. Same issue which i reported to them 1 year ago.

I immediately reported to them.
They didn’t had these subdomains in their scope list, but because it is a high impact issue they accepted it.
I didn’t found these subdomain through scanner like findomain, sublist3r, etc. It was manual one. These subdomains were not on the google.
What I Learned from this :-

Don’t rely on scanner to find you interesting subdomain, poke around their web application as well as android application. You may find some interesting domains to test. Always try to increase your attack area.

If you find it interesting and if it helped you in anyway share it and, hope you learned something.
