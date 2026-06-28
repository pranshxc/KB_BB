---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-25_support-supports-a-hacker.md
original_filename: 2022-10-25_support-supports-a-hacker.md
title: Support supports a Hacker
category: documents
detected_topics:
- sso
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- sso
- access-control
- command-injection
- api-security
language: en
raw_sha256: 4192d20fb6914c0065124596836e6ff8b3bcb3881ddd3dee37820de658c3b9af
text_sha256: 0632e5d2a14705a41b9b0bc420e8d5e8e45eb30489849ef92f06cc1bd6252828
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Support supports a Hacker

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-25_support-supports-a-hacker.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `4192d20fb6914c0065124596836e6ff8b3bcb3881ddd3dee37820de658c3b9af`
- Text SHA256: `0632e5d2a14705a41b9b0bc420e8d5e8e45eb30489849ef92f06cc1bd6252828`


## Content

---
title: "Support supports a Hacker"
url: "https://mechboy.medium.com/support-supports-a-hacker-be9931104923"
authors: ["mechboy (@mechboy_)"]
bugs: ["Social engineering", "Spoofing", "Broken authorization", "Account takeover"]
publication_date: "2022-10-25"
added_date: "2022-10-28"
source: "pentester.land/writeups.json"
original_index: 1994
scraped_via: "browseros"
---

# Support supports a Hacker

Support supports a Hacker
mechboy
Follow
4 min read
·
Oct 25, 2022

35

Manipulating user accounts via Helpdesk

Press enter or click to view image in full size
I need help

Muhe here, hope you are all doing well. Before getting into this write-up I wanna thank Inti for this Ticket Trick. What an amazing finding, whenever I read this my question will be how can he think like this?? It really inspired me and ended up here:)

Attack Surface:

While doing recon I have a habit of reading the support articles or documentation of that website. Once doing this on a website I found below

Press enter or click to view image in full size
To delete our account

In order to delete our account we have to send an account deletion request to their support. After that our request will be reviewed by their support team and they will delete our account. Many organizations were following this method for account deletion mainly E-commerce and Financial websites.

Now we are going to exploit this functionality. We all know hacking a human is easier than breaking into a computer😜 So here we are going to hack the humans, not software…

Mail
Forms
Chatbox
Phone call

Above methods were used to contact the support. Let’s exploit them one by one

— — — — — — — — — — — — — — — — — — —

MAIL:
Press enter or click to view image in full size
Send account deletion request to their support mail

From above we can see, to delete our account we have to send a request to their support mail. While exploiting this I encountered two attack scenario

With verification
Without verification
With Verification:

For example, I sent a deletion request to support@redacted.com as below

Hi,
I would like to delete my account from H1.
Email: attacker@gmail.com

In this mail, I have asked to delete the account of attacker@gmail.com. So when the Support team saw this they will check whether the mail came from (Sender) attacker@gmail.com. If yes, they will delete the user account attached attacker@gmail.com.

The support is checking whether the sender and requested emails are same for verification.

Get mechboy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After seeing this I just went to the emkei.cz and sent spoofed mail to support@redacted.com on behalf of attacker@gmail.com.

Press enter or click to view image in full size
Spoofed Mail

Boom💥💥 I received ‘’Ticket Confirmation” auto-reply mail at attacker@gmail.com.

Their Helpdesk failed to check the SPF records of incoming Emails because of this our spoofed mail was created as a ticket and after seeing that ticket support team will delete the account belongs to attacker@gmail.com.

Press enter or click to view image in full size
Without Verification:

In the above at least there was one security check but nothing here.

Press enter or click to view image in full size
Deleting without verification

You can see I’m sending the deletion request from totmu***@gmail.com to delete the account of muhe.victim@gmail.com and I got the reply of my account was deactivated (deleted in 2 days)

In this, I was able to delete any user’s account…..

Unauthenticated Forms:

Some websites use forms to contact the support. On unauthenticated forms without any restrictions, we can submit those forms on behalf of other users, and in the backend, the Helpdesk will assign this as a ticket to a original user.

Press enter or click to view image in full size
Form

While checking those tickets the support team should verify whether the request came from a respective user or not. But the support teams were failed to verify this in many organizations. Because of this attackers can perform malicious activities on user accounts. Like this, I was able to delete user accounts in Glassdoor site.

Many sites are vulnerable to this attack……

Chat-Box:

Here we can directly interact with Support staff. I really love this, do you know why?? see this👇

Deactivating a user account
Reactivating a user account
Account TakeOver
Press enter or click to view image in full size

Even I can’t believe it ended in ATO.

The support team failed to verify the user, this is the root cause of it. “When an activity is associated with user data the process should undergo an authentication check” this is what I can say because every organization has different internal disciplines so based on its infrastructure you have to handle this.

Look here I only tried account deletion and takeover(tested less than 5 Orgs). There is N number of things that can be done via support.

Sorry:

I was thinking about this for the last 1 year to write this blog but I was too lazy to write. Anyhow, I completed this today hope you enjoyed it:)

Note: Social Engineering is out-of-scope in many programs

Follow me on Twitter , Instagram
