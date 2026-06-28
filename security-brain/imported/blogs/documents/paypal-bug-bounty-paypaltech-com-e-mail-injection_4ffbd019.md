---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-09-26_paypal-bug-bounty-paypaltechcom-e-mail-injection.md
original_filename: 2013-09-26_paypal-bug-bounty-paypaltechcom-e-mail-injection.md
title: 'PayPal Bug Bounty: PayPaltech.com E-Mail Injection'
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 4ffbd019535baedb9875b712286f2e2e9a694b73af87dc1c2666be7240d47b43
text_sha256: e0f8f3885640950937836578969f196d25eaecbf5ef6c804fc74153f122bc449
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# PayPal Bug Bounty: PayPaltech.com E-Mail Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-09-26_paypal-bug-bounty-paypaltechcom-e-mail-injection.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `4ffbd019535baedb9875b712286f2e2e9a694b73af87dc1c2666be7240d47b43`
- Text SHA256: `e0f8f3885640950937836578969f196d25eaecbf5ef6c804fc74153f122bc449`


## Content

---
title: "PayPal Bug Bounty: PayPaltech.com E-Mail Injection"
page_title: "PayPal Bug Bounty: PayPaltech.com E-Mail … | RCE Security"
url: "https://www.rcesecurity.com/2013/09/paypal-bug-bounty-paypaltech-com-e-mail-injection/"
final_url: "https://www.rcesecurity.com/2013/09/paypal-bug-bounty-paypaltech-com-e-mail-injection/"
authors: ["Julien Ahrens (@MrTuxracer)"]
programs: ["Paypal"]
bugs: ["Email injection"]
publication_date: "2013-09-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6396
---

# PayPal Bug Bounty: PayPaltech.com E-Mail Injection'

Sep 26, 2013 · By [Julien Ahrens](/about/)

Bag the bug! I’ve reported another interesting vulnerability to the PayPal site security team in May 2013 affecting their domain [www.paypaltech.com](https://www.paypaltech.com) , which is in scope of the official Bug Bounty program.

But this time, it’s not one of the common web vulnerabilities! I’m talking about a quite hazardous E-Mail Injection vulnerability paired with a less interesting Fullpath-Disclosure vulnerability, which - by the way - was really shocking…guess why ;-)

The E-Mail injection vulnerability allowed an attacker to send emails using the PayPal - servers with some restrictions via crafted GET requests. The parameters of the GET request were directly and without any filters used in a PHP [mail](https://php.net/manual/de/function.mail.php) call:

![paypaltech-email-injection](/2013/09/paypal-bug-bounty-paypaltech-com-e-mail-injection/images/paypaltech-email-injection.e9d1389466e1125c961b0f8efa41990adf9d4a2c0d71f115a71c5deca3e3eec3.png)

Unfortunately PayPal did not implement any kind of technical restriction (like a captcha for example) regarding the number of GET requests that could be sent to the script. This type of vulnerability could become very annoying, because an attacker only has to call the script using some kind of loop while parsing his own email-database - sounds quite interesting for a spammer or phisher.

Good to see that this issue has been fixed now - although the fix took several months :-(. Anyways, I’d like to thank PayPal for the nice bounty payment and the “[Wall of Fame](https://www.paypal.com/webapps/mpp/security-tools/wall-of-fame-honorable-mention) ” listing.

![paypal-hof](/2013/09/paypal-bug-bounty-paypaltech-com-e-mail-injection/images/paypal-hof.56b8a8ee947a4248131bd3ae62b589866ec14c7ba66ed5cb98dc806c71799f7b.png)
