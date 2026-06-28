---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-05_taking-over-files-in-a-chat-idor-in-microsoft-teams.md
original_filename: 2020-07-05_taking-over-files-in-a-chat-idor-in-microsoft-teams.md
title: Taking Over Files in a chat —IDOR in Microsoft Teams
category: documents
detected_topics:
- idor
- command-injection
- file-upload
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- idor
- command-injection
- file-upload
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: 73564199cf978555ef23d331de3c8fbf1f675ac73327851bd75670fe812d79b4
text_sha256: fca61a6d2ab17425ca54a37bf6fca3855aa38bde2a90c2d76572c3143bf00ed4
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Taking Over Files in a chat —IDOR in Microsoft Teams

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-05_taking-over-files-in-a-chat-idor-in-microsoft-teams.md
- Source Type: markdown
- Detected Topics: idor, command-injection, file-upload, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `73564199cf978555ef23d331de3c8fbf1f675ac73327851bd75670fe812d79b4`
- Text SHA256: `fca61a6d2ab17425ca54a37bf6fca3855aa38bde2a90c2d76572c3143bf00ed4`


## Content

---
title: "Taking Over Files in a chat —IDOR in Microsoft Teams"
url: "https://medium.com/@alyanwar/taking-over-files-in-a-chat-idor-in-microsoft-teams-e5289c2efd0"
authors: ["Aly Anwar (@alyanwarr)"]
programs: ["Microsoft"]
bugs: ["IDOR"]
publication_date: "2020-07-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4437
scraped_via: "browseros"
---

# Taking Over Files in a chat —IDOR in Microsoft Teams

Taking Over Files in a chat —IDOR in Microsoft Teams
Aly Anwar
Follow
5 min read
·
Jul 5, 2020

100

Out of curiosity, I started looking into the file uploading process in the browser version of Microsoft Teams. Found a couple of IDORs in a single endpoint and some leaks in another. Combining both, I found that it is possible for a user to delete what other users upload, give arbitrary ownership, and even change the content of any file being uploaded, ie. full takeover.

Let me walk you through the attack scenarios..

Background:

When you upload a file to a Microsoft Teams chat, a couple of requests will be issued. For our attack scenarios, we will be focusing on 2 main endpoints:

Endpoint A, responsible for PUTing the data related to the uploaded file:
PUT https://emea.ng.msg.teams.microsoft.com/v1/users/ME/conversations/<thread_id>/messages
Press enter or click to view image in full size

This endpoint request contains some interesting params such as:

imidisplayname -> the sender name
itemid -> the referenced ID for the uploaded image/file
fileUrl -> the content of the file (a sharepoint link)
content -> the message linked to the uploaded file

2. Endpoint B, responsible for retriving info related to the available files in a chat:

POST https://eu-prod.asyncgw.teams.microsoft.com/msgsearch/v1/query
Press enter or click to view image in full size

This endpoint response contains some interesting params such as:

ThreadId -> the referenced ID for the messaging thread
itemid -> the referenced ID for the uploaded image/file
Attack Narrative:
Targeting “imidisplayname” — Change file ownership (self):

Status: Unpatched — this still works as of the day of this writing.

From Endpoint A, lets focus on “imidisplayname” param:

Press enter or click to view image in full size

This value is being reflected in the files details in the chat:

Press enter or click to view image in full size

Changing this value to anything will be successful:

Press enter or click to view image in full size

To confirm that the value is also changed for the referenced object, if we check Endpoint B we can see that it has been changed successfully:

Press enter or click to view image in full size

2. Targeting “imidisplayname” — Change file ownership (others’ files):

Status: patched.

Checking other uses’ uploaded files for a different chat in the web application, we can see only 1 file uploaded by user “Greg xxx”:

Press enter or click to view image in full size

Via Endpoint B, we can retrieve the “itemid” for this file:

Press enter or click to view image in full size

From Endpoint A, we craft a similar request but with the grabbed values for “id” and “itemid”. Those two params are the ones responsible for referencing the uploaded file as mentioned earlier.

Press enter or click to view image in full size

We can confirm that the change took place, moreover, the file itself has been overridden— no other files appear on the list except our file:

Press enter or click to view image in full size

3. Targeting “itemid” and “fileUrl”— Takeover files (same chat):

Get Aly Anwar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Status: patched.

As shown in the previous scenario, we already caused this accidently when attempting to change the file owner (diplay name).

To clarify more, notice the “fileurl” variable which basically fetches the file content whenever the image is being loaded:

Press enter or click to view image in full size

Submitting the PUT request of Endpoint A with a new “fileUrl” value and the “itemid” of the other users’s uploaded file will make the application override this file with the new data. At this point file deletion, as well as changing file content is possible:

Press enter or click to view image in full size

4. Targeting “itemid”, “fileUrl”, “ThreadId” — Takeover files (different chat):

Status: patched.

From Endpoint B, we can see that among the details of the uploaded file we have a “ThreadID” value:

Press enter or click to view image in full size

Via Endpoint A, if we change the “<thread_id>” to this value, we can do all the previously mentioned scenarios for other chats as well.

PUT https://emea.ng.msg.teams.microsoft.com/v1/users/ME/conversations/<thread_id>/messages
Risks:

A user can delete what other users upload, give arbitrary ownership, and even change the content of any file being uploaded, ie. full takeover.

Reporting Timeline:

28 April 2020 — Reported

29 April 2020 — Rejected because its considered a “social engineering” or “man in the middle” attack:

Press enter or click to view image in full size

29 April 2020 — Re-reported with tackling the mentioned points:

Press enter or click to view image in full size

One month later I didn’t receive anything, so I asked for an update.

20 May 2020 — Update:

Press enter or click to view image in full size

2 June 2020 — Rejected because “it does not meet the bar for servicing”,
worth noting that I had 0 views on my 2 PoC videos after being asked to re-upload them.

Press enter or click to view image in full size

16 June 2020 — Clarification for the rejection of the report:

Press enter or click to view image in full size

TL;DR Altering the value of “message.properties.file” property for another user is not considered a security risk.

29 June 2020 — Public disclosure permission granted.
