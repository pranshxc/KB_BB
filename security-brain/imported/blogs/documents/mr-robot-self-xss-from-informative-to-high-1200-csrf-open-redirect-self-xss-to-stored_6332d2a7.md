---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-06_mr-robot-self-xss-from-informative-to-high-1200-csrf-open-redirectself-xss-to-st.md
original_filename: 2022-10-06_mr-robot-self-xss-from-informative-to-high-1200-csrf-open-redirectself-xss-to-st.md
title: 'Mr. Robot: Self Xss from Informative to high 1200$ ,csrf, open redirect,self
  xss to stored'
category: documents
detected_topics:
- xss
- command-injection
- otp
- automation-abuse
- csrf
tags:
- imported
- documents
- xss
- command-injection
- otp
- automation-abuse
- csrf
language: en
raw_sha256: 6332d2a7e279b66c0df3da3330764d7278cbf693070d69b8e669b3822b0551d4
text_sha256: 2094f909cca1344f0ba2ef0f54f15ceb711502d5396232d1bc3256d3a86ae850
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Mr. Robot: Self Xss from Informative to high 1200$ ,csrf, open redirect,self xss to stored

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-06_mr-robot-self-xss-from-informative-to-high-1200-csrf-open-redirectself-xss-to-st.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, automation-abuse, csrf
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `6332d2a7e279b66c0df3da3330764d7278cbf693070d69b8e669b3822b0551d4`
- Text SHA256: `2094f909cca1344f0ba2ef0f54f15ceb711502d5396232d1bc3256d3a86ae850`


## Content

---
title: "Mr. Robot: Self Xss from Informative to high 1200$ ,csrf, open redirect,self xss to stored"
url: "https://ahmadaabdulla.medium.com/mr-robot-self-xss-from-informative-to-high-1200-csrf-open-redirect-self-xss-to-stored-92f371ba3da1"
authors: ["Ahmad A Abdulla (@lu3ky13)"]
bugs: ["Self-XSS", "CSRF"]
bounty: "1,200"
publication_date: "2022-10-06"
added_date: "2022-10-08"
source: "pentester.land/writeups.json"
original_index: 2078
scraped_via: "browseros"
---

# Mr. Robot: Self Xss from Informative to high 1200$ ,csrf, open redirect,self xss to stored

Ahmad A Abdulla
Follow
3 min read
·
Oct 6, 2022

101

1

If you want to learn bug bounty in an easy and affordable way, visit our website. The course is taught in English.

https://www.cybershield.krd/Courses/Course/28

Mr. Robot: Self Xss from Informative to high 1200$ ,csrf, open redirect,self xss to stored

Hello all bug bounty hunters sorry for any mistake if I forget something to use this writeup for your RECON or you’re RESEARCHING, I found 2 w 3 bugs with the same idea

I submitted this bug to private programs but I changed everything here name website and panel and photos just to help the new bug bounty hunter it’s not the real name and photos

The first time I found csrf in the first name and last name no have a csrf token but the website not accepted csrf and self xss from the csrf i can change name to any word or payload xss but have no impact and not accepted by the website it’s too bored

after 2 or 3 hours I found a demo panel with the same information when you change the first name will change in the demo i changed to xss payload first name and the last name will be done and worked xss but the website not accepting self xss we need to change to stored xss but how?

ok now we have CSRF to change the profile name to xss and we found a demo website to reflect the xss it’s good

Get Ahmad A Abdulla’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

we need to redirect users from the normal website to the demo I found the button to create this redirection from the normal website to the demo website and the xss reflected

and I create two csrf one to change the profile name to xss and two to redirect users to the demo and injection like this

Press enter or click to view image in full size

steps like this

1 goto xxx.com change profile name and capture request and create csrf

2 capture request, the button will redirect you to the demo website, and create csrf

done

HackerOne profile - lu3ky-13
Security Researcher And Security Developer #gamers Bachelor of Business Administration in accounting …

hackerone.com

JavaScript is not available.
Edit description

twitter.com

https://www.linkedin.com/in/lu3ky13/
