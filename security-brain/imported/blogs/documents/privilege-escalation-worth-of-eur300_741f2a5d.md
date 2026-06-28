---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-12_privilege-escalation-worth-of-300.md
original_filename: 2021-11-12_privilege-escalation-worth-of-300.md
title: Privilege Escalation, worth of €300
category: documents
detected_topics:
- access-control
- idor
- command-injection
tags:
- imported
- documents
- access-control
- idor
- command-injection
language: en
raw_sha256: 741f2a5d1915f8448e3c137b39fda4cde0fb4daabc728fa1c13d511d553ec2d2
text_sha256: 8d8256b803d93e35a1019b5a46564cceee5d8c6c345ee3aad469a4be7caf2098
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege Escalation, worth of €300

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-12_privilege-escalation-worth-of-300.md
- Source Type: markdown
- Detected Topics: access-control, idor, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `741f2a5d1915f8448e3c137b39fda4cde0fb4daabc728fa1c13d511d553ec2d2`
- Text SHA256: `8d8256b803d93e35a1019b5a46564cceee5d8c6c345ee3aad469a4be7caf2098`


## Content

---
title: "Privilege Escalation, worth of €300"
url: "https://medium.com/@kashyapherry147/privilege-escalation-worth-of-300-b9a6eac3b0fa"
authors: ["Hemant Kumar"]
bugs: ["Broken Access Control", "IDOR", "Privilege escalation"]
bounty: "300"
publication_date: "2021-11-12"
added_date: "2022-09-16"
source: "pentester.land/writeups.json"
original_index: 3175
scraped_via: "browseros"
---

# Privilege Escalation, worth of €300

Privilege Escalation, worth of €300
HEMANT
Follow
2 min read
·
Mar 12, 2023

200

4

Hi folks, Hemant here. Today i’m going to tell you about one of my finding. Which is Privilege Escalation to demote the owner of the organization. About target type: I was hunting on multiple roles website. Websites has many user roles like: Owner, Managed Owner, Store owner, and integrator.

Press enter or click to view image in full size

Let’s start the story

So, I created an account with owner privileges. And i invited a user with Store owner permission. Store owner doesn’t have access to demote the Owner, but he/she can demote lower privilege users like, Integrator, store manager. Then i logged into the store owner account, and playing with the functionality. So, i invited a user with permission of store read access from store owner account, and then i edited permission to integrator, and i captured this request in burpsuite. Request is like this:

Press enter or click to view image in full size

You can see the request line.

POST /api/v1.0/fd25374/teammates/Base64-encoded-email-address|team-id. So, i decoded this base64 email address. And i found that, this email is belongs to invited user ( Store read access user email). So, i encoded owner email and team-id with base64. And replace with store read access user. And then request look like this:

Get HEMANT’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

POST /api/v1.0/fd25374/teammates/ZmQyNTM3NHx0ZWthdDk4ODc3QGZzb3VkYS5jb20=

Press enter or click to view image in full size

And send the request, and i got 200 OK.It’s mean Owner is demoted succesfully. Also i checked in browser, and is successfully demoted.

I reported this vulnerability, and i rewarded with 300 Euros.

Linkedin: https://www.linkedin.com/in/hemant-k-714564199/

Instagram: https://www.instagram.com/cyber__hawk/
