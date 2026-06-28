---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-30_my-first-csrf-to-account-takeover-worth-750.md
original_filename: 2019-05-30_my-first-csrf-to-account-takeover-worth-750.md
title: My First CSRF to Account Takeover worth $750
category: documents
detected_topics:
- command-injection
- automation-abuse
- csrf
tags:
- imported
- documents
- command-injection
- automation-abuse
- csrf
language: en
raw_sha256: 35ac5d2edab5a724225353a93c6dbecc208eaada8a2e354ca1e7aca7fd44b22d
text_sha256: c25f0ab6dd3ec22656b65438d4b60757fd285e5c62f3ad78a66417bd2acd8fa7
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# My First CSRF to Account Takeover worth $750

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-30_my-first-csrf-to-account-takeover-worth-750.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, csrf
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `35ac5d2edab5a724225353a93c6dbecc208eaada8a2e354ca1e7aca7fd44b22d`
- Text SHA256: `c25f0ab6dd3ec22656b65438d4b60757fd285e5c62f3ad78a66417bd2acd8fa7`


## Content

---
title: "My First CSRF to Account Takeover worth $750"
url: "https://medium.com/@nishantrustlingup/my-first-csrf-to-account-takeover-worth-750-1332641d4304"
authors: ["Nishant Saurav (@inishantsinha)"]
bugs: ["CSRF", "Account takeover"]
bounty: "750"
publication_date: "2019-05-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5238
scraped_via: "browseros"
---

# My First CSRF to Account Takeover worth $750

My First CSRF to Account Takeover worth $750
Nishant Saurav
Follow
3 min read
·
May 30, 2019

343

Before I start. I want to take a moment to all who helped me learn Web Application Security and Bug Bounty Hunting! :)

Hello, Guys, the Program was a private Invite and I am still working with this program. So, for the sake of the privacy of the program, let us call it “example.com” in this writeup.

I got this invite around 6 months back. The Website has the functionality of making an order of using public transport ( e.g. Purchasing tickets, passes, storing user information like card details, home address, work address, etc.).

Get Nishant Saurav’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To test the CSRF, I created two accounts. One for the attacker and another for the Victim. Let us call it as “Attacker@gmail.com” and “victim@gmail.com”.

Press enter or click to view image in full size
“attacker@gmail.com”

Now, I filled in the details for both the account. And then I started making some changes into it like adding work address and making an order from the Attacker’s account. I Put the Burp Intercept ON and clicked on the “save” button. Here is the burp request which I captured.

Press enter or click to view image in full size

Now, I generated the CSRF poc using the burp suite and saved it as an html page. And send it to the victim account who was logged in using the Chrome browser. I opened the HTML page in the new tab of the Chrome browser and refreshed the page where I was already logged in. And Boom….. The work address of the victim was changed to “bla….bla…bla” and a new order was made on behalf of the victim. As the card details were not added in both the accounts, the order was eligible for on-spot payment.

Now…I thought that if the attacker is able to make order on behlaf of the victim then he could probably also takeover the victim’s account. I said to let’s check it out.. :)

Now to take over the account, I went to the setting page of the attacker's account first and then gave a temporary email address from the temp-mail.ord and captured the request in Burp without any changes by re-saving the same information. Then I saved the CSRF POC and sent it to the victim. As soon as I opened the page in the victim’s browser the email of the account changed from “victim@gmail.com” to the temp-mail one. Then I was like….

Finally, I made a nice report and submitted it to the program. The Company took almost 3 months to respond and closed the report by paying $750 in the next 1 month. Although it was less for the account takeover ;).

I thought of putting this writeup a million times but I am Lazy! Lol! :P

Thanks for being patient and reading this writeup. This is my first ever writeup. I hope you all like it and let me know if you want me to put anything else in my next writeup or any mistakes in this writeup.

You can always find me on:
Twitter: https://twitter.com/inishantsinha
LinkedIn: https://www.linkedin.com/in/nishantsaurav/

:) :)
