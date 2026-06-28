---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-08_abusing-auto-mail-responders-to-access-internal-workplaces.md
original_filename: 2024-06-08_abusing-auto-mail-responders-to-access-internal-workplaces.md
title: Abusing auto mail responders to access internal workplaces
category: documents
detected_topics:
- sso
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- sso
- command-injection
- business-logic
- api-security
language: en
raw_sha256: e7e3a020c299301ce443fe565b7db870b7958135823462f9f7cb867373196f2d
text_sha256: df2e59443ac01e742d4fc5d4b70d7fc899ea99e6ec82cd9cfa791af71e550491
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing auto mail responders to access internal workplaces

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-08_abusing-auto-mail-responders-to-access-internal-workplaces.md
- Source Type: markdown
- Detected Topics: sso, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `e7e3a020c299301ce443fe565b7db870b7958135823462f9f7cb867373196f2d`
- Text SHA256: `df2e59443ac01e742d4fc5d4b70d7fc899ea99e6ec82cd9cfa791af71e550491`


## Content

---
title: "Abusing auto mail responders to access internal workplaces"
url: "https://rikeshbaniya.medium.com/abusing-auto-mail-responders-to-access-internal-workplaces-04fcc8ba2c99"
authors: ["Rikesh Baniya (@rikeshbaniya)"]
bugs: ["Logic flaw"]
bounty: "1,000"
publication_date: "2024-06-08"
added_date: "2024-08-22"
source: "pentester.land/writeups.json"
original_index: 258
scraped_via: "browseros"
---

# Abusing auto mail responders to access internal workplaces

Abusing auto mail responders to access internal workplaces
Rikesh Baniya
Follow
4 min read
·
Jun 8, 2024

519

4

When ever you send an email to a company address support@example.com , contact@example.com you might have noticed you will be greeted with an auto reply.

Press enter or click to view image in full size

Now do you see something interesting with the auto reply.

The email consists of 2 parts:

The automatic message from mail server.
The original message that was sent by client.
Press enter or click to view image in full size

The email content is being sent back to the sender himself, so there is not much of a damage we can do.

or can we?

The reply-to feature.

Almost all mail services provide us with an option to specify a reply-to address.

If we send an email from rikesh@gmail.com with reply-to set as rksh@gmail.com , the email’s reply will be forwarded to rksh@gmail.com instead of rikesh@gmail.com

The invite feature.

Many SAAS organizations allow the admin to invite users to their organization.

One such website is Figma.

Figma is one the popular SAAS being used by many companies.

During my testing what i observed was:

If I,rikesh.baniya@gmail.comsend invite to an user rikesh@gmail.com

The invite link would be sent in the following manner.

from: no-reply@email.figma.com [Figma ]

to: rikesh@gmail.com [ Invitee]

reply-to: rikesh.baniya@gmail.com [ Inviter]

Wow, we are able to set the attacker controlled email address as a reply-to ?

Chaining everything

The invite link sent by figma was also a signup link to join the organization.

Now assume that redacted@hackerone.com is an autoresponder address.

Get Rikesh Baniya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It will auto reply to all the emails it receives.

The auto-reply consists of 2 parts:
-”thank you for your message”
-”original email that is received”

So now i f I , rikesh@gmail.com invited redacted@hackerone.com to my figma team

Figma would first email the signup link to redacted@hackerone.com .

redacted@hackerone.com would then auto respond to that email saying

“We have received your request”
Plus append
“The original email that it received containing the invite link”

The issue here was Figma was setting the inviter address as the reply-to address ;rikesh@gmail.com

Thus all the replies were getting forwarded to the inviter himself.

how cool is that.😂

Trying to demonstrate the flow

Image of email received by the inviter

Press enter or click to view image in full size

Exploit and impact

Ton of sites have autoresponders that’ll automatically reply to the email.

support@target.com , help@target.com and so on

This allowed an attacker to claim any @target.com in Figma.

Figma has domain capture feature.

Meaning if you have a verified @target.com account you can auto join the internal workplace in figma.

Press enter or click to view image in full size

Figma does have SSO login option, so SSO login based organizations were secure against this attack.

Exploiting it against Figma themself

Figma uses zendesk to handle their user support tickets.

You can login to zendesk using your own figma account.

To exploit it , I sent an invite to figma@redacted-figma-asset.com , which was an auto responder

Got access to the signup link and created a verified figma account using the figma email address.

Then , logging in to zendesk with that figma account gave me access to internal tickets.

To sum it up , it was a very cool chain of issues.
