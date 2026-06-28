---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-16_param-hunting-to-injections.md
original_filename: 2022-12-16_param-hunting-to-injections.md
title: Param Hunting to Injections
category: documents
detected_topics:
- xss
- automation-abuse
- command-injection
- password-reset
- api-security
- mobile-security
tags:
- imported
- documents
- xss
- automation-abuse
- command-injection
- password-reset
- api-security
- mobile-security
language: en
raw_sha256: 3947e634306f4326d851e053c7ed72e83b25e4e3f3bdfe752c305263e08a4917
text_sha256: c5fb34dec152872f1614862279c62f6d752c65f747ac52bc42071bef27f1f5a5
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Param Hunting to Injections

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-16_param-hunting-to-injections.md
- Source Type: markdown
- Detected Topics: xss, automation-abuse, command-injection, password-reset, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `3947e634306f4326d851e053c7ed72e83b25e4e3f3bdfe752c305263e08a4917`
- Text SHA256: `c5fb34dec152872f1614862279c62f6d752c65f747ac52bc42071bef27f1f5a5`


## Content

---
title: "Param Hunting to Injections"
url: "https://infosecwriteups.com/param-hunting-to-injections-4365da5447cf"
authors: ["302 Found"]
bugs: ["HTML injection", "XSS"]
publication_date: "2022-12-16"
added_date: "2022-12-20"
source: "pentester.land/writeups.json"
original_index: 1771
scraped_via: "browseros"
---

# Param Hunting to Injections

Param Hunting to Injections
Hey hackers! How’s your week going?
TheBountyBox
Follow
4 min read
·
Dec 16, 2022

180

1

Here we are back with another blog.

Today we are going to discuss Effective Param-Hunting to Injections

So recently we have been working on a private project . Let’s call it redacted.com .

Since there were a lot of subdomains, we thought of filtering the subdomains based on the content-length to find domains which offer a large number of functionalities.

Press enter or click to view image in full size

So after filtering, we landed on <Sub.redacted.com> which had a login page.

Initially, we were looking for BAC; meanwhile, we noticed that when we enter invalid credentials on the login page, it responds with an error parameter in the url.

So briskly we started to inject XSS payloads to generate an XSS but no luck since we were unable to bypass the filtering.

Soon after we started to test the password reset functionality .

Here we noticed that after entering any invalid email there was no error param generated in the url so we thought of manually adding this param .

To our surprise the param was actually reflecting .

Again we tried injecting the XSS payloads but WAF was blocking everything.

Finally we thought of balancing using the </div> tag since the and boom here comes HTML Injection .

We know what you’re thinking, yeah IFRAME did the rest of the work .

Press enter or click to view image in full size

Finding Hidden Parameters :

Get TheBountyBox’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

There are a lot of tools like Paramminer , Arjun ,x8 etc that help us in finding hidden parameters but unfortunately in our case neither tool worked because the parameter might not be present in the default word list .

Active Param Hunting :

Active Param Hunting helps in detecting all the params and generating a custom target specific wordlist .

For Creating a custom wordlist we need to extract all the parameters related to the domain and for this we will use this beautiful tool getAllParams .

Steps :
Download and configure getAllParams extension in your burp suite
Now start crawling the website automatically as well as manually .

A combination of manually testing and automation will always provide you with better results than blinding using the scripts

3. Now Target -> Sitemap -> Choose the target->Right Click-> Extensions -> Get All Params (GAP)

4. Save all the extracted params in a file

5. You can also gather all the urls using gau , wayback , Katana or any other tool and then extract all the parameters from the extracted urls .

We have written a very basic script which can extract all the parameters from the urls gathered from various tools :

Param-Extract (Yeah lazy script but works also we will update it later)

Press enter or click to view image in full size

Alternatively you can also use the below one-liner to extract the urls using unfurl tool :

cat urls | unfurl format %q | cut -d “=” -f1 | sort -u > params.txt

6. Now merge both the param files and sort -u

7. Once you have created a custom wordlist with all the params you can easily use the Paraminer burp extension to discover the hidden params .

8. Once you have identified the hidden parameters you can test for various injection or other bugs based on the case scenarios .

Happy Hunting !!!!

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
