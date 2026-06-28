---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-25_massive-users-account-takeoverschaining-vulnerabilities-to-idor.md
original_filename: 2021-12-25_massive-users-account-takeoverschaining-vulnerabilities-to-idor.md
title: Massive Users Account Takeovers(Chaining Vulnerabilities to IDOR)😲
category: documents
detected_topics:
- rate-limit
- otp
- idor
- command-injection
- api-security
tags:
- imported
- documents
- rate-limit
- otp
- idor
- command-injection
- api-security
language: en
raw_sha256: 17dbdac94a3bde309a15da511a1ed488cf0461db4f12a3e1d5032f086e9bcc0c
text_sha256: 0ae8df53d0f3e47eafd0c0ac166fdc83c78da2b0f480cd3939f83ec6754bf589
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Massive Users Account Takeovers(Chaining Vulnerabilities to IDOR)😲

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-25_massive-users-account-takeoverschaining-vulnerabilities-to-idor.md
- Source Type: markdown
- Detected Topics: rate-limit, otp, idor, command-injection, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `17dbdac94a3bde309a15da511a1ed488cf0461db4f12a3e1d5032f086e9bcc0c`
- Text SHA256: `0ae8df53d0f3e47eafd0c0ac166fdc83c78da2b0f480cd3939f83ec6754bf589`


## Content

---
title: "Massive Users Account Takeovers(Chaining Vulnerabilities to IDOR)😲"
url: "https://infosecwriteups.com/massive-users-account-takeovers-chaining-vulnerabilities-to-idor-ea4e1b6407d2"
authors: ["Anurag__Verma"]
bugs: ["Authentication bypass", "IDOR", "Lack of rate limiting"]
publication_date: "2021-12-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3063
scraped_via: "browseros"
---

# Massive Users Account Takeovers(Chaining Vulnerabilities to IDOR)😲

Massive Users Account Takeovers(Chaining Vulnerabilities to IDOR)😲
Anurag__Verma
Follow
3 min read
·
Dec 25, 2021

300

2

Hello hunters 👋✌ this is my 7th writeup 🧾,

In this, I will show an interesting case where I was able to take over any user account of an application even the admin/employee account.

let's move the use case,

Consider website as redacted.com, now the website uses the phone numbers for users login, Now after observation, I found that there are some phone numbers like 9999999999,8888888888,7777777777 …………1111111111 etc. which does not need actual authentication and I was able to login to them with any OTP number, but with other phone numbers(like mine one), they are actually doing authentication.

But why there is no actual authentication for the above-mentioned phone numbers?

The reason behind that is before deploying to actual production environment sometimes developers use some default phone numbers like 999999999,8888888888…….. for instantly accessing the application and testing internal functionalities without any actual authentication like in this case no correct OTP is needed to access the application.

Now, whenever the application is deployed to the production environment then it's the developer responsibility to disable this functionality because still, these account contains some developer or employee information like address, email, bank details and more meta info.

But sometimes developer forgets to change the functionality and an outsider can log in to these default phone numbers.

Now at this point, I think of reporting the issue but I didn’t reported it at this point, I think what if I use this functionality to enter into other users account.

Now Here comes the Chaining part,

Now I started analysing the request and responses, their parameters and tokens.

Get Anurag__Verma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

sign up POST request looks like below screenshot,

Press enter or click to view image in full size

now you can observe there are a lot of parameters where the given phone number is passed and the phone numbers mentioned above can be assessed for any OTP value.

Now, I manually checked for responses for all the three parameters mobileNo,uid and socialMediaId parameters by changing them with victim phone numbers,

Now the uid parameter is found to be vulnerable and below is the sample screenshot of how I can view the user information and then log in to their account.

Press enter or click to view image in full size

the response JSON parameter “isExistingUser” and message“ Login Successful” confirms the existence as well as the takeover of a user account, this way I can log in to any account via knowing their phone numbers,

You can get a lot of phone numbers via reconnaissance(like google, GitHub dorks, LinkedIn, contact pages) and you can test the vulnerability.

Increasing more impact due to NO RATE LIMIT ON SIGN UP ENDPOINT.

As there was no rate limit I can even brute force phone numbers and use intruder and filter results via response JSON parameter “isExistingUser=true”(this will confirm existing user) and this way I can enter into any user/employee/admin account.

So this way impact becomes critical and then I reported the issue to the respective organisation and received $$$ bounty (cant disclose the target due to privacy policy reasons).

Hope you like the write-up 😁, dropdown your comments and suggestions👇 .

Subscribe to my youtube channel for bug hunting related stuff: redirect _poc

You can follow me on Instagram varmaanu001

follow me on Linkedin: my_linkedin

buy me a coffee 😍: here
