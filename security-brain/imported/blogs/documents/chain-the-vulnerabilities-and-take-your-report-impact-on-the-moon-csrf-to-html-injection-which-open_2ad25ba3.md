---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-08-12_chain-the-vulnerabilities-and-take-your-report-impact-on-the-moon-csrf-to-html-i.md
original_filename: 2017-08-12_chain-the-vulnerabilities-and-take-your-report-impact-on-the-moon-csrf-to-html-i.md
title: Chain the vulnerabilities and take your report impact on the moon (CSRF to
  HTML INJECTION which results OPEN REDIRECT and could steal USER CREDENTIALS)
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- csrf
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- csrf
- mobile-security
language: en
raw_sha256: 2ad25ba3e5ae8d411a645ecec1e8dbbadcef9d2f4bd48ccb92e659961edd2b2e
text_sha256: bbaf335b13b8b8b53592523adf7a649a9fd7a1af70356bdd2cef95ee2b21f8d9
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Chain the vulnerabilities and take your report impact on the moon (CSRF to HTML INJECTION which results OPEN REDIRECT and could steal USER CREDENTIALS)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-08-12_chain-the-vulnerabilities-and-take-your-report-impact-on-the-moon-csrf-to-html-i.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, csrf, mobile-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `2ad25ba3e5ae8d411a645ecec1e8dbbadcef9d2f4bd48ccb92e659961edd2b2e`
- Text SHA256: `bbaf335b13b8b8b53592523adf7a649a9fd7a1af70356bdd2cef95ee2b21f8d9`


## Content

---
title: "Chain the vulnerabilities and take your report impact on the moon (CSRF to HTML INJECTION which results OPEN REDIRECT and could steal USER CREDENTIALS)"
url: "https://medium.com/@armaanpathan/chain-the-vulnerabilities-and-take-your-report-impact-on-the-moon-csrf-to-html-injection-which-608fa6e74236"
authors: ["Armaan Pathan (@armaancrockroax)"]
programs: ["Legal Robot"]
bugs: ["CSRF", "HTML injection"]
bounty: "40"
publication_date: "2017-08-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6127
scraped_via: "browseros"
---

# Chain the vulnerabilities and take your report impact on the moon (CSRF to HTML INJECTION which results OPEN REDIRECT and could steal USER CREDENTIALS)

Chain the vulnerabilities and take your report impact on the moon (CSRF to HTML INJECTION which results in USER CREDENTIALS Stealing)
Armaan Pathan
Follow
4 min read
·
Aug 12, 2017

281

4

It was weekend and time for some Research. So i started reading some public disclosures from https://hackerone.com/hacktivity.
after reading some good blogs i have decided to implement them. so i quickly i had selected my target.

So i had noticed that legalrobot (
Legal Robot
)has a quick response and it is resolving the vulnerabilities quicky. so i have selected 
Legal Robot
 as my target and started looking into the assets and its scope.

after understanding the scope i had started looking into the application.and i had noticed that is not sanitizing the spacial characters from some parameters. so i started injecting some html tags and was able to inject html tags.

Press enter or click to view image in full size

So yeah i had found HTML injection. BUG #1.

So i started finding xss over there that if i am able to execute xss or not.

so it had injected the payload but i had found that web application is using CSP. and alert was not popping up. :(((((((( sad part. :(

Press enter or click to view image in full size

but if you are a hacker then you will never get satisfied until and unless you will exploit it

so i had started digging more and i put my second use case payload. which was

“/><META HTTP-EQUIV=”refresh” CONTENT=”1;url=https://app.legalrobot.com/sign-out">

So yes i with the help of this payload whenever the user visits the roadmap page it will automatically get log out from his-her account.

and i had found this tricky. so next i had tried to redirect on my website. and executive malicious script. so i used this payload

“/><META HTTP-EQUIV=”refresh” CONTENT=”1;url=http://www.mysite.com/malicious_script.html">

and what it was resulting to open redirectBUG #2

and also executing my malicious scripts.

Press enter or click to view image in full size

some how i was able to perform malicious tasks.

Get Armaan Pathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Quickly i made a PoC of it and reported. and i got quick reply from team, which was this.

Press enter or click to view image in full size

though the bug was triaged but the team member has mentioned that attacker has to do a little social engineering. i was like yeah but was not satisfied when i read “SOCIAL ENGINEERING” but the team member had gave me a hint by mentioning “UNKNOWN EXPLOIT”. well i that was enough hint for me.

again i started digging into the application. and while i was digging into the web application had noticed that the web application is using the websockets.

okay now i started checking headers of every pages and i found a Origin header. which was misconfigured. #BUG 3

so i started connecting to third party web sockets to this application and i was able to connect to the application by using the third party web sockets.

Press enter or click to view image in full size

it was allows web socket connecting from different Origin & it should not work from different origin.

i think mobile app hasn’t origin. (I am still not sure about this)

so some how i was able to do CSRF attack BUG #4 by using this & i had chained HTML INJECTION WHICH WAS RESULTING TO OPEN REDIRECT to CSRF ATTACK.

again i quickly made a poc of this and reported it.

This was a quick reply & bug has patched in a single day. (SO QUICK)

Press enter or click to view image in full size

got a good feedback with a sweet bounty amout.

Thanks 
HackerOne
 
Legal Robot
.

Thanks for reading guys. Comments most welcome.
have a great day ahead.
