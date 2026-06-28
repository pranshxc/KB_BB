---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-21_hack-till-your-last-breath.md
original_filename: 2020-07-21_hack-till-your-last-breath.md
title: Hack Till Your Last Breath
category: documents
detected_topics:
- password-reset
- idor
- xss
- command-injection
- business-logic
tags:
- imported
- documents
- password-reset
- idor
- xss
- command-injection
- business-logic
language: en
raw_sha256: d7bffa8143981ad7598b8ddd2d5308bf1ce36f3affbf9889b1d5d1acc63abab5
text_sha256: 2e64534d68940e6241059a9081b67e6f47964ac395dad823d8830559c713e7a5
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Hack Till Your Last Breath

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-21_hack-till-your-last-breath.md
- Source Type: markdown
- Detected Topics: password-reset, idor, xss, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `d7bffa8143981ad7598b8ddd2d5308bf1ce36f3affbf9889b1d5d1acc63abab5`
- Text SHA256: `2e64534d68940e6241059a9081b67e6f47964ac395dad823d8830559c713e7a5`


## Content

---
title: "Hack Till Your Last Breath"
url: "https://medium.com/@totmukesh/hack-till-your-last-breath-3e58f4fb1738"
authors: ["mechboy / _m.u.h.e_ (@Muhe76355002)"]
bugs: ["IDOR"]
bounty: "200"
publication_date: "2020-07-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4392
scraped_via: "browseros"
---

# Hack Till Your Last Breath

Hack Till Your Last Breath
mechboy
Follow
4 min read
·
Jul 21, 2020

230

1

A Tale of my ATO

Hey fellow hackers, Muhe. This is my first write-up. I will share, how I was able to perform a complete account takeover on a million-dollar organization. Ok, let’s start…….

P1 in 10 minutes

It was a HackerOne private program so I can’t disclose its name. Let’s assume it is “redacted.com”. It has a very small scope so I decide to hunt in the main domain. Actually, I won’t do recon but not now. So directly I jumped for testing. Just powered up my burp and browser to monitor the requests. While looking user’s dashboard there was an option to change the email for our account. I changed the mail id and moved to burp.

Press enter or click to view image in full size

{“userId”:”xxxxx-xxxxxxxx-xxxx-xxxxx",”email”:”test12@gmail.com”}

There were two parameters, one is the user-id and another one is our new email. You can see that in the above image. User-id is unique for every user. I had replaced my user id with the victim’s user-id (another account) in that request. When I checked the victim account Booom….. victim mail got changed. Now I can take over the victim’s account by requesting a forgotten password. Hoooo within 10 mins, I found a P1 bug. I reported that in h1. But my report is not ended here!

Unexpected quotes

I just waited to see this “triaged” but there was a surprise for me. Yes, my report was marked as “NOT APPLICABLE”. And that triager left this below message for me

The user_id parameter is a UUID value that has very high entropy. I don’t see an impact here because the UUID cannot be guessed.

User-id has very strong entropy. I tried to crack it. But nothing happened. Yes, the site is secure because I can’t get others’ user-id.

Wait….. what they can do if the user-id was revealed by them? Yeah, accidentally I noticed the user-id was leaking in URLs, password reset links, and cookie. I gave this info to triager.

Again and Again

But he replied as below,

There are two same reports before, and the team informed us that they are not willing to accept this UUID is not publicly available.
What example you gave for UUID was self exploitable. If you are able to find UUID of another user without any self-attack, I can ask the team to have another look.

So it was closed as a duplicate. But I didn’t stop. I already told you that user-id was leaking in a cookie so I started hunting for an XSS and I got it. Through this XSS I can get any user’s user-id by executing my payload in his browser. Through IDOR and XSS I can do an account takeover. I commented this on my closed report.

Again Again Again

Again dupe…………………..This is the reply of that triager

This XSS was also reported before and again it is a duplicate of #XXXXXX

This made me mad…………………..

Get mechboy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I just took a break. But now I decided to learn RECON this time. Every day, I read some blogs and watched 
Jason Haddix
 and 
Behrouz Sadeghipour
 youtube videos.

Now I decided to start hunting again. In an hour I found a Business logic vulnerability in a site. And I got 200$ for that. It was a small bug but………….. it gave me the solution.

Dorks Cure’s Dork

Yup, this small bug gave me the solution. While hunting this bug I used Google Dork to gather some information. Then only it came to my mind ”why don’t we use Google Dorks to find URLs which having user-id of redacted.com users”. Yes, I used Google Dorks in order to perform account takeover in “redacted.com”.

I already said user-id was leaking in URLs.

site:redacted.com inurl:”xxxxxxxx”

By using the above dorks, I got more than 1000 URLs which having user-id redacted.com users. From that URLs, I have taken a random user-id and changed the email with the help of my IDOR bug. Through “Forgot password’ I changed the password. Then I logged in to VICTIM account. I gave this as a PoC to triager.

At last, my report got TRIAGED

IDOR + DORKS = ACCOUNT TAKEOVER
Conclusion

“How to be successful in bug bounty”. You may face hard times in bug bounty. But Persistence is the key to success. Two hackers were reported this bug before me. Their report is closed as N/A but my reported got triaged. Because I ran till the endpoint. “Never Give_up” it may look like a cinematic dialogue but it will drive you to success so use this in your hard times.

Ping me:

Instagram

Twitter
