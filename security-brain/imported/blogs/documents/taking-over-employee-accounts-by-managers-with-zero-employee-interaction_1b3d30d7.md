---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-12_taking-over-employee-accounts-by-managers-with-zero-employee-interaction.md
original_filename: 2021-08-12_taking-over-employee-accounts-by-managers-with-zero-employee-interaction.md
title: Taking Over Employee Accounts by Managers with Zero Employee Interaction
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 1b3d30d72fde69730296607f151c6c68a20f13294246e2972181ae642c42e2e3
text_sha256: a640b0445c6cc062edb87a554a3555feb6c28fe574d32ee60428009a7eb15630
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Taking Over Employee Accounts by Managers with Zero Employee Interaction

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-12_taking-over-employee-accounts-by-managers-with-zero-employee-interaction.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `1b3d30d72fde69730296607f151c6c68a20f13294246e2972181ae642c42e2e3`
- Text SHA256: `a640b0445c6cc062edb87a554a3555feb6c28fe574d32ee60428009a7eb15630`


## Content

---
title: "Taking Over Employee Accounts by Managers with Zero Employee Interaction"
page_title: "Simple HTML Injection to $250. Hi everyone, It’s my first blog about… | by Chaitanya Rajhans | Medium"
url: "https://medium.com/@chaitanyarajhans024/simple-html-injection-to-250-895b760409ed"
authors: ["Chaitanya Rajhans (@Chaitanya_024)"]
bugs: ["HTML injection"]
bounty: "250"
publication_date: "2021-08-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3426
scraped_via: "browseros"
---

# Taking Over Employee Accounts by Managers with Zero Employee Interaction

Simple HTML Injection to $250
Chaitanya Rajhans
Follow
3 min read
·
Aug 12, 2021

946

6

Hi everyone, It’s my first blog about bug bounty so today I’m going to share that how I earned $250 with simple HTML Injection. I hope you’ll enjoy it!

Let me introduce myself first. My name is Chaitanya and I’m learning about web app testing from past 6 months. I would like to thank 
Vedant Tekale
 for introducing me to this field.

Let’s get started…

So first of all I’ll tell you lil’bit about the target. I received a private invitation on 
HackerOne
 which is having a large scope but only the main domains are in scope. Whenever I test main domains, I don’t go for the main functionalities like signup/signin, reset password etc. I look for the endpoints like contact us, newsletters, support etc. Let’s suppose the site as redacted.com

It’s time to get into the bug…

While surfing on the site I came across the contact us page so there are lot of options for getting in touch with the company but one of them was the live chat support. So when I clicked, it opened the chat Box so I filled out the main stuff like Name and Email and it took me to the chatting page where we can talk with their support team.

I typed some random words. Suddenly I noticed that there is an option for getting the copy of our chat with the support. So I clicked on it and ended the chat session. I went to mail inbox just to verify so I got the exact copy of my chat. Again I followed the same process as it is and instead of random words I entered the XSS paylaod and checked the inbox. As I opened the inbox it get triggered, because it was a temporary mail site. So I’m like

Immediately I done the same process but this time I entered my email and entered the image payload as
<img src=”https://test.com/mrbean.jpg"> and went to the inbox and yeah I got this

Press enter or click to view image in full size

I quickly made PoC and reported. Next day in the morning I got response as triaged and on the same day in the afternoon I got rewarded with $250.

Impact

By this way attacker can enter anyone's email to send this kind of mails which may contains malicious links, unwanted phishing stuff, attacker can insert some pictures which may result into bad reputation of company as the email is coming directly from the company.

Get Chaitanya Rajhans’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

For a beginner like me it's challenging to find this bug on main domain as it was a big program and lot’s of reports were resolved.

I hope you enjoyed this. Thank you so much for taking time to read this. You can get in touch with me here.

Have a great day ;)
