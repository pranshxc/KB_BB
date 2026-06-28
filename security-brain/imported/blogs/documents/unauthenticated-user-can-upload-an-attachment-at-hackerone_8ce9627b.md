---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-24_unauthenticated-user-can-upload-an-attachment-at-hackerone.md
original_filename: 2018-12-24_unauthenticated-user-can-upload-an-attachment-at-hackerone.md
title: Unauthenticated user can upload an attachment at HackerOne
category: documents
detected_topics:
- rate-limit
- access-control
- command-injection
tags:
- imported
- documents
- rate-limit
- access-control
- command-injection
language: en
raw_sha256: 8ce9627ba7358eb4c892778282101f6799bf1f768a5f74cb37632247a9cb7145
text_sha256: ed6d85f88e50df6aa7d1e03698982a8d11be9b622328efa459f74d524678630e
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthenticated user can upload an attachment at HackerOne

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-24_unauthenticated-user-can-upload-an-attachment-at-hackerone.md
- Source Type: markdown
- Detected Topics: rate-limit, access-control, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `8ce9627ba7358eb4c892778282101f6799bf1f768a5f74cb37632247a9cb7145`
- Text SHA256: `ed6d85f88e50df6aa7d1e03698982a8d11be9b622328efa459f74d524678630e`


## Content

---
title: "Unauthenticated user can upload an attachment at HackerOne"
url: "https://medium.com/@modam3r5/unauthenticated-user-can-upload-an-attachment-at-hackerone-aff2a0c573b8"
authors: ["Ahamed Morad (@Modam3r5)"]
programs: ["HackerOne"]
bugs: ["Broken authorization"]
publication_date: "2018-12-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5505
scraped_via: "browseros"
---

# Unauthenticated user can upload an attachment at HackerOne

Unauthenticated user can upload an attachment at HackerOne
Modam3r5
Follow
3 min read
·
Dec 25, 2018

57

Hi every one, i few week ago i was apply to find an a bug that lead to upload Unauthenticated file to HackerOne platform, the bug found when i was tested a brute-force attack against some endpoint at HackerOne.

the behavior is related with another step [ function behavior ] to make this possible.

if you try to log-out from your account at HackerOne and you have two tab used HackerOne, all of them will sign-out automatic, this step as i think is to protect the platform from used submit form and you are not login-in for e.g.

what i found here is that you can for e.g stay in the submit form and you are not login-in and upload the attachment as Anonymous since the /attachments will check if you login-in then relate this attachment with your account, or by generate tracer id if you are as Anonymous so this attachment will linked to it.

so what i did to find this behavior is :

tourn-on burpsuite tool and login-in to your HackerOne account.
in burpsuite you will find an a request send to /sessions, send it to intruder.
go and click on create a report for any program/team you want, and stay in submit page.
start a brute-force attack against /sessions endpoint for e.g 100 password, HackerOne have an protection against the brute-force so after 100 request your account will be Locked as a protection .
after the attack finish go back to submit form and upload an attachment, the file will upload, and the tracer id will connect with it.
Press enter or click to view image in full size
the file was uploaded and the account is in Locked mode

and the /draft_sync , /preview will return with 401 Unauthorized error since the account is login-out [locked], but the /attachments will let you upload the files.

Get Modam3r5’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

what actually happen here is :

account got brute-force.
the rate limiting protection will locked the account as a safety step.
the account will locked silently, and there are no notification/auto login-out if he/she already login-in, and the only way to know that is by click on link/path in site, then the message will show message that the account is locked .
if the user stay in the same page he will not know that his account are locked, and he/she can used some function as upload file in submit form foe e.g .
the attachment will be uploaded/stored as Anonymous and will linked to the tracer id that will generate since there are no user information to linked to it.
Impact

Unauthenticated user can upload an attachment without need to login-in or used the Embedded Submission Form even if is closed/opened.

after send this report to 
HackerOne
 i got this response

Press enter or click to view image in full size
i am the first one how got duplicate with one of 
HackerOne
 engineers :d

it sad when your report change to duplicate if anther hacker/research/internal team found it before you :( .

Time Line:

Nov 8th 2018: bug found.
Nov 8th 2018: send the report to 
HackerOne
Nov 8th 2018: jobert replay and closed the report as Duplicate.
Nov 8th 2018: ask for disclose the report since it Duplicate.
Nov 14th 2018: jobert response that they can’t disclose the Duplicate report and give me the agree to publish the write-up.
DEC 24th 2018: write-up publish.
