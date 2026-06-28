---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-19_adobe-bug-bounty-using-idor-confidential-data-leaks.md
original_filename: 2022-03-19_adobe-bug-bounty-using-idor-confidential-data-leaks.md
title: Adobe bug bounty using IDOR, Confidential data leaks
category: documents
detected_topics:
- idor
- sso
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- sso
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 4e3fa8d5e1a4789894e50039514e6035dc584c03af965ad5790bd17279f85db0
text_sha256: 400317b78afe550e75ae40e79580df44d9b3c0926d9d2fdf76d89cefa2ef4643
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Adobe bug bounty using IDOR, Confidential data leaks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-19_adobe-bug-bounty-using-idor-confidential-data-leaks.md
- Source Type: markdown
- Detected Topics: idor, sso, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `4e3fa8d5e1a4789894e50039514e6035dc584c03af965ad5790bd17279f85db0`
- Text SHA256: `400317b78afe550e75ae40e79580df44d9b3c0926d9d2fdf76d89cefa2ef4643`


## Content

---
title: "Adobe bug bounty using IDOR, Confidential data leaks"
url: "https://debprasadbanerjee502.medium.com/adobe-bug-bounty-using-idor-confidential-data-leaks-f6c55e5143d0"
authors: ["Debprasad Banerjee"]
programs: ["Adobe"]
bugs: ["IDOR"]
publication_date: "2022-03-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2802
scraped_via: "browseros"
---

# Adobe bug bounty using IDOR, Confidential data leaks

Adobe bug bounty using IDOR, Confidential data leaks
Ravaan
Follow
3 min read
·
Mar 18, 2022

162

4

Hey, amazing hackers. So I hacked Adobe, and here’s exactly how I did it. Let this be a lesson to the beginner bug bounty enthusiasts who are looking for good bugs. I'll tell you what you need to do to find bugs and where to find them.

INTRO: Beginner’s Nightmare

This was my first-month doing bug bounty hunting and if you don’t know it already I took up a 6 months challenge. I’m from a network penetration background so I basically sucked in the web apps. In my first month, I spent every day listening to all the good lectures by the bug crowd and reading a ton of books such as OWASP Testing guide. The theory is different from practical and I was basically lost. I decided to leave my pending work and focus deeply. I spent countless hours looking for bugs but everything was to no avail. I found some low-hanging fruits using tools but never reported them cause not worth it

ADOBE:

I took up the challenge to hack adobe and yeah it was hella secure, everything was neatly wrapped under WAF and i was always getting blocked. I decided to focus to slight manipulation techniques such as IDORs so i started gathering every single parameter. How?

Gauplus, gauplus is basically Gau on drugs, its faster, more stable and easier to use.

Firstly I collected all the domains and using subdomain enumeration, from my previous blog, I sorted them into a text file adobe.txt Using gau i now collect every single parameter and endpoint, I like to exclude images and other stuff but you can add it.

cat adobe.txt | gauplus — subs -b png,jpg,gif,jpeg,swf,woff -o adobeurl.txt

Now I use my httpx to check which URLs are live, this is optional

cat adobeurl.txt | httpx -mc 200 >> finalurls.txt

Finally, we have a beautiful list of URLs with parameters to choose from.

Get Ravaan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I grep through various stuff such as id= and confidential, secret, employee but this time i went through a URL called document which is normally usual.

The climax:

I visit the document URL, now I find a usual document, nothing interesting but then i looked at the URL, it had document/200, I changed that 200 to 201 but nothing happened so maybe no IDOR? I sent the request to burp>Intruder> use 100–1000 as payload set and fuzz the document/$200$, BOOM! here's the response. But now the question is, are the files really confidential? So turns out yes, not only documents but highly critical internal data is also leaked.

Press enter or click to view image in full size
Sorting by length or status code
Press enter or click to view image in full size
EXAMPLE OF SUCH

Reported it 3 months ago, it got a medium 5.3 severity and got fixed today so I'm extremely happy.

KEY POINTS: DIG THROUGH ALL PARAMETERS

Understand the application

LOOK FOR OUT-OF-THE-BOX SOLUTIONS.

PS: I don’t write to show off but to teach so no mentions of the bounty will be entertained. The motive of a learner is to learn and these days hackers are getting distracted. Keep shining. PEACE- RAVAAN
