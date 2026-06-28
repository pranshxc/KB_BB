---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-21_abusing-autoresponders-and-email-bounces.md
original_filename: 2019-02-21_abusing-autoresponders-and-email-bounces.md
title: Abusing autoresponders and email bounces
category: documents
detected_topics:
- sso
- xss
- command-injection
- file-upload
- otp
- automation-abuse
tags:
- imported
- documents
- sso
- xss
- command-injection
- file-upload
- otp
- automation-abuse
language: en
raw_sha256: 9dd8caadbca5886739265a3d8a892a6f6c986f4f4c5d2e7c29805fbbd9b354ec
text_sha256: 98b2db8a86131fb0afe44893829a7a26168a53601a4a544bc9a8d0e1f3496b9a
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing autoresponders and email bounces

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-21_abusing-autoresponders-and-email-bounces.md
- Source Type: markdown
- Detected Topics: sso, xss, command-injection, file-upload, otp, automation-abuse
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `9dd8caadbca5886739265a3d8a892a6f6c986f4f4c5d2e7c29805fbbd9b354ec`
- Text SHA256: `98b2db8a86131fb0afe44893829a7a26168a53601a4a544bc9a8d0e1f3496b9a`


## Content

---
title: "Abusing autoresponders and email bounces"
url: "https://medium.com/intigriti/abusing-autoresponders-and-email-bounces-9b1995eb53c2"
authors: ["Inti De Ceukelaire (@securinti)"]
programs: ["Google", "Intigriti"]
bugs: ["Information disclosure", "Logic flaw"]
publication_date: "2019-02-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5396
scraped_via: "browseros"
---

# Abusing autoresponders and email bounces

Abusing autoresponders and email bounces
Inti De Ceukelaire
Follow
6 min read
·
Feb 21, 2019

985

5

Press enter or click to view image in full size

Being a bug bounty hunter, I face a lot of competition. Lots of companies are willing to issue rewards for vulnerabilities in their systems, but only if they haven’t been reported by someone else. If you want to beat the odds of finding duplicates, you better look for bugs in places others don’t.

Rather than focussing on a bounty target, I try to find vulnerabilities in widely used functionalities or integrations. After finding such a flaw in support portals I called ‘Ticket Trick’, I found that e-mail systems can be an interesting point of intrusion for attackers. Service e-mails often include sensitive information and tokens, yet work separately from the main application and its security models.

As their name suggests, autoresponders automatically return information to incoming e-mails. This can be an out of office message, an e-mail bounce or a service message. As it turns out, some of them include sensitive information attackers can abuse to bypass authentication models.

I learned you could use RCPT and VRFY SMPT commands to map out which e-mail aliases my targets use, to avoid spamming them with my test e-mails:

Press enter or click to view image in full size
Use RCPT or VRFY to check whether an e-mail address exists

Aliases I often encountered included:

Support inboxes: support@, helpdesk@, customerservice@, help@, …
These inboxes are sometimes vulnerable to the “Ticket Trick” I mentioned earlier.
Billing systems: billing@, finance@, …
Some billing systems would automatically upload or parse incoming e-mail attachments, effectively leading to blind XSS or in the worst case scenario RCE by arbitrary file upload.
Services: printer@, printing@, uploads@, ftp@, test@, …
In some cases, these e-mail addresses would lead to unauthorised actions. Combined with e-mail spoofing, the printing@ e-mail address sometimes allow remote attackers to add documents to someone else’s printer queue.
Ticket trackers: tickets@, jira@, helpdesk@, bugs@, issues@…
Quite a few companies allow internal ticket creation over e-mail for convenience, but do not restrict ticket creation to members of their own company. Some internal issue tracker autoresponders are configured to create an account for every unknown user that submits an issue, others include a signup link as in the example shown below. Both will result in remote attackers gaining access to parts of your internal ticket system, depending on its permission settings.
Press enter or click to view image in full size
Insecurely configured autoresponders are happy to provide accounts for internal issue trackers for anyone

