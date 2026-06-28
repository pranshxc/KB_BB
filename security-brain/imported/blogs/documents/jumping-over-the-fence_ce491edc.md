---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-05_jumping-over-the-fence.md
original_filename: 2019-02-05_jumping-over-the-fence.md
title: Jumping Over The Fence
category: documents
detected_topics:
- idor
- command-injection
- otp
- rate-limit
- business-logic
tags:
- imported
- documents
- idor
- command-injection
- otp
- rate-limit
- business-logic
language: en
raw_sha256: ce491edc4716c18aab9ce51dc05b8fab5240f5f8d7c1d1fb4eec950b273e4808
text_sha256: 585ac4d5ff12dbd07ca8682a54994263a5d6e2e20659463a36f2d709f4152621
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Jumping Over The Fence

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-05_jumping-over-the-fence.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, rate-limit, business-logic
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `ce491edc4716c18aab9ce51dc05b8fab5240f5f8d7c1d1fb4eec950b273e4808`
- Text SHA256: `585ac4d5ff12dbd07ca8682a54994263a5d6e2e20659463a36f2d709f4152621`


## Content

---
title: "Jumping Over The Fence"
url: "https://medium.com/@albeckshahar/jumping-over-the-fence-ce0fe5f9a3a2"
authors: ["Shahar Albeck"]
bugs: ["Open redirect"]
publication_date: "2019-02-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5431
scraped_via: "browseros"
---

# Jumping Over The Fence

Jumping Over The Fence
Shahar Albeck
Follow
4 min read
·
Feb 5, 2019

5

Note: The following article was published on 13/09/2016 on https://FogMarks.com

Press enter or click to view image in full size
credit: Google Images

“Fences were made to be jumped over” — John Doe

As

you might have already guessed (or not), today’s case-study is all about open redirects, and bypassing mechanisms that were made to prevent them. Fun!

I have already shared with you my thoughts about open redirects and their consequences on the website’s general security.
Now it is the time to demonstrate how open redirects can be achieved by manipulating the AOR (Anti Open Redirects) mechanism.

A great example for a great AOR is again Facebook’s linkshim system.
Its basically attaching an access token to every URL that is being posted on Facebook.
That access token is personal, so only the user who now viewing the link can be the one to click on it and be redirected to its destination; other don’t. In addition, the linkshim mechanism checks the destination for the user and prevents the user from being redirected to a malicious website. Yes, pretty cool.

Well, until now the sun is shining and we all are having fun at the beach

Hang me that beer, would you?
But what happens when the AOR mechanism, the same one that we trust so much, is being manipulated to act differently?
That’s exactly what we are going to witness today.

Sadly, most websites that use an AOR manage the links that are being posted to them only if those links are of 3rd party websites. Which means, that if I am on the website x.com and I am posting a link to website y.com, the link will appear this way on x.com: x.com/out?url=y.com&access_token=1asd2ad6fdC

But if I’ll post a link to the same domain (post x.com/blabla on x.com), the link will appear as is: x.com/blabla

The reason this is happening is because websites usually trust themselves to redirect users within themselves. They think this is ‘safe’ and ‘pointless’ to attach an access token to a link that is redirecting the user to the same domain. And you can agree with them, like many has. I have heard the argument ‘if a certain page is vulnerable to an open redirect there is no reason to check redirection to it‘ countless times. But now I’m about to change that thought once and for all.

A very popular designs website

Which unfortunately I can’t reveal its name, it had this exact vulnerability.
The site allowed “inner links” to be redirected without any access token or validation, but required the referrer to be the same domain. Pretty smart.
But the AOR mechanism allowed any inner link to be redirected, as long as its domain was one of that company’s domains or subdomains.

Get Shahar Albeck’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Using a domain enumeration software I was able to detect a sub domain of the website that contained a mail service for the company’s employees, and that mail service had an open redirect vulnerability on its logout page — Even if the user was not logged in, when the logout page was being accessed with a ‘redirect after’ GET parameter, the user was redirected to any other page, even of a 3rd party web. That mail service, by the way, does not consider this behaviour to an open redirect vulnerability. Go figure.

Now that I have an open redirect on a sub domain page, how can I make it rain from the main domain?

Well, the answer was quite easy — I’ll simply use the logic flaw of the AOR mechanism to redirect the user to the sub domain and from there to the 3rd party site.

But there was still a problem — as I said before, the AOR mechanism allowed the link to be redirected to a subdomain, but only if the referrer was the same website.

So what have I done?

I have simply redirected the user to the same page, and then he got redirected again.

Example:
If the 2 vulnerable pages are:
Vulnerable mail service: http://mail.x.com/out?url=y.com
‘Vulnerable’ page within the domain: http://x.com/redirect?to=mail.x.com/out?url=y.com

And the second page requires the referrer header to be from x.com, I have simply issued the following URL:

http://x.com/redirect?to=x.com/redirect?to=mail.x.com/out?url=y.com

That’s it.

Here’s an example of a simple, easy-to-use logic flaw within an AOR mechanism.

Press enter or click to view image in full size

As always,

Cheers!
