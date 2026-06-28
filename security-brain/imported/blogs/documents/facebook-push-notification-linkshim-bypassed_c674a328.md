---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-07_facebook-push-notification-linkshim-bypassed.md
original_filename: 2020-12-07_facebook-push-notification-linkshim-bypassed.md
title: Facebook push notification linkshim bypassed
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: c674a328752e6e332c058e0207be7dcfc8556aa96c341ebce50109823b562555
text_sha256: 6f4a13599a1bee0132511a5098cba3082ce2705b52cdbf0e665f4e26eb9a1336
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook push notification linkshim bypassed

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-07_facebook-push-notification-linkshim-bypassed.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `c674a328752e6e332c058e0207be7dcfc8556aa96c341ebce50109823b562555`
- Text SHA256: `6f4a13599a1bee0132511a5098cba3082ce2705b52cdbf0e665f4e26eb9a1336`


## Content

---
title: "Facebook push notification linkshim bypassed"
page_title: "Facebook Push Notification Linkshim Bypassed | by Neil Mark Ochea / mhl_0xnmo | InfoSec Write-ups"
url: "https://infosecwriteups.com/facebook-push-notification-linkshim-bypassed-385fe471516"
authors: ["Neil Mark Ochea (@nmochea)"]
programs: ["Meta / Facebook"]
bugs: ["Open redirect"]
publication_date: "2020-12-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4083
scraped_via: "browseros"
---

# Facebook push notification linkshim bypassed

Facebook Push Notification Linkshim Bypassed
Neil Mark Ochea / mhl_0xnmo
Follow
3 min read
·
Dec 7, 2020

71

1

While browsing and finding facebook vulnerability I accidentally found this facebook push notification link

Press enter or click to view image in full size

when I visited the facebook link something strange the whole facebook page has blank, there’s nothing here hmm so I view the source code and read it to analyze

Snippet JavaScript Code

Press enter or click to view image in full size

The redirectUrl are vulnerable to open redirect by adding link in the endpoint parameter so I quickly check if the url have endpoint parameter and yess.

I add my website on the endpoint parameter ?ref= but nothing happened hmm so I try to bypassed using url encode

Press enter or click to view image in full size

but still nothing happened and then I add more %2f to the web url

Press enter or click to view image in full size

then Boomm the facebook page redirect to my website

Press enter or click to view image in full size

although I trying to perform xss but its already filtered by hex encoding and my knowledge is not enough to bypassed the hex filters.

What is Linkshim

Every time a link is clicked on the site, the link will check that the URL against Facebook has its own internal list of malicious links, along with the lists of numerous external partners including McAfee, Google, Web of Trust, and Websense. If Facebook detects that a URL is malicious, Facebook will display an interstitial page before the browser actually requests the suspicious page.

Read the full explanation in this link: www.facebook.com

Get Neil Mark Ochea / mhl_0xnmo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Setup

User UserOne

Step to Reproduce

From any web browser login as UserOne and go to
Press enter or click to view image in full size
Now insert website on the parameter endpoint the result look like this
Press enter or click to view image in full size
Add more slash / and then encode the website url to url encode and insert to the endpoint parameter
Press enter or click to view image in full size
Hit enter it will redirect to www.mydomain.com/login.php linkshim finally bypassed.
Press enter or click to view image in full size
Disclosure Timeline
September 22, 2020 – I reported this vulnerability issue in facebook whitehat page.
September 23, 2020 – The Facebook team reproduces & investigates regarding this vulnerability issue.
September 28, 2020 – I provided more details regarding this vulnerability issue.
October 08, 2020 – The vulnerability issue has been patched.
October 21, 2020 – Bounty rewarded.

Thanks for reading this article, I hope you guys learn something new today. Please share this article to spread the knowledge.

Don’t forget to follow and connect with me through LinkedIn, and Twitter.