Another type of an automated response are e-mail bounces that occur whenever an e-mail cannot be delivered for some reason. Since e-mail bounces only include the original e-mail sent by the attacker and some metadata, they don’t seem to be directly exploitable — unless this information is unknown to the attacker and contains confidential information, as is the case with the following examples:

Leaking Google Drive metadata

While doing reconnaissance, I often stumble upon protected Google Drive documents. I always click the ‘Request access’ button, often with a very slim success ratio:

Press enter or click to view image in full size

What struck me was the way this request was sent: behind the scenes, Google would send a request for access e-mail originating from my e-mail address. This e-mail would look like this:

Press enter or click to view image in full size
This e-mail originates from the attacker’s email, yet includes confidential information

Since the FROM header and the Return-Path are set to the attacker’s e-mail, the confidential information would return in case of a bounce, we just need to find a way to make the request for access e-mail bounce back to me. One of the ways an attacker could achieve this is by e-mail bombing a target, eventually reaching the victim’s inbox capacity limit.

Get Inti De Ceukelaire’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Once the victim’s inbox is full, the access request e-mail bounce back to the attacker, disclosing the owner e-mail address and the document title:

Press enter or click to view image in full size
If a document owner’s inbox was full, Google used to bounce back their e-mail address and the document title

Google resolved this issue and awarded a bounty as part of their vulnerability reporting program.

Unmasking e-mail aliases

As seen in the previous example, e-mail bounces include the e-mail address of the recipient. This comes in handy to determine the destination e-mail address hidden by an e-mail forwarder alias. If webmaster@example.com redirects e-mails to john.doe@gmail.com, bounces to the webmaster e-mail would actually disclose john.doe’s e-mail address:

attacker@acme.com → webmaster@example.com → john.doe@gmail.com

In a normal situation, the attacker would not be able to disclose the final e-mail address, but if the attacker can force a bounce, john.doe@gmail.com will bounce the e-mail straight to attacker@acme.com, disclosing the destination e-mail address.

One way to force a bounce on john.doe’s side is by configuring a strict DMARC policy for the attacker-controlled acme.com, which makes sure other services can’t easily spoof or forward it. Attackers could send an unauthenticated e-mail to the forwarder: webmaster@example.com, which would then forward the e-mail to the gmail address. Upon arrival, Google’s servers would bounce it back, as it does not comply with the sender’s DMARC policy. The bounce would include the original e-mail address.

Real-life scenario: bug bounty platforms

Like many other bug bounty platforms, intigriti uses hacker e-mail aliases. Ethical hackers are given a <username>@intigriti.me e-mail address upon registration they can use to sign up for the programs they test. Using the method described above, it used to be possible to obtain the e-mail address linked to an username.

An unauthenticated e-mail from attacker@acme.com to intidc@intigriti.me would result in the following bounce, in case acme.com has a strict DMARC policy:

Press enter or click to view image in full size
The bounce revealed the true e-mail address behind intidc@intigriti.me

As you can see, my personal e-mail address, inti.de.ceukelaire@gmail.com would be included in the e-mail bounce.

The intigriti developers have patched the vulnerability by no longer using the original e-mail address as the bounce address. I tested other bug bounty platforms as well, so no need to spam them with test e-mails.

Closing thoughts

As a bug bounty hunter, it can be worth the time to try and find very specific attack scenarios and then go look for targets that fit this configuration afterwards. This often results in unique and creative bugs, and reduces the risks of a duplicate. When testing for e-mail related vulnerabilities, do check the program’s scope and make sure you don’t spam around — companies will not appreciate that. When in doubt, ask.

As a company, it can be interesting to look into the e-mail enabled services and internal ticket trackers associated with your domain. Don’t just check if the originating e-mail address matches your company domain, as e-mails are easily spoofed and your autoresponders can be used against you. In other words, treat your e-mail flows with the same security care you treat your main product — because very often, they process the same sensitive data.
