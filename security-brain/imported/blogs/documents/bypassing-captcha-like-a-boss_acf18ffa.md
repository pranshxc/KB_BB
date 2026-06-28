---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-16_bypassing-captcha-like-a-boss.md
original_filename: 2018-04-16_bypassing-captcha-like-a-boss.md
title: Bypassing Captcha Like a Boss
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: acf18ffa14146ee07813b22898d4cdde59a8349afb8e99fe4945534034cee17e
text_sha256: 4ac03c3441d0e15e91216fba247b6b5a3bc6dbe5eec55f1ef522d61d9f2d867b
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Captcha Like a Boss

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-16_bypassing-captcha-like-a-boss.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `acf18ffa14146ee07813b22898d4cdde59a8349afb8e99fe4945534034cee17e`
- Text SHA256: `4ac03c3441d0e15e91216fba247b6b5a3bc6dbe5eec55f1ef522d61d9f2d867b`


## Content

---
title: "Bypassing Captcha Like a Boss"
url: "https://medium.com/bugbountywriteup/bypassing-captcha-like-a-boss-d0edcc3a1c1"
authors: ["Ak1T4 (@akita_zen)"]
bugs: ["Captcha bypass"]
publication_date: "2018-04-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5916
scraped_via: "browseros"
---

# Bypassing Captcha Like a Boss

Top highlight

Bypassing Captcha Like a Boss
Ak1T4
Follow
3 min read
·
Apr 17, 2018

861

14

Hello Hunters! It’s been a while since my last write up, so i decide to share a fun experience that i had while hunting on a private program.

What the hell is a captcha?

From my point of view: A captcha solution is mostly utilized for avoid bots and ensure that the User behind the app is a real human.

Share is care, so let’s go to the write up!

Mapping the Application, i found a subscription endpoint with a captcha filter like this:

http://example.com/captcha/captchaCheck?

This took my attention quickly so i move to the src page:

<form action=”/captcha/captchaCheck” method=”post”>
<input name=”hash” value=”09573e52f752f3f5e6250b62aa34b8a8c08a4d22" type=”hidden”>
<input name=”emailAddress” value=”test@email.com” type=”hidden”>
<input name=”name” value=”” type=”hidden”>
<input name=”enteredValue” size=”25" type=”text”>
<input value=”Subscribe” type=”submit”>
</form>

If you look at the form you can realize that there are 2 interesting params:

”hash” (encryption hash) and ”enteredValue” (number value of the captcha)

So, i fill the captcha and sent the form:

At this point i needed to realize the behavior/functionality of this captcha, so:

I found this:

If “hash” == “enteredValue” then Request is Accepted

If “hash” != “enteredValue” then Request is Blocked

Nice, so.. its quite simple: if params match: requests is accepted.. Now the complex thing is: that hash can be decrypted? : Challenge Accepted!

So i paste the hash in my terminal and try to decrypt with “dcipher”:

Get Ak1T4’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

(Decipher hashes using online rainbow tables [hash toolkit, GromWeb, MD5Hashing] & lookup table attack services.)

Press enter or click to view image in full size

Nice! Decrypted: OK! If you notice the 6 digits number is equal to the captcha image below:

Well well well, now we have all the pieces in the table: so.. let’s create a bot!

I created a bot in python for PoC purposes to show how an attacker can easily bypass this captcha behavior and abuse of his functionality:

1) First the bot sent a request to the subscription page with the captcha -> https://company.com/captcha/form/?
2) Bot scrape on the page and retrieve the ‘hash’ value param.
3) Bot decrypt the Hash (dcipher)
4) With decrypted value the bot creates a POST request to http://company.com//captcha/captchaCheck and automatically fills all user form required params with random values (email, name, ipaddress, etc)
5) Bot sent the POST request and bypass the captcha

The bot is very basic but works like a charm.. so i sent this PoC to the program with the next explanation:

Security Impact

An attacker can create a bot to bypass the captcha and automate the tasks to sent unlimited requests to a multiple urls or lists with random/fake users, emails, IP address.. for spamming or evil purposes (collect data, analyze traffic behaviors, etc)

( The program had a really fast response! < 1h )

TIMELINE

Submitted 2018–04–16 03:51:17 UTC

Team Response with triage and bounty 2018–04–16 04:48:17 UTC

(Bounty $ xxx)

So ak1t4 is happy!

I hope you enjoyed this reading as i enjoyed writing it!

And remember: if you fail? try harder!

Happy Hunting!

ak1t4 z3n 🇦🇷 (@knowledge_2014) | Twitter
The latest Tweets from ak1t4 z3n 🇦🇷 (@knowledge_2014). Bug Bounty Hunter — HoF : Google — Mozilla — PayPal …

twitter.com
