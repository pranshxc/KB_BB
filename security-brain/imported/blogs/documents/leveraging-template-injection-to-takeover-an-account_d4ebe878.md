---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-04_leveraging-template-injection-to-takeover-an-account.md
original_filename: 2021-03-04_leveraging-template-injection-to-takeover-an-account.md
title: Leveraging Template injection to takeover an account.
category: documents
detected_topics:
- idor
- xss
- command-injection
- api-security
tags:
- imported
- documents
- idor
- xss
- command-injection
- api-security
language: en
raw_sha256: d4ebe87841cc46b5a1f39c7f29feaabd0ce81131722d80b6cff766eedc6e6cb8
text_sha256: 5e60f83d8d21ca2736f63236d2531af192059394e287d4dbc5f2e2155d7b06c7
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Leveraging Template injection to takeover an account.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-04_leveraging-template-injection-to-takeover-an-account.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `d4ebe87841cc46b5a1f39c7f29feaabd0ce81131722d80b6cff766eedc6e6cb8`
- Text SHA256: `5e60f83d8d21ca2736f63236d2531af192059394e287d4dbc5f2e2155d7b06c7`


## Content

---
title: "Leveraging Template injection to takeover an account."
url: "https://infosecwriteups.com/leveraging-template-injection-to-takeover-an-account-1dba7c4ae315"
authors: ["Akash Methani (@0xAkash)"]
bugs: ["CSTI", "XSS"]
publication_date: "2021-03-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3840
scraped_via: "browseros"
---

# Leveraging Template injection to takeover an account.

Top highlight

Leveraging Template injection to takeover an account.
Akash Methani
Follow
3 min read
·
Mar 4, 2021

92

Hi, I am back again with an interesting writeup, this is about a template injection bug I reported to a private program last year.

I was browsing through the application and trying to understand what it does. Walking through the app, I landed on the account settings page and looked for usual things that one should look at while testing the settings page.

After testing for some time and not finding anything meaningful, I thought maybe I’ve got nothing here and should move on to the next functionality.

The next day, I was exploring other functionalities on the application and found this interesting feature which allowed users to write a customized message for viewers visiting the page, kinda like a blog post with a customized greeting. The interesting part about this was that it allowed users to access certain properties of the user object to create customized messages, it even allowed users to set default values for some properties.

For example, if the user wants to write a post that starts with a customized greeting for each viewer. He could do something like this.

Hi user.name,
XXXX
XXXX

If a user named Akash visits this page he would see

Hi Akash,
XXXX
XXXX

There were lots of properties that could be used to display different messages to users with different privileges on the application.

I created a blog post that began with a greeting like

Hi user.name,
XXXX
XXXX

and visited this page from my account and to my surprise, it displayed Hi 9,I was not expecting this, but then I recalled while testing for bugs on the settings page, I entered my name as {{3*3}} and nothing happened that time. I left the name unchanged and moved on to test another functionality.

Get Akash Methani’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It was evaluating the expression {{3*3}} and displaying the result 9. This meant the application was vulnerable to a client-side template injection (CSTI) attack. The application was using AngularJS and user-submitted input (expression) in the name field under the account settings page was evaluating on this blog page.

I was thinking of a way to exploit this behavior and went ahead to look for an IDOR, which could have allowed an attacker to change a user’s name and replace it with a payload that sends the user’s session cookies to a server controlled by an attacker or programmatically change his account email to takeover his account.

Unfortunately, I couldn’t find an IDOR and concluded that this behavior alone is unexploitable since this was just a harmless self-injection vulnerability.

But wait, remember I mentioned that the application allowed users to set default values for some properties? An attacker could set a variable’s default value to a CSTI payload to exploit this behavior.

I set this AngularJS CSTI Payload as default value for redacted_property

{{a=toString().constructor.prototype;a.charAt=a.trim;$eval(‘a,alert(1),a’)}}

and used this redacted_property on the blog,

Hi user.name,
user.redacted_property
XXXX
XXXX

visiting this page greeted me with an alert popup, just like a classic XSS PoC.

Instead of popping an alert, an attacker could exploit this to steal the user’s session cookie or simply change his email address and takeover his account.

I hope you guys enjoyed reading this, follow me for more such interesting writeups.

For any questions, you can DM me on Twitter @0xAkash
