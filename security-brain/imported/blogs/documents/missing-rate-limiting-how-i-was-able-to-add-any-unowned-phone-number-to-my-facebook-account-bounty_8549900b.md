---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-31_missing-rate-limiting-how-i-was-able-to-add-any-unowned-phone-number-to-my-faceb.md
original_filename: 2022-01-31_missing-rate-limiting-how-i-was-able-to-add-any-unowned-phone-number-to-my-faceb.md
title: 'Missing rate-limiting. How I was able to add any unowned phone number to my
  Facebook account? (Bounty: 5000 USD)'
category: documents
detected_topics:
- rate-limit
- command-injection
- otp
tags:
- imported
- documents
- rate-limit
- command-injection
- otp
language: en
raw_sha256: 8549900bae86ab90fe1329300102c639d4c3e41990532217788d91677ad356bd
text_sha256: 3d630f89f9223d86d5517296459612efd423ac3829806717edc0066487ebb648
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Missing rate-limiting. How I was able to add any unowned phone number to my Facebook account? (Bounty: 5000 USD)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-31_missing-rate-limiting-how-i-was-able-to-add-any-unowned-phone-number-to-my-faceb.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, otp
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `8549900bae86ab90fe1329300102c639d4c3e41990532217788d91677ad356bd`
- Text SHA256: `3d630f89f9223d86d5517296459612efd423ac3829806717edc0066487ebb648`


## Content

---
title: "Missing rate-limiting. How I was able to add any unowned phone number to my Facebook account? (Bounty: 5000 USD)"
page_title: "[WRITE-UP] Missing rate-limiting. How I was able to add any unowned phone number to my Facebook account? (Bounty: 5000 USD) | by Shubham Bhamare | InfoSec Write-ups"
url: "https://theshubh77.medium.com/write-up-missing-rate-limiting-how-i-was-able-to-add-any-unowned-phone-number-to-my-fb-account-fe4d7e67cf10"
authors: ["Shubham Bhamare (@theshubh77)"]
programs: ["Meta / Facebook"]
bugs: ["OTP bruteforce", "Lack of rate limiting"]
bounty: "5,000"
publication_date: "2022-01-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2960
scraped_via: "browseros"
---

# Missing rate-limiting. How I was able to add any unowned phone number to my Facebook account? (Bounty: 5000 USD)

Missing rate-limiting. How I was able to add any unowned phone number to my Facebook account? (Bounty: 5000 USD)
Shubham Bhamare
Follow
4 min read
·
Jan 30, 2022

764

3

Press enter or click to view image in full size

Hi guys, I’m Shubham Bhamare again. In this write-up, I’m going to tell you how I was able to add any unowned phone number to my Facebook account without the victim’s knowledge. It was a very easy finding.

Without wasting time, let’s start! 👉

===

Reproduction steps:

Step 1: Using d.facebook.com subdomain, create a new Facebook account with the victim’s phone number.

Step 2: After successfully creating an account, do some suspicious activities (e.g. send friend requests to random people, post multiple comments, etc.) so that Facebook will block you from doing further activities and show the following checkpoint screen.

Step 3: Now, click the Continue button and complete the CAPTCHA verification. So that you'll be redirected to the following screen where you’ll have to enter the same phone number of the victim (which you’ve used to create a new Facebook account before.)

Step 4: Enter the victim’s phone number and click on the Send Code button. You’ll be redirected to the following screen where you’ll have to enter OTP.

Press enter or click to view image in full size

Step 5: If you try to brute-force here, you’ll find that rate-limiting is missing so that you can confirm any unowned phone number.

Press enter or click to view image in full size

To test this issue, I tried 5000+ payloads though the system didn’t block me and I was able to confirm that unowned phone number with valid payload after 5000+ requests.

First I tested this issue on the main domain of Facebook but it wasn’t vulnerable. So I tested it on one of my favorite Facebook subdomain d.facebook.com. (However other subdomains i.e. m.facebook, x.facebook, mbasic.facebook, touch.facebook, iphone.facebook was also vulnerable.)

===

The story behind it:

On Jul 17, 2019 (when I reported this issue), I wasn’t in the mood of hunting bugs and was just browsing some meme pages on Facebook. That time I thought I should also start my own meme page and earn some passive income. So I created a new Facebook account with my other phone number.

Get Shubham Bhamare’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But after some actions and as the phone number wasn’t verified, Facebook blocked me and asked me to confirm my phone number. That time I thought that why not I should brute-force here? And BOOOOOOOM!💥 I found that the rate-limiting was missing.

===

Timeline:

Jul 17, 2019: Report sent

Jul 22, 2019: Pre-triaged

Jul 26, 2019: Triaged

Jul 27, 2019: Issue mitigated with following message

Press enter or click to view image in full size

Aug 01, 2019: Fixed completely

Aug 12, 2019: 5000 USD bounty awarded

Press enter or click to view image in full size

===

Things I tried to bypass this issue:

After reading this awesome article on IP Rotation by Lokesh Kumar, I tried to bypass this issue with the same technique. But I couldn’t bypass it. 🥲

===

Takeaway(s):

While browsing something (even though you’re not in the mood of hunting bugs), always observe whether something’s working as intended or not.
Always try to bypass the fix of your every finding. Even though you won’t be able to bypass it, you’ll learn something new. (In my case, I learned how to rotate IPs.)

===

Thank you for reading! Stay tuned for my next write-up, and don’t forget to follow me on Facebook, Twitter, LinkedIn, and Instagram. 😊

===

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
