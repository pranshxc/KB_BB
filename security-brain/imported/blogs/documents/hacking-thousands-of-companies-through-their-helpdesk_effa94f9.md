---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-17_hacking-thousands-of-companies-through-their-helpdesk.md
original_filename: 2018-07-17_hacking-thousands-of-companies-through-their-helpdesk.md
title: Hacking thousands of companies through their helpdesk
category: documents
detected_topics:
- sso
- command-injection
- business-logic
- api-security
- mobile-security
tags:
- imported
- documents
- sso
- command-injection
- business-logic
- api-security
- mobile-security
language: en
raw_sha256: effa94f9281a7d6a5c225896429068bdd0c6471851d23c14ab476d67c6ab5903
text_sha256: d9818d27953ecf90d058313ab3a141cc8188cf6732576a313e89e25c48fbb59d
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking thousands of companies through their helpdesk

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-17_hacking-thousands-of-companies-through-their-helpdesk.md
- Source Type: markdown
- Detected Topics: sso, command-injection, business-logic, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `effa94f9281a7d6a5c225896429068bdd0c6471851d23c14ab476d67c6ab5903`
- Text SHA256: `d9818d27953ecf90d058313ab3a141cc8188cf6732576a313e89e25c48fbb59d`


## Content

---
title: "Hacking thousands of companies through their helpdesk"
url: "https://medium.com/@khaled.hassan/hacking-thousands-of-companies-through-their-helpdesk-8f180a8595ef"
authors: ["Khaled Hassan"]
bugs: ["Account takeover", "DoS", "Logic flaw"]
publication_date: "2018-07-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5805
scraped_via: "browseros"
---

# Hacking thousands of companies through their helpdesk

Hacking thousands of companies through their helpdesk
Khaled Hassan
Follow
7 min read
·
Jul 17, 2018

1.1K

11

Introduction

I would like to write about my simple and clear security vulnerability that I was able to hack many companies through it, As I found that’s there are thousands of companies are affected by this vulnerability and I couldn’t report every single company about the vulnerability so I would like to publish this writeup to help companies secure their support portal as well. Also, I think this vulnerability maybe be similar to this one Ticket-Trick

Four weeks ago when I was working on a private program and after spending a few hours on this program I didn’t find anything given to the level of security on this site, I assume that I have been invited to this program lately, But what prompted me to keep searching for bugs is the insane payout of this program.

After changing my recon steps, I started to read program policy very well and when reading rules I noticed the next line

Security issues on support. redacted.com are out of scope, but If you can escalate the attack to the main application please report to us away.

Hmmm, I think this worth to give a look and to see how I can attack website user’s through support portal.

After opening the support portal It was a zendesk instance, And as we know that zendesk has a not bad security application but even if it’s not secure, How I can attack the user’s of main website through zendesk? The options were very limited until I saw this support article.

Press enter or click to view image in full size
You can’t delete your account from profile settings

After I clicked on contact us button, the website redirected me to the main login page as to submit a ticket to support domain, you should log in to your original account through SSO.
https://www. redacted.com/login?callback=https://support.redacted.com/hc/en-us&zendesk=zendesk

After you log in to your account you can file a ticket to the support team asking them to delete your account, Then after a few hours of submitting the ticket your account will get deleted.

Deleting or takeover accounts of others:

Then an idea came into my mind about what if I submit tickets behalf on other users to support team asks them to delete the user account. Well, How I can do something like that?

To create a ticket on the support subdomain users need to visit the support subdomain and log in to their account to be able to add new tickets, and this is what is makes support team consider all the tickets are original and created by the website user.

Another option is that Zendesk allows creating tickets by email. Which means the user can send an email to the company support email to a add a new ticket to his activities. So when you send an email to support@website.com / help@website.com from your email address, this ticket will be created on the account that you have registered with the email.

Simply, You send an email to support mail from your (khaled@gmail.com) email then the content of your email will be created as a ticket on your account on the support subdomain.

So the first attack that might come into your mind to do something like that is (“Email spoofing”) right?

