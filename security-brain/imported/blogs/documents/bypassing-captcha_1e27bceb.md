---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-20_bypassing-captcha-.md
original_filename: 2019-12-20_bypassing-captcha-.md
title: Bypassing Captcha !
category: documents
detected_topics:
- command-injection
- password-reset
- automation-abuse
tags:
- imported
- documents
- command-injection
- password-reset
- automation-abuse
language: en
raw_sha256: 1e27bceb2c605b6f9d9328ea78a910737a252ae72edf7c5d7e4aa4f80a6d3d9b
text_sha256: f818bb76d16696f77cdc545156731dd3f3e40e7977f2ed8f549cfd5df6392485
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Captcha !

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-20_bypassing-captcha-.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `1e27bceb2c605b6f9d9328ea78a910737a252ae72edf7c5d7e4aa4f80a6d3d9b`
- Text SHA256: `f818bb76d16696f77cdc545156731dd3f3e40e7977f2ed8f549cfd5df6392485`


## Content

---
title: "Bypassing Captcha !"
url: "https://medium.com/@abhishake100/bypassing-captcha-17c59d37f459"
authors: ["Abhishek Yadav (@abhishake100)"]
bugs: ["Captcha bypass"]
bounty: "200"
publication_date: "2019-12-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4876
scraped_via: "browseros"
---

# Bypassing Captcha !

Bypassing Captcha !
Abhishek
Follow
3 min read
·
Dec 20, 2019

150

3

Curated list of Bug Bounty programs — https://bugbountydirectory.com

I don’t really look for captcha bypass, but this one specified that if a captcha bypass is found it will be rewarded.

So i started looking for the most common places where captcha can be found like signup, login and password reset pages. The one i found was on the Signin page.

Press enter or click to view image in full size
Press enter or click to view image in full size

As you can see the sign-in button is disabled and is only enabled after we check I’m not a robot. Since it was disabled, i quickly right clicked on the button and clicked Inspect Element and changed the disabled parameter to enabled.

The button was now enabled and i could click to sign.

So i entered the email and password and i was logged in without clicking on I’m not a robot. CAPTCHA BYPASSED

I was still curious how the request looked like, so i opened burpsuite and looked at the request and noticed that the server didn’t check for captcha’s response in the first place. I could simple remove the captcha-response and send it and it redirected me to the dashboard.

Press enter or click to view image in full size

There was no need for me to enable the button, i just had to look at the request and remove the captcha response.

Get Abhishek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I made a quick POC, sent it to the security team and within a day they replied.

Press enter or click to view image in full size

I had read previous reports like this in the past to bypass captcha but to find one was great. Hope you learned something from this and if you liked it then please do share.

Follow me on twitter — https://twitter.com/abhishekY495

Thank You.
