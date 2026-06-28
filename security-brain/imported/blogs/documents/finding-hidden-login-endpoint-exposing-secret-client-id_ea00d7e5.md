---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-07_finding-hidden-login-endpoint-exposing-secret-client-id.md
original_filename: 2021-03-07_finding-hidden-login-endpoint-exposing-secret-client-id.md
title: Finding Hidden Login Endpoint Exposing Secret `Client ID`
category: documents
detected_topics:
- sso
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- sso
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: ea00d7e55729f3dace42d20113fc1e38386da69e558f4ea740f08de6b5d9bc1c
text_sha256: 4cccae1cb012d6ebbc6ce5e213a682a3ccc7a0aebd73889748d55ac5959b18c3
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: true
---

# Finding Hidden Login Endpoint Exposing Secret `Client ID`

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-07_finding-hidden-login-endpoint-exposing-secret-client-id.md
- Source Type: markdown
- Detected Topics: sso, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: True
- Raw SHA256: `ea00d7e55729f3dace42d20113fc1e38386da69e558f4ea740f08de6b5d9bc1c`
- Text SHA256: `4cccae1cb012d6ebbc6ce5e213a682a3ccc7a0aebd73889748d55ac5959b18c3`


## Content

---
title: "Finding Hidden Login Endpoint Exposing Secret `Client ID`"
url: "https://ahmdhalabi.medium.com/finding-hidden-login-endpoint-exposing-secret-client-id-88c3c2a1af45"
authors: ["Ahmad Halabi (@Ahmad_Halabi_)"]
bugs: ["Information disclosure"]
bounty: "700"
publication_date: "2021-03-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3835
scraped_via: "browseros"
---

# Finding Hidden Login Endpoint Exposing Secret `Client ID`

Top highlight

Finding Hidden Login Endpoint Exposing Secret `Client ID`
Ahmad Halabi
Follow
4 min read
·
Mar 7, 2021

843

5

Press enter or click to view image in full size

Hello,

My name is Ahmad Halabi, Founder & CTO at Cybit Sec and part time bug bounty hunter on Hackerone.

Today I am going to share one of my cool findings about an information disclosure bug in a private program on HackerOne.

Turning a Low Severity bug into a High one.

Overview ::

I came across a Subdomain as the following https://accounts.redacted.com/redacted/login but I found that there is no Login Form in the page, And there is an error stating No client id found.

Press enter or click to view image in full size

Then I did some recon steps and I found the Login endpoint with a client id value in the URL as the following https://accounts.redacted.com/redacted/redacted?client_id=hashvalue. Then I found a Low Severity bug in the target URL and I reported it.

Turning The Bug From Low to High Severity ::

Feb 16, 2021: Submitted the Initial Report as stated above.
Feb 18, 2021: HackerOne Team Triaged The Report.
Feb 24, 2021: Internal Team Reviewing the Report and Investigating the Submitted Issue.
Feb 26, 2021: Internal Team Want to Know How I Discovered The Endpoint.

HackerOne Triage Team Commented as below:

The team would like to know how were you able to discover the endpoint:

Our understanding is while accessible, it’s not easily discoverable — so insights into how it was discovered would be helpful.

Press enter or click to view image in full size

Here Where Fun Begins ::

So I submitted my Methodology on How I found the target endpoint. And From that comment I realized that the Client ID is a secret value should not be exposed to public since the Login Form is not for Public Users.

I commented as below::

Get Ahmad Halabi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The whole game is in the recon process.

Discovering Login Endpoint & client_id value :

If you navigate to https://accounts.redacted.com/redacted/login you will get an error message stating No client id found.
From the above error I resulted that there should be a parameter named client_id or clientid.
Simple Google Dorking: site:accounts.redacted.com inurl:client_id.
Found the login endpoint and the client_id value: https://accounts.redacted.com/redacted/redacted/redacted?client_id=***REDACTED-SUSPECT-TOKEN***Press enter or click to view image in full size
Press enter or click to view image in full size

By exposing this client_id value, I chained my old bug reported with this value and then I found multiple tokens that seems secret and are exposed as well and reported them all in the same report.

Feb 26, 2021: HackerOne Team Forwarded the comment to the Internal Team.

Mar 3, 2021: Bounty Awarded ($700).

Lessons Learned ::

If you found an Endpoint hiding the Login form and then you managed to find the hidden Login Form then this is highly possible to be a valid bug. Try identifying additional bug in the discovered Login form and report it.
At first, I didn’t know that the client_id that I discovered is secret until I saw the internal team’s comment. So try to be creative and curious about any word commented by the internal team.
Notice the power of Google Dorks. I found the hidden login page by using a Google Dork to search for the client_id value.

Hope to give my Startup Company `Cybit Sec` a follow on its social media profiles: Twitter , LinkedIn , Facebook , Instagram.

Press enter or click to view image in full size

If you didn’t read my article yet about how I started bug bounty hunting, how I ranked 1st at U.S. Dept Of Defense (2019) and how I reached top 100 hackers on hackerone, You can find it below.

My Bug Bounty Journey & Ranking 1st in U.S. DoD & Achieving top 100 hackers in 1 year
I am sharing some of my methodology, recourses, tips and advices to become a better bug bounty hunter.

ahmdhalabi.medium.com

The article also contains all needed resources to start learning and a lot of valuable tips.

Good Luck :)

Thanks For Reading !
