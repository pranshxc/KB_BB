---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-18_million-users-pii-leak-data-leak_2.md
original_filename: 2019-11-18_million-users-pii-leak-data-leak_2.md
title: Million Users PII Leak Data Leak
category: documents
detected_topics:
- xss
- cloud-security
- idor
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- xss
- cloud-security
- idor
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: b8b7dd4d844c150c24f48136c69ed722d0dbaa2e13b2e0245d26e865f0844876
text_sha256: 8fc5b78157ef7c30f39df57a802fb7952b2eafa5b3572bec66f954eece1e1dfb
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Million Users PII Leak Data Leak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-18_million-users-pii-leak-data-leak_2.md
- Source Type: markdown
- Detected Topics: xss, cloud-security, idor, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `b8b7dd4d844c150c24f48136c69ed722d0dbaa2e13b2e0245d26e865f0844876`
- Text SHA256: `8fc5b78157ef7c30f39df57a802fb7952b2eafa5b3572bec66f954eece1e1dfb`


## Content

---
title: "Million Users PII Leak Data Leak"
page_title: "Million Users PII — Data Leak | by Shivbihari Pandey | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/million-users-pii-leak-attack-288c5e37b283"
authors: ["Shivbihari Pandey (@ninja_pandit_)"]
bugs: ["Information disclosure", "Blind XSS"]
bounty: "3,250"
publication_date: "2019-11-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4933
scraped_via: "browseros"
---

# Million Users PII Leak Data Leak

Million Users PII — Data Leak
Shivbihari Pandey
Follow
3 min read
·
Nov 18, 2019

170

1

Hello Everyone

Hope you are doing good

Today i am going to discuss about the information leak in some popular websites .For Privacy Purpose we will not discuss about company Name.

1: Million of users Medical records and there personal Details Leak due to AWS S3 bucket mis-configuration:

I was testing there websites for an hour and didn’t able to find any High Severity bug,after an hour of reconan dtesting ,i was able to found couple of IDOR and XSS, but i wanted to find some critical issue.

I was about to give up , suddenly i see ,they are using Amazon Cloudfront Service for storing public image && URL look something like this

https://d3ez8in977xyz.cloudfront.net/avatars/009afs8253c47248886d8ba021fd411f.jpg

initially i think its just public data but i try to visit https://d3ez8in977xyz.cloudfront.net , and i found that they storing public images , but after seeing other files i was shocked to see they have stored some personal data publicly like:

video chat, audio calls, text message and some user private files.

well these files have contained conversion between the patient and Doctors.

and different domain have there different storage bucket and so i start finding the other domain image storage location, and each bucket have thousands of data, well i didn’t calculated how many users info stored in it, but after googling the company users , found out they have millions users.

this is the one of bucket Pic :in csv file ,it contain Text Messages between them

Press enter or click to view image in full size
Bucket List

So I Quickly reported to them and they resolved it within hour and awarded me $2500 bounty with $500 bonus bounty.

Get Shivbihari Pandey’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Funny Thing here is that

I have listened some of the audio files and i found one thing common , most of them are about Girlfriend/Boyfriend Issues, and they all crying about how they are suffering with anxiety after he/she dumped him/her ,because they find there partners Cheating . 😄

2: Internal Admin Account Access ,Leak Business Partners Details

So this is Story About blind stored XSS Found in Giant MNC Company, website,by this i was able to get the details of admin account [Access Token and other personal details]and along with, i was able to get there Business Clients details too.

I found Vulnerable point in their form , and these form data is stored in Local admin account.

so instead of simple XSS payload, i used XSSHunter Payload , so whenever my payload executed , it will send data back to me.

Press enter or click to view image in full size
PII Data Leak

For this Issue, they awarded me $1250 Bounty

That’s it for Now

If you Love It, Feel Free to ReTweet it.

Rich Guy Can Donate Here 😄

Good Bye..!!

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
