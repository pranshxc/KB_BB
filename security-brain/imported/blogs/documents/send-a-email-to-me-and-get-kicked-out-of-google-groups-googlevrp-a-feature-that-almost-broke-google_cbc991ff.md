---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-20_send-a-email-to-me-and-get-kicked-out-of-google-groups-googlevrp-a-feature-that-.md
original_filename: 2022-02-20_send-a-email-to-me-and-get-kicked-out-of-google-groups-googlevrp-a-feature-that-.md
title: 'Send a Email to me and get kicked out of Google Groups !! — #GoogleVRP — A
  Feature that almost broke Google Groups !!'
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
- api-security
language: en
raw_sha256: cbc991ff8d3b5f63373692de4c5acbdaaf66497904e6be73da23185a51aa8104
text_sha256: 5eff6489598abae1d01a69bf604b788019da49cb1561f96a3ae143449cec6fbc
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Send a Email to me and get kicked out of Google Groups !! — #GoogleVRP — A Feature that almost broke Google Groups !!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-20_send-a-email-to-me-and-get-kicked-out-of-google-groups-googlevrp-a-feature-that-.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `cbc991ff8d3b5f63373692de4c5acbdaaf66497904e6be73da23185a51aa8104`
- Text SHA256: `5eff6489598abae1d01a69bf604b788019da49cb1561f96a3ae143449cec6fbc`


## Content

---
title: "Send a Email to me and get kicked out of Google Groups !! — #GoogleVRP — A Feature that almost broke Google Groups !!"
url: "https://infosecwriteups.com/send-a-email-to-me-and-get-kicked-out-of-google-groups-29b5c2c60e95"
authors: ["Sriram Kesavan (@sriramoffcl)"]
programs: ["Google"]
bugs: ["Logic flaw", "Broken authorization"]
bounty: "3,133.7"
publication_date: "2022-02-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2883
scraped_via: "browseros"
---

# Send a Email to me and get kicked out of Google Groups !! — #GoogleVRP — A Feature that almost broke Google Groups !!

Send a Email to me and get kicked out of Google Groups !! — #GoogleVRP — A Feature that almost broke Google Groups !!
Sriram Kesavan
Follow
5 min read
·
Feb 20, 2022

302

1

Press enter or click to view image in full size

Reported: Jun 26, 2021 12:51PM

A lot of people might know what Google Groups is. For people who doesn’t, Google Groups allows users to create a group with multiple users in them and a common mail ID would be provided. That can be used to interact with the members in the group by simply sending a email.

For example:

You create a group named “Apple fans” and a Mail ID “apple_fans@googlegroups.com” will be provided. And members in the group can simply send a email and the message will be posted in the group !!

Organizations use Google Groups even as a Ticket tracking system, and a modified version is been used by Google as Payment Support System as per my knowledge and some information I gathered.

I never really wanted to test on Google Groups but revised UI made me to hunt there. And tbh it was cool.

So I created a group named “Test Groups” added some of my test accounts and followed by that I was provided with a common email ID “test_groups_one@googlegroups.com”

When I started sending out messages to the Google Groups one feature got my attention which was “+unsubscribe@googlegroups.com” in the email. This feature is available in Google Groups for so many years. But i never saw a single person test on this, so i decided to test it myself this time !!

Press enter or click to view image in full size

When a user in my “Test Group One” isn’t interested to continue in a group he/she can simply send a email to “test_groups_one+unsubscribe@googlegroups.com”

So let’s assume I added my friend “friend1@example.com” and he isn’t interested in continuing in the group, he can send a mail to “test_groups_one+unsubscribe@googlegroups.com” and he will be removed from the group automatically. Here’s a video how it actually works.

Lot of you people might think of Email Spoofing is the issue, but it wasn’t !!

I initially spent more time (probably more than week even more) how the users were removed from the groups and SPF policy actually worked in this case. So, in-order to remove the user, we need to trick the victim to directly reply to the “+unsubscribe@googlegroups.com” so i tried “reply-to” function which is common in most mailing services.

So when we send out a email, the user’s reply will be sent to the unsubscribe email. And the user will be removed from the group. Refer below image for a spoofed mail which reply-to

Press enter or click to view image in full size

But there was a disadvantage, the victim can visibly see which email he/she is replying. Even if I report this , there’s no way guys from Google guys will accept this. So i had to rethink even more in-order to find better attack scenario.

Press enter or click to view image in full size

So what I planned was to mask the unsubscribe email. Right now there are so many proxy services but it was too costly and i opted for a even more cheaper version.

The trick is here by Auto-Forwarding Emails (Google Support). Here’s a simple image for better understanding:

Press enter or click to view image in full size

So, when the Victim sends an random email to our ID ‘random-user@gmail.com’ and all the incoming emails will be automatically forwarded to ‘test_groups_one+unsubscribe@googlegroups.com’ and the Victim will be removed from the Google groups automatically and the system actually fails to verify it.

Press enter or click to view image in full size
Simplified version of the attack scenario.

A Simple image for better understanding !! I tried this attack scenario where i created a group for my organization, added my friends with their consent and sent them a email. They replied to my email and BOOM, they got removed from the group one by one. LOL

Get Sriram Kesavan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And here’s a Final Video POC how it is achieved.

But, when I decided to send this issue to Google VRP the response didn’t make me happy :(

Press enter or click to view image in full size

Yes, the report was closed as ‘Intended Behavior’ with above explanation. Seriously, Google Security bois, i started crying literally :(

But I wasn’t giving up. The next thing I did was get a permission from Google bois to publish a write-up regarding this. So i quickly made a write-up and sent back to get approval. And after a week back, i got this back: The Product team was favorable in addressing this issue.

Hoooray !!!

And yes, this was the same I was expecting and it happened. It was exactly two weeks that crossed and it was time for the reward now.

Press enter or click to view image in full size

And yes it was rewarded $3133.7 it was higher than I expected coz i estimated this issue to be $500 or $1337 and it was higher than I expected. And this is the one more reason to love Google and Google VRP.

A initial patch has been applied to and i’ve also reported a patch bypass which is accepted and waiting for a Google VRP Panel review.

So see y’all in a new write-up soon guys !!

Thanks for reading !!

Twitter: sriramoffcl

Instagram: sriram_offcl

LinkedIn: sriramkesavan

Well if you love this write up drop a clap 👏, let’s connect then:

Peace ✌️ !!!

Thanks for proof-reading: Sandiyo Christan

🔈 🔈 Infosec Writeups is organizing its first-ever virtual conference and networking event. If you’re into Infosec, this is the coolest place to be, with 16 incredible speakers and 10+ hours of power-packed discussion sessions. Check more details and register here.
IWCon2022 - Infosec WriteUps Virtual Conference
Network With World's Best Infosec Professionals. Find How Cybersecurity Pros Achieved Success. Add New Skills to Your…

iwcon.live