Exactly, I tried to spoof an email behalf on my email to the support mail asking them to delete my account forever, and after a few hours of sending the spoofed email. I got this notification

Press enter or click to view image in full size
Support team close my account even the ticket has been created by a spoofing tool

The bad thing on this attack is that you can’t restore your account again in some websites.

At first, I thought that this is a zendesk vulnerability and not a vulnerability on the targeted website. But after I contacted my colleague Sherif Afifi about this, he found out that Zendesk already pushed a fix regarding spoofed tickets under (“Enabling sender authentication with DMARC”) feature. That’s mean If you didn’t enable this feature on your zendesk instance you could say then that you’re vulnerable to this attack.

Quickly I reported the vulnerability to the program, and within three days the report has been triaged and I got a very nice bounty.

Attack Scenarios

In a lot of companies, you can’t update your email address or delete your account directly via your profile settings. So such companies that have this policy were my targets to test my attack.

So I made a google dork that helps me to bring the vulnerable websites and here is a example of sites that close your by creating a support ticket.

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size
Attack Scenario #1

These three examples are nothing compared to other dozens websites that closes your account by submitting a ticket to support team, So it was a good start to try the attack on these websites.

Get Khaled Hassan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

#1 The first result on testing the attack:

Press enter or click to view image in full size
The sad thing that invision closed my report as out of scope:/

Then I tried the attack on the second website and spoofed an email behalf on of my colleague email (“Sherif Afifi”) to support team that asks them to close the account and happened what I expected. >>

#2

Press enter or click to view image in full size

To confirm that I want to delete the account of sherif, I have sent another email to this address ( support+id59628@website.com ) with the ticket ID as this address is customized only for customers to follow-up on their tickets through email.

#3 Another website >

Press enter or click to view image in full size

#4 This website deleted all my data from their servers.

Press enter or click to view image in full size

At the time, I have tested this attack on more than 30 popular organization, Most of them have bug bounty program and other haven’t so here is the result of testing.

Press enter or click to view image in full size

Red = Worked and victim account has been closed forever.
Yellow= Didn’t worked and support team required a physical confirmation or PIN code.

Press enter or click to view image in full size
Attack Scenario 2 — Takeover user’s accounts

Although the impact of closing user account is not a little, but I wanted to make this attack more dangerous as possible. So I start to see If I can get a full account takeover through this one. quickly I created an account on a vulnerable website with the following details

marksteava1@gmail.com > Victim
marksteava2@gmail.com > Attacker email that I created

So I have sent a spoofed email behalf on of the victim account to support team that asks them to change my account to this new email which is > marksteava2@gmail.com

And in order to make it done quickly, I’ve been communicating with the support team through their chat and here is the conversation history.

Press enter or click to view image in full size

Summary of this chat.

Mark is me.
Marry is the support agent,

What pushed them to change the email of victim account for me is that I created a ticket on behalf of the victim account and that’s mean If you can create tickets on your account this means that you’re already authorized enough to them.

After reporting the vulnerability to the CEO of the vulnerable company, He rewarded me with a good bounty given to the impact vulnerability.

Press enter or click to view image in full size
Attacking non zendesk instances

As we know that there are many softwares that provides the same helpdesk service so I started to see if the attack will work on FreshDesk, Kayako, etc.

By doing the same steps, I discovered that they’re are all vulnerable to the same attack. Even the companies who are developing their own support system. They’re vulnerable too.

Conclusion

This is not a genius finding, but sharing what you’ve learned or what you see is useful and new to the community makes me always happy. Another thing, don’t forget to use this Technic in your testing and I’m sure you’ll see many websites that are vulnerable to this attack and for sure they will consider your report as valid vulnerability.

Recommendation fix:

If you’re using zendesk you must enable (“Authenticating incoming email using DMARC”) feature on zendesk (“https://support.zendesk.com/hc/en-us/articles/115014034108-Authenticating-incoming-email-using-DMARC%E2%80%9D) to prevent this happening anymore.
Critical actions like changing email or close account should be verify by sending PIN code to user email and asks him to reply back the code again.
The last fix and I don’t like is disable creating tickets via your support email for more security
