---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-08_how-i-hacked-100k-godaddy-users-and-help-to-secure-for-free.md
original_filename: 2023-06-08_how-i-hacked-100k-godaddy-users-and-help-to-secure-for-free.md
title: How I Hacked 100K+ Godaddy Users And Help To Secure For Free
category: documents
detected_topics:
- api-security
- access-control
- command-injection
- mobile-security
tags:
- imported
- documents
- api-security
- access-control
- command-injection
- mobile-security
language: en
raw_sha256: dba36064c9682c38c7b6deef4686f8268d3773b091722f1aad94da6f7bc8699e
text_sha256: f9b4a29a4a072e2ad443c84db39443859cd21a5226cb6d837f6b3c05da2a4d84
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# How I Hacked 100K+ Godaddy Users And Help To Secure For Free

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-08_how-i-hacked-100k-godaddy-users-and-help-to-secure-for-free.md
- Source Type: markdown
- Detected Topics: api-security, access-control, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `dba36064c9682c38c7b6deef4686f8268d3773b091722f1aad94da6f7bc8699e`
- Text SHA256: `f9b4a29a4a072e2ad443c84db39443859cd21a5226cb6d837f6b3c05da2a4d84`


## Content

---
title: "How I Hacked 100K+ Godaddy Users And Help To Secure For Free"
page_title: "How I Hacked GoDaddy Users and Helped to Secure | by Bishal Shrestha | PenTester Nepal | Medium"
url: "https://medium.com/pentesternepal/how-i-hacked-100k-godaddy-users-and-help-to-secure-for-free-65f172bd726a"
authors: ["Bishal Shrestha (@bishal0x01)"]
programs: ["GoDaddy"]
bugs: [".git folder disclosure"]
publication_date: "2023-06-08"
added_date: "2023-06-12"
source: "pentester.land/writeups.json"
original_index: 1069
scraped_via: "browseros"
---

# How I Hacked 100K+ Godaddy Users And Help To Secure For Free

How I Hacked GoDaddy Users and Helped to Secure
Bishal Shrestha
Follow
4 min read
·
Jun 7, 2023

204

1

Introduction:

After a while, I made a plan to test one of my favorite programs. After scanning the subdomain, I discovered that it had expired and came across another domain on that page. Judging by the thumbnail, I visited their main domain to see if I could take it over. While browsing, a pop-up from the dotgit extension informed me that the root domain had exposed the .git directory.

Press enter or click to view image in full size
Dotgit extension alert

Intrigued, I tried to dump all the files through the .git directory, and to my surprise, I obtained their internal source code, complete with various API keys and other sensitive data. However, I still had no idea which program I had stumbled upon, so I searched for their contact support email to offer my assistance in securing their application.

Press enter or click to view image in full size

I found the email address support@go.co and attempted to send them a message. Regrettably, I received an auto-generated reply from a Godaddy email address. This made me realize that the domain I had discovered might be owned by Godaddy. To confirm my suspicions, I checked the Godaddy program scope on HackerOne, a platform for reporting vulnerabilities. Not finding any strict scope limitations, I decided to report the issue to Godaddy.

Press enter or click to view image in full size

Hours later, hackerone requested more evidence to confirm that the domain was indeed owned by Godaddy. I once again reached out to support@go.co and this time received a response. After some discussions, hackerone’s triage team agreed to escalate the issue and involve the Godaddy team in the scope and resolution process.

Press enter or click to view image in full size

After few findings I posted on Twitter https://twitter.com/bishal0x01/status/1621752337760153600

Press enter or click to view image in full size
Got this response from Godaddy Program Owner
Overview of the Vulnerability:

Disclosure of secrets for internal assets occurs when sensitive data for the internal assets is not behind an authorization barrier. When this information is exposed it can place sensitive data, such as secrets, at risk. This can occur due to a variety of scenarios such as not encrypting data, secrets committed to GitHub within public repositories, or exposed internal assets.

Disclosure of secrets for this internal asset could be leveraged by an attacker to access the internal application or the environment where the application is hosted.

Business Impact:

Disclosure of secrets for internal assets can lead to indirect financial loss due to an attacker accessing, deleting, or modifying data from within the application. This could happen through an insider threat, existing data breaches, or a malicious internal attacker escalating their privileges. Reputational damage for the business can also occur via the impact to customers’ trust that these events create. The severity of the impact to the business is dependent on the sensitivity of the data being stored in, and transmitted by the application.

Steps to Reproduce:
Setup a HTTP interception proxy, such as Burp Suite or OWASP ZAP
First, I attempted to download a file via the “download.php?value=somevalue” endpoint using my account. However, the downloaded file turned out to be empty.
Then, by looking the downloaded source code via git exposed I navigated to the following URL:

Proof of Concept (PoC):

Get Bishal Shrestha’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://test.somedomain.com/download.php?q=

Successfully demonstrated access to non-public user data.

Additionally, it was possible to modify the email content on the website, such as registration emails, reset password messages, and more.

Press enter or click to view image in full size

Despite achieving the top #1 ranking in Godaddy’s Vulnerability Disclosure Program (VDP) and reporting several critical and high-risk vulnerabilities I did not receive any reward for my findings.

Conclusion:
Best practices for enhancing security include conducting thorough source code reviews to identify and address potential vulnerabilities at the root level.
By proactively examining the source code, developers can gain deep insights into the inner workings of their application and identify potential security weaknesses before they manifest in real-world scenarios.
Additionally, organizations should conduct internal and external vulnerability assessment & penetration testing(VAPT) as well as secure development workshops, and these practices should be implemented within the Software Development Life Cycle itself.

Timeline:

Feb 4, 2023: Report submitted via hackerone

Feb 4, 2023: H1 triage marked as pending program review

Feb 6, 2023: Godaddy team marked report as Triaged.

Feb 7, 2023: Marked as resolved by Godaddy

Feb 8, 2023: I retested and informed them it’s still reproducible.

February 8, 2023: The Godaddy team marked the issue as back to the triage state since it is still reproducible.

Mar 23, 2023: Issue has been fixed.

June 8, 2023: Writeup published.

Updated:

PS: After a request from the GoDaddy security team, a few pieces of information regarding data exposure, as well as some screenshots of the proof of concept (PoC) and its impact, have been modified in the writeup.

That’s a wrap! Thank you for taking the time to read. Happy hacking/hunting! See you in the next write-up. If you want to contact me, you can email me at bishal0x01@wearehackerone.com or find me on Twitter.
