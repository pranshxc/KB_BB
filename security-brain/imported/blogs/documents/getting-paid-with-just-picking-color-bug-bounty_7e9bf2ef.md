---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-16_getting-paid-with-just-picking-color-bug-bounty.md
original_filename: 2022-09-16_getting-paid-with-just-picking-color-bug-bounty.md
title: Getting Paid With Just Picking Color — Bug Bounty
category: documents
detected_topics:
- idor
- xss
- command-injection
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- idor
- xss
- command-injection
- otp
- automation-abuse
- csrf
language: en
raw_sha256: 7e9bf2efff203189e4159dfc0b08829847f2922ae4ddc03872057891d60ccefd
text_sha256: 19a9594958c3def1a18a52858918ec0fd76924b4f9352820b9ab162b761017b8
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Getting Paid With Just Picking Color — Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-16_getting-paid-with-just-picking-color-bug-bounty.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `7e9bf2efff203189e4159dfc0b08829847f2922ae4ddc03872057891d60ccefd`
- Text SHA256: `19a9594958c3def1a18a52858918ec0fd76924b4f9352820b9ab162b761017b8`


## Content

---
title: "Getting Paid With Just Picking Color — Bug Bounty"
url: "https://medium.com/@rdzsp/getting-paid-with-just-picking-color-bug-bounty-d3dbbac277fa"
authors: ["Redza"]
bugs: ["CSS injection"]
publication_date: "2022-09-16"
added_date: "2022-09-17"
source: "pentester.land/writeups.json"
original_index: 2161
scraped_via: "browseros"
---

# Getting Paid With Just Picking Color — Bug Bounty

Getting Paid With Just Picking Color — Bug Bounty
rdzsp
Follow
4 min read
·
Sep 17, 2022

84

Press enter or click to view image in full size

Suppppp guysss, this is my first write-up about bug bounty, let me introduce myself, my name is Redza you can call me za, ja, dza, red, or whatever. I’m currently working on Cyber Security Company called Cyber Army Indonesia as Backend Engineer. Sooo that’s it a little summary about me, let’s gooo to the topiiic.

Press enter or click to view image in full size
Photo by Darius Bashar on Unsplash

I’m currently having a lot of fun on Bugcrowd’s Programs, especially on Pinterest. But, right now, I’m not gonna talk about my findings on Pinterest, because my report hasn’t been resolve by Pinterest. This time, I will talk about Private Program, I would called it redacted.com. The company who runs this program is working on Healthcare, This Company provides web application to bridging Hospital with Patient, like online appointment with Doctor A on Hospital A. After some research about background of this company, I’m dive into the web application.

This program has two different roles,
1. Patient.
2. Hospital.

This program provides credentials for those two accounts for each researcher. This web application is just for testing only (researcher not permitted to testing on real envy / production), the researcher is free to testing on Hospital Dashboard. Because the real case on production envy the attacker as user is has to be a patient ( because it doesn’t has Hospital Account Register page ), so I’m pick as Patient to first test.

I’m focusing on PII (Personally Identifiable Information) Leakage of other patients via IDOR (Insecure Direct Object Reference) but the endpoint is well handled, and XSS (Cross Site Scripting) I tried to inject all input and parameter with payloads but all tags and quotes is encoded as HTML Entity. It’s sad tho, but the life must go on, right? :)

Press enter or click to view image in full size
Photo by Christian Erfurt on Unsplash

Because I’m desperate to find some juicy things on Patient Dashboard, I’m givin up, and straightly go to Hospital Dashboard.

Get rdzsp’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I’m clicked all the buttons, and use all the features while my eyes focusing on HTTP history on my Burpsuite, and founds nothing. After a while, I’m comes up with color picker for the marker of doctor appointment, I’m tried to click the submit button while my Burpsuite Interceptor is ON, and the Burpsuite Interceptor intercept the request below:

POST /hospital/2163/doctor/22/appointment/update
Host: redacted.com
Content-Type: application/json
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30
Cookie: REDACTED
X-Csrf-Token: REDACTED

{“name”: “My Appointment”, “color”: “#FFFFFF”}

After I’m seen this request, i tried to change the color value to ‘ #FFFFFF>” ’, and the response shows 200 OK, soooo I’m check where this color that I’m injected is rendered, yessss, on Hospital Dashboard, when I check on Hospital Dashboard, the appointment color of doctor with id 22 is gray, i think. So I’m open up the Inspect Element and pick the card of doctor’s appointment, and surprisingly the color where I’m injected the >” is added on CSS Inline with property background-color, and it seems encoded quotes (“) to HTML Entity (&quotes;), so the tag with CSS Inline looks like below:

<div style=”background-color: #FFFFFF>&quotes;”></div>

And it seems I can’t bypass the encode flow, but with this flexibility of add anything to CSS Inline, we can use CSS Injection (Stored). But is it really have an impact for other users, if it’s only shows on own Hospital’s user? I don’t think soo.

So I tried to create Hospital’s Account with limited action but can change the color of appointment, and log into those account. And test the color picker and inject this payload below that I created to crash the page of Hospital Dashboard and the color picker itself:

#3fb5ab; position: fixed !important; width: 100% !important; height: 100% !important; top: 0 !important; left: 0 !important; right: 0 !important; bottom: 0 !important; background-color: rgba(0,0,0,1) !important; z-index: -1 !important; cursor: pointer !important;

And the CSS Inline would injected with those payload, and would looks like below:

<div style=”background-color: #3fb5ab; position: fixed !important; width: 100% !important; height: 100% !important; top: 0 !important; left: 0 !important; right: 0 !important; bottom: 0 !important; background-color: rgba(0,0,0,1) !important; z-index: -1 !important; cursor: pointer !important;”></div>

And after I clicked the submit button, the color picker and the Hospital Dashboard is crashed with overlay effect. All the Hospital Account’s inside those Hospital can’t see the Appointment and change the color.

With this CSS Injection, actually we can take advantage like stealing CSRF Token other users who view this poisoned CSS Inline with ^ on CSS to enumerating CSRF Token (reference: https://infosecwriteups.com/exfiltration-via-css-injection-4e999f63097d), but I don’t think about it on that time, idk why:( .

Sooo, this is the endd of me explaining a nonsense:) I hope you can take some knowledge from this nonsense:) cheersss guysssssssssss..

Timeline:

[ 05 Jun 2022 ] Submission submitted.
[ 07 Jun 2022 ] Ask more information about the submission.
[ 13 Jun 2022 ] Submission marked as Triage with P4.
[ 13 Jun 2022 ] Submission marked as Unresolved with P4 ( Points: 5, $XXX )
[ 27 Aug 2022 ] Submission marked as Resolved.

LinkedIn: https://linkedin.com/in/rdzsp
