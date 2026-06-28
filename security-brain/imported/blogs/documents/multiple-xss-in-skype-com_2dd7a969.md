---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-10_multiple-xss-in-skypecom.md
original_filename: 2019-04-10_multiple-xss-in-skypecom.md
title: Multiple xss in *.skype.com
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
language: en
raw_sha256: 2dd7a969449c9ed301ce5954db282a2499d73dd8a95d8e1e2e0022210ebc6950
text_sha256: 7d4a9ab73b8fdbf80aa4c41d0287fb7e12e3fa2d27d24e425ed10d50deb9b93a
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Multiple xss in *.skype.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-10_multiple-xss-in-skypecom.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `2dd7a969449c9ed301ce5954db282a2499d73dd8a95d8e1e2e0022210ebc6950`
- Text SHA256: `7d4a9ab73b8fdbf80aa4c41d0287fb7e12e3fa2d27d24e425ed10d50deb9b93a`


## Content

---
title: "Multiple xss in *.skype.com"
url: "https://medium.com/@jayateerthag/multiple-xss-in-skype-com-81d65919ed24"
authors: ["Jayateertha Guruprasad (@JayateerthaG)"]
programs: ["Microsoft"]
bugs: ["XSS"]
publication_date: "2019-04-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5317
scraped_via: "browseros"
---

# Multiple xss in *.skype.com

Multiple xss in *.skype.com
Jayateertha Guruprasad
Follow
2 min read
·
Apr 10, 2019

66

PART 1:

To keep it simple ,I want to make this blog to the point ,instead of writing a script for MahaBharath !!!

How It all started?

I was thinking of services provided by microsoft, Skype came to my mind.

I tested out skype but couldn’t find anything ,Then after some usual recon ,I found a subdomain manager.skype.com.If your visiting the website as first time the following pop up will appear asking for name of group.

I entered the payload “><svg/onload=confirm(document.domain)> and clicked continue.

Guess what ??? Nothing happened then ,I visited My profile Section and was surprised too see the payload got executed!!!

Then I started researching why this Xss has popped ,I opened the source code and found that Group name was already sanitized by there was a reflection of it in a option called (“make this member admin of group_name”),This is were the input was not sanitized and was the cause of xss.

I sent this report with the following impacts to let them know severity of what xss can do other than getting cookies of user :

Get Jayateertha Guruprasad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1. Stored xss is reflected in many places ,wherever same input is passed without sanitizing it,Thus if a admin of website visits the profile for inspection etc ,admin can be exploited.

2. XSS attacks can be used to steal cookies and login as user

3. It can be used to control browser by using a js shell. This is very greatly explained by brutelogic

https://brutelogic.com.br/blog/using-xss-to-control-a-browser/

4)Can be used to redirect user to malicious sites.

5)Possibility of account takeover and user data leak.

This was my first report which I sent to Microsoft for this issue .

But I mentioned Multiple Xss right??? But this was a self-stored xss,How can I make it to affect other users ?

using CSRF??? no — The website was secure from csrf too which uses skype vrf tokens .

But I found a way to escalated XSS to other users that too with 0 user interactions .

How??? Lets’s see that in my next blog to keep this short.
