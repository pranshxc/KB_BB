---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-04_easily-leaking-passenger-information-on-an-airline.md
original_filename: 2020-02-04_easily-leaking-passenger-information-on-an-airline.md
title: Easily leaking passenger information on an Airline
category: documents
detected_topics:
- idor
- xss
- command-injection
tags:
- imported
- documents
- idor
- xss
- command-injection
language: en
raw_sha256: f5842775d822e65badd33fdfa5a6fac3b0ac83ac36192b080a8c71cae08e9b21
text_sha256: fface77470aa0622fa12894cd28e169567464aa00774181c93a84f2f0f01d94a
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Easily leaking passenger information on an Airline

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-04_easily-leaking-passenger-information-on-an-airline.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `f5842775d822e65badd33fdfa5a6fac3b0ac83ac36192b080a8c71cae08e9b21`
- Text SHA256: `fface77470aa0622fa12894cd28e169567464aa00774181c93a84f2f0f01d94a`


## Content

---
title: "Easily leaking passenger information on an Airline"
url: "https://medium.com/@zseano/easily-leaking-passenger-information-on-an-airline-18f99b22cf95"
authors: ["Zseano (@zseano)"]
bugs: ["IDOR"]
publication_date: "2020-02-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4796
scraped_via: "browseros"
---

# Easily leaking passenger information on an Airline

Easily leaking passenger information on an Airline
Sean (zseano)
Follow
4 min read
·
Feb 4, 2020

441

1

Press enter or click to view image in full size

This post is going to outline how I simply applied my methodology and managed to find multiple vulnerabilities leaking airline passenger information on a YesWeHack bug bounty program. My experience on YesWeHack has been extremely good as the companies engage & communicate with you on reports to understand the issue in a very timely manner. I feel like the companies I dealt with on YesWeHack treat me with full respect and honestly I recommend you checkout their platform, I just wish there was more programs! :D

For these findings I spent approx ~15hours max over 3 days to find these bugs. I used zero recon tools and only targeted their main web application. I was shocked at how easy I found these bugs and to this day I still think about other airlines which DO NOT welcome hackers and if they are vulnerable in similar areas. If you work for an airline, please reach out and maybe I can help you! @zseano (or perhaps contact YesWeHack & invite me? :D)

I’d also like to use this opportunity to remind people that you should never post your plane tickets publicly, no information at all. Seriously, keep it to yourself.

For those not familiar with what an IDOR (Insecure Direct Object Reference) is, imagine you have an url: https://api.example.com/user/1 which reflects private information such as email. You are id ‘1’ and changing this to “2” should present you with an error that you don’t have the right access to view this users’ information. If however it does then you have a valid IDOR bug for enumerating user information. (Of course in some cases it is intended functionality, you should be looking for sensitive information leaked) IDOR is about changing certain values to another and being able to view / modify other users’ data. In my opinion IDOR is just as common as XSS.

Tip: Don’t get distracted by “encrypted” values or guids as sometimes integer values are accepted anyway!;)
Second tip: Inject “id”:1 when you see JSON post requests even if it’s not there. It may still be handled and you’ll find a ‘blind’ IDOR ;)

On with the hacking!
Hi Sean, you have been invited to hack on zseanosflights.com

Nice. The website offers lots to play with but more importantly, the website holds sensitive information. It’s an Airline, passport information etc. When there’s sensitive information at risk I will always go in with the mindset of they’re secure. They’re holding info about passengers and they will want to keep this secure, so let’s check: just how secure is their production site which thousands of users are using daily?

Get Sean (zseano)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

My methodology is focused around using the website as intended, so the very first thing I did after signing up was to simply purchase a flight. I bought a ticket for £20 which flies next year and armed with a valid booking reference. it was time to hunt for IDORs across the entire site. I also googled for this particular Airline and found a promotion from 2018 which contained another booking reference. At this point I didn’t know if it worked but I saved it for future reference. Whenever you test for IDOR always test against your own accounts or ids owned by the company (so you are not affecting real users!)

This is where things got a bit too easy. Now if you have tried to view your plane booking online before you will know that it requires your booking reference AND last name. Well in this case when checking in a request was made to fetch my passenger information with only my booking reference as the parameter. Simply changing this to another users’ booking reference would display their information to me. “Wow” I thought.. that easy huh? Yes really, that easy. No tools needed, no crazy skills.

At this stage I went and found as many features as possible which required a booking reference and found multiple areas leaking full passenger information. The scope is pretty locked down on this program so I was still just targeting their main web application. I am still waiting for the scope to be increased so I can continue my hunting.

I’m afraid this is the end of the hacking. I literally just used the site as intended, captured the request, changed the “bookingRef” parameter to another ID and was able to leak sensitive passenger information in multiple areas. The issue affected pretty much all features which handled a booking reference. As you know also booking references for flights are easily guessable, they are only up to 6 characters long and usually only contain 2 numbers. It would not be hard to generate every combination and run a tool to mass-scrape passenger information.

Hacking really isn’t that hard, I just use the site as intended :)

I am presenting a talk at Securi-Tay2020 titled, “Saving user data one company at a time — Hacking with zseano” so if you are there feel free to come and say hi and I hope you enjoy my talk! https://securi-tay.co.uk/

Remember: BE CAREFUL WHAT YOU SHARE ONLINE
