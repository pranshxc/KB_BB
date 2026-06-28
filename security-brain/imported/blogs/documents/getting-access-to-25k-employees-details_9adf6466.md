---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-08-11_getting-access-to-25k-employees-details.md
original_filename: 2017-08-11_getting-access-to-25k-employees-details.md
title: Getting access to 25k employees details
category: documents
detected_topics:
- command-injection
- rate-limit
- graphql
- api-security
tags:
- imported
- documents
- command-injection
- rate-limit
- graphql
- api-security
language: en
raw_sha256: 9adf64666ae9f31bae8684940b939dcf36515fdf1ad270a4ee6c24ad185b264c
text_sha256: 951b78f260d9ee0c8f800db43414659a550ad52e1c04871097807648969c9774
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Getting access to 25k employees details

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-08-11_getting-access-to-25k-employees-details.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, graphql, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `9adf64666ae9f31bae8684940b939dcf36515fdf1ad270a4ee6c24ad185b264c`
- Text SHA256: `951b78f260d9ee0c8f800db43414659a550ad52e1c04871097807648969c9774`


## Content

---
title: "Getting access to 25k employees details"
page_title: "Getting access to 25000 employees details | by Sahil Ahamad | Medium"
url: "https://medium.com/securityescape/getting-access-to-25k-employees-details-c085d18b73f0"
authors: ["Sahil Ahamad (@ehsahil)"]
bugs: ["Exposed registration page"]
bounty: "2,500"
publication_date: "2017-08-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6129
scraped_via: "browseros"
---

# Getting access to 25k employees details

Top highlight

Getting access to 25000 employees details
Sahil Ahamad
Follow
3 min read
·
Nov 8, 2017

1.1K

1

Hi guys,

I want to share one of my findings in a private program on HackerOne, which was — critical but straightforward one. During testing for that private program. I found an endpoint for Internal team management.

Press enter or click to view image in full size
Internal Team management endpoint

After opening the endpoint (refer the Image above), the only thing running in my mind was “How about I check the directories.” Thus, I immediately utilized Dirsearch to brute force all the directories.

Here is the exciting output.

Press enter or click to view image in full size
I renamed dirsearch to `dir` because I am lazy :v

Noticed? Anything?

It’s https://37.--.--.--/register :P

Upon opening the URL.

Yuss!!!! Registration page. 😮 anddd….

Press enter or click to view image in full size

I tried to register with my details. And.. there was a configuration error. I was like…

I decided to register one more time with the same email and ended up with an error i.e.

“The email is already registered.”

okay, let’s go and log in.

So, I tried to log in with my registered credentials anddd…..

Successfully Logged in….

Admin management page.

Press enter or click to view image in full size
All administrators name & email address was disclosed, I was even able to delete them.

Typical employee details pages

Disclosed details include Name, Email, Phone-No, Employee ID, Shifts, Reports, Salaries etc.

Press enter or click to view image in full size
Typical Employee details (25k Records)

Sorry, but I needed to hide some details due to confidentiality issues. Some other critical data was disclosing too but don’t have permission to write further.

Get Sahil Ahamad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After verifying the issue, I quickly submitted the detailed report to the program via HackerOne. They validated and fixed the problem within a few hours.

They permanently fixed the issue by removing the public registration page from the endpoint.

After reporting the issue, I applied dirsearch on most of the critical endpoints belongs to them however no more endpoint was vulnerable to the same problem.

Timeline.

Report Submitted: 25–10–2017

Report Triaged: 25–10–2017

Initial 1300$ Awarded: 25–10–2017

Report closed as Resolved: 25–10–2017

Final 1200$ Awarded: 26–10–2017

Update

As many people messaging me and asking how I found this Asset/Internal team management endpoint. I am providing info about it here,

I found this endpoint using Github issues conversations.

My recon process.

Tools

Sublister,knockpy,dnsresolver,dirsearch,bucket finder,massdns etc.

After reporting some low hanging issues, I go out and follow engineering/Security teams on Twitter and Github & look for anything interesting

I go through all the issues/Repositories companies engineering team created publicly on Github.

I read all blog posts by engineering and security team.

I check their DNS every month. Generally, companies stopped using a service and forgot to delete CNAMES pointing to service.

I use their services as the user and continue my recon processes,

I also use Burp Suite pro history tool to find exciting endpoints.

According to me, Recon is not a one time process it’s a continuous process.

If you like my blog posts and my work, Please consider checking out my “Buy me a coffee” page

Buy Me A Coffee - Best Way for Creators to Receive Tips
Buy Me A Coffee help creators receive support from their audience in a friendly manner. Quickly accept donations and…

www.buymeacoffee.com
