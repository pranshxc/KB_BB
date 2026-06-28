---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-19_open-redirect-in-email.md
original_filename: 2021-01-19_open-redirect-in-email.md
title: Open-redirect [in email]
category: documents
detected_topics:
- ssrf
- command-injection
tags:
- imported
- documents
- ssrf
- command-injection
language: en
raw_sha256: f10ffdd8307de38ce88c2b368ac64667b91de8f6e7cb3ed6d6183c86895b4b9e
text_sha256: d1fbf87527164fcdb666759daf140a9804a94b81ab5d1d6e5a45e07bae0051fb
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Open-redirect [in email]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-19_open-redirect-in-email.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `f10ffdd8307de38ce88c2b368ac64667b91de8f6e7cb3ed6d6183c86895b4b9e`
- Text SHA256: `d1fbf87527164fcdb666759daf140a9804a94b81ab5d1d6e5a45e07bae0051fb`


## Content

---
title: "Open-redirect [in email]"
page_title: "Open-redirect in Acknowledgement email | by Akhil | System Weakness"
url: "https://inakcf.medium.com/open-redirect-in-email-c658c248eec1"
authors: ["Akhil"]
bugs: ["Open redirect"]
publication_date: "2021-01-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3982
scraped_via: "browseros"
---

# Open-redirect [in email]

Open-redirect in Acknowledgement email
Akhil
Follow
3 min read
·
Jan 19, 2021

116

1

Hi Everyone

This is my first writeup about my unique finding open redirect vulnerability in acknowledgement email.

Open-redirect Vulnerability:

An Open Redirection is when a web application or server uses an unvalidated user-submitted link to redirect the user to a given website or page. Even though it seems like a harmless action to let a user decide to which page he wants to be redirected, such technique if exploited can have a serious impact on the application security, especially when combined with other vulnerabilities and tricks.

About my finding :

I got a private invite in bugcrowd which has limited scope. let’s consider the target as private.com. It has in-scope subdomain form.private.com I thought to check it out.

The subdomain https://form.private.com has different forms like feedback form, send CV/Resume etc., So, I have chosen a feedback form.

After navigating to the form it asks for different details like our email address, query, etc., after filling all the details I thought to look at the request in burpsuite. So I captured that POST request which has the following data shown below

{“submissionUrl”:”https://form.private.com/?k=jsdkjsdkhskdgjgs&d=228735228",”fieldValues”:{“1861396”:”test”:”email@gmail.com”}}

Press enter or click to view image in full size

Did you find anything suspicious in the above request ??

Yes, the submissionUrl parameter .

What will we do basically after seeing a http request in the body ?

Get Akhil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

we will try to check whether it is vulnerable to SSRF.

Here, I replaced the submissionUrl parameter with my burp collaborator link but I didn’t get any DNS or HTTP interaction. But, I got acknowledgement email to the email address I’ve given.

I opened the email, It shows all the details I’ve given while filling the form.

One thing in that email looks suspicious is, there is a hyperlink in the heading Feedback on Home as shown in the below screenshot:

Press enter or click to view image in full size

I clicked on that and it got redirected to my burp collaborator link. Now I went back to the form , filled all the details. This time in submissionUrl parameter instead of burp collab link I’ve given https://google.com and passed the request.

This time I got similar email to my email address. But, this time if I click on the heading it is being redirected to google.com

Link looks as shown below

https://app.private.com/app/xxx/-/log?se=xxxxx&dest=https://google.com&hash=xxxxxxxxxxxxxxxxx

Misconfiguration:

Here what we enter in the submissionUrl parameter is being reflected as a redirect URL in the acknowledgement email.

Thanks a lot for reading.

Bounty 200$

Regards,

Akhil
