---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-25_from-information-disclosure-to-interesting-privilege-escalation.md
original_filename: 2021-06-25_from-information-disclosure-to-interesting-privilege-escalation.md
title: From Information Disclosure to interesting Privilege Escalation
category: documents
detected_topics:
- access-control
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 7ebfeb578f1770e2d4091a792318b265835c44e3c30b9cc2f5385d233158ad5e
text_sha256: 3899989d15af8d7cf52933ac80a1545beb9fbf7a6ebb94a401cda1029242804b
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# From Information Disclosure to interesting Privilege Escalation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-25_from-information-disclosure-to-interesting-privilege-escalation.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `7ebfeb578f1770e2d4091a792318b265835c44e3c30b9cc2f5385d233158ad5e`
- Text SHA256: `3899989d15af8d7cf52933ac80a1545beb9fbf7a6ebb94a401cda1029242804b`


## Content

---
title: "From Information Disclosure to interesting Privilege Escalation"
url: "https://dudy2kk.medium.com/from-information-disclosure-to-interesting-privilege-escalation-61ed3aaaf218"
authors: ["David Shaul (@dudy2kk)"]
bugs: ["Information disclosure", "Account takeover", "Privilege escalation"]
publication_date: "2021-06-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3545
scraped_via: "browseros"
---

# From Information Disclosure to interesting Privilege Escalation

From Information Disclosure to interesting Privilege Escalation
David Shaul
Follow
4 min read
·
Jun 24, 2021

139

The bug bounty program on which this vulnerability was discovered has not allowed for public disclosure. Therefore I will name the program REDACTED.com.

Summary:

In this web application (subdomain.REDACTED.com), users can create a money program for their own company.

I was able to find a cool information disclosure which leads me to be an admin of the application eventually.

Description:

After I logged into the application as a simple user, there were not many features that I could play with.

However, the one that got my attention was the “Edit Account” feature.

I Turned on my Burp Suite and caught the request after editing some fields in my profile, I saw the request was sent to the following endpoint: /ProgramManagerREDACTED/REDACTED/updateuser

The request method was “PUT” with many parameters, but what caught my eyes was “role_id” and “user_info_id”:

Press enter or click to view image in full size

So the first thing I have done was to change the “role_id” parameter value from 1 to 2. However, the server response was “401 Unauthorized” :(

(Lets did not forget we still have the second parameter to play with, but let’s keep that one for later)

After a while of playing with the endpoint (“/ProgramManagerREDACTED/REDACTED/updateuser”), I removed the body request and the two last directories and changed the “PUT” request into “GET”. The response from the server was “200 OK”, and the response body was massive information about hidden endpoints:

Press enter or click to view image in full size

The response body was pretty huge, so I decided to search for several keywords, such as admin, passwords, user, and more.

The “user” keyword led to an interesting endpoint: “/ProgramManagerREDACTED/userInfoDetailsEntities”.

Get David Shaul’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Hitting that endpoint with a “GET” request got me amazed. The server response body contained huge leaks about every user on the web application (here I also understand that there are four role ids):

Press enter or click to view image in full size

With this information leakage, I thought about submitting the vulnerability to BugCrowd, but something inside of me told me that there is more, so… I KEPT DIGGING AND TRIED HARDER :)

So I sent another request to that endpoint, but now I was using my “user_info_id” value for searching only for my user information (“/ProgramManagerREDACTED/userInfoDetailsEntities/{user_info_id}”).

I was able to see my user information in the server response — including “role_id” and “mail” (another thing that is important to say, mail was not introduced as cleartext, mail was some hash):

Press enter or click to view image in full size

I decided to take the first request (“Edit Account”) with the same original request body, but changing the endpoint to the one I just found (“/ProgramManagerREDACTED/userInfoDetailsEntities/{user_info_id}”), so I sent a “PUT” request, with changing the “role_id” parameter value to “4” and the “mail” parameter value to hash mail.

My “Burp Suite” was not responding, so I thought to myself, there is nothing more that I can do. BUT, 5 seconds later, I got the response from the server with the status code of “200 OK”, and I realized that the role_id had been changed successfully; I WAS SHOCKED!

Press enter or click to view image in full size
role_id has changed successfully to 4 (admin)

I logged out from the application and then logged in, and I was the admin!!

I had access to the admin control panel with features such as:

deleting users, see other users’ money applications, sensitive information, etc.

10 minutes after submitted the bug to BugCrowd, it was triaged as a critical vulnerability and resolved within 1 day.

Conclusion:

Even if you have found an information leak vulnerability, try to find a more serious vulnerability with its help.

Thanks for reviewing my first Medium post, have a happy hunting!

If you enjoyed reading the article, do clap and follow:

Twitter: https://www.twitter.com/dudy2kk
