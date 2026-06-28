---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-07_sony-hunting-i-discovering-hidden-parameters-5x-swag.md
original_filename: 2021-11-07_sony-hunting-i-discovering-hidden-parameters-5x-swag.md
title: 'SONY Hunting I: Discovering Hidden Parameters (5x SWAG)'
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: c32572884efbeb9eca0f9b25312ae245d94ea3977c928e8106d9424a95bd678f
text_sha256: 05b23591e9f43911b780e73dfc26fff43d44a6ee3ea316a27b00396d28520217
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# SONY Hunting I: Discovering Hidden Parameters (5x SWAG)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-07_sony-hunting-i-discovering-hidden-parameters-5x-swag.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `c32572884efbeb9eca0f9b25312ae245d94ea3977c928e8106d9424a95bd678f`
- Text SHA256: `05b23591e9f43911b780e73dfc26fff43d44a6ee3ea316a27b00396d28520217`


## Content

---
title: "SONY Hunting I: Discovering Hidden Parameters (5x SWAG)"
url: "https://infosecwriteups.com/sony-hunting-i-discovering-hidden-parameters-5x-swag-c3396c0064bc"
authors: ["can1337 (@canmustdie)"]
programs: ["Sony"]
bugs: ["Open redirect"]
publication_date: "2021-11-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3189
scraped_via: "browseros"
---

# SONY Hunting I: Discovering Hidden Parameters (5x SWAG)

SONY Hunting I: Discovering Hidden Parameters (5x SWAG)
can1337
Follow
4 min read
·
Nov 7, 2021

212

Hello everyone.

It’s been a long time. Hope everyone is well. I thought, I should publish a new write-up and I feel ready for it.
Today I’m going to talk about a series of vulnerabilities that I found in Sony a few months ago. OK, Let’s go then!

Press enter or click to view image in full size

As you know, SONY is a huge target and even though I don’t have any financial profit (only swag), I especially like to take care of it.
In general, it’s not my style to concentrate on a single vulnerability type. However, in this wide scope, I wanted to make things a little easier and focused only on Open Redirect vulnerabilities. Because hunting for vulnerabilities such as open redirect is forgotten or overlooked. So, the topic of this write-up will be Open Redirect. (I plan to continue this series with other vulnerabilities later.)

Recon is My Life

Press enter or click to view image in full size
crt.sh/?q=Sony

I’ve noticed that it is more useful to use a keyword instead of entering the domain names of the targets in programs with a wide scope.

So, trying keywords like “Sony” “Sonypictures” instead of “sony.com” or “sony.net” may produce more output for you in some programs. At the same time, dorks such as “%.%.%.target.%” and “%.target.net” can still be creative on crt.sh

Hunting for Hidden Parameters

Press enter or click to view image in full size
The “redirectUrl” parameter is a potential Open Redirect.

In this time, I was reviewing the Sony subdomains with GAU and FFUF. (sometimes waybackurls) In general, I focused on domains with a login or register section.
Basically what I do is discover pages that take input from the user and then try to redirect the user and see if the parameters are working correctly.
Besides, JS files are always important to discover new parameters. When I get a js file as a result of any output, I look at the parameters in it with the LinkFinder. Finally, Paramspider or Arjun can help us discovering hidden parameters.

Now that we’ve basically seen what we can do, let’s move on to the cases I’ve come across.

CASE I: Basic Open Redirect using a hidden parameter

In the first case, I was browsing the subdomains of SonyPictures and what I noticed was that most of them didn’t receive input from the user. However, I found a few exceptions.

Get can1337’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I open the source code of the page, I usually search for hidden parameters and keywords like “redirect” or “return”.
Before long, I came across a parameter like the one below.

Press enter or click to view image in full size

Hidden parameters are not visible in the URL, so we have to add the parameter ourselves. I tried to interfere with the parameter by creating a structure like the one below.
“sonypicturessite.tld/login/?redirect_to=targetsite.com”

Press enter or click to view image in full size

When trying to redirect the parameter, the first thing I do is add “.evil.com” to the end of the domain. Makes the target site a subdomain and redirects to evil.com. This is a shortcut, it allows us to see that the end of the parameter is not filtered.

Case II: Duplicating hidden parameters

Similar to the first case, I found a hidden parameter in different login panel. However, this time it was not allowing Open Redirect. I tried many ways but couldn’t bypass it.

Press enter or click to view image in full size

But of course the game doesn’t end there, I thought of trying the same parameter in different potential redirect areas. Just like log in, the log out screen is one of them.
At this point, I think the parameter I discovered on the log in screen is a common parameter used to log out or redirect on the same site.

Press enter or click to view image in full size

I added the parameter I found to the end of the log out URL and got another successful redirect.

Case III: Interfere with redirects

The last case of this write-up is about interfering with redirects made with mirrored parameters on the URL. Let’s look at the example to understand this better.

In the final target, when I clicked login it was redirecting me to login via sony.com. However, the redirect parameter in between don’t escape my attention. This URL looked pretty messy so I decided to examine it using Burp Suite.

Press enter or click to view image in full size

I was able to redirect the “redirect_url” parameter to the target site on my first try.

For now I have 5 SWAGs from SONY. Other redirects I found were similar to these.

That’s all for now, thank you for reading. You can follow me on twitter. https://twitter.com/canmustdie
