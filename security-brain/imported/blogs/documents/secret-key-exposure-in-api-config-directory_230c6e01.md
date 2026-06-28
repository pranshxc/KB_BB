---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-01_secret-key-exposure-in-api-config-directory.md
original_filename: 2021-03-01_secret-key-exposure-in-api-config-directory.md
title: Secret Key Exposure in API Config Directory
category: documents
detected_topics:
- sso
- command-injection
- otp
- information-disclosure
- api-security
tags:
- imported
- documents
- sso
- command-injection
- otp
- information-disclosure
- api-security
language: en
raw_sha256: 230c6e01c19ab4d773825c8877ab8927446ef96165f748ecc3f2737fbd3de87f
text_sha256: db3641eed5c25d5c1cdd348a7603b0b34dd824f892a05b6ba70b524ab1dc8a47
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Secret Key Exposure in API Config Directory

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-01_secret-key-exposure-in-api-config-directory.md
- Source Type: markdown
- Detected Topics: sso, command-injection, otp, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `230c6e01c19ab4d773825c8877ab8927446ef96165f748ecc3f2737fbd3de87f`
- Text SHA256: `db3641eed5c25d5c1cdd348a7603b0b34dd824f892a05b6ba70b524ab1dc8a47`


## Content

---
title: "Secret Key Exposure in API Config Directory"
url: "https://ahmdhalabi.medium.com/secret-key-exposure-in-api-config-directory-79cf7e7b976"
authors: ["Ahmad Halabi (@Ahmad_Halabi_)"]
bugs: ["Information disclosure"]
bounty: "800"
publication_date: "2021-03-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3849
scraped_via: "browseros"
---

# Secret Key Exposure in API Config Directory

Secret Key Exposure in API Config Directory
Ahmad Halabi
Follow
3 min read
·
Mar 1, 2021

446

2

Hello,

My name is Ahmad Halabi, Founder & CTO at Cybit Sec and I am currently a part time bug bounty hunter mostly on Hackerone.

At the beginning of this month, I got an invitation to a private program specialized in Big Data and Integration services. The scope was limited to a website having dashboard.

Going after the Dashboard, I was able to find one valid bug. Then while checking the traffic in Burpsuite, I found that there is an API for this dashboard as the following: https://redacted.com/api.

Time For Some Recon:

First interesting thing to do is Discovering API Content and Directories. So I used a Wordlist that I usually customize it and FFUF tool to bruteforce the API Content.

I found an interesting directory called config: https://redacted.com/api/config. After checking its content I found that there is a token called `LoginUrlSecretKey`. And its value is something like: S#@x%^&$!1 … This value left my attention.

Press enter or click to view image in full size

Doing Additional Recon About Key Value:

So I found a secret key that is probably used for API Login purpose. My main goal after that was to know where the token is used ?

I tried several methods and techniques to detect where the key is used or any other useful information connected to that key. Below are some steps that I did:

I used Github to search for the Secret Key inside the target program Github Repositories. Sadly no positive results were found.
I used Google Dorks trying to find any info related to the secret token. Also got negative results.
I also checked WaybackUrls and Javascript Files and sadly got negative results.

This means that there are two possibilities:
1. Either the secret key is a dummy key used for testing purposes.
2. Or the key is truly secret as its name represents and because I didn’t find any information related to it in my recon.

Get Ahmad Halabi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I decided to report the issue based on the second assumption.

Reporting The Bug:

Feb 4, 2021: I sent the report describing the issue that I found.
Feb 5, 2021: HackerOne Triage Closed the Report as Informative. Stating that an app is “leaking” these secrets doesn’t necessarily mean that there’s a security risk. And asking me to provide more details if I want my report to be reconsidered.
Feb 5, 2021: I provided additional details about my recon process in determining why the Key is Secret to the Program proving how I didn’t find any information related to it based on my second assumption.
Feb 5, 2021: HackerOne Triage Forwarded the report to the internal team.
Feb 22, 2021: Report got Triaged by HackerOne Triage Team.
Feb 26, 2021: Severity Updated to High. Bounty Awarded ($800). Report Resolved & Fix Confirmed.

Lesson Learned:

There are some times where you find a secret key, token or password and you don’t know how it can be used or if it is secret exposed or not.
Some programs don’t accept the report because you are unable to prove that the exposed key is sensitive since you don’t know where or how to use it. So try flipping the scenario to the opposite and prove to them that the key is secret because nothing related to it is found publicly on the internet by demonstrating your recon approach in identifying that.

Hope to give my Startup Company `Cybit Sec` a follow on its social media profiles: Twitter , LinkedIn , Facebook , Instagram.

Press enter or click to view image in full size

For those who didn’t read my article yet about how I started bug bounty hunting, how I ranked 1st at U.S. Dept Of Defense (2019) and how I reached top 100 hackers on hackerone, You can find it below.

My Bug Bounty Journey & Ranking 1st in U.S. DoD & Achieving top 100 hackers in 1 year
I am sharing some of my methodology, recourses, tips and advices to become a better bug bounty hunter.

ahmdhalabi.medium.com

The article also contains all needed resources to start learning and a lot of valuable tips.

Good Luck :)

Thanks For Reading !
