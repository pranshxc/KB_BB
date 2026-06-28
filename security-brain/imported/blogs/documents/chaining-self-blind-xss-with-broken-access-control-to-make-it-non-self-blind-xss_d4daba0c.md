---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-30_chaining-self-blind-xss-with-broken-access-control-to-make-it-non-self-blind-xss.md
original_filename: 2023-06-30_chaining-self-blind-xss-with-broken-access-control-to-make-it-non-self-blind-xss.md
title: Chaining Self Blind XSS with Broken Access Control To Make it Non Self Blind
  XSS
category: documents
detected_topics:
- access-control
- xss
- command-injection
- otp
- csrf
tags:
- imported
- documents
- access-control
- xss
- command-injection
- otp
- csrf
language: en
raw_sha256: d4daba0c1c0afb2860daee42d08aa81a56d4685ff161d374396508b2c08b2c46
text_sha256: 7b06cafd2bdb46b9d4e95cbe5047e7f16a2f82ebfbd75901692272328416340b
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining Self Blind XSS with Broken Access Control To Make it Non Self Blind XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-30_chaining-self-blind-xss-with-broken-access-control-to-make-it-non-self-blind-xss.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `d4daba0c1c0afb2860daee42d08aa81a56d4685ff161d374396508b2c08b2c46`
- Text SHA256: `7b06cafd2bdb46b9d4e95cbe5047e7f16a2f82ebfbd75901692272328416340b`


## Content

---
title: "Chaining Self Blind XSS with Broken Access Control To Make it Non Self Blind XSS"
url: "https://sudhanshukashyap123.medium.com/chaining-self-blind-xss-with-broken-access-control-to-make-it-non-self-blind-xss-626a70c8bbc7"
authors: ["sudhanshu Kumar kashyap (@ReebootToInit5)"]
bugs: ["Blind XSS", "Self-XSS", "Broken Access Control"]
publication_date: "2023-06-30"
added_date: "2023-07-04"
source: "pentester.land/writeups.json"
original_index: 985
scraped_via: "browseros"
---

# Chaining Self Blind XSS with Broken Access Control To Make it Non Self Blind XSS

Chaining Self Blind XSS with Broken Access Control To Make it Non Self Blind XSS
sudhanshu Kumar kashyap
Follow
3 min read
·
Jun 30, 2023

59

1

okay so the first thing it is not gonna be a fancy write up as i am running out of time, but definitely excited for this vulnerability so dropping the write up here.

Okay , so the story begins with an application. the application has multiple roles , but i am focusing one 1 higher role and 1 the lower role. I have already exploited a lot of vulnerabilities in the application like RXSS and HTMLi etc. At one endpoint i got a stored XSS and it was self xss.

lets talk about the stored xss. there are a few reports in the application and each report have an option to put a comment on it. i assume you got it where i exploited the stored XSS right? yes it was on the comment section. a simple onerror payload worked. then i tried a Blind XSS payload from my xss dot report. it triggered as well , but since it is self there is no use here.

I moved forward for chaining it with CSRF , but unfortunately they are using CSRF token in body with all the validations…sed life. in short i couldn’t chain it with CSRF.

I had to exploit it because it was a challenge for me.

Get sudhanshu Kumar kashyap’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now the thing is for every user the reports are different , its not the same so my BXSS will not trigger because my reports are for me only. what can be done. i remembered something similar that i exploited almost 2 years back. A Vertical privilege escalation. so what i thought here was if and only if i can access the other user reports somehow.

Since i had the credentials for higer accounts as well i quickly logged into admin account accessed one of the reports and sent the request to repeater. i noticed the path being used to fetch the report. the report name is the only thing which is different in the path. umm okay i can do something here.

I logged out of the admin account , logged into the normal user account. clicked on on of the report and then captured the request. noticed the path , did not forward the request and changed the report name.

Bingooo!!!….i got the report in my account. yayyy….i quickly checked if i can surf through the report and yes i was able to access the report and surf through it. i quickly went to the comment section and added my Blind XSS payload there. saved it. logged out from that account and again logged into the Admin account. accessed the report and the Payload finally triggered from the admin account , i went to my xss dot report account and confirmed i was able to capture the Admin’s Cookies and DOM.

So in short I exploited a Vertical privilege escalation to access the Admin report then i added my BXSS payload and then when Admin opened the same report it triggered.

The question is do i need to perform the BXSS if there is already privilege escalation….yes the privilege escalation is only for reports , i couldn't do much. but with BXSS the impact is much more.

Thanks and please don’t mind the spelling mistakes if any…you can follow me on twitter @RebootToInit5
