---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-26_bypassing-the-confirmation-email-for-newsletter-bofnl.md
original_filename: 2018-04-26_bypassing-the-confirmation-email-for-newsletter-bofnl.md
title: Bypassing the Confirmation Email for Newsletter (bof.nl)
category: documents
detected_topics:
- idor
- access-control
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 2ac691687cdf3cafa0904e757743cba0983d942da5fb4931e1ec44555ff9835d
text_sha256: c39eb1138c9bf447d39fcf0ee7a385d6de31f2ea4087bb4cf5a7406b2b55ed48
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: true
---

# Bypassing the Confirmation Email for Newsletter (bof.nl)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-26_bypassing-the-confirmation-email-for-newsletter-bofnl.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: True
- Raw SHA256: `2ac691687cdf3cafa0904e757743cba0983d942da5fb4931e1ec44555ff9835d`
- Text SHA256: `c39eb1138c9bf447d39fcf0ee7a385d6de31f2ea4087bb4cf5a7406b2b55ed48`


## Content

---
title: "Bypassing the Confirmation Email for Newsletter (bof.nl)"
url: "https://medium.com/@mdisrail2468/bypassing-the-confirmation-email-for-newsletter-bof-nl-682c05cb927f"
authors: ["Mohammed Israil (@mdisrail2468)"]
programs: ["Bits of Freedom"]
bugs: ["Broken authorization", "IDOR"]
publication_date: "2018-04-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5897
scraped_via: "browseros"
---

# Bypassing the Confirmation Email for Newsletter (bof.nl)

Bypassing the Confirmation Email for Newsletter (bof.nl)
Mohammed Israil
Follow
3 min read
·
Apr 27, 2018

156

Press enter or click to view image in full size
Voor Jouw Internetvrijheid

I’ve been meaning to write about this for a while. It all started back in September 2017 when I decided to look for vulnerabilities on BoF.

The reason I chose BoF was because a lot of friends (Facebook) of mine posting about the the cool Swag which they got from BoF. And I am just in love with the Swag and eager to test my skills as well.

Summary:

This blog post is all about an issue on Bof on their Newsletter section which is marked as Fixed now. I always believed that sharing is caring, and I have been learning from multiple security researchers in the Bug Bounty field, so I decided to share this.

Description:

A couple of months back during testing and spending a lot of time on https://www.bof.nl/ I didn’t find anything interesting so at last I notice there’s a Newsletter section and as because I found their Blog posts interesting I thought to subscribe for their Newsletter.

So I just enter my email on the email field and hit the subscribe button. And after that I got to know that they have a mechanism in place to confirm the email if you want to recieve the Newsletters. So I login to my email and there’s a email from the info@bof.nl to confirm the same. But the email which I recieved to confirm the subscription seems vulnerable to me and after digging some more about that I was able to confirm anyone’s email and can activate the BoF Newsletter subscription without even their prior knowledge.

Brief Explanation:

Here I have used two dummy emails to demonstrate the vulnerability.

(01) testuser01@protonmail.com
(02) testuser02@protonmail.com

At first I used the first email (testuser01@protonmail.com) for subscription and to confirm the same I got a confirmation email which has 3 parts,
the endpoint, action and data part.

https://www.bof.nl/je-bent-ingeschreven/?mailpoet_router&endpoint=subscription&action=confirm&data=eyJ0b2tlbiI6IjQ4NTQwOSIsIm***REDACTED-SUSPECT-TOKEN***Here the endpoint simply for the method, action for the process and data is the token.

Reproduction Instruction:

(01) Go to official website as https://www.bof.nl
(02) Go to the Newsletter section at the bottom of the page and enter your email. (e.g — testuser01@protonmail.com)
(03) Then you’ll get a confirmation mail to that email address.
(04) Just copy the confirmation link and paste that somewhere where you can able to edit that.

https://www.bof.nl/je-bent-ingeschreven/?mailpoet_router&endpoint=subscription&action=confirm&data=eyJ0b2tlbiI6IjQ4NTQwOSIsIm***REDACTED-SUSPECT-TOKEN***This is for the email address testuser01@protonmail.com, right?

Get Mohammed Israil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

(05) Then just edit the URL as:

https://www.bof.nl/je-bent-ingeschreven/?mailpoet_router&endpoint=subscription&action=confirm&data=testuser02@protonmail.com

Here I have used my second email but you can use any email ID to activate the subscription.

(06) Visit the new edited URL. Boom!!

And there on the page you’ll see a message from the BoF as:

You are registered on one or more of our newsletters or mailing lists. Can not you wait? Then read our latest news .

At the bottom of each newsletter, you can unsubscribe you and all your newsletters at once and manage your listings.

What’s the issue:

The BoF team is using MailPoet newsletter plugin and the issue is with the MailPoet plugin not with the site actually. The MailPoet system is failed to validate the token.

How can it effect:

A attacker can subscribe anyone by simply knowing their email somehow.

At the end, I got a cool T-shirt and some BoF stickers as a token of appreciation from BoF team.

Press enter or click to view image in full size
Token of Appreciation

Thanks for Reading!

~ Mohammed Israil: https://twitter.com/mdisrail2468
